Here is the converted markdown:
### st.code - Streamlit Docs
![logo](/logo.svg)
#### Documentation
### Search
#### Get started
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)
#### Develop
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ PAGE ELEMENTS
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
	* [Tutorials](/develop/tutorials)
	* [Quick reference](/develop/quick-reference)
#### Deploy
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)
#### Knowledge base
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)
### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Text elements](/develop/api-reference/text)
* [st.code](/develop/api-reference/text/st.code)

## st.code
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Display a code block with optional syntax highlighting.

### Function signature
```python
st.code(body, language="python", *, line_numbers=False, wrap_lines=False, height="content", width="stretch")
```
### Parameters

* `body` (str): The string to display as code or monospace text.
* `language` (str or None): The language that the code is written in, for syntax highlighting. Defaults to "python". If this is None, the code will be plain, monospace text.
* `line_numbers` (bool): An optional boolean indicating whether to show line numbers to the left of the code block. Defaults to False.
* `wrap_lines` (bool): An optional boolean indicating whether to wrap lines. Defaults to False.
* `height` ("content", "stretch", or int): The height of the code block element.
	+ "content" (default): The height of the element matches the height of its content.
	+ "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger.
	+ An integer specifying the height in pixels: The element has a fixed height.
* `width` ("stretch", "content", or int): The width of the code block element.
	+ "stretch" (default): The width of the element matches the width of the parent container.
	+ "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width.

### Note
Use scrolling containers sparingly. If you use scrolling containers, avoid heights that exceed 500 pixels. Otherwise, the scroll surface of the container might cover the majority of the screen on mobile devices, which makes it hard to scroll the rest of the app.

### Examples
```python
import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")
```

```python
import streamlit as st
code = '''Is it a crown or boat?
                        ii
                      iiiiii
WWw                 .iiiiiiii.                ...:
 WWWWWWw          .iiiiiiiiiiii.         ........
  WWWWWWWWWWw    iiiiiiiiiiiiiiii    ...........
   WWWWWWWWWWWWWWwiiiiiiiiiiiiiiiii............
    WWWWWWWWWWWWWWWWWWWWwiiiiiiiiiiiiii.........
     WWWWWWWWWWWWWWWWWWWWWWWWwiiiiiii....
      WWWWWWWWWWWWWWWWWWWWWWWWWWWWwiiii.
       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWwiiii.
          -MMMWWWWWWWWWWWWWWWWWWWWWWMMM-'''
st.code(code, language=None)
```
For more information, visit the [Streamlit forums](https://discuss.streamlit.io) or check out the [Streamlit documentation](https://streamlit.io).