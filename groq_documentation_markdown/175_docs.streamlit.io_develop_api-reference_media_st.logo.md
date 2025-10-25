Here is the HTML content converted to clean Markdown:

# st.logo - Streamlit Docs
![logo](/logo.svg)

## Documentation

### Search
Search

### Menu
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
			- [st.audio](/develop/api-reference/media/st.audio)
			- [st.image](/develop/api-reference/media/st.image)
			- [st.logo](/develop/api-reference/media/st.logo)
			- [st.pdf](/develop/api-reference/media/st.pdf)
			- [st.video](/develop/api-reference/media/st.video)
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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Media elements](/develop/api-reference/media)
* [st.logo](/develop/api-reference/media/st.logo)

## st.logo
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Renders a logo in the upper-left corner of your app and its sidebar.

If `st.logo` is called multiple times within a page, Streamlit will render the image passed in the last call. For the most consistent results, call `st.logo` early in your page script and choose an image that works well in both light and dark mode. Avoid empty margins around your image.

If your logo does not work well for both light and dark mode, consider setting the theme and hiding the settings menu from users with the [configuration option](https://docs.streamlit.io/develop/api-reference/configuration/config.toml) `client.toolbarMode="minimal"`.

### Function signature
```python
st.logo(image, *, size="medium", link=None, icon_image=None)
```

### Parameters

* `image`: The image to display in the upper-left corner of your app and its sidebar. This can be any of the types supported by `st.image` except a list. If `icon_image` is also provided, then Streamlit will only display `image` in the sidebar.
* `size`: The size of the image displayed in the upper-left corner of the app and its sidebar. The possible values are:
	+ "small": 20px max height
	+ "medium" (default): 24px max height
	+ "large": 32px max height
* `link`: The external URL to open when a user clicks on the logo. The URL must start with "http://" or "https://". If `link` is `None` (default), the logo will not include a hyperlink.
* `icon_image`: An optional, typically smaller image to replace `image` in the upper-left corner when the sidebar is closed. This can be any of the types supported by `st.image` except a list. If `icon_image` is `None` (default), Streamlit will always display `image` in the upper-left corner, regardless of whether the sidebar is open or closed. Otherwise, Streamlit will render `icon_image` in the upper-left corner of the app when the sidebar is closed.

### Examples

A common design practice is to use a wider logo in the sidebar, and a smaller, icon-styled logo in your app's main body.
```python
import streamlit as st

st.logo(
    LOGO_URL_LARGE,
    link="https://streamlit.io/gallery",
    icon_image=LOGO_URL_SMALL,
)
```

Try switching logos around in the following example:
```python
import streamlit as st

HORIZONTAL_RED = "images/horizontal_red.png"
ICON_RED = "images/icon_red.png"
HORIZONTAL_BLUE = "images/horizontal_blue.png"
ICON_BLUE = "images/icon_blue.png"

options = [HORIZONTAL_RED, ICON_RED, HORIZONTAL_BLUE, ICON_BLUE]
sidebar_logo = st.selectbox("Sidebar logo", options, 0)
main_body_logo = st.selectbox("Main body logo", options, 1)

st.logo(sidebar_logo, icon_image=main_body_logo)
st.sidebar.markdown("Hi!")
```