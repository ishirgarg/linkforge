Here is the converted text in clean Markdown format:
### st.progress - Streamlit Docs
![Logo](/logo.svg)

#### Documentation
### Search
[Get started](/get-started)
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

[Develop](/develop)
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ PAGE ELEMENTS
	+ [Write and magic](/develop/api-reference/write-magic)
	+ [Text elements](/develop/api-reference/text)
	+ [Data elements](/develop/api-reference/data)
	+ [Chart elements](/develop/api-reference/charts)
	+ [Input widgets](/develop/api-reference/widgets)
	+ [Media elements](/develop/api-reference/media)
	+ [Layouts and containers](/develop/api-reference/layout)
	+ [Chat elements](/develop/api-reference/chat)
	+ [Status elements](/develop/api-reference/status)
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
	+ [Third-party components](https://streamlit.io/components)
	+ APPLICATION LOGIC
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
	+ TOOLS
		- [App testing](/develop/api-reference/app-testing)
		- [Command line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

[Deploy](/deploy)
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

[Knowledge base](/knowledge-base)
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

### Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Status elements](/develop/api-reference/status)
* [st.progress](/develop/api-reference/status/st.progress)

## st.progress
Display a progress bar.

### Function signature
```python
st.progress(value, text=None, width="stretch")
```

### Parameters

* **value** (int or float): 0 <= value <= 100 for int, 0.0 <= value <= 1.0 for float
* **text** (str or None): A message to display above the progress bar, supporting GitHub-flavored Markdown (Bold, Italics, Strikethroughs, Inline Code, Links, and Images)
* **width** ("stretch" or int): The width of the progress element, either "stretch" (default) or an integer specifying the width in pixels

### Example
```python
import streamlit as st
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Rerun")
```
Note: I removed the unnecessary links and footers, and formatted the text to be more readable in Markdown. Let me know if you'd like me to make any further changes!