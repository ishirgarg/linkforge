```markdown
# st.cache_resource - Streamlit Docs

**Reference:** [https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)

> **Tip:** This page only contains information on the `st.cache_resource` API. For a deeper dive into caching and how to use it, check out [Caching](/develop/concepts/architecture/caching).

## `st.cache_resource`
```


Decorator to cache functions that return global resources (e.g. database connections, ML models).

Cached objects are shared across all users, sessions, and reruns. They must be thread-safe because they can be accessed from multiple threads concurrently. If thread safety is an issue, consider using `st.session_state` to store resources per session instead.

You can clear a function's cache with `func.clear()` or clear the entire cache with `st.cache_resource.clear()`.

A function's arguments must be hashable to cache it. If you have an unhashable argument (like a database connection) or an argument you want to exclude from caching, use an underscore prefix in the argument name. In this case, Streamlit will return a cached value when all other arguments match a previous function call. Alternatively, you can declare custom hashing functions with `hash_funcs`.

Cached values are available to all users of your app. If you need to save results that should only be accessible within a session, use [Session State](https://docs.streamlit.io/develop/concepts/architecture/session-state) instead. Within each user session, an `@st.cache_resource`-decorated function returns the cached instance of the return value (if the value is already cached). Therefore, objects cached by `st.cache_resource` act like singletons and can mutate. To cache data and return copies, use `st.cache_data` instead. To learn more about caching, see [Caching overview](https://docs.streamlit.io/develop/concepts/architecture/caching).

> **Warning:** Async objects are not officially supported in Streamlit. Caching async objects or objects that reference async objects may have unintended consequences. For example, Streamlit may close event loops in its normal operation and make the cached object raise an `Event loop closed` error.
>
> To upvote official asyncio support, see GitHub issue [#8488](https://github.com/streamlit/streamlit/issues/8488). To upvote support for caching async functions, see GitHub issue [#8308](https://github.com/streamlit/streamlit/issues/8308).

### Function signature

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/runtime/caching/cache_resource_api.py#L259 "View st.cache_resource source code on GitHub")

```python
st.cache_resource(func, *, ttl, max_entries, show_spinner, show_time=False, validate, hash_funcs=None)
```

### Parameters

*   **func** (`callable`): The function that creates the cached resource. Streamlit hashes the function's source code.
*   **ttl** (`float`, `timedelta`, `str`, or `None`): The maximum time to keep an entry in the cache. Can be one of:
    *   `None` if cache entries should never expire (default).
    *   A number specifying the time in seconds.
    *   A string specifying the time in a format supported by [Pandas's Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html), e.g. `"1d"`, `"1.5 days"`, or `"1h23s"`.
    *   A `timedelta` object from [Python's built-in `datetime` library](https://docs.python.org/3/library/datetime.html#timedelta-objects), e.g. `timedelta(days=1)`.
*   **max_entries** (`int` or `None`): The maximum number of entries to keep in the cache, or `None` for an unbounded cache. When a new entry is added to a full cache, the oldest cached entry will be removed. Defaults to `None`.
*   **show_spinner** (`bool` or `str`): Enable the spinner. Default is `True` to show a spinner when there is a "cache miss" and the cached resource is being created. If string, value of `show_spinner` param will be used for spinner text.
*   **show_time** (`bool`): Whether to show the elapsed time next to the spinner text. If this is `False` (default), no time is displayed. If this is `True`, elapsed time is displayed with a precision of 0.1 seconds. The time format is not configurable.
*   **validate** (`callable` or `None`): An optional validation function for cached data. `validate` is called each time the cached value is accessed. It receives the cached value as its only parameter and it must return a boolean. If `validate` returns `False`, the current cached value is discarded, and the decorated function is called to compute a new value. This is useful e.g. to check the health of database connections.
*   **hash_funcs** (`dict` or `None`): Mapping of types or fully qualified names to hash functions. This is used to override the behavior of the hasher inside Streamlit's caching mechanism: when the hasher encounters an object, it will first check to see if its type matches a key in this dict and, if so, will use the provided function to generate a hash for it. See below for an example of how this can be used.

#### Example

```python
import streamlit as st

@st.cache_resource
def get_database_session(url):
    # Create a database session object that points to the URL.
    return session

s1 = get_database_session(SESSION_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

s2 = get_database_session(SESSION_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the connection object in s1 is the same as in s2.

s3 = get_database_session(SESSION_URL_2)
# This is a different URL, so the function executes.
```

By default, all parameters to a `cache_resource` function must be hashable. Any parameter whose name begins with `_` will not be hashed. You can use this as an "escape hatch" for parameters that are not hashable:

```python
import streamlit as st

@st.cache_resource
def get_database_session(_sessionmaker, url):
    # Create a database connection object that points to the URL.
    return connection

s1 = get_database_session(create_sessionmaker(), DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

s2 = get_database_session(create_sessionmaker(), DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value - even though the _sessionmaker parameter was different
# in both calls.
```

A `cache_resource` function's cache can be procedurally cleared:

```python
import streamlit as st

@st.cache_resource
def get_database_session(_sessionmaker, url):
    # Create a database connection object that points to the URL.
    return connection

fetch_and_clean_data.clear(_sessionmaker, "https://streamlit.io/")
# Clear the cached entry for the arguments provided.

get_database_session.clear()
# Clear all cached entries for this function.
```

To override the default hashing behavior, pass a custom hash function. You can do that by mapping a type (e.g. `Person`) to a hash function (`str`) like this:

```python
import streamlit as st
from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_resource(hash_funcs={Person: str})
def get_person_name(person: Person):
    return person.name
```

Alternatively, you can map the type's fully-qualified name (e.g. `"__main__.Person"`) to the hash function instead:

```python
import streamlit as st
from pydantic import BaseModel

class Person(BaseModel):
    name: str

@st.cache_resource(hash_funcs={"__main__.Person": str})
def get_person_name(person: Person):
    return person.name
```

### `st.cache_resource.clear`

This section is missing from the provided HTML.

### `st.cache_resource.clear()`

Clear all `st.cache_resource` caches.

**Function signature:**

```python
st.cache_resource.clear()
```

**Example:**

In the example below, pressing the "Clear All" button will clear _all_ `cache_resource` caches. i.e. Clears cached global resources from all functions decorated with `@st.cache_resource`.

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

### `CachedFunc.clear()`

Clear the cached function's associated cache.

If no arguments are passed, Streamlit will clear all values cached for the function. If arguments are passed, Streamlit will clear the cached value for these arguments only.

**Function signature:**

```python
CachedFunc.clear(*args, **kwargs)
```

**Parameters:**

*   `*args` (Any): Arguments of the cached functions.
*   `**kwargs` (Any): Keyword arguments of the cached function.

**Example:**

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

Since version 1.16.0, cached functions can contain Streamlit commands! For example, you can do this:

```python
from transformers import pipeline

@st.cache_resource
def load_model():
    model = pipeline("sentiment-analysis")
    st.success("Loaded NLP model from Hugging Face!") # 👈 Show a success message
    return model
```

On the first run, the `st.success` message will appear in the app. On subsequent runs, Streamlit replays static elements that were saved during the first run. This works for both caching decorators.

You can also use this functionality to cache entire parts of your UI:

```python
@st.cache_resource
def load_model():
    st.header("Data analysis")
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT)
    st.success("Loaded model!")
    st.write("Turning on evaluation mode...")
    model.eval()
    st.write("Here's the model:")
    return model
```

### Input widgets

You can also use [interactive input widgets](/develop/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature. To enable it, set the `experimental_allow_widgets` parameter:

```python
@st.cache_resource(experimental_allow_widgets=True) # 👈 Set the parameter
def load_model():
    pretrained = st.checkbox("Use pre-trained model:") # 👈 Add a checkbox
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT, pretrained=pretrained)
    return model
```

Streamlit treats the widget value as an additional input parameter to the cached function. If the widget's state changes, Streamlit will rerun the function if it hasn't cached a result for that specific state.

Using widgets in cached functions is powerful for caching UI components, but can lead to excessive memory usage if not managed carefully. Streamlit caches results for every permutation of widget values, even if they don't directly influence the return value. This can cause the cache to grow rapidly. It's recommended to use this feature only for isolated UI parts where widgets directly affect the cached return value.

#### Warning

Support for widgets in cached functions is currently experimental and may change or be removed without notice. Use with care.

#### Note

`st.file_uploader` and `st.camera_input` are not currently supported in cached functions. You can [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them.

[_arrow\_back_Previous: st.cache\_data](/develop/api-reference/caching-and-state/st.cache_data)[_arrow\_forward_Next: st.experimental\_memo](/develop/api-reference/caching-and-state/st.experimental_memo)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.