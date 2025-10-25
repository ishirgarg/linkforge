Here is the HTML content converted to clean Markdown:
### st.line_chart - Streamlit Docs

#### Documentation
[Search](/)

### Menu
* **Get started**
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* **Develop**
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- PAGE ELEMENTS
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
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
* **Deploy**
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* **Knowledge base**
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chart elements](/develop/api-reference/charts)
* [st.line_chart](/develop/api-reference/charts/st.line_chart)

Here is the cleaned-up Markdown version of the provided HTML text:

## st.line_chart
### Streamlit Version
1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Display a line chart.

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's Altair spec. As a result, this is easier to use for many "just plot this" scenarios, while being less customizable.

### Function signature
```python
st.line_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, width="stretch", height="content", use_container_width=None)
```

### Parameters
* `data`: Data to be plotted. Anything supported by `st.dataframe`.
* `x`: Column name or key associated to the x-axis data. If `x` is `None` (default), Streamlit uses the data index for the x-axis values.
* `y`: Column name(s) or key(s) associated to the y-axis data. If this is `None` (default), Streamlit draws the data of all remaining columns as data series. If this is a Sequence of strings, Streamlit draws several series on the same chart by melting your wide-format table into a long-format table behind the scenes.
* `x_label`: The label for the x-axis. If this is `None` (default), Streamlit will use the column name specified in `x` if available, or else no label will be displayed.
* `y_label`: The label for the y-axis. If this is `None` (default), Streamlit will use the column name(s) specified in `y` if available, or else no label will be displayed.
* `color`: The color to use for different lines in this chart.
* `width`: The width of the chart element. This can be one of the following:
	+ `"stretch"` (default): The width of the element matches the width of the parent container.
	+ `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.
* `height`: The height of the chart element. This can be one of the following:
	+ `"content"` (default): The height of the element matches the height of its content.
	+ `"stretch"`: The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content.
	+ An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled.
* `use_container_width`: (Deprecated) Whether to override width with the width of the parent container. If `use_container_width` is `True` (default), Streamlit sets the width of the chart to match the width of the parent container. If `use_container_width` is `False`, Streamlit sets the chart's width according to `width`.

### Examples
#### Example 1: Basic line chart from a dataframe
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.line_chart(df)
```

#### Example 2: Line chart from specific dataframe columns
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame({
    "col1": list(range(20)) * 3,
    "col2": rng(0).standard_normal(60),
    "col3": ["a"] * 20 + ["b"] * 20 + ["c"] * 20,
})
st.line_chart(df, x="col1", y="col2", color="col3")
```

#### Example 3: Line chart from wide-format dataframe
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.line_chart(df, x="a", y=["b", "c"], color=["#FF0000", "#0000FF"])
```

## element.add_rows
### Streamlit Version
1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Concatenate a dataframe to the bottom of the current one.

### Function signature
```python
element.add_rows(data=None, **kwargs)
```

### Parameters
* `data`: Table to concat. Optional.
* `**kwargs`: The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the `data` parameter).

### Example
```python
import time
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df1 = pd.DataFrame(rng(0).standard_normal(size=(50, 20)), columns=("col %d" % i for i in range(20)))
df2 = pd.DataFrame(rng(1).standard_normal(size=(50, 20)), columns=("col %d" % i for i in range(20)))

my_table = st.table(df1)
time.sleep(1)
my_table.add_rows(df2)
```

You can do the same thing with plots. For example, if you want to add more data to a line chart:
```python
my_chart = st.line_chart(df1)
time.sleep(1)
my_chart.add_rows(df2)
```
And for plots whose datasets are named, you can pass the data with a keyword argument where the key is the name:
```python
my_chart = st.vega_lite_chart({
    "mark": "line",
    "encoding": {"x": "a", "y": "b"},
    "datasets": {
        "some_fancy_name": df1,  # <-- named dataset
    },
    "data": {"name": "some_fancy_name"},
})
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
```