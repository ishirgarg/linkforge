Here is the Markdown version of the provided HTML:

### st.connection - Streamlit Docs
#### Documentation

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
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
			- SECRETS
			- [st.secrets](/develop/api-reference/connections/st.secrets)
			- [secrets.toml](/develop/api-reference/connections/secrets.toml)
			- CONNECTIONS
			- [st.connection](/develop/api-reference/connections/st.connection)
			- [SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection)
			- [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection)
			- [BaseConnection](/develop/api-reference/connections/st.connections.baseconnection)
			- [SnowparkConnection](/develop/api-reference/connections/st.connections.snowparkconnection)
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

### Tip
This page only contains the `st.connection` API. For a deeper dive into creating and managing data connections within Streamlit apps, read [Connecting to data](/develop/concepts/connections/connecting-to-data).

## st.connection
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Create a new connection to a data store or API, or return an existing one.

Configuration options, credentials, and secrets for connections are combined from the following sources:
* The keyword arguments passed to this command.
* The app's secrets.toml files.
* Any connection-specific configuration files.

The connection returned from `st.connection` is internally cached with `st.cache_resource` and is therefore shared between sessions.

### Function signature
```python
st.connection(name, type=None, max_entries=None, ttl=None, **kwargs)
```
### Parameters
* `name` (str): The connection name used for secrets lookup in secrets.toml.
* `type` (str, connection class, or None): The type of connection to create.
* `max_entries` (int or None): The maximum number of connections to keep in the cache.
* `ttl` (float, timedelta, or None): The maximum number of seconds to keep results in the cache.
* `**kwargs` (any): Connection-specific keyword arguments.

### Returns
An initialized connection object of the specified type.

### Examples
#### Example 1: Inferred connection type
```python
import streamlit as st
conn = st.connection("sql")
```
#### Example 2: Named connections
```python
import streamlit as st
conn1 = st.connection("first_connection", type="sql")
conn2 = st.connection("second_connection")
```
#### Example 3: Using a path to the connection class
```python
import streamlit as st
conn = st.connection("my_sql_connection", type="streamlit.connections.SQLConnection")
```
#### Example 4: Importing the connection class
```python
import streamlit as st
from streamlit.connections import SQLConnection
conn = st.connection("my_sql_connection", type=SQLConnection)
```
For a comprehensive overview of this feature, check out this video tutorial by Joshua Carroll, Streamlit's Product Manager for Developer Experience.

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit)[YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)[Twitter](https://twitter.com/streamlit)[LinkedIn](https://www.linkedin.com/company/streamlit)[Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

2025 Snowflake Inc. [Cookie policy](https://www.streamlit.io/cookie-policy)