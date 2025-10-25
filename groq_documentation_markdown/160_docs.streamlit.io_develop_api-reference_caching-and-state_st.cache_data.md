Here is the converted markdown:
### st.cache_data - Streamlit Docs
#### Documentation
[Logo](/logo.svg)

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
			- [Caching and state](/develop/api-reference/caching-and-state)
				- SERVER
					- [st.cache_data](/develop/api-reference/caching-and-state/st.cache_data)
					- [st.cache_resource](/develop/api-reference/caching-and-state/st.cache_resource)
					- [st.session_state](/develop/api-reference/caching-and-state/st.session_state)
				- BROWSER
					- [st.context](/develop/api-reference/caching-and-state/st.context)
					- [st.query_params](/develop/api-reference/caching-and-state/st.query_params)
					- [st.experimental_get_query_params](/develop/api-reference/caching-and-state/st.experimental_get_query_params)
					- [st.experimental_set_query_params](/develop/api-reference/caching-and-state/st.experimental_set_query_params)
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

### Breadcrumbs
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Caching and state](/develop/api-reference/caching-and-state)
* [st.cache_data](/develop/api-reference/caching-and-state/st.cache_data)

#### Tip
This page only contains information on the `st.cache_data` API. For a deeper dive into caching and how to use it, check out [Caching](/develop/concepts/architecture/caching).

Here is the converted markdown:

# st.cache_data
## Overview
`st.cache_data` is a decorator to cache functions that return data, such as dataframe transforms, database queries, or ML inference. The cached objects are stored in "pickled" form, which means the return value of a cached function must be pickleable.

## Parameters
* `func`: The function to cache. Streamlit hashes the function's source code.
* `ttl`: The maximum time to keep an entry in the cache. Can be `None` (default), a number specifying the time in seconds, a string specifying the time in a format supported by Pandas's Timedelta constructor, or a timedelta object from Python's built-in datetime library.
* `max_entries`: The maximum number of entries to keep in the cache, or `None` for an unbounded cache.
* `show_spinner`: Enable the spinner. Default is `True` to show a spinner when there is a "cache miss" and the cached data is being created.
* `show_time`: Whether to show the elapsed time next to the spinner text. If `False` (default), no time is displayed.
* `persist`: Optional location to persist cached data to. Passing `"disk"` (or `True`) will persist the cached data to the local disk. `None` (or `False`) will disable persistence.
* `hash_funcs`: Mapping of types or fully qualified names to hash functions.

## Examples
```python
import streamlit as st

@st.cache_data
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data

d1 = fetch_and_clean_data(DATA_URL_1)
# Actually executes the function, since this is the first time it was encountered.

d2 = fetch_and_clean_data(DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed value.
```

## Note
Caching async functions is not supported. To upvote this feature, see GitHub issue [#8308](https://github.com/streamlit/streamlit/issues/8308).

## Warning
`st.cache_data` implicitly uses the `pickle` module, which is known to be insecure. Anything your cached function returns is pickled and stored, then unpickled on retrieval. Ensure your cached functions return trusted values because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

# st.cache_data.clear
## Overview
Clear all in-memory and on-disk data caches.

## Example
```python
import streamlit as st

@st.cache_data
def square(x):
    return x**2

@st.cache_data
def cube(x):
    return x**3

if st.button("Clear All"):
    # Clear values from *all* all in-memory and on-disk data caches:
    st.cache_data.clear()
```

# CachedFunc.clear
## Overview
Clear the cached function's associated cache.

## Parameters
* `*args`: Arguments of the cached functions.
* `**kwargs`: Keyword arguments of the cached function.

## Example
```python
import streamlit as st
import time

@st.cache_data
def foo(bar):
    time.sleep(2)
    st.write(f"Executed foo({bar}).")
    return bar

if st.button("Clear all cached values for `foo`", on_click=foo.clear):
    foo.clear()

if st.button("Clear the cached value of `foo(1)`"):
    foo.clear(1)

foo(1)
foo(2)
```

## Using Streamlit commands in cached functions
### Static elements
Since version 1.16.0, cached functions can contain Streamlit commands. For example:
```python
@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("Fetched data from API!")  # Show a success message
    return data
```
### Input widgets
You can also use interactive input widgets like `st.slider` or `st.text_input` in cached functions. To enable this feature, you need to set the `experimental_allow_widgets` parameter:
```python
@st.cache_data(experimental_allow_widgets=True)
def get_data():
    num_rows = st.slider("Number of rows to get")  # Add a slider
    data = api.get(..., num_rows)
    return data
```
Note that using widgets in cached functions can be dangerous and may lead to excessive memory usage.

## Warning
Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!