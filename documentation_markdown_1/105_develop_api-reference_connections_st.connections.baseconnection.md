```markdown
# st.connections.BaseConnection

[Original URL](https://docs.streamlit.io/develop/api-reference/connections/st.connections.baseconnection)

#### Tip

This page only contains information on the `st.connections.BaseConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

## st.connections.BaseConnection

Streamlit VersionVersion 1.50.0Version 1.49.0Version 1.48.0Version 1.47.0Version 1.46.0Version 1.45.0Version 1.44.0Version 1.43.0Version 1.42.0Version 1.41.0Version 1.40.0Version 1.39.0Version 1.38.0Version 1.37.0Version 1.36.0Version 1.35.0Version 1.34.0Version 1.33.0Version 1.32.0Version 1.31.0Version 1.30.0Version 1.29.0Version 1.28.0Version 1.27.0Version 1.26.0Version 1.25.0Version 1.24.0Version 1.23.0Version 1.22.0

The abstract base class that all Streamlit Connections must inherit from.

This base class provides connection authors with a standardized way to hook into the `st.connection()` factory function: connection authors are required to provide an implementation for the abstract method `_connect` in their subclasses.

Additionally, it also provides a few methods/properties designed to make implementation of connections more convenient. See the docstrings for each of the methods of this class for more information

**Note**

While providing an implementation of `_connect` is technically all that's required to define a valid connection, connections should also provide the user with context-specific ways of interacting with the underlying connection object. For example, the first-party `SQLConnection` provides a `query()` method for reads and a `session` property for more complex operations.

**Class description**

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/connections/base_connection.py#L27 "View st.BaseConnection source code on GitHub")

`st.connections.BaseConnection(connection_name, **kwargs)`

**Methods**

*   [`reset()`](/develop/api-reference/connections/st.connections.baseconnection#baseconnectionreset)

    Reset this connection so that it gets reinitialized the next time it's used.

## BaseConnection.reset
```

Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has expired, or in similar scenarios where a broken connection might be fixed by reinitializing it. Note that some connection methods may already use reset() in their error handling code.

### Function signature [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/connections/base_connection.py#L123 "View st.reset source code on GitHub")

```python
BaseConnection.reset()
```

**Returns**

(None)

No description

#### Example

```python
import streamlit as st

conn = st.connection("my_conn")

# Reset the connection before using it if it isn't healthy
# Note: is_healthy() isn't a real method and is just shown for example here.
if not conn.is_healthy():
    conn.reset()

# Do stuff with conn...
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---