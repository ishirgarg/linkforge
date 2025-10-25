Here is the HTML converted to clean Markdown:

# st.latex - Streamlit Docs
![logo](/logo.svg)

## Documentation
_search_

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

## Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Text elements](/develop/api-reference/text)
* [st.latex](/develop/api-reference/text/st.latex)

## st.latex
Display mathematical expressions formatted as LaTeX.

Supported LaTeX functions are listed at [https://katex.org/docs/supported.html](https://katex.org/docs/supported.html).

### Function Signature
```python
st.latex(body, *, help=None, width="stretch")
```
### Parameters

* **body** (str or SymPy expression): The string or SymPy expression to display as LaTeX. If str, it's a good idea to use raw Python strings since LaTeX uses backslashes a lot.
* **help** (str or None): A tooltip that gets displayed next to the LaTeX expression. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown.
* **width** ("stretch", "content", or int): The width of the LaTeX element. This can be one of the following:
  * "stretch" (default): The width of the element matches the width of the parent container.
  * "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
  * An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Example
```python
import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \\cdots + a r^{n-1} =
    \\sum\_{k=0}^{n-1} ar^k =
    a \\left(\\frac{1-r^{n}}{1-r}\\right)
    ''')
```
For more information and support, visit the [Streamlit forums](https://discuss.streamlit.io). 

You can also check out the [Streamlit documentation](https://docs.streamlit.io) for more details on how to use st.latex and other Streamlit functions. 

Additionally, you can find more resources and information on the [Streamlit website](https://www.streamlit.io). 

Please note that the information provided is based on the data available up to the cutting knowledge date of December 2023, and may not reflect any changes or updates made after that date. As of today, October 25, 2025, the provided information should still be relevant and accurate.