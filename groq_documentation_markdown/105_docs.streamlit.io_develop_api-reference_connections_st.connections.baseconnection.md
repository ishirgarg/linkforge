### st.connections.BaseConnection - Streamlit Docs
#### Documentation
### Navigation
* [Get started](/get-started)
    + [Installation](/get-started/installation)
    + [Fundamentals](/get-started/fundamentals)
    + [First steps](/get-started/tutorials)
* [Develop](/develop)
    + [Concepts](/develop/concepts)
    + [API reference](/develop/api-reference)
        - [PAGE ELEMENTS](#)
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
        - [APPLICATION LOGIC](#)
        - [Authentication and user info](/develop/api-reference/user)
        - [Navigation and pages](/develop/api-reference/navigation)
        - [Execution flow](/develop/api-reference/execution-flow)
        - [Caching and state](/develop/api-reference/caching-and-state)
        - [Connections and secrets](/develop/api-reference/connections)
            - [SECRETS](#)
            - [st.secrets](/develop/api-reference/connections/st.secrets)
            - [secrets.toml](/develop/api-reference/connections/secrets.toml)
            - [CONNECTIONS](#)
            - [st.connection](/develop/api-reference/connections/st.connection)
            - [SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection)
            - [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection)
            - [BaseConnection](/develop/api-reference/connections/st.connections.baseconnection)
            - [SnowparkConnection](/develop/api-reference/connections/st.connections.snowparkconnection)
        - [Custom components](/develop/api-reference/custom-components)
        - [Configuration](/develop/api-reference/configuration)
        - [TOOLS](#)
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
* [Connections and secrets](/develop/api-reference/connections)
* [BaseConnection](/develop/api-reference/connections/st.connections.baseconnection)

### Tip
This page only contains information on the `st.connections.BaseConnection` class. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

Here is the cleaned-up Markdown version of the provided HTML:
### st.connections.BaseConnection
The abstract base class that all Streamlit Connections must inherit from.

This base class provides connection authors with a standardized way to hook into the `st.connection()` factory function: connection authors are required to provide an implementation for the abstract method `_connect` in their subclasses.

Additionally, it also provides a few methods/properties designed to make implementation of connections more convenient. See the docstrings for each of the methods of this class for more information.

**Note**: While providing an implementation of `_connect` is technically all that's required to define a valid connection, connections should also provide the user with context-specific ways of interacting with the underlying connection object. For example, the first-party SQLConnection provides a `query()` method for reads and a `session` property for more complex operations.

#### Class Description
`st.connections.BaseConnection(connection_name, **kwargs)`

#### Methods
##### BaseConnection.reset()
Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has expired, or in similar scenarios where a broken connection might be fixed by reinitializing it. Note that some connection methods may already use `reset()` in their error handling code.

**Function Signature**: `BaseConnection.reset()`

**Returns**: `None`

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