Here is the HTML content converted to clean Markdown:
### Layouts and Containers - Streamlit Docs
#### Documentation
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
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Layouts and containers](/develop/api-reference/layout)

Here is the HTML content converted to clean Markdown:

# Layouts and Containers
Streamlit provides several options for controlling how different elements are laid out on the screen.

## Complex layouts

### Columns
Insert containers laid out as side-by-side columns.
```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

### Container
Insert a multi-element container.
```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

### Modal dialog
Insert a modal dialog that can rerun independently from the rest of the script.
```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

### Empty
Insert a single-element container.
```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```

### Expander
Insert a multi-element container that can be expanded/collapsed.
```python
with st.expander("Open to see more"):
    st.write("This is more content")
```

### Popover
Insert a multi-element popover container that can be opened/closed.
```python
with st.popover("Settings"):
    st.checkbox("Show completed")
```

### Sidebar
Display items in a sidebar.
```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```

### Tabs
Insert containers separated into tabs.
```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

## Third-party components
These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

### Streamlit Elements
[Create a draggable and resizable dashboard in Streamlit.](https://github.com/okld/streamlit-elements)
```python
from streamlit_elements import elements, mui, html
with elements("new_element"):
    mui.Typography("Hello world")
```

### Pydantic
[Auto-generate Streamlit UI from Pydantic Models and Dataclasses.](https://github.com/lukasmasuch/streamlit-pydantic)
```python
import streamlit_pydantic as sp
sp.pydantic_form(key="my_form", model=ExampleModel)
```

### Streamlit Pages
[An experimental version of Streamlit Multi-Page Apps.](https://github.com/blackary/st_pages)
```python
from st_pages import Page, show_pages, add_page_title
show_pages([
    Page("streamlit_app.py", "Home", "🏠"),
    Page("other_pages/page2.py", "Page 2", ":books:"),
])
```

Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts. 

[Home](/)|[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)|[Community](https://discuss.streamlit.io)

[(GitHub)](https://github.com/streamlit)|[(YouTube)](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)|[(Twitter)](https://twitter.com/streamlit)|[(LinkedIn)](https://www.linkedin.com/company/streamlit)|[(Newsletter)](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

 2025 Snowflake Inc.[Cookie policy](#)