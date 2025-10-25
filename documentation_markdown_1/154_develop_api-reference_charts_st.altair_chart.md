```markdown
# st.altair_chart

> Source: [https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart](https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart)

## Introduction

This section will provide information about the `st.altair_chart` function in Streamlit.
```


Display a chart using the Vega-Altair library.

[Vega-Altair](https://altair-viz.github.io/) is a declarative statistical visualization library for Python, based on Vega and Vega-Lite.

### Function signature [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/vega_charts.py#L1669 "View st.altair_chart source code on GitHub")

```python
st.altair_chart(altair_chart, *, use_container_width=None, theme="streamlit", key=None, on_select="ignore", selection_mode=None)
```

### Parameters

*   **altair_chart** (`altair.Chart`)
    The Altair chart object to display. See [https://altair-viz.github.io/gallery/](https://altair-viz.github.io/gallery/) for examples of graph descriptions.

*   **use_container_width** (`bool` or `None`)
    Whether to override the chart's native width with the width of the parent container. This can be one of the following:
    *   `None` (default): Streamlit will use the parent container's width for all charts except those with known incompatibility (`altair.Facet`, `altair.HConcatChart`, and `altair.RepeatChart`).
    *   `True`: Streamlit sets the width of the chart to match the width of the parent container.
    *   `False`: Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container.

*   **theme** (`"streamlit"` or `None`)
    The theme of the chart. If `theme` is `"streamlit"` (default), Streamlit uses its own design default. If `theme` is `None`, Streamlit falls back to the default behavior of the library.

    The `"streamlit"` theme can be partially customized through the configuration options `theme.chartCategoricalColors` and `theme.chartSequentialColors`. Font configuration options are also applied.

*   **key** (`str`)
    An optional string to use for giving this element a stable identity. If `key` is `None` (default), this element's identity will be determined based on the values of the other parameters.

    Additionally, if selections are activated and `key` is provided, Streamlit will register the `key` in Session State to store the selection state. The selection state is read-only.

*   **on_select** (`"ignore"`, `"rerun"`, or `callable`)
    How the figure should respond to user selection events. This controls whether or not the figure behaves like an input widget. `on_select` can be one of the following:
    *   `"ignore"` (default): Streamlit will not react to any selection events in the chart. The figure will not behave like an input widget.
    *   `"rerun"`: Streamlit will rerun the app when the user selects data in the chart. In this case, `st.altair_chart` will return the selection data as a dictionary.
    *   A `callable`: Streamlit will rerun the app and execute the callable as a callback function before the rest of the app. In this case, `st.altair_chart` will return the selection data as a dictionary.

    To use selection events, the object passed to `altair_chart` must include selection parameters. To learn about defining interactions in Altair and how to declare selection-type parameters, see [Interactive Charts](https://altair-viz.github.io/user_guide/interactions.html) in Altair's documentation.

*   **selection_mode** (`str` or `Iterable` of `str`)
    The selection parameters Streamlit should use. If `selection_mode` is `None` (default), Streamlit will use all selection parameters defined in the chart's Altair spec.

    When Streamlit uses a selection parameter, selections from that parameter will trigger a rerun and be included in the selection state. When Streamlit does not use a selection parameter, selections from that parameter will not trigger a rerun and not be included in the selection state.

    Selection parameters are identified by their `name` property.

### Returns

(`element` or `dict`)
If `on_select` is `"ignore"` (default), this command returns an internal placeholder for the chart element that can be used with the `.add_rows()` method. Otherwise, this command returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the `VegaLiteState` dictionary schema.

#### Example

```python
import altair as alt
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((60, 3)), columns=["a", "b", "c"])

chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(chart)
```

## Chart selections

### VegaLiteState

The schema for the Vega-Lite event state.

The event state is stored in a dictionary-like object that supports both key and attribute notation. Event states cannot be programmatically changed or set through Session State.

Only selection events are supported at this time.

### Attributes

*   `selection` (`dict`)
    The state of the `on_select` event. This attribute returns a dictionary-like object that supports both key and attribute notation. The name of each Vega-Lite selection parameter becomes an attribute in the selection dictionary. The format of the data within each attribute is determined by the selection parameter definition within Vega-Lite.

#### Examples

The following two examples have equivalent definitions. Each one has a point and interval selection parameter include in the chart definition. The point selection parameter is named "point\_selection". The interval or box selection parameter is named "interval\_selection".

**Example 1: Chart selections with `st.altair_chart`**

```python
import altair as alt
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

point_selector = alt.selection_point("point_selection")
interval_selector = alt.selection_interval("interval_selection")
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(
        x="a",
        y="b",
        size="c",
        color="c",
        tooltip=["a", "b", "c"],
        fillOpacity=alt.condition(point_selector, alt.value(1), alt.value(0.3)),
    )
    .add_params(point_selector, interval_selector)
)

event = st.altair_chart(chart, key="alt_chart", on_select="rerun")

event
```

**Example 2: Chart selections with `st.vega_lite_chart`**

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

spec = {
    "mark": {"type": "circle", "tooltip": True},
    "params": [
        {"name": "interval_selection", "select": "interval"},
        {"name": "point_selection", "select": "point"},
    ],
    "encoding": {
        "x": {"field": "a", "type": "quantitative"},
        "y": {"field": "b", "type": "quantitative"},
        "size": {"field": "c", "type": "quantitative"},
        "color": {"field": "c", "type": "quantitative"},
        "fillOpacity": {
            "condition": {"param": "point_selection", "value": 1},
            "value": 0.3,
        },
    },
}

event = st.vega_lite_chart(df, spec, key="vega_chart", on_select="rerun")

event
```

Try selecting points in this interactive example. When you click a point, the selection will appear under the attribute, "point\_selection", which is the name given to the point selection parameter. Similarly, when you make an interval selection, it will appear under the attribute "interval\_selection". You can give your selection parameters other names if desired.

If you hold Shift while selecting points, existing point selections will be preserved. Interval selections are not preserved when making additional selections.

---

## element.add_rows

Concatenate a dataframe to the bottom of the current one.

**Function signature** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/arrow.py#L866 "View st.add_rows source code on GitHub")

```python
element.add_rows(data=None, **kwargs)
```

### Parameters

*   `data` (`pandas.DataFrame`, `pandas.Styler`, `pyarrow.Table`, `numpy.ndarray`, `pyspark.sql.DataFrame`, `snowflake.snowpark.dataframe.DataFrame`, `Iterable`, `dict`, or `None`)
    Table to concat. Optional.
*   `**kwargs` (`pandas.DataFrame`, `numpy.ndarray`, `Iterable`, `dict`, or `None`)
    The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter).

#### Example

```python
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(
    rng(0).standard_normal(size=(50, 20)), columns=("col %d" % i for i in range(20))
)

df2 = pd.DataFrame(
    rng(1).standard_normal(size=(50, 20)), columns=("col %d" % i for i in range(20))
)

my_table = st.table(df1)
time.sleep(1)
my_table.add_rows(df2)
```

You can do the same thing with plots. For example, if you want to add more data to a line chart:

```python
# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
time.sleep(1)
my_chart.add_rows(df2)
```

And for plots whose datasets are named, you can pass the data with a keyword argument where the key is the name:

```python
my_chart = st.vega_lite_chart(
    {
        "mark": "line",
        "encoding": {"x": "a", "y": "b"},
        "datasets": {
            "some_fancy_name": df1,  # <-- named dataset
        },
        "data": {"name": "some_fancy_name"},
    }
)
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
```

---

## Theming

### Streamlit Theme for Altair Charts

Altair charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette, ensuring your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it and use Altair's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Altair theme:

```python
import altair as alt
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open_in_new_](https://doc-altair-chart.streamlit.app/?utm_medium=oembed)

### Customizing Charts with the Streamlit Theme

Your own customizations will still be taken into account. You can make changes to your chart configurations, and although the Streamlit theme is enabled by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

Here's an example of an Altair chart where manual color passing is done and reflected:

```python
import altair as alt
import streamlit as st
from vega_datasets import data

source = data.seattle_weather()

scale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
)
color = alt.Color("weather:N", scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=["x"])
click = alt.selection_multi(encodings=["color"])

# Top panel is scatter plot of temperature vs time
points = (
    alt.Chart()
    .mark_point()
    .encode(
        alt.X("monthdate(date):T", title="Date"),
        alt.Y(
            "temp_max:Q",
            title="Maximum Daily Temperature (C)",
            scale=alt.Scale(domain=[-5, 40]),
        ),
        color=alt.condition(brush, color, alt.value("lightgray")),
        size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
    )
    .properties(width=550, height=300)
    .add_selection(brush)
    .transform_filter(click)
)

# Bottom panel is a bar chart of weather type
bars = (
    alt.Chart()
    .mark_bar()
    .encode(
        x="count()",
        y="weather:N",
        color=alt.condition(click, color, alt.value("lightgray")),
    )
    .transform_filter(brush)
    .properties(width=550)
    .add_selection(click)
)

chart = alt.vconcat(points, bars, data=source, title="Seattle Weather: 2012-2015")

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)

with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)
```

Notice how the custom colors are still reflected in the chart, even when the Streamlit theme is enabled.

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open_in_new_](https://doc-altair-custom-colors.streamlit.app/?utm_medium=oembed)

For many more examples of Altair charts with and without the Streamlit theme, check out the [altair.streamlit.app](https://altair.streamlit.app).

---

### Conclusion

The `st.altair_chart` function provides a seamless way to integrate Altair visualizations into your Streamlit applications. By leveraging the built-in Streamlit theme, you can ensure a consistent and visually appealing design across your dashboards. The ability to easily switch between the Streamlit theme and Altair's native theme, along with the preservation of custom configurations, offers great flexibility for data visualization in Streamlit.

---

### Further Resources

*   **Streamlit Forums:** Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

* * *

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[](https://github.com/streamlit "GitHub")[](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q "YouTube")[](https://twitter.com/streamlit "Twitter")[](https://www.linkedin.com/company/streamlit "LinkedIn")[](https://info.snowflake.com/streamlit-newsletter-sign-up.html "Newsletter")

© 2025 Snowflake Inc.Cookie policy