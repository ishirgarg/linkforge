```markdown
# st.context - Streamlit

> Source: [https://docs.streamlit.io/develop/api-reference/caching-and-state/st.context](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.context)

## st.context

An interface to access user session context.

`st.context` provides a read-only interface to access headers and cookies for the current user session.

Each property (`st.context.headers` and `st.context.cookies`) returns a dictionary of named values.

Class description [\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/runtime/context.py#L148 "View st.context source code on GitHub")

### Attributes

*   [cookies](/develop/api-reference/caching-and-state/st.context#contextcookies)

    A read-only, dict-like object containing cookies sent in the initial request.

*   [headers](/develop/api-reference/caching-and-state/st.context#contextheaders)

    A read-only, dict-like object containing headers sent in the initial request.

*   [ip\_address](/develop/api-reference/caching-and-state/st.context#contextip_address)

    The read-only IP address of the user's connection.

*   [is\_embedded](/develop/api-reference/caching-and-state/st.context#contextis_embedded)

    Whether the app is embedded.

*   [locale](/develop/api-reference/caching-and-state/st.context#contextlocale)

    The read-only locale of the user's browser.

*   [theme](/develop/api-reference/caching-and-state/st.context#contexttheme)

    A read-only, dictionary-like object containing theme information.

*   [timezone](/develop/api-reference/caching-and-state/st.context#contexttimezone)

    The read-only timezone of the user's browser.

*   [timezone\_offset](/develop/api-reference/caching-and-state/st.context#contexttimezone_offset)

    The read-only timezone offset of the user's browser.

*   [url](/develop/api-reference/caching-and-state/st.context#contexturl)

    The read-only URL of the app in the user's browser.
```


## context.cookies

A read-only, dict-like object containing cookies sent in the initial request.

**Function signature:**

```python
context.cookies
```

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/runtime/context.py#L205 "View st.cookies source code on GitHub")

#### Examples

**Example 1: Access all available cookies**

Show a dictionary of cookies:

```python
import streamlit as st

st.context.cookies
```

**Example 2: Access a specific cookie**

Show the value of a specific cookie:

```python
import streamlit as st

st.context.cookies["_ga"]
```

## context.headers

A read-only, dict-like object containing headers sent in the initial request.

Keys are case-insensitive and may be repeated. When keys are repeated, dict-like methods will only return the last instance of each key. Use `.get_all(key="your_repeated_key")` to see all values if the same header is set multiple times.

**Function signature:**

```python
context.headers
```

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/runtime/context.py#L159 "View st.headers source code on GitHub")

#### Examples

**Example 1: Access all available headers**

Show a dictionary of headers (with only the last instance of any repeated key):

```python
import streamlit as st

st.context.headers
```

**Example 2: Access a specific header**

Show the value of a specific header (or the last instance if it's repeated):

```python
import streamlit as st

st.context.headers["host"]
```

Show of list of all headers for a given key:

```python
import streamlit as st

st.context.headers.get_all("pragma")
```

## context.ip_address

The read-only IP address of the user's connection.

This should not be used for security measures because it can easily be spoofed. When a user accesses the app through localhost, the IP address is `None`. Otherwise, the IP address is determined from the [`remote_ip`](https://www.tornadoweb.org/en/stable/httputil.html#tornado.httputil.HTTPServerRequest.remote_ip) attribute of the Tornado request object and may be an IPv4 or IPv6 address.

**Function signature:**

```python
context.ip_address
```

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/runtime/context.py#L394 "View st.ip_address source code on GitHub")

#### Example

Check if the user has an IPv4 or IPv6 address:

```python
import streamlit as st

ip = st.context.ip_address
if ip is None:
    st.write("No IP address. This is expected in local development.")
elif ip.contains(":"):
    st.write("You have an IPv6 address.")
elif ip.contains("."):
    st.write("You have an IPv4 address.")
else:
    st.error("This should not happen.")
```

## context.is_embedded

Whether the app is embedded.

This property returns a boolean value indicating whether the app is running in an embedded context. This is determined by the presence of `embed=true` as a query parameter in the URL. This is the only way to determine if the app is currently configured for embedding because embedding settings are not accessible through `st.query_params` or `st.context.url`.

**Function signature:**

```python
context.is_embedded
```

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/runtime/context.py#L432 "View st.is_embedded source code on GitHub")

#### Example

Conditionally show content when the app is running in an embedded context:

```python
import streamlit as st

if st.context.is_embedded:
    st.write("You are running the app in an embedded context.")
```

## context.locale

The read-only locale of the user's browser.

`st.context.locale` returns the value of [`navigator.language`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language) from the user's DOM. This is a string representing the user's preferred language (e.g. "en-US").

**Function signature:**

```python
context.locale
```

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/runtime/context.py#L335 "View st.locale source code on GitHub")

#### Example

Access the user's locale to display locally:

```python
import streamlit as st

if st.context.locale == "fr-FR":
    st.write("Bonjour!")
else:
    st.write("Hello!")
```

## context.theme

A read-only, dictionary-like object containing theme information.

Theme information is restricted to the type of the theme (dark or light) and is inferred from the background color of the app.

**Note:**

Changes made to the background color through CSS are not included. Additionally, the theme type may be incorrect during a change in theme, like in the following situations:

*   When the app is first loaded within a session
*   When the user changes the theme in the settings menu

For more information and to upvote an improvement, see GitHub issue [#11920](https://github.com/streamlit/streamlit/issues/11920).

**Function signature:**

```python
context.theme
```

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/runtime/context.py#L239 "View st.theme source code on GitHub")

**Parameters**

*   `type ("light", "dark")`: The theme type inferred from the background color of the app.

#### Example

Access the theme type of the app:

```python
import streamlit as st

st.write(f"The current theme type is {st.context.theme.type}.")
```

## context.timezone


## context.timezone

The read-only timezone of the user's browser.

**Function signature:**

```python
context.timezone
```

**Example:**

Access the user's timezone, and format a datetime to display locally:

```python
import streamlit as st
from datetime import datetime, timezone
import pytz

tz = st.context.timezone
tz_obj = pytz.timezone(tz)

now = datetime.now(timezone.utc)

f"The user's timezone is {tz}."
f"The UTC time is {now}."
f"The user's local time is {now.astimezone(tz_obj)}"
```

## context.timezone_offset

The read-only timezone offset of the user's browser.

**Function signature:**

```python
context.timezone_offset
```

**Example:**

Access the user's timezone offset, and format a datetime to display locally:

```python
import streamlit as st
from datetime import datetime, timezone, timedelta

tzoff = st.context.timezone_offset
tz_obj = timezone(-timedelta(minutes=tzoff))

now = datetime.now(timezone.utc)

f"The user's timezone is {tz}."
f"The UTC time is {now}."
f"The user's local time is {now.astimezone(tz_obj)}"
```

## context.url

The read-only URL of the app in the user's browser.

`st.context.url` returns the URL through which the user is accessing the app. This includes the scheme, domain name, port, and path. If query parameters or anchors are present in the URL, they are removed and not included in this value.

**Function signature:**

```python
context.url
```

**Example:**

Conditionally show content when you access your app through localhost:

```python
import streamlit as st

if st.context.url.startswith("http://localhost"):
    st.write("You are running the app locally.")
```

---

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.