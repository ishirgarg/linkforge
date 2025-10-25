Here is the converted markdown:

# st.table - Streamlit Docs
![logo](/logo.svg)

## Documentation
### Search
Search

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
* **Deploy**
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* **Knowledge base**
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Tip
Static tables with `st.table` are the most basic way to display dataframes. For the majority of cases, we recommend using [`st.dataframe`](/develop/api-reference/data/st.dataframe) to display interactive dataframes, and [`st.data_editor`](/develop/api-reference/data/st.data_editor) to let users edit dataframes.

## st.table
Display a static table.

While st.dataframe is geared towards large datasets and interactive data exploration, st.table is useful for displaying small, styled tables without sorting or scrolling. For example, st.table may be the preferred way to display a confusion matrix or leaderboard. Additionally, st.table supports Markdown.

### Function signature
```python
st.table(data=None, *, border=True)
```

### Parameters

* `data` (Anything supported by st.dataframe): The table data.
* `border` (bool or "horizontal"): Whether to show borders around the table and between cells.

### Examples

#### Example 1: Display a confusion matrix as a static table
```python
import pandas as pd
import streamlit as st

confusion_matrix = pd.DataFrame({
    "Predicted Cat": [85, 3, 2, 1],
    "Predicted Dog": [2, 78, 4, 0],
    "Predicted Bird": [1, 5, 72, 3],
    "Predicted Fish": [0, 2, 1, 89],
}, index=["Actual Cat", "Actual Dog", "Actual Bird", "Actual Fish"])
st.table(confusion_matrix)
```

#### Example 2: Display a product leaderboard with Markdown and horizontal borders
```python
import streamlit as st

product_data = {
    "Product": [
        ":material/devices: Widget Pro",
        ":material/smart_toy: Smart Device",
        ":material/inventory: Premium Kit",
    ],
    "Category": [":blue[Electronics]", ":green[IoT]", ":violet[Bundle]"],
    "Stock": [" Full", " Low", " Empty"],
    "Units sold": [1247, 892, 654],
    "Revenue": [125000, 89000, 98000]
}
st.table(product_data, border="horizontal")
```

## element.add_rows
Concatenate a dataframe to the bottom of the current one.

### Function signature
```python
element.add_rows(data=None, **kwargs)
```

### Parameters

* `data` (pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None): Table to concat. Optional.
* `**kwargs` (pandas.DataFrame, numpy.ndarray, Iterable, dict, or None): The named dataset to concat. Optional.

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