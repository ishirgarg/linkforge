Here is the HTML content converted to clean markdown:

# st.bokeh_chart - Streamlit Docs
![logo](/logo.svg)

## Documentation
.Search
### Get started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

### Develop
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ [Write and magic](/develop/api-reference/write-magic)
	+ [Text elements](/develop/api-reference/text)
	+ [Data elements](/develop/api-reference/data)
	+ [Chart elements](/develop/api-reference/charts)
		- SIMPLE
		- [st.area_chart](/develop/api-reference/charts/st.area_chart)
		- [st.bar_chart](/develop/api-reference/charts/st.bar_chart)
		- [st.line_chart](/develop/api-reference/charts/st.line_chart)
		- [st.map](/develop/api-reference/charts/st.map)
		- [st.scatter_chart](/develop/api-reference/charts/st.scatter_chart)
		- ADVANCED
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
	+ APPLICATION LOGIC
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
	+ TOOLS
		- [App testing](/develop/api-reference/app-testing)
		- [Command line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

### Deploy
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

### Knowledge base
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

[Home](/) | [Develop](/develop) | [API reference](/develop/api-reference) | [Chart elements](/develop/api-reference/charts) | [st.bokeh_chart](/develop/api-reference/charts/st.bokeh_chart)

Here is the converted Markdown text:

### st.bokeh_chart
#### Deprecation notice
`st.bokeh_chart` was deprecated in version 1.49.0. Use the [streamlit-bokeh](https://github.com/streamlit/streamlit-bokeh) custom component instead.

Display an interactive Bokeh chart. Bokeh is a charting library for Python. The arguments to this function closely follow the ones for Bokeh's show function. You can find more about Bokeh at [https://bokeh.pydata.org](https://bokeh.pydata.org).

To show Bokeh charts in Streamlit, call `st.bokeh_chart` wherever you would call Bokeh's show.

**Important**: You must install `bokeh==2.4.3` and `numpy<2` to use this command, which is deprecated and will be removed in a future version. For more current updates, use the [streamlit-bokeh](https://github.com/streamlit/streamlit-bokeh) custom component instead.

#### Function signature
```python
st.bokeh_chart(figure, use_container_width=True)
```
#### Parameters

* `figure` (bokeh.plotting.figure.Figure): A Bokeh figure to plot.
* `use_container_width` (bool): Whether to override the figure's native width with the width of the parent container. If `use_container_width` is `True` (default), Streamlit sets the width of the figure to match the width of the parent container. If `use_container_width` is `False`, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container.

#### Example
```python
import streamlit as st
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="simple line example", x_axis_label="x", y_axis_label="y")
p.line(x, y, legend_label="Trend", line_width=2)

st.bokeh_chart(p)
```
Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.