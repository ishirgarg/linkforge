Here is the HTML content converted to clean Markdown:

# st.toast - Streamlit Docs
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
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
			- CALLOUTS
			- [st.success](/develop/api-reference/status/st.success)
			- [st.info](/develop/api-reference/status/st.info)
			- [st.warning](/develop/api-reference/status/st.warning)
			- [st.error](/develop/api-reference/status/st.error)
			- [st.exception](/develop/api-reference/status/st.exception)
			- OTHER
			- [st.progress](/develop/api-reference/status/st.progress)
			- [st.spinner](/develop/api-reference/status/st.spinner)
			- [st.status](/develop/api-reference/status/st.status)
			- [st.toast](/develop/api-reference/status/st.toast)
			- [st.balloons](/develop/api-reference/status/st.balloons)
			- [st.snow](/develop/api-reference/status/st.snow)
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

### Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Status elements](/develop/api-reference/status)
* [st.toast](/develop/api-reference/status/st.toast)

Here is the HTML content converted to clean Markdown:

## st.toast
### Streamlit Version
1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Display a short message, known as a notification "toast". The toast appears in the app's top-right corner and disappears after four seconds.

**Warning:** `st.toast` is not compatible with Streamlit's [caching](https://docs.streamlit.io/develop/concepts/architecture/caching) and cannot be called within a cached function.

### Function signature
```python
st.toast(body, *, icon=None, duration="short")
```
### Parameters

* `body` (str): The string to display as GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).
* `icon` (str, None): An optional emoji or icon to display next to the alert. If `icon` is `None` (default), no icon is displayed. If `icon` is a string, the following options are valid:
	+ A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.
	+ An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case.
* `duration` ("short", "long", "infinite", or int): The time to display the toast message. This can be one of the following:
	+ "short" (default): Displays for 4 seconds.
	+ "long": Displays for 10 seconds.
	+ "infinite": Shows the toast until the user dismisses it.
	+ An integer: Displays for the specified number of seconds.

### Examples

#### Example 1: Show a toast message
```python
import streamlit as st
st.toast("Your edited image was saved!", icon="😍")
```

#### Example 2: Show multiple toasts
When multiple toasts are generated, they will stack. Hovering over a toast will stop it from disappearing. When hovering ends, the toast will disappear after time specified in `duration`.
```python
import time
import streamlit as st
if st.button("Three cheers"):
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hip!")
    time.sleep(0.5)
    st.toast("Hooray!", icon="🎉")
```

#### Example 3: Update a toast message
Toast messages can also be updated. Assign `st.toast(my_message)` to a variable and use the `.toast()` method to update it. If a toast has already disappeared or been dismissed, the update will not be seen.
```python
import time
import streamlit as st
def cook_breakfast():
    msg = st.toast("Gathering ingredients...")
    time.sleep(1)
    msg.toast("Cooking...")
    time.sleep(1)
    msg.toast("Ready!", icon="🥞")
if st.button("Cook breakfast"):
    cook_breakfast()
```