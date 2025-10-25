# Connections and Databases

**Original URL:** https://docs.streamlit.io/develop/api-reference/connections

## Setup your connection

### [Create a connection](/develop/api-reference/connections/st.connection)
Connect to a data source or API

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

## Built-in connections

### [SnowflakeConnection](/develop/api-reference/connections/st.connections.snowflakeconnection)
A connection to Snowflake.

```python
conn = st.connection('snowflake')
```

### [SQLConnection](/develop/api-reference/connections/st.connections.sqlconnection)
A connection to a SQL database using SQLAlchemy.

```python
conn = st.connection('sql')
```

## Third-party connections

### [Connection base class](/develop/api-reference/connections/st.connections.baseconnection)
Build your own connection with `BaseConnection`.

```python
class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)

    def query(self, query):
        return self._instance.query(query)
```

## Secrets

### [Secrets singleton](/develop/api-reference/connections/st.secrets)
Access secrets from a local TOML file.

```python
key = st.secrets["OpenAI_key"]
```

### [Secrets file](/develop/api-reference/connections/secrets.toml)
Save your secrets in a per-project or per-profile TOML file.

```toml
OpenAI_key = "<YOUR_SECRET_KEY>"
```

## Deprecated classes

### [SnowparkConnection](/develop/api-reference/connections/st.connections.snowparkconnection)
A connection to Snowflake.

```python
conn = st.connection("snowpark")
```