**st.connections.SnowflakeConnection**
=====================================

### Overview

The `st.connections.SnowflakeConnection` class provides a connection to a Snowflake database using the Snowflake Connector for Python.

### Initialization

To initialize a `SnowflakeConnection` object, use the `st.connection()` function and pass the connection name and type as arguments.
```python
conn = st.connection("snowflake")
```
Alternatively, you can pass a connection name and type as keyword arguments.
```python
conn = st.connection("", type="snowflake")
```
### Methods

#### `cursor()`

Create a new cursor object from the connection.
```python
cur = conn.cursor()
```
#### `query()`

Run a read-only SQL query and return the results as a pandas DataFrame.
```python
df = conn.query("SELECT * FROM my_table")
```
#### `raw_connection`

Access the underlying Snowflake Connector connection object.
```python
raw_conn = conn.raw_connection
```
#### `reset()`

Reset the connection so that it gets reinitialized the next time it's used.
```python
conn.reset()
```
#### `session()`

Create a new Snowpark session from the connection.
```python
session = conn.session()
```
#### `write_pandas()`

Write a pandas DataFrame to a table in the Snowflake database.
```python
df = pd.DataFrame({"Name": ["Mary", "John", "Robert"], "Pet": ["dog", "cat", "bird"]})
conn.write_pandas(df, "my_table")
```
### Examples

#### Configuration with Streamlit secrets
```python
# .streamlit/secrets.toml
[connections.snowflake]
account = "xxx-xxx"
user = "xxx"
private_key_file = "/xxx/xxx/xxx.p8"
role = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"

# App code
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
```
#### Configuration with keyword arguments and external authentication
```python
# App code
conn = st.connection(
    "",
    type="snowflake",
    account="xxx-xxx",
    user="xxx",
    authenticator="externalbrowser",
)
df = conn.query("SELECT * FROM my_table")
```
#### Named connection with Snowflake's connection configuration file
```python
# ~/.snowflake/connections.toml
[my_connection]
account = "xxx-xxx"
user = "xxx"
password = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"

# App code
conn = st.connection("my_connection", type="snowflake")
df = conn.query("SELECT * FROM my_table")
```
### Notes

* The `snowflake-snowpark-python` library must be installed in your environment to use this connection.
* Account identifiers must be in the format `<orgname>-<account_name>`.
* The `query()` method implements query result caching and simple error handling/retries.