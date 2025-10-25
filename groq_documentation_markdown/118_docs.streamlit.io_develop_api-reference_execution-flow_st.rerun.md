Here is the converted HTML to clean markdown:

# st.rerun - Streamlit Docs

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
				- [st.dialog](/develop/api-reference/execution-flow/st.dialog)
				- [st.form](/develop/api-reference/execution-flow/st.form)
				- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
				- [st.fragment](/develop/api-reference/execution-flow/st.fragment)
				- [st.rerun](/develop/api-reference/execution-flow/st.rerun)
				- [st.stop](/develop/api-reference/execution-flow/st.stop)
			- [Caching and state](/develop/api-reference/caching-and-state)
			- [Connections and secrets](/develop/api-reference/connections)
			- [Custom components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- TOOLS
			- [App testing](/develop/api-reference/app-testing)
			- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
* **Deploy**
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* **Knowledge base**
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Execution flow](/develop/api-reference/execution-flow)
* [st.rerun](/develop/api-reference/execution-flow/st.rerun)

## st.rerun
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Rerun the script immediately.

When `st.rerun()` is called, Streamlit halts the current script run and executes no further statements. Streamlit immediately queues the script to rerun.

When using `st.rerun` in a fragment, you can scope the rerun to the fragment. However, if a fragment is running as part of a full-app rerun, a fragment-scoped rerun is not allowed.

### Function signature
```python
st.rerun(*, scope="app")
```
#### Parameters

* `scope` ("app" or "fragment"): Specifies what part of the app should rerun. If `scope` is "app" (default), the full app reruns. If `scope` is "fragment", Streamlit only reruns the fragment from which this command is called.

Setting `scope="fragment"` is only valid inside a fragment during a fragment rerun. If `st.rerun(scope="fragment")` is called during a full-app rerun or outside of a fragment, Streamlit will raise a `StreamlitAPIException`.

### Caveats for `st.rerun`
`st.rerun` is one of the tools to control the logic of your app. While it is great for prototyping, there can be adverse side effects:

* Additional script runs may be inefficient and slower.
* Excessive reruns may complicate your app's logic and be harder to follow.
* If misused, infinite looping may crash your app.

In many cases where `st.rerun` works, [callbacks](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state) may be a cleaner alternative. [Containers](https://docs.streamlit.io/develop/api-reference/layout) may also be helpful.

### A simple example in three variations
#### Using `st.rerun` to update an earlier header
```python
import streamlit as st
if "value" not in st.session_state:
    st.session_state.value = "Title"
st.header(st.session_state.value)
if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()
```

#### Using a callback to update an earlier header
```python
st.header(st.session_state.value)
def update_value():
    st.session_state.value = "Bar"
st.button("Bar", on_click=update_value)
```

#### Using containers to update an earlier header
```python
container = st.container()
if st.button("Baz"):
    st.session_state.value = "Baz"
container.header(st.session_state.value)
```
Still have questions? Check out our [forums](https://discuss.streamlit.io) for helpful information and Streamlit experts.