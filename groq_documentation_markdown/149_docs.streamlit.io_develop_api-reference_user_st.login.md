Here is the content converted to clean Markdown:
## st.login - Streamlit Docs

### Documentation

#### Search
Search

### Menu
* **Get started**
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* **Develop**
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
			- [st.login](/develop/api-reference/user/st.login)
			- [st.logout](/develop/api-reference/user/st.logout)
			- [st.user](/develop/api-reference/user/st.user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- TOOLS
		- [App testing](/develop/api-reference/app-testing)
		- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
* **Deploy**
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* **Knowledge base**
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deply)

### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Authentication and user info](/develop/api-reference/user)
* [st.login](/develop/api-reference/user/st.login)

### Tip
Learn more in [User authentication and information](/develop/concepts/connections/authentication).

## st.login
### Description
Initiate the login flow for the given provider.

This command redirects the user to an OpenID Connect (OIDC) provider. After the user authenticates their identity, they are redirected back to the home page of your app. Streamlit stores a cookie with the user's identity information in the user's browser. You can access the identity information through [st.user](https://docs.streamlit.io/develop/api-reference/user/st.user). Call `st.logout()` to remove the cookie and start a new session.

### Parameters
* `provider` (str or None): The name of your provider configuration to use for login.

### Examples
#### Example 1: Use an unnamed default identity provider
Configure Google as the default provider in your `secrets.toml` file:
```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```
Your app code:
```python
import streamlit as st

if not st.user.is_logged_in:
    if st.button("Log in"):
        st.login()
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")
```
#### Example 2: Use a named identity provider
Configure Microsoft as the provider in your `secrets.toml` file:
```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.microsoft]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration"
```
Your app code:
```python
import streamlit as st

if not st.user.is_logged_in:
    st.login("microsoft")
else:
    st.write(f"Hello, {st.user.name}!")
```
#### Example 3: Use multiple, named providers
Configure multiple providers in your `secrets.toml` file:
```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.microsoft]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration"

[auth.okta]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{subdomain}.okta.com/.well-known/openid-configuration"
```
Your app code:
```python
import streamlit as st

if not st.user.is_logged_in:
    st.header("Log in:")
    if st.button("Microsoft"):
        st.login("microsoft")
    if st.button("Okta"):
        st.login("okta")
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")
```
#### Example 4: Change the default connection settings
Use `prompt="login"` to force users to log in every time:
```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"

[auth.auth0]
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://{account}.{region}.auth0.com/.well-known/openid-configuration"
client_kwargs = { "prompt" = "login" }
```
Your app code:
```python
import streamlit as st

if st.button("Log in"):
    st.login("auth0")
if st.user.is_logged_in:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")
```
Note: You must install Authlib>=1.3.2 to use this command. You can install it as an extra with Streamlit: `pip install streamlit[auth]`