Here is the converted HTML to clean markdown:
### Streamlit Docs

[Logo](/logo.svg)

#### Documentation

### Search
Search

### Navigation
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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Layouts and containers](/develop/api-reference/layout)
* [st.container](/develop/api-reference/layout/st.container)

## st.container
Insert a multi-element container.

### Description
Inserts an invisible container into your app that can be used to hold multiple elements. This allows you to, for example, insert multiple elements into your app out of order.

### Function Signature
```python
st.container(
    *,
    border=None,
    key=None,
    width="stretch",
    height="content",
    horizontal=False,
    horizontal_alignment="left",
    vertical_alignment="top",
    gap="small"
)
```
### Parameters

* `border` (bool or None): Whether to show a border around the container. If None (default), a border is shown if the container is set to a fixed height and not shown otherwise.
* `key` (str or None): An optional string to give this container a stable identity. Additionally, if key is provided, it will be used as CSS class name prefixed with `st-key-`.
* `width` ("stretch" or int): The width of the container. This can be one of the following:
	+ "stretch" (default): The width of the container matches the width of the parent container.
	+ An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container.
* `height` ("content", "stretch", or int): The height of the container. This can be one of the following:
	+ "content" (default): The height of the container matches the height of its content.
	+ "stretch": The height of the container matches the height of its content or the height of the parent container, whichever is larger. If the container is not in a parent container, the height of the container matches the height of its content.
	+ An integer specifying the height in pixels: The container has a fixed height. If the content is larger than the specified height, scrolling is enabled.
* `horizontal` (bool): Whether to use horizontal flexbox layout. If this is False (default), the container's elements are laid out vertically. If this is True, the container's elements are laid out horizontally and will overflow to the next line if they don't fit within the container's width.
* `horizontal_alignment` ("left", "center", "right", or "distribute"): The horizontal alignment of the elements inside the container. This can be one of the following:
	+ "left" (default): Elements are aligned to the left side of the container.
	+ "center": Elements are horizontally centered inside the container.
	+ "right": Elements are aligned to the right side of the container.
	+ "distribute": Elements are distributed evenly in the container. This increases the horizontal gap between elements to fill the width of the container. A standalone element is aligned to the left.
* `vertical_alignment` ("top", "center", "bottom", or "distribute"): The vertical alignment of the elements inside the container. This can be one of the following:
	+ "top" (default): Elements are aligned to the top of the container.
	+ "center": Elements are vertically centered inside the container.
	+ "bottom": Elements are aligned to the bottom of the container.
	+ "distribute": Elements are distributed evenly in the container. This increases the vertical gap between elements to fill the height of the container. A standalone element is aligned to the top.
* `gap` ("small", "medium", "large", or None): The minimum gap size between the elements inside the container. This can be one of the following:
	+ "small" (default): 1rem gap between the elements.
	+ "medium": 2rem gap between the elements.
	+ "large": 4rem gap between the elements.
	+ None: No gap between the elements.

### Examples

#### Example 1: Inserting elements using `with` notation
```python
import streamlit as st

with st.container():
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")
```

#### Example 2: Inserting elements out of order
```python
import streamlit as st

container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")
container.write("This is inside too")
```

#### Example 3: Grid layout with columns and containers
```python
import streamlit as st

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")
```

#### Example 4: Vertically scrolling container
```python
import streamlit as st

long_text = "Lorem ipsum. " * 1000

with st.container(height=300):
    st.markdown(long_text)
```

#### Example 5: Horizontal container
```python
import streamlit as st

flex = st.container(horizontal=True, horizontal_alignment="right")

for card in range(3):
    flex.button(f"Button {card + 1}")
```