Here is the converted text in clean Markdown:

# st.connections.SQLConnection
Streamlit Version: 1.50.0
## Description
A connection to a SQL database using a SQLAlchemy Engine.

Initialize this connection object using `st.connection("sql")` or `st.connection("<name>", type="sql")`. Connection parameters for a SQLConnection can be specified using `secrets.toml` and/or `**kwargs`.

### Parameters
* `url` or keyword arguments for `sqlalchemy.engine.URL.create()`, except `drivername`. Use `dialect` and `driver` instead of `drivername`.
* Keyword arguments for `sqlalchemy.create_engine()`, including custom `connect()` arguments used by your specific dialect or driver.
* `autocommit`. If this is `False` (default), the connection operates in manual commit (transactional) mode. If this is `True`, the connection operates in autocommit (non-transactional) mode.

### Examples
#### Example 1: Configuration with URL
You can configure your SQL connection using Streamlit's [Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management).

```toml
# .streamlit/secrets.toml
[connections.sql]
url = "xxx+xxx://xxx:xxx@xxx:xxx/xxx"
```

```python
import streamlit as st

conn = st.connection("sql")
df = conn.query("SELECT * FROM pet_owners")
st.dataframe(df)
```

#### Example 2: Configuration with dialect, host, and username
If you do not specify `url`, you must at least specify `dialect`, `host`, and `username` instead.

```toml
# .streamlit/secrets.toml
[connections.sql]
dialect = "xxx"
host = "xxx"
username = "xxx"
password = "xxx"
```

```python
import streamlit as st

conn = st.connection("sql")
df = conn.query("SELECT * FROM pet_owners")
st.dataframe(df)
```

#### Example 3: Configuration with keyword arguments
You can configure your SQL connection with keyword arguments (with or without `secrets.toml`).

```python
import streamlit as st

conn = st.connection(
    "sql",
    dialect="mssql",
    driver="pyodbc",
    host="xxx.database.windows.net",
    database="xxx",
    username="xxx",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "authentication": "ActiveDirectoryInteractive",
        "encrypt": "yes",
    },
)

df = conn.query("SELECT * FROM pet_owners")
st.dataframe(df)
```

## Methods
### SQLConnection.connect
Call `.connect()` on the underlying SQLAlchemy Engine, returning a new connection object.

#### Function signature
```python
SQLConnection.connect()
```

#### Returns
* `sqlalchemy.engine.Connection`: A new SQLAlchemy connection object.

### SQLConnection.query
Run a read-only query.

This method implements query result caching and simple error handling/retries.

#### Function signature
```python
SQLConnection.query(sql, *, show_spinner="Running `sql.query(...)`.", ttl=None, index_col=None, chunksize=None, params=None, **kwargs)
```

#### Parameters
* `sql` (str): The read-only SQL query to execute.
* `show_spinner` (boolean or string): Enable the spinner.
* `ttl` (float, int, timedelta or None): The maximum number of seconds to keep results in the cache.
* `index_col` (str, list of str, or None): Column(s) to set as index(MultiIndex).
* `chunksize` (int or None): If specified, return an iterator where `chunksize` is the number of rows to include in each chunk.
* `params` (list, tuple, dict or None): List of parameters to pass to the execute method.
* `**kwargs` (dict): Additional keyword arguments are passed to `pandas.read_sql`.

#### Returns
* `pandas.DataFrame`: The result of running the query, formatted as a pandas DataFrame.

### SQLConnection.reset
Reset this connection so that it gets reinitialized the next time it's used.

#### Function signature
```python
SQLConnection.reset()
```

#### Returns
* `None`

## Attributes
### SQLConnection.driver
The name of the driver used by the underlying SQLAlchemy Engine.

#### Function signature
```python
SQLConnection.driver
```

#### Returns
* `str`: The name of the driver.

### SQLConnection.engine
The underlying SQLAlchemy Engine.

#### Function signature
```python
SQLConnection.engine
```

#### Returns
* `sqlalchemy.engine.base.Engine`: The underlying SQLAlchemy Engine.

### SQLConnection.session
Return a SQLAlchemy Session.

Users of this connection should use the contextmanager pattern for writes, transactions, and anything more complex than simple read queries.

#### Function signature
```python
SQLConnection.session
```

#### Returns
* `sqlalchemy.orm.Session`: A SQLAlchemy Session.

#### Example
```python
import streamlit as st
conn = st.connection("sql")
n = st.slider("Pick a number")
if st.button("Add the number!"):
    with conn.session as session:
        session.execute("INSERT INTO numbers (val) VALUES (:n);", {"n": n})
        session.commit()
```