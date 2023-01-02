
Til 을 시작해 보자


## Today I Learn! 2022
```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": { "url" : "Haha-Blog/til/csv/2022.csv"},
  "title": "Today I Learn",
  "config": {
    "mark": {
      "width": 11,
      "height": 11,
      "cornerRadius": 2,
      "outerRadius": 10,
      "stroke": "#E8E8E8",
      "strokeWidth": 1
    }
  },
  "mark": "rect",
  "encoding": {
    "x": {
      "field": "date",
      "timeUnit": "week",
      "type": "nominal"
    },
    "y": {"field": "date", "timeUnit": "day", "type": "ordinal"},
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
    }
  }
}
```


## Today I Learn! 2023
```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": { "url" : "Haha-Blog/til/csv/2023.csv"},
  "title": "Today I Learn",
  "config": {
    "mark": {
      "width": 11,
      "height": 11,
      "cornerRadius": 2,
      "outerRadius": 10,
      "stroke": "#E8E8E8",
      "strokeWidth": 1
    }
  },
  "mark": "rect",
  "encoding": {
    "x": {
      "field": "date",
      "timeUnit": "week",
      "type": "nominal"
    },
    "y": {"field": "date", "timeUnit": "day", "type": "ordinal"},
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
    }
  }
}
```
