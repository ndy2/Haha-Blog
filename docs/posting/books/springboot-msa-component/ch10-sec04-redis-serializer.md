자동 설정이 아닌 빈 직접 생성 방식으로 RedisTemplate<String, String> 을 생성하여 레디스에 저장해 보자.

```java
@Bean  
public RedisConnectionFactory redisConnectionFactory() {  
    RedisStandaloneConfiguration configuration = new RedisStandaloneConfiguration("127.0.0.1", 6379);  
    return new LettuceConnectionFactory(configuration);  
}  
  
@Bean  
public RedisTemplate<String, String> redisTemplate(){  
    RedisTemplate<String, String> redisTemplate = new RedisTemplate<>();  
    redisTemplate.setConnectionFactory(redisConnectionFactory());  
    return redisTemplate;  
}
```

---

### 1. 기본 `RedisTemplate` 사용 - `JdkSerializationRedisSerializer`

```java
@Autowired  
private RedisTemplate<String, String> redisTemplate;

@Test  
void set() {  
    ValueOperations<String, String> valueOperations = redisTemplate.opsForValue();  
    valueOperations.set("key", "value");  
}
```

- redis monitor 를 통해 확인한 실행된 명령어

```redis
"SET" "\xac\xed\x00\x05t\x00\x03key" "\xac\xed\x00\x05t\x00\x05value"
```

위 처럼 아무 설정을 하지 않고 RedisTemplate 을 만들게 되면 Key 와 Value 의 직렬화`JdkSerialization

`RedisSerializer` 를 사용해서 위 처럼 알아보기 힘든 문자가 저장된다. 만약 직접 정의한 Key 와 Value 타입을 사용할때 `JdkSerializationRedisSerializer` 를 사용하고 싶다면 꼭 `java.io.Serializable` 을 구현 해야 한다. 이런 두가지 이유로 저자분은 `JdkSerializationRedisSerializer` 의 사용을 반대한다.

---

### 2. `StringRedisTemplate` - `StringRedisSerializer` 사용!

그럼 이번에는 StringRedisTemplate 을 사용해보자!

```java

@Autowired  
private StringRedisTemplate stringRedisTemplate;

@Test  
void set2() {  
    ValueOperations<String, String> valueOperations = stringRedisTemplate.opsForValue();  
    valueOperations.set("key", "value");  
}
```

```
"SET" "key" "value"
```

깔끔하다!

### 3. 직접 RedisSerializer 클래스 구현!

만약 String 이 아니라 직접만든 객체를 RedisTemplate 의 Key 와 Value 로 사용하고 싶다면 RedisSerializer 클래스를 구현하여야 한다. (`JdkSerializertionRedisSerializer` 를 사용하지 말자!)

그럼 링크와 같은 Key 와 Value 객체를 위한 RedisSerializer 를 만들어 보자!

```java title="HotelCacheKeySerializer"
public class HotelCacheKeySerializer implements RedisSerializer<HotelCacheKey> {  
  
    private final Charset UTF_8 = Charset.forName("UTF-8");  
  
    @Override  
    public byte[] serialize(HotelCacheKey hotelCacheKey) throws SerializationException {  
        if (Objects.isNull(hotelCacheKey))  
            throw new SerializationException("hotelCacheKey is null");  
  
        return hotelCacheKey.toString().getBytes(UTF_8);  
    }  
  
    @Override  
    public HotelCacheKey deserialize(byte[] bytes) throws SerializationException {  
        if (Objects.isNull(bytes))  
            throw new SerializationException("bytes is null");  
  
        return HotelCacheKey.fromString(new String(bytes, UTF_8));  
    }  
}
```

```java title = 
  
@Slf4j  
public class HotelCacheValueSerializer implements RedisSerializer<HotelCacheValue> {  
  
    // JSON Mapper  
    public static final ObjectMapper MAPPER = new ObjectMapper();  
    private final Charset UTF_8 = Charset.forName("UTF-8");  
  
    @Override  
    public byte[] serialize(HotelCacheValue hotelCacheValue) throws SerializationException {  
        if (Objects.isNull(hotelCacheValue))  
            return null;  
  
        try {  
            String json = MAPPER.writeValueAsString(hotelCacheValue);  
            return json.getBytes(UTF_8);  
        } catch (JsonProcessingException e) {  
            throw new SerializationException("json serialize error", e);  
        }  
    }  
  
    @Override  
    public HotelCacheValue deserialize(byte[] bytes) throws SerializationException {  
  
        if (Objects.isNull(bytes))  
            return null;  
  
        try {  
            return MAPPER.readValue(new String(bytes, UTF_8), HotelCacheValue.class);  
        } catch (JsonProcessingException e) {  
            throw new SerializationException("json deserialize error", e);  
        }  
    }  
}
```

이제 명령을 실행해 보자!

```java
@Test  
void set3() {  
    ValueOperations<HotelCacheKey, HotelCacheValue> valueOperations = hotelRedisTemplate.opsForValue();  
    valueOperations.set(  
            HotelCacheKey.from(1L),  
            HotelCacheValue.of("haha", "대구 수성구")  
    );  
}
```

```redis
"SET" "HOTEL::1" "{\"name\":\"haha\",\"address\":\"\xeb\x8c\x80\xea\xb5\xac \xec\x88\x98\xec\x84\xb1\xea\xb5\xac\"}"
```

분명 Serializer 에 Encoding 옵션을 주었는데도 한글이 깨진다.

찾아 보니 이는 redis-cli 실행시 --raw 옵션을 넣어 조회하면 정상적으로 볼 수 있다.

![redis-get.png](images/redis-get.png)
