Here is the HTML converted to clean Markdown:

# Streamlit Docs

## Documentation

### Get Started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

### Develop
* [Concepts](/develop/concepts)
* [API Reference](/develop/api-reference)
	+ [Page Elements](#)
	+ [Write and Magic](/develop/api-reference/write-magic)
	+ [Text Elements](/develop/api-reference/text)
		- [st.title](/develop/api-reference/text/st.title)
		- [st.header](/develop/api-reference/text/st.header)
		- [st.subheader](/develop/api-reference/text/st.subheader)
		- [st.markdown](/develop/api-reference/text/st.markdown)
		- [Formatted Text](#)
			- [st.badge](/develop/api-reference/text/st.badge)
			- [st.caption](/develop/api-reference/text/st.caption)
			- [st.code](/develop/api-reference/text/st.code)
			- [st.divider](/develop/api-reference/text/st.divider)
			- [st.echo](/develop/api-reference/text/st.echo)
			- [st.latex](/develop/api-reference/text/st.latex)
			- [st.text](/develop/api-reference/text/st.text)
		- [Utilities](#)
			- [st.help](/develop/api-reference/text/st.help)
			- [st.html](/develop/api-reference/text/st.html)
	+ [Data Elements](/develop/api-reference/data)
	+ [Chart Elements](/develop/api-reference/charts)
	+ [Input Widgets](/develop/api-reference/widgets)
	+ [Media Elements](/develop/api-reference/media)
	+ [Layouts and Containers](/develop/api-reference/layout)
	+ [Chat Elements](/develop/api-reference/chat)
	+ [Status Elements](/develop/api-reference/status)
	+ [Third-party Components](https://streamlit.io/components)
	+ [Application Logic](#)
		- [Authentication and User Info](/develop/api-reference/user)
		- [Navigation and Pages](/develop/api-reference/navigation)
		- [Execution Flow](/develop/api-reference/execution-flow)
		- [Caching and State](/develop/api-reference/caching-and-state)
		- [Connections and Secrets](/develop/api-reference/connections)
		- [Custom Components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
	+ [Tools](#)
		- [App Testing](/develop/api-reference/app-testing)
		- [Command Line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick Reference](/develop/quick-reference)

### Deploy
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other Platforms](/deploy/tutorials)

### Knowledge Base
* [FAQ](/knowledge-base/using-streamlit)
* [Installing Dependencies](/knowledge-base/dependencies)
* [Deployment Issues](/knowledge-base/deploy)

[Home](/) | [Develop](/develop) | [API Reference](/develop/api-reference) | [Text Elements](/develop/api-reference/text) | [st.title](/develop/api-reference/text/st.title)

## st.title
Display text in title formatting.

Each document should have a single `st.title()`, although this is not enforced.

### Function Signature
```python
st.title(body, anchor=None, *, help=None, width="stretch")
```
### Parameters
* **body** (str): The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).
* **anchor** (str or False): The anchor name of the header that can be accessed with `#anchor` in the URL. If omitted, it generates an anchor using the body. If False, the anchor is not shown in the UI.
* **help** (str or None): A tooltip that gets displayed next to the title. If this is None (default), no tooltip is displayed.
* **width** ("stretch", "content", or int): The width of the title element. This can be one of the following:
	+ "stretch" (default): The width of the element matches the width of the parent container.
	+ "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Examples
```python
import streamlit as st

st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
```
Note: The `st.title` function is used to display text in title formatting. It can be used to create a single title for each document, although this is not enforced. The function takes in several parameters, including `body`, `anchor`, `help`, and `width`, which can be used to customize the title's appearance and behavior.