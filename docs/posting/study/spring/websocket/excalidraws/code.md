```java
@Configuration(proxyBeanMethods = false)
@ConditionalOnBean({ DelegatingWebSocketMessageBrokerConfiguration.class, ObjectMapper.class })
@ConditionalOnClass({ ObjectMapper.class, AbstractMessageBrokerConfiguration.class })
static class WebSocketMessageConverterConfiguration implements WebSocketMessageBrokerConfigurer {

		private final ObjectMapper objectMapper;

		WebSocketMessageConverterConfiguration(ObjectMapper objectMapper) {
				this.objectMapper = objectMapper;
		}

		@Override
		public boolean configureMessageConverters(List<MessageConverter> messageConverters) {
				MappingJackson2MessageConverter converter = new MappingJackson2MessageConverter();
				converter.setObjectMapper(this.objectMapper);
				DefaultContentTypeResolver resolver = new DefaultContentTypeResolver();
				resolver.setDefaultMimeType(MimeTypeUtils.APPLICATION_JSON);
				converter.setContentTypeResolver(resolver);
				messageConverters.add(new StringMessageConverter());
				messageConverters.add(new ByteArrayMessageConverter());
				messageConverters.add(converter);
				return false;
		}

		@Bean
		static LazyInitializationExcludeFilter eagerStompWebSocketHandlerMapping() {
				return (name, definition, type) -> name.equals("stompWebSocketHandlerMapping");
		}

}

```
