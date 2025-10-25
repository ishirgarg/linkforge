Here is the Markdown version of the provided HTML:

# st.metric - Streamlit Docs
![logo](/logo.svg)

## Documentation

### Search
Search

### Menu
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- PAGE ELEMENTS
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
			- [st.dataframe](/develop/api-reference/data/st.dataframe)
			- [st.data_editor](/develop/api-reference/data/st.data_editor)
			- [st.column_config](/develop/api-reference/data/st.column_config)
			- [st.table](/develop/api-reference/data/st.table)
			- [st.metric](/develop/api-reference/data/st.metric)
			- [st.json](/develop/api-reference/data/st.json)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- APPLICATION LOGIC
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- TOOLS
		- [App testing](/develop/api-reference/app-testing)
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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Data elements](/develop/api-reference/data)
* [st.metric](/develop/api-reference/data/st.metric)

## st.metric
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Display a metric in big bold font, with an optional indicator of how the metric changed.

Tip: If you want to display a large number, it may be a good idea to shorten it using packages like [millify](https://github.com/azaitsev/millify) or [numerize](https://github.com/davidsa03/numerize). E.g. 1234 can be displayed as 1.2k using `st.metric("Short number", millify(1234))`.

### Function signature
```python
st.metric(label, value, delta=None, delta_color="normal", *, help=None, label_visibility="visible", border=False, width="stretch", height="content", chart_data=None, chart_type="line")
```
### Parameters

* `label` (str): The header or title for the metric. The label can optionally contain GitHub-flavored Markdown.
* `value` (int, float, decimal.Decimal, str, or None): Value of the metric. None is rendered as a long dash.
* `delta` (int, float, decimal.Decimal, str, or None): Indicator of how the metric changed, rendered with an arrow below the metric.
* `delta_color` ("normal", "inverse", or "off"): If "normal" (default), the delta indicator is shown as described above. If "inverse", it is red when positive and green when negative. If "off", delta is shown in gray regardless of its value.
* `help` (str or None): A tooltip that gets displayed next to the metric label.
* `label_visibility` ("visible", "hidden", or "collapsed"): The visibility of the label.
* `border` (bool): Whether to show a border around the metric container.
* `height` ("content", "stretch", or int): The height of the metric element.
* `width` ("stretch", "content", or int): The width of the metric element.
* `chart_data` (Iterable or None): A sequence of numeric values to display as a sparkline chart.
* `chart_type` ("line", "bar", or "area"): The type of sparkline chart to display.

### Examples

#### Example 1: Show a metric
```python
import streamlit as st

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
```
#### Example 2: Create a row of metrics
```python
import streamlit as st

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
```
#### Example 3: Modify the delta indicator
```python
import streamlit as st

st.metric(label="Gas price", value=4, delta=-0.5, delta_color="inverse")

st.metric(
    label="Active developers",
    value=123,
    delta=123,
    delta_color="off",
)
```
#### Example 4: Create a grid of metric cards
```python
import streamlit as st

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)
```
#### Example 5: Show sparklines
```python
import streamlit as st
from numpy.random import default_rng as rng

changes = list(rng(4).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)

row = st.container(horizontal=True)
with row:
    st.metric(
        "Line", 10, delta, chart_data=data, chart_type="line", border=True
    )
    st.metric(
        "Area", 10, delta, chart_data=data, chart_type="area", border=True
    )
    st.metric(
        "Bar", 10, delta, chart_data=data, chart_type="bar", border=True
    )
```