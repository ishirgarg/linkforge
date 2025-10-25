Here is the HTML converted to clean markdown:

# st.data_editor - Streamlit Docs
![Logo](/logo.svg)

## Documentation
### Search
Search

### Get Started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

### Develop
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ PAGE ELEMENTS
	+ [Write and magic](/develop/api-reference/write-magic)
	+ [Text elements](/develop/api-reference/text)
	+ [Data elements](/develop/api-reference/data)
		- [st.dataframe](/develop/api-reference/data/st.dataframe)
		- [st.data_editor](/develop/api-reference/data/st.data_editor)
		- [st.column_config](/develop/api-reference/data/st.column_config)
		- [st.table](/develop/api-reference/data/st.table)
		- [st.metric](/develop/api-reference/data/st.metric)
		- [st.json](/develop/api-reference/data/st.json)
	+ [Chart elements](/develop/api-reference/charts)
	+ [Input widgets](/develop/api-reference/widgets)
	+ [Media elements](/develop/api-reference/media)
	+ [Layouts and containers](/develop/api-reference/layout)
	+ [Chat elements](/develop/api-reference/chat)
	+ [Status elements](/develop/api-reference/status)
	+ [Third-party components](https://streamlit.io/components)
	+ APPLICATION LOGIC
	+ [Authentication and user info](/develop/api-reference/user)
	+ [Navigation and pages](/develop/api-reference/navigation)
	+ [Execution flow](/develop/api-reference/execution-flow)
	+ [Caching and state](/develop/api-reference/caching-and-state)
	+ [Connections and secrets](/develop/api-reference/connections)
	+ [Custom components](/develop/api-reference/custom-components)
	+ [Configuration](/develop/api-reference/configuration)
	+ TOOLS
	+ [App testing](/develop/api-reference/app-testing)
	+ [Command line](/develop/api-reference/cli)
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

### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Data elements](/develop/api-reference/data)
* [st.data_editor](/develop/api-reference/data/st.data_editor)

### Tip
This page only contains information on the `st.data_editor` API. For an overview of working with dataframes and to learn more about the data editor's capabilities and limitations, read [Dataframes](/develop/concepts/design/dataframes).

# st.data_editor
================================

Display a data editor widget.

The data editor widget allows you to edit dataframes and many other data structures in a table-like UI.

### Function Signature
```python
st.data_editor(
    data, 
    *, 
    width="stretch", 
    height="auto", 
    use_container_width=None, 
    hide_index=None, 
    column_order=None, 
    column_config=None, 
    num_rows="fixed", 
    disabled=False, 
    key=None, 
    on_change=None, 
    args=None, 
    kwargs=None, 
    row_height=None
)
```

### Parameters

* **data**: The data to edit in the data editor. Anything supported by `st.dataframe`.
* **width**: The width of the data editor. One of "stretch", "content", or an integer specifying the width in pixels.
* **height**: The height of the data editor. One of "auto" or an integer specifying the height in pixels.
* **use_container_width**: Whether to override width with the width of the parent container. (Deprecated)
* **hide_index**: Whether to hide the index column(s).
* **column_order**: The ordered list of columns to display.
* **column_config**: Configuration to customize how columns are displayed.
* **num_rows**: Specifies if the user can add and delete rows in the data editor. One of "fixed" or "dynamic".
* **disabled**: Controls the editing of columns. A boolean or an iterable of column names and/or positional indices.
* **key**: An optional string to use as the unique key for this widget.
* **on_change**: An optional callback invoked when this data_editor's value changes.
* **args**: An optional list or tuple of args to pass to the callback.
* **kwargs**: An optional dict of kwargs to pass to the callback.
* **row_height**: The height of each row in the data editor in pixels.

### Returns
The edited data. The edited data is returned in its original data type if it corresponds to any of the supported return types. All other data types are returned as a pandas DataFrame.

### Examples

#### Example 1: Basic usage
```python
import pandas as pd
import streamlit as st

df = pd.DataFrame([
    {"command": "st.selectbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3, "is_widget": True},
])

edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** ")
```

#### Example 2: Allowing users to add and delete rows
```python
import streamlit as st
import pandas as pd

df = pd.DataFrame([
    {"command": "st.selectbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3, "is_widget": True},
])

edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** ")
```

#### Example 3: Data editor configuration
```python
import pandas as pd
import streamlit as st

df = pd.DataFrame([
    {"command": "st.selectbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3, "is_widget": True},
])

edited_df = st.data_editor(
    df,
    column_config={
        "command": "Streamlit Command",
        "rating": st.column_config.NumberColumn(
            "Your rating",
            help="How much do you like this command (1-5)?",
            min_value=1,
            max_value=5,
            step=1,
            format="%d ",
        ),
        "is_widget": "Widget ?",
    },
    disabled=["command", "is_widget"],
    hide_index=True,
)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** ")
```

### Configuring columns
You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/develop/api-reference/data/st.column_config).