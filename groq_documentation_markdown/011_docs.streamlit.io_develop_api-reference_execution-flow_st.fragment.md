Here is the HTML content converted to clean Markdown:

# st.fragment - Streamlit Docs

![logo](/logo.svg)

## Documentation

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
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

[Home](/)  
[Develop](/develop)  
[API reference](/develop/api-reference)  
[Execution flow](/develop/api-reference/execution-flow)  
[st.fragment](/develop/api-reference/execution-flow/st.fragment)

## st.fragment
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Decorator to turn a function into a fragment which can rerun independently of the full app.

When a user interacts with an input widget created inside a fragment, Streamlit only reruns the fragment instead of the full app. If `run_every` is set, Streamlit will also rerun the fragment at the specified interval while the session is active, even if the user is not interacting with your app.

To trigger an app rerun from inside a fragment, call `st.rerun()` directly. To trigger a fragment rerun from within itself, call `st.rerun(scope="fragment")`. Any values from the fragment that need to be accessed from the wider app should generally be stored in Session State.

When Streamlit element commands are called directly in a fragment, the elements are cleared and redrawn on each fragment rerun, just like all elements are redrawn on each app rerun. The rest of the app is persisted during a fragment rerun. When a fragment renders elements into externally created containers, the elements will not be cleared with each fragment rerun. Instead, elements will accumulate in those containers with each fragment rerun, until the next app rerun.

Calling `st.sidebar` in a fragment is not supported. To write elements to the sidebar with a fragment, call your fragment function inside a `with st.sidebar` context manager.

Fragment code can interact with Session State, imported modules, and other Streamlit elements created outside the fragment. Note that these interactions are additive across multiple fragment reruns. You are responsible for handling any side effects of that behavior.

### Warning
* Fragments can only contain widgets in their main body. Fragments can't render widgets to externally created containers.

### Function signature
```python
st.fragment(func=None, *, run_every=None)
```
#### Parameters
* `func` (callable): The function to turn into a fragment.
* `run_every` (int, float, timedelta, str, or None): The time interval between automatic fragment reruns.

### Examples

#### Basic usage of `@st.fragment`
```python
import streamlit as st
import time

@st.fragment
def release_the_balloons():
    st.button("Release the balloons", help="Fragment rerun")
    st.balloons()

with st.spinner("Inflating balloons..."):
    time.sleep(5)
release_the_balloons()
st.button("Inflate more balloons", help="Full rerun")
```

#### Updating elements inside and outside of a fragment
```python
import streamlit as st

if "app_runs" not in st.session_state:
    st.session_state.app_runs = 0
    st.session_state.fragment_runs = 0

@st.fragment
def my_fragment():
    st.session_state.fragment_runs += 1
    st.button("Rerun fragment")
    st.write(f"Fragment says it ran {st.session_state.fragment_runs} times.")

st.session_state.app_runs += 1
my_fragment()
st.button("Rerun full app")
st.write(f"Full app says it ran {st.session_state.app_runs} times.")
st.write(f"Full app sees that fragment ran {st.session_state.fragment_runs} times.")
```

#### Triggering an app rerun from inside a fragment
```python
import streamlit as st

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

@st.fragment
def count_to_five():
    if st.button("Plus one!"):
        st.session_state.clicks += 1
        if st.session_state.clicks % 5 == 0:
            st.rerun()
    return

count_to_five()
st.header(f"Multiples of five clicks: {st.session_state.clicks // 5}")

if st.button("Check click count"):
    st.toast(f"## Total clicks: {st.session_state.clicks}")
```