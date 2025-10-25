Here is the HTML content converted to clean markdown:

### st.area_chart - Streamlit Docs

#### Documentation

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

### Navigation

* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Chart elements](/develop/api-reference/charts)
* [st.area_chart](/develop/api-reference/charts/st.area_chart)

Here is the cleaned-up version of the HTML in Markdown format:

## st.area_chart
### Description
Display an area chart.

This is a syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's Altair spec. As a result, this is easier to use for many "just plot this" scenarios, while being less customizable.

### Function Signature
```python
st.area_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, stack=None, width=None, height=None, use_container_width=True)
```
### Parameters

* `data`: Data to be plotted. Can be anything supported by `st.dataframe`.
* `x`: Column name or key associated to the x-axis data. If `x` is `None` (default), Streamlit uses the data index for the x-axis values.
* `y`: Column name(s) or key(s) associated to the y-axis data. If this is `None` (default), Streamlit draws the data of all remaining columns as data series. If this is a sequence of strings, Streamlit draws several series on the same chart by melting your wide-format table into a long-format table behind the scenes.
* `x_label`: The label for the x-axis. If this is `None` (default), Streamlit will use the column name specified in `x` if available, or else no label will be displayed.
* `y_label`: The label for the y-axis. If this is `None` (default), Streamlit will use the column name(s) specified in `y` if available, or else no label will be displayed.
* `color`: The color to use for different series in this chart.
* `stack`: Whether to stack the areas. If this is `None` (default), Streamlit uses Vega's default.
* `width`: Desired width of the chart expressed in pixels. If `width` is `None` (default), Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container.
* `height`: Desired height of the chart expressed in pixels. If `height` is `None` (default), Streamlit sets the height of the chart to fit its contents according to the plotting library.
* `use_container_width`: Whether to override `width` with the width of the parent container.

### Examples

#### Example 1: Basic area chart from a dataframe
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.area_chart(df)
```

#### Example 2: Area chart from specific dataframe columns
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame({
    "col1": list(range(20)) * 3,
    "col2": rng(0).standard_normal(60),
    "col3": ["a"] * 20 + ["b"] * 20 + ["c"] * 20,
})
st.area_chart(df, x="col1", y="col2", color="col3")
```

#### Example 3: Area chart from wide-format dataframe
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame({
    "col1": list(range(20)),
    "col2": rng(0).standard_normal(20),
    "col3": rng(1).standard_normal(20),
})
st.area_chart(df, x="col1", y=["col2", "col3"], color=["#FF000080", "#0000FF80"])
```

#### Example 4: Area chart with different stacking
```python
import streamlit as st
from vega_datasets import data

df = data.unemployment_across_industries()
st.area_chart(df, x="date", y="count", color="series", stack="center")
```

## element.add_rows
### Description
Concatenate a dataframe to the bottom of the current one.

### Function Signature
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