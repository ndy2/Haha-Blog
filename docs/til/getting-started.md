
Til 을 시작해 보자

```dataviewjs
dv.span("** Today I Learn **") 
const calendarData = {
    colors: {
        blue:        ["#8cb9ff", "#69a3ff", "#428bff", "#1872ff", "#0058e2"],
        green:       ["#c6e48b", "#7bc96f", "#49af5d", "#2e8840", "#196127"],
        red:         ["#ff9e82", "#ff7b55", "#ff4d1a", "#e73400", "#bd2a00"],
        orange:      ["#ffa244", "#fd7f00", "#dd6f00", "#bf6000", "#9b4e00"],
        pink:        ["#ff96cb", "#ff70b8", "#ff3a9d", "#ee0077", "#c30062"],
        orangeToRed: ["#ffdf04", "#ffbe04", "#ff9a03", "#ff6d02", "#ff2c01"]
    },
    entries: [],
}

//DataviewJS loop
for (let page of dv.pages('"docs/til"').where(p => p.til)) {
    calendarData.entries.push({
        date: page.file.name,
        intensity: page.til,
        color: "green",  
        content: await dv.span(`[](${page.file.name})`),
    })
}

renderHeatmapCalendar(this.container, calendarData)
```


