Here is the converted HTML to clean markdown:

# st.context - Streamlit Docs
## Documentation

### Search

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
			- [SERVER](#)
			- [st.cache_data](/develop/api-reference/caching-and-state/st.cache_data)
			- [st.cache_resource](/develop/api-reference/caching-and-state/st.cache_resource)
			- [st.session_state](/develop/api-reference/caching-and-state/st.session_state)
			- [BROWSER](#)
			- [st.context](/develop/api-reference/caching-and-state/st.context)
			- [st.query_params](/develop/api-reference/caching-and-state/st.query_params)
			- [st.experimental_get_query_params](/develop/api-reference/caching-and-state/st.experimental_get_query_params)
			- [st.experimental_set_query_params](/develop/api-reference/caching-and-state/st.experimental_set_query_params)
		- [Connections and secrets](/develop/api-reference/connections)
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

### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Caching and state](/develop/api-reference/caching-and-state)
* [st.context](/develop/api-reference/caching-and-state/st.context)

## st.context
An interface to access user session context.

st.context provides a read-only interface to access headers and cookies for the current user session.

Each property (st.context.headers and st.context.cookies) returns a dictionary of named values.

### Attributes

* **cookies**: A read-only, dict-like object containing cookies sent in the initial request.
* **headers**: A read-only, dict-like object containing headers sent in the initial request.
* **ip_address**: The read-only IP address of the user's connection.
* **is_embedded**: Whether the app is embedded.
* **locale**: The read-only locale of the user's browser.
* **theme**: A read-only, dictionary-like object containing theme information.
* **timezone**: The read-only timezone of the user's browser.
* **timezone_offset**: The read-only timezone offset of the user's browser.
* **url**: The read-only URL of the app in the user's browser.

## context.cookies
A read-only, dict-like object containing cookies sent in the initial request.

### Examples

* Access all available cookies: `st.context.cookies`
* Access a specific cookie: `st.context.cookies["_ga"]`

## context.headers
A read-only, dict-like object containing headers sent in the initial request.

### Examples

* Access all available headers: `st.context.headers`
* Access a specific header: `st.context.headers["host"]`
* Access all headers for a given key: `st.context.headers.get_all("pragma")`

## context.ip_address
The read-only IP address of the user's connection.

### Example

Check if the user has an IPv4 or IPv6 address:
```python
ip = st.context.ip_address
if ip is None:
    st.write("No IP address. This is expected in local development.")
elif ":" in ip:
    st.write("You have an IPv6 address.")
elif "." in ip:
    st.write("You have an IPv4 address.")
else:
    st.error("This should not happen.")
```

## context.is_embedded
Whether the app is embedded.

### Example

Conditionally show content when the app is running in an embedded context:
```python
if st.context.is_embedded:
    st.write("You are running the app in an embedded context.")
```

## context.locale
The read-only locale of the user's browser.

### Example

Access the user's locale to display locally:
```python
if st.context.locale == "fr-FR":
    st.write("Bonjour!")
else:
    st.write("Hello!")
```

## context.theme
A read-only, dictionary-like object containing theme information.

### Example

Access the theme type of the app:
```python
st.write(f"The current theme type is {st.context.theme.type}.")
```

## context.timezone
The read-only timezone of the user's browser.

### Example

Access the user's timezone, and format a datetime to display locally:
```python
import pytz
tz = st.context.timezone
tz_obj = pytz.timezone(tz)
now = datetime.now(timezone.utc)
st.write(f"The user's timezone is {tz}.")
st.write(f"The UTC time is {now}.")
st.write(f"The user's local time is {now.astimezone(tz_obj)}")
```

## context.timezone_offset
The read-only timezone offset of the user's browser.

### Example

Access the user's timezone offset, and format a datetime to display locally:
```python
tzoff = st.context.timezone_offset
tz_obj = timezone(-timedelta(minutes=tzoff))
now = datetime.now(timezone.utc)
st.write(f"The user's timezone is {tz}.")
st.write(f"The UTC time is {now}.")
st.write(f"The user's local time is {now.astimezone(tz_obj)}")
```

## context.url
The read-only URL of the app in the user's browser.

### Example

Conditionally show content when you access your app through localhost:
```python
if st.context.url.startswith("http://localhost"):
    st.write("You are running the app locally.")
```