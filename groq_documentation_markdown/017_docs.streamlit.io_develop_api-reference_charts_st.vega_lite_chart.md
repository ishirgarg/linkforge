Here is the converted markdown:

# st.vega_lite_chart - Streamlit Docs
## Documentation
### Search
[Get started](/get-started)
	* [Installation](/get-started/installation)
	* [Fundamentals](/get-started/fundamentals)
	* [First steps](/get-started/tutorials)
[Develop](/develop)
	* [Concepts](/develop/concepts)
	* [API reference](/develop/api-reference)
		+ [Write and magic](/develop/api-reference/write-magic)
		+ [Text elements](/develop/api-reference/text)
		+ [Data elements](/develop/api-reference/data)
		+ [Chart elements](/develop/api-reference/charts)
			- [st.area_chart](/develop/api-reference/charts/st.area_chart)
			- [st.bar_chart](/develop/api-reference/charts/st.bar_chart)
			- [st.line_chart](/develop/api-reference/charts/st.line_chart)
			- [st.map](/develop/api-reference/charts/st.map)
			- [st.scatter_chart](/develop/api-reference/charts/st.scatter_chart)
			- [st.altair_chart](/develop/api-reference/charts/st.altair_chart)
			- [st.bokeh_chart](/develop/api-reference/charts/st.bokeh_chart)
			- [st.graphviz_chart](/develop/api-reference/charts/st.graphviz_chart)
			- [st.plotly_chart](/develop/api-reference/charts/st.plotly_chart)
			- [st.pydeck_chart](/develop/api-reference/charts/st.pydeck_chart)
			- [st.pyplot](/develop/api-reference/charts/st.pyplot)
			- [st.vega_lite_chart](/develop/api-reference/charts/st.vega_lite_chart)
		+ [Input widgets](/develop/api-reference/widgets)
		+ [Media elements](/develop/api-reference/media)
		+ [Layouts and containers](/develop/api-reference/layout)
		+ [Chat elements](/develop/api-reference/chat)
		+ [Status elements](/develop/api-reference/status)
		+ [Third-party components](https://streamlit.io/components)
		+ [Authentication and user info](/develop/api-reference/user)
		+ [Navigation and pages](/develop/api-reference/navigation)
		+ [Execution flow](/develop/api-reference/execution-flow)
		+ [Caching and state](/develop/api-reference/caching-and-state)
		+ [Connections and secrets](/develop/api-reference/connections)
		+ [Custom components](/develop/api-reference/custom-components)
		+ [Configuration](/develop/api-reference/configuration)
		+ [App testing](/develop/api-reference/app-testing)
		+ [Command line](/develop/api-reference/cli)
	* [Tutorials](/develop/tutorials)
	* [Quick reference](/develop/quick-reference)
[Deploy](/deploy)
	* [Concepts](/deploy/concepts)
	* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	* [Snowflake](/deploy/snowflake)
	* [Other platforms](/deploy/tutorials)
[Knowledge base](/knowledge-base)
	* [FAQ](/knowledge-base/using-streamlit)
	* [Installing dependencies](/knowledge-base/dependencies)
	* [Deployment issues](/knowledge-base/deploy)

[Home](/)/
[Develop](/develop)/
[API reference](/develop/api-reference)/
[Chart elements](/develop/api-reference/charts)/
[st.vega_lite_chart](/develop/api-reference/charts/st.vega_lite_chart)

Here is the converted Markdown text:

# st.vega_lite_chart
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Display a chart using the Vega-Lite library.

[Vega-Lite](https://vega.github.io/vega-lite/) is a high-level grammar for defining interactive graphics.

## Function signature
```python
st.vega_lite_chart(data=None, spec=None, *, use_container_width=None, theme="streamlit", key=None, on_select="ignore", selection_mode=None, **kwargs)
```
### Parameters

* `data`: The data to be plotted or a Vega-Lite spec containing the data.
* `spec`: The Vega-Lite spec for the chart.
* `use_container_width`: Whether to override the chart's native width with the width of the parent container.
* `theme`: The theme of the chart. If "streamlit" (default), Streamlit uses its own design default. If `None`, Streamlit falls back to the default behavior of the library.
* `key`: An optional string to use for giving this element a stable identity.
* `on_select`: How the figure should respond to user selection events.
* `selection_mode`: The selection parameters Streamlit should use.
* `**kwargs`: The Vega-Lite spec for the chart as keywords.

### Returns
If `on_select` is "ignore" (default), this command returns an internal placeholder for the chart element that can be used with the `.add_rows()` method. Otherwise, this command returns a dictionary-like object that supports both key and attribute notation.

### Example
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((60, 3)), columns=["a", "b", "c"])

st.vega_lite_chart(
    df,
    {
        "mark": {"type": "circle", "tooltip": True},
        "encoding": {
            "x": {"field": "a", "type": "quantitative"},
            "y": {"field": "b", "type": "quantitative"},
            "size": {"field": "c", "type": "quantitative"},
            "color": {"field": "c", "type": "quantitative"},
        },
    },
)
```
## Chart selections

### VegaLiteState
The schema for the Vega-Lite event state.

#### Attributes
* `selection`: The state of the on_select event.

#### Examples
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
## element.add_rows
Concatenate a dataframe to the bottom of the current one.

### Function signature
```python
element.add_rows(data=None, **kwargs)
```
### Parameters

* `data`: Table to concat.
* `**kwargs`: The named dataset to concat.

### Example
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
## Theming
Vega-Lite charts are displayed using the Streamlit theme by default.

### Example
```python
import streamlit as st
from vega_datasets import data

source = data.cars()
chart = {
    "mark": "point",
    "encoding": {
        "x": {"field": "Horsepower", "type": "quantitative"},
        "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(source, chart, theme="streamlit", use_container_width=True)

with tab2:
    st.vega_lite_chart(source, chart, theme=None, use_container_width=True)
```