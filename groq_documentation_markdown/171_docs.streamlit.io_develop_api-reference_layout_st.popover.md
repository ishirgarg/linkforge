Here is the converted text in clean markdown:

# st.popover - Streamlit Docs

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
* [st.popover](/develop/api-reference/layout/st.popover)

Here is the converted text in clean Markdown:

## st.popover
### Overview
Insert a popover container. Inserts a multi-element container as a popover. It consists of a button-like element and a container that opens when the button is clicked.

### Behavior
Opening and closing the popover will not trigger a rerun. Interacting with widgets inside of an open popover will rerun the app while keeping the popover open. Clicking outside of the popover will close it.

### Usage
To add elements to the returned container, you can use the "with" notation (preferred) or just call methods directly on the returned object. See examples below.

### Note
To follow best design practices, don't nest popovers.

### Function Signature
```python
st.popover(label, *, help=None, icon=None, disabled=False, use_container_width=None, width="content")
```

### Parameters

* `label` (str): The label of the button that opens the popover container. The label can optionally contain GitHub-flavored Markdown.
* `help` (str or None): A tooltip that gets displayed when the popover button is hovered over. If this is None (default), no tooltip is displayed.
* `icon` (str): An optional emoji or icon to display next to the button label.
* `disabled` (bool): An optional boolean that disables the popover button if set to True. The default is False.
* `use_container_width` (bool): **Deprecated**. Use `width="stretch"` instead.
* `width` (int, "stretch", or "content"): The width of the button.

### Examples

You can use the with notation to insert any element into a popover:
```python
import streamlit as st

with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)
```
Or you can just call methods directly on the returned objects:
```python
import streamlit as st

popover = st.popover("Filter items")
red = popover.checkbox("Show red items.", True)
blue = popover.checkbox("Show blue items.", True)

if red:
    st.write(":red[This is a red item.]")
if blue:
    st.write(":blue[This is a blue item.]")
```