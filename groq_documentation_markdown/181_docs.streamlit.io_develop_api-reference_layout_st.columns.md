Here is the converted HTML to clean markdown:

# st.columns - Streamlit Docs
![Logo](/logo.svg)

## Documentation
### Search

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
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
			- [st.columns](/develop/api-reference/layout/st.columns)
			- [st.container](/develop/api-reference/layout/st.container)
			- [st.dialog](/develop/api-reference/execution-flow/st.dialog)
			- [st.empty](/develop/api-reference/layout/st.empty)
			- [st.expander](/develop/api-reference/layout/st.expander)
			- [st.form](/develop/api-reference/execution-flow/st.form)
			- [st.popover](/develop/api-reference/layout/st.popover)
			- [st.sidebar](/develop/api-reference/layout/st.sidebar)
			- [st.tabs](/develop/api-reference/layout/st.tabs)
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

### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Layouts and containers](/develop/api-reference/layout)
* [st.columns](/develop/api-reference/layout/st.columns)

Here is the converted text in clean Markdown:

### st.columns
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Insert containers laid out as side-by-side columns.

Inserts a number of multi-element containers laid out side-by-side and returns a list of container objects.

To add elements to the returned containers, you can use the `with` notation (preferred) or just call methods directly on the returned object. See examples below.

**Note**: To follow best design practices and maintain a good appearance on all screen sizes, don't nest columns more than once.

#### Function signature

`st.columns(spec, *, gap="small", vertical_alignment="top", border=False, width="stretch")`

* `spec` (int or Iterable of numbers): Controls the number and width of columns to insert.
	+ An integer that specifies the number of columns. All columns have equal width in this case.
	+ An Iterable of numbers (int or float) that specify the relative width of each column.
* `gap` ("small", "medium", "large", or None): The size of the gap between the columns.
* `vertical_alignment` ("top", "center", or "bottom"): The vertical alignment of the content inside the columns.
* `border` (bool): Whether to show a border around the column containers.
* `width` (int or "stretch"): The desired width of the columns expressed in pixels.

#### Returns

A list of container objects.

#### Examples

##### Example 1: Use context management

You can use the `with` statement to insert any element into a column:
```python
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
```

##### Example 2: Use commands as container methods

You can just call methods directly on the returned objects:
```python
import streamlit as st
from numpy.random import default_rng as rng

df = rng(0).standard_normal((10, 1))
col1, col2 = st.columns([3, 1])

col1.subheader("A wide column with a chart")
col1.line_chart(df)

col2.subheader("A narrow column with the data")
col2.write(df)
```

##### Example 3: Align widgets

Use `vertical_alignment="bottom"` to align widgets:
```python
import streamlit as st

left, middle, right = st.columns(3, vertical_alignment="bottom")

left.text_input("Write something")
middle.button("Click me", use_container_width=True)
right.checkbox("Check me")
```

##### Example 4: Use vertical alignment to create grids

Adjust vertical alignment to customize your grid layouts:
```python
import streamlit as st

vertical_alignment = st.selectbox(
    "Vertical alignment", ["top", "center", "bottom"], index=2
)

left, middle, right = st.columns(3, vertical_alignment=vertical_alignment)
left.image("https://static.streamlit.io/examples/cat.jpg")
middle.image("https://static.streamlit.io/examples/dog.jpg")
right.image("https://static.streamlit.io/examples/owl.jpg")
```

##### Example 5: Add borders

Add borders to your columns instead of nested containers for consistent heights:
```python
import streamlit as st

left, middle, right = st.columns(3, border=True)

left.markdown("Lorem ipsum " * 10)
middle.markdown("Lorem ipsum " * 5)
right.markdown("Lorem ipsum ")
```

Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts. 

[Home](/) | [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20) | [Community](https://discuss.streamlit.io)

GitHub | YouTube | Twitter | LinkedIn | Newsletter

&copy; 2025 Snowflake Inc. Cookie policy