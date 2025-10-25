Here is the HTML content converted to clean markdown:

## st.dataframe - Streamlit Docs
#### Documentation

### Menu
* **Get started**
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* **Develop**
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
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
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Data elements](/develop/api-reference/data)
* [st.dataframe](/develop/api-reference/data/st.dataframe)

#### Tip
Learn more in our [Dataframes](/develop/concepts/design/dataframes) guide and check out our tutorial, [Get dataframe row-selections from users](/develop/tutorials/elements/dataframe-row-selections).

Here is the content converted to clean markdown:
### st.dataframe
#### Display a dataframe as an interactive table.

This command works with a wide variety of collection-like and dataframe-like object types.

##### Function signature
```python
st.dataframe(
    data=None, 
    width="stretch", 
    height="auto", 
    *, 
    use_container_width=None, 
    hide_index=None, 
    column_order=None, 
    column_config=None, 
    key=None, 
    on_select="ignore", 
    selection_mode="multi-row", 
    row_height=None
)
```
##### Parameters

* `data`: The data to display. Dataframe-like objects include dataframe and series objects from popular libraries like Dask, Modin, Numpy, pandas, Polars, PyArrow, Snowpark, Xarray, and more.
* `width`: The width of the dataframe element. This can be one of the following: 
    * "stretch" (default): The width of the element matches the width of the parent container.
    * "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    * An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.
* `height`: The height of the dataframe element. This can be one of the following:
    * "auto" (default): Streamlit sets the height to show at most ten rows.
    * An integer specifying the height in pixels: The element has a fixed height.
* `use_container_width`: _delete_ use_container_width is deprecated and will be removed in a future release. For use_container_width=True, use width="stretch".
* `hide_index`: Whether to hide the index column(s). If hide_index is None (default), the visibility of index columns is automatically determined based on the data.
* `column_order`: The ordered list of columns to display. If this is None (default), Streamlit displays all columns in the order inherited from the underlying data structure.
* `column_config`: Configuration to customize how columns are displayed. If this is None (default), columns are styled based on the underlying data type of each column.
* `key`: An optional string to use for giving this element a stable identity. If key is None (default), this element's identity will be determined based on the values of the other parameters.
* `on_select`: How the dataframe should respond to user selection events. This controls whether or not the dataframe behaves like an input widget.
* `selection_mode`: The types of selections Streamlit should allow when selections are enabled with on_select.
* `row_height`: The height of each row in the dataframe in pixels. If row_height is None (default), Streamlit will use a default row height, which fits one line of text.

##### Returns
If on_select is "ignore" (default), this command returns an internal placeholder for the dataframe element that can be used with the .add_rows() method. Otherwise, this command returns a dictionary-like object that supports both key and attribute notation.

#### Examples

##### Example 1: Display a dataframe
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((50, 20)), columns=("col %d" % i for i in range(20))
)

st.dataframe(df)
```

##### Example 2: Use Pandas Styler
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((10, 20)), columns=("col %d" % i for i in range(20))
)

st.dataframe(df.style.highlight_max(axis=0))
```

##### Example 3: Use column configuration
```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
        ],
        "stars": rng(0).integers(0, 1000, size=3),
        "views_history": rng(0).integers(0, 5000, size=(3, 30)).tolist(),
    }
)

st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
```

### Dataframe selections

#### DataframeState

The schema for the dataframe event state.

##### Attributes

* `selection`: The state of the on_select event.

#### DataframeSelectionState

The schema for the dataframe selection state.

##### Attributes

* `rows`: The selected rows, identified by their integer position.
* `columns`: The selected columns, identified by their names.
* `cells`: The selected cells, provided as a tuple of row integer position and column name.

#### Example

```python
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((12, 5)), columns=["a", "b", "c", "d", "e"]
)

event = st.dataframe(
    df,
    key="data",
    on_select="rerun",
    selection_mode=["multi-row", "multi-column", "multi-cell"],
)

event.selection
```

### element.add_rows

Concatenate a dataframe to the bottom of the current one.

#### Function signature
```python
element.add_rows(data=None, **kwargs)
```

#### Parameters

* `data`: Table to concat. Optional.
* `**kwargs`: The named dataset to concat. Optional.

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

### Interactivity

Dataframes displayed with `st.dataframe` are interactive. End users can sort, resize, search, and copy data to their clipboard.

### Configuring columns

You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/develop/api-reference/data/st.column_config).