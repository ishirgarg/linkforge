Here is the HTML converted to clean markdown:
### st.status - Streamlit Docs
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

* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Status elements](/develop/api-reference/status)
* [st.status](/develop/api-reference/status/st.status)

## st.status
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Insert a status container to display output from long-running tasks.

The `st.status` function inserts a container into your app that is typically used to show the status and details of a process or task. The container can hold multiple elements and can be expanded or collapsed by the user similar to `st.expander`. When collapsed, all that is visible is the status icon and label.

The label, state, and expanded state can all be updated by calling `.update()` on the returned object. To add elements to the returned container, you can use `with` notation (preferred) or just call methods directly on the returned object.

By default, `st.status()` initializes in the "running" state. When called using `with` notation, it automatically updates to the "complete" state at the end of the `with` block.

**Note**: All content within the status container is computed and sent to the frontend, even if the status container is closed.

To follow best design practices and maintain a good appearance on all screen sizes, don't nest status containers.

### Function Signature
```python
st.status(label, *, expanded=False, state="running", width="stretch")
```
### Parameters

* `label` (str): The initial label of the status container. The label can optionally contain GitHub-flavored Markdown.
* `expanded` (bool): If True, initializes the status container in "expanded" state. Defaults to False (collapsed).
* `state` ("running", "complete", or "error"): The initial state of the status container which determines which icon is shown.
* `width` ("stretch" or int): The width of the status container.

### Returns

A mutable status container that can hold multiple elements. The label, state, and expanded state can be updated after creation via `.update()`.

### Examples

You can use the `with` notation to insert any element into an status container:
```python
import time
import streamlit as st

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
```
You can also use `.update()` on the container to change the label, state, or expanded state:
```python
import time
import streamlit as st

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(
        label="Download complete!", state="complete", expanded=False
    )
```
## StatusContainer.update
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Update the status container.

Only specified arguments are updated. Container contents and unspecified arguments remain unchanged.

### Function Signature
```python
StatusContainer.update(*, label=None, expanded=None, state=None)
```
### Parameters

* `label` (str or None): A new label of the status container. If None, the label is not changed.
* `expanded` (bool or None): The new expanded state of the status container. If None, the expanded state is not changed.
* `state` ("running", "complete", "error", or None): The new state of the status container. This mainly changes the icon. If None, the state is not changed.