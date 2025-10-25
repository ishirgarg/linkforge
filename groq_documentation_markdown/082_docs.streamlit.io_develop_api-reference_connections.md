# Connections and Databases
## Setup your connection

Create a connection to a data source or API. 
```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

## Built-in connections

### SnowflakeConnection
A connection to Snowflake.
```python
conn = st.connection('snowflake')
```

### SQLConnection
A connection to a SQL database using SQLAlchemy.
```python
conn = st.connection('sql')
```

## Third-party connections

### Connection base class
Build your own connection with `BaseConnection`.
```python
class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)
    def query(self, query):
        return self._instance.query(query)
```

## Secrets

### Secrets singleton
Access secrets from a local TOML file.
```python
key = st.secrets["OpenAI_key"]
```

### Secrets file
Save your secrets in a per-project or per-profile TOML file.
```toml
OpenAI_key = "<YOUR_SECRET_KEY>"
```

## Deprecated classes

### SnowparkConnection
A connection to Snowflake.
```python
conn = st.connection("snowpark")
```

Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts. 

[Home](/) | [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20) | [Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit) | [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q) | [Twitter](https://twitter.com/streamlit) | [LinkedIn](https://www.linkedin.com/company/streamlit) | [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. [Cookie policy](https://www.streamlit.io/cookie-policy)