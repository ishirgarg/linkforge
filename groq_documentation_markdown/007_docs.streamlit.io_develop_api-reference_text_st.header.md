Here is the HTML converted to clean markdown:
### st.header - Streamlit Docs
![logo](/logo.svg)
#### Documentation
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
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

[Home](/)/
[Develop](/develop)/
[API reference](/develop/api-reference)/
[Text elements](/develop/api-reference/text)/
[st.header](/develop/api-reference/text/st.header)

## st.header
### Streamlit Version
Version 1.50.0, Version 1.49.0, Version 1.48.0, Version 1.47.0, Version 1.46.0, Version 1.45.0, Version 1.44.0, Version 1.43.0, Version 1.42.0, Version 1.41.0, Version 1.40.0, Version 1.39.0, Version 1.38.0, Version 1.37.0, Version 1.36.0, Version 1.35.0, Version 1.34.0, Version 1.33.0, Version 1.32.0, Version 1.31.0, Version 1.30.0, Version 1.29.0, Version 1.28.0, Version 1.27.0, Version 1.26.0, Version 1.25.0, Version 1.24.0, Version 1.23.0, Version 1.22.0

Display text in header formatting.

### Function signature
[View st.header source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/heading.py#L45)

```python
st.header(body, anchor=None, *, help=None, divider=False, width="stretch")
```

### Parameters
* **body** (str): The text to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).
* **anchor** (str or False): The anchor name of the header that can be accessed with #anchor in the URL. If omitted, it generates an anchor using the body. If False, the anchor is not shown in the UI.
* **help** (str or None): A tooltip that gets displayed next to the header. If this is None (default), no tooltip is displayed.
* **divider** (bool, "blue", "green", "orange", "red", "violet", "yellow", "gray"/"grey", or "rainbow"): Shows a colored divider below the header. If this is True, successive headers will cycle through divider colors, except gray and rainbow.
* **width** ("stretch", "content", or int): The width of the header element. This can be one of the following:
  + "stretch" (default): The width of the element matches the width of the parent container.
  + "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
  + An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Examples
```python
import streamlit as st

st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)
```

For more information and examples, please visit the [Streamlit documentation](https://docs.streamlit.io). 

If you have any questions or need further assistance, please don't hesitate to [contact us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20) or [join our community forum](https://discuss.streamlit.io).