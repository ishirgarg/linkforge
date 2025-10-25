Here is the HTML content converted to clean Markdown:

# st.caption - Streamlit Docs
![Logo](/logo.svg)

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
				- HEADINGS AND BODY
				- [st.title](/develop/api-reference/text/st.title)
				- [st.header](/develop/api-reference/text/st.header)
				- [st.subheader](/develop/api-reference/text/st.subheader)
				- [st.markdown](/develop/api-reference/text/st.markdown)
				- FORMATTED TEXT
				- [st.badge](/develop/api-reference/text/st.badge)
				- [st.caption](/develop/api-reference/text/st.caption)
				- [st.code](/develop/api-reference/text/st.code)
				- [st.divider](/develop/api-reference/text/st.divider)
				- [st.echo](/develop/api-reference/text/st.echo)
				- [st.latex](/develop/api-reference/text/st.latex)
				- [st.text](/develop/api-reference/text/st.text)
				- UTILITIES
				- [st.help](/develop/api-reference/text/st.help)
				- [st.html](/develop/api-reference/text/st.html)
			- [Data elements](/develop/api-reference/data)
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
		- [Tutorials](/develop/tutorials)
		- [Quick reference](/develop/quick-reference)
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
* [Text elements](/develop/api-reference/text)
* [st.caption](/develop/api-reference/text/st.caption)

Here is the HTML converted to clean markdown:
### st.caption
Display text in small font.

This should be used for captions, asides, footnotes, sidenotes, and other explanatory text.

#### Function Signature
```python
st.caption(body, unsafe_allow_html=False, *, help=None, width="stretch")
```
#### Parameters
* **body** (str): The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm.
* **unsafe_allow_html** (bool): Whether to render HTML within body. If this is False (default), any HTML tags found in body will be escaped and therefore treated as raw text. If this is True, any HTML expressions within body will be rendered.
* **help** (str or None): A tooltip that gets displayed next to the caption. If this is None (default), no tooltip is displayed.
* **width** ("stretch", "content", or int): The width of the caption element. This can be one of the following:
  * "stretch" (default): The width of the element matches the width of the parent container.
  * "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
  * An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Examples
```python
import streamlit as st

st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
```
### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

Note: I removed the unnecessary links and images, and reformatted the text to make it more readable. I also removed the footer information as it is not relevant to the documentation of the `st.caption` function.