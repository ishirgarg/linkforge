Here is the converted markdown:

# Streamlit Docs

## Documentation

### Search
Search

### Navigation
* [Get Started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First Steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API Reference](/develop/api-reference)
		- [Page Elements](#)
		- [Write and Magic](/develop/api-reference/write-magic)
		- [Text Elements](/develop/api-reference/text)
			- [Headings and Body](#)
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
		- [Data Elements](/develop/api-reference/data)
		- [Chart Elements](/develop/api-reference/charts)
		- [Input Widgets](/develop/api-reference/widgets)
		- [Media Elements](/develop/api-reference/media)
		- [Layouts and Containers](/develop/api-reference/layout)
		- [Chat Elements](/develop/api-reference/chat)
		- [Status Elements](/develop/api-reference/status)
		- [Third-Party Components](https://streamlit.io/components)
		- [Application Logic](#)
		- [Authentication and User Info](/develop/api-reference/user)
		- [Navigation and Pages](/develop/api-reference/navigation)
		- [Execution Flow](/develop/api-reference/execution-flow)
		- [Caching and State](/develop/api-reference/caching-and-state)
		- [Connections and Secrets](/develop/api-reference/connections)
		- [Custom Components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- [Tools](#)
		- [App Testing](/develop/api-reference/app-testing)
		- [Command Line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick Reference](/develop/quick-reference)
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other Platforms](/deploy/tutorials)
* [Knowledge Base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing Dependencies](/knowledge-base/dependencies)
	+ [Deployment Issues](/knowledge-base/deploy)

### Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API Reference](/develop/api-reference)
* [Text Elements](/develop/api-reference/text)
* [st.badge](/develop/api-reference/text/st.badge)

## st.badge
### Streamlit Version
1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Display a colored badge with an icon and label.

This is a thin wrapper around the color-badge Markdown directive. The following are equivalent:
* `st.markdown(":blue-badge[Home]")`
* `st.badge("Home", color="blue")`

Note: You can insert badges everywhere Streamlit supports Markdown by using the color-badge Markdown directive. See `st.markdown` for more information.

### Function signature
```python
st.badge(label, *, icon=None, color="blue", width="content")
```

### Parameters
* `label` (str): The label to display in the badge. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code.
* `icon` (str or None): An optional emoji or icon to display next to the badge label. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid:
	+ A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.
	+ An icon from the Material Symbols library (rounded style) in the format `:material/icon_name:` where `icon_name` is the name of the icon in snake case.
* `color` (str): The color to use for the badge. This defaults to "blue". This can be one of the following supported colors: red, orange, yellow, blue, green, violet, gray/grey, or primary.
* `width` ("content", "stretch", or int): The width of the badge element. This can be one of the following:
	+ "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
	+ "stretch": The width of the element matches the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Examples
Create standalone badges with `st.badge` (with or without icons). If you want to have multiple, side-by-side badges, you can use the Markdown directive in `st.markdown`.
```python
import streamlit as st

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)
```