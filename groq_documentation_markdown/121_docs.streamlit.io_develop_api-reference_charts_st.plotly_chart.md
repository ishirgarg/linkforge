Here is the HTML converted to clean Markdown:
### st.plotly_chart - Streamlit Docs

#### Documentation

* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
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
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [Application logic](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- [Tools](/develop/api-reference/app-testing)
		- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

[Breadcrumbs]
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chart elements](/develop/api-reference/charts)
* [st.plotly_chart](/develop/api-reference/charts/st.plotly_chart)

Here's the HTML content converted to clean Markdown:

### st.plotly_chart
#### Streamlit Version
Version 1.50.0
Version 1.49.0
Version 1.48.0
Version 1.47.0
Version 1.46.0
Version 1.45.0
Version 1.44.0
Version 1.43.0
Version 1.42.0
Version 1.41.0
Version 1.40.0
Version 1.39.0
Version 1.38.0
Version 1.37.0
Version 1.36.0
Version 1.35.0
Version 1.34.0
Version 1.33.0
Version 1.32.0
Version 1.31.0
Version 1.30.0
Version 1.29.0
Version 1.28.0
Version 1.27.0
Version 1.26.0
Version 1.25.0
Version 1.24.0
Version 1.23.0
Version 1.22.0

Display an interactive Plotly chart.

[Plotly](https://plot.ly/python) is a charting library for Python. The arguments to this function closely follow the ones for Plotly's `plot()` function.

To show Plotly charts in Streamlit, call `st.plotly_chart` wherever you would call Plotly's `py.plot` or `py.iplot`.

**Important**: You must install `plotly>=4.0.0` to use this command. Your app's performance may be enhanced by installing `orjson` as well. You can install all charting dependencies (except Bokeh) as an extra with Streamlit:
```bash
pip install streamlit[charts]
```
#### Function Signature
```python
st.plotly_chart(
    figure_or_data,
    use_container_width=True,
    *,
    theme="streamlit",
    key=None,
    on_select="ignore",
    selection_mode=("points", "box", "lasso"),
    config=None,
    **kwargs
)
```
#### Parameters

* `figure_or_data`: The Plotly Figure or Data object to render.
* `use_container_width`: Whether to override the figure's native width with the width of the parent container.
* `theme`: The theme of the chart.
* `key`: An optional string to use for giving this element a stable identity.
* `on_select`: How the figure should respond to user selection events.
* `selection_mode`: The selection mode of the chart.
* `config`: A dictionary of Plotly configuration options.
* `**kwargs`: Additional arguments accepted by Plotly's `plot()` function.

#### Returns
If `on_select` is `"ignore"` (default), this command returns an internal placeholder for the chart element. Otherwise, this command returns a dictionary-like object that supports both key and attribute notation.

### Examples
#### Example 1: Basic Plotly Chart
```python
import plotly.figure_factory as ff
import streamlit as st
from numpy.random import default_rng as rng

hist_data = [
    rng(0).standard_normal(200) - 2,
    rng(1).standard_normal(200),
    rng(2).standard_normal(200) + 2,
]
group_labels = ["Group 1", "Group 2", "Group 3"]

fig = ff.create_distplot(
    hist_data, group_labels, bin_size=[0.1, 0.25, 0.5]
)

st.plotly_chart(fig)
```
#### Example 2: Plotly Chart with Configuration
```python
import plotly.graph_objects as go
import streamlit as st

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 3, 2, 5, 4]
    )
)

st.plotly_chart(fig, config={'scrollZoom': False})
```
### Chart Selections
#### PlotlyState
The schema for the Plotly chart event state.

#### Attributes
* `selection`: The state of the `on_select` event.
#### Example
```python
import plotly.express as px
import streamlit as st

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

event = st.plotly_chart(fig, key="iris", on_select="rerun")

event
```
### Theming
Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette.

You can disable the Streamlit theme and use Plotly's native theme by setting `theme=None`.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:
```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()
fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])

with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
```