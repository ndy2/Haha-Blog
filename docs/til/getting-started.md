
### Til 을 시작해 보자

아래 그래프의 색칠된 부분을 클릭하면 해당 날짜의 TIL 로 이동합니다.

색칠된 정도는 1~4의 숫자로 스스로 공부한 정도를 체크해서 기록한 것입니다.

## Today I Learn! 2022

```vegalite
--8<--
docs/til/resources/2022-til-heat-map-vega.json
--8<--
```

---

## Today I Learn! 2023
```vegalite
--8<--
docs/til/resources/2023-til-heat-map-vega.json
--8<--
```

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "url": "https://ndy2.github.io/Haha-Blog/til/resources/2023.csv"
  },
  "title": "Today I Learn",
  "transform": [
    {
      "calculate": "'../til/' + utcFormat(datum.date,'%Y-%m-%d') +'/'",
      "as": "til-link"
    },
    {
      "calculate": "utcFormat(datum.date,'%Y-%m-%d')",
      "as": "til-date"
    }
  ],
  "mark": {
    "type": "rect",
    "width": 11,
    "height": 11,
    "cornerRadius": 2,
    "outerRadius": 10,
    "stroke": "#E8E8E8",
    "strokeWidth": 1,
    "tooltip": true
  },
  "encoding": {
    "x": {
      "field": "date",
      "timeUnit": "yearweek",
      "type": "nominal"
    },
    "y": {
      "field": "date",
      "timeUnit": "day",
      "type": "ordinal"
    },
    "color": {
      "field": "til",
      "type": "quantitative",
      "scale": {
        "range": [
          "#E8E8E8",
          "#c6e48b",
          "#7bc96f",
          "#49af5d",
          "#2e8840",
          "#196127"
        ]
      },
      "legend": null
    },
    "href": {
      "condition": {
        "test": "datum['til'] == 0 ",
        "value": ""
      },
      "field": "til-link"
    },
    "tooltip": [
      {
        "field": "til",
        "type": "quantitative"
      },
      {
        "field": "til-date"
      }
    ]
  }
}
```
