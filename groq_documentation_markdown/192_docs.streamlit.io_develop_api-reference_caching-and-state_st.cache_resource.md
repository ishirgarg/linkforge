Here is the cleaned-up markdown version of the provided HTML:

# st.cache_resource - Streamlit Docs
![Logo](/logo.svg)

## Documentation
### Search
Search

### Navigation
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

## Tip
This page only contains information on the `st.cache_resource` API. For a deeper dive into caching and how to use it, check out [Caching](/develop/concepts/architecture/caching).

Here is the clean markdown version of the provided HTML:

## st.cache_resource
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Decorator to cache functions that return global resources (e.g., database connections, ML models).

Cached objects are shared across all users, sessions, and reruns. They must be thread-safe because they can be accessed from multiple threads concurrently. If thread safety is an issue, consider using `st.session_state` to store resources per session instead.

You can clear a function's cache with `func.clear()` or clear the entire cache with `st.cache_resource.clear()`.

A function's arguments must be hashable to cache it. If you have an unhashable argument (like a database connection) or an argument you want to exclude from caching, use an underscore prefix in the argument name. In this case, Streamlit will return a cached value when all other arguments match a previous function call. Alternatively, you can declare custom hashing functions with `hash_funcs`.

Cached values are available to all users of your app. If you need to save results that should only be accessible within a session, use [Session State](https://docs.streamlit.io/develop/concepts/architecture/session-state) instead. Within each user session, an `@st.cache_resource`-decorated function returns the cached instance of the return value (if the value is already cached). Therefore, objects cached by `st.cache_resource` act like singletons and can mutate. To cache data and return copies, use `st.cache_data` instead. To learn more about caching, see [Caching overview](https://docs.streamlit.io/develop/concepts/architecture/caching).

### Warning
Async objects are not officially supported in Streamlit. Caching async objects or objects that reference async objects may have unintended consequences. For example, Streamlit may close event loops in its normal operation and make the cached object raise an Event loop closed error.

To upvote official asyncio support, see GitHub issue [#8488](https://github.com/streamlit/streamlit/issues/8488). To upvote support for caching async functions, see GitHub issue [#8308](https://github.com/streamlit/streamlit/issues/8308).

### Function signature
```python
st.cache_resource(
    func, 
    *, 
    ttl, 
    max_entries, 
    show_spinner, 
    show_time=False, 
    validate, 
    hash_funcs=None
)
```
### Parameters

* `func` (callable): The function that creates the cached resource. Streamlit hashes the function's source code.
* `ttl` (float, timedelta, str, or None): The maximum time to keep an entry in the cache.
* `max_entries` (int or None): The maximum number of entries to keep in the cache, or None for an unbounded cache.
* `show_spinner` (bool or str): Enable the spinner.
* `show_time` (bool): Whether to show the elapsed time next to the spinner text.
* `validate` (callable or None): An optional validation function for cached data.
* `hash_funcs` (dict or None): Mapping of types or fully qualified names to hash functions.

### Example
```python
import streamlit as st

@st.cache_resource
def get_database_session(url):
    # Create a database session object that points to the URL.
    return session

s1 = get_database_session(SESSION_URL_1)
# Actually executes the function, since this is the first time it was encountered.

s2 = get_database_session(SESSION_URL_1)
# Does not execute the function. Instead, returns its previously computed value. This means that now the connection object in s1 is the same as in s2.

s3 = get_database_session(SESSION_URL_2)
# This is a different URL, so the function executes.
```
## st.cache_resource.clear
Clear all cache_resource caches.

### Function signature
```python
st.cache_resource.clear()
```
### Example
```python
import streamlit as st
from transformers import BertModel

@st.cache_resource
def get_database_session(url):
    # Create a database session object that points to the URL.
    return session

@st.cache_resource
def get_model(model_type):
    # Create a model of the specified type.
    return BertModel.from_pretrained(model_type)

if st.button("Clear All"):
    # Clears all st.cache_resource caches:
    st.cache_resource.clear()
```
## CachedFunc.clear
Clear the cached function's associated cache.

If no arguments are passed, Streamlit will clear all values cached for the function. If arguments are passed, Streamlit will clear the cached value for these arguments only.

### Function signature
```python
CachedFunc.clear(*args, **kwargs)
```
### Parameters

* `*args` (Any): Arguments of the cached functions.
* `**kwargs` (Any): Keyword arguments of the cached function.

### Example
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
### Using Streamlit commands in cached functions
#### Static elements
Since version 1.16.0, cached functions can contain Streamlit commands! For example, you can do this:
```python
from transformers import pipeline

@st.cache_resource
def load_model():
    model = pipeline("sentiment-analysis")
    st.success("Loaded NLP model from Hugging Face!")  # 
    return model
```
#### Input widgets
You can also use [interactive input widgets](https://docs.streamlit.io/library/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the `experimental_allow_widgets` parameter:
```python
@st.cache_resource(experimental_allow_widgets=True)  # 
def load_model():
    pretrained = st.checkbox("Use pre-trained model:")  # 
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT, pretrained=pretrained)
    return model
```
### Warning
Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!