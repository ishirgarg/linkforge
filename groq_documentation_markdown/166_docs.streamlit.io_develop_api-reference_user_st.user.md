Here is the HTML content converted to clean Markdown:

# st.user - Streamlit Docs
![Logo](/logo.svg)

## Documentation
### Search
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
	+ [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Authentication and user info](/develop/api-reference/user)
* [st.user](/develop/api-reference/user/st.user)

Here is the converted text in clean Markdown:
### st.user
#### Streamlit Version
1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A read-only, dict-like object for accessing information about the current user.

`st.user` is dependent on the host platform running your Streamlit app. If your host platform has not configured the object, `st.user` will behave as it does in a locally running app.

When authentication is configured in `secrets.toml`, Streamlit will parse the OpenID Connect (OIDC) identity token and copy the attributes to `st.user`. Check your provider's documentation for their available attributes (known as claims).

When authentication is not configured, `st.user` has no attributes.

You can access values via key or attribute notation. For example, use `st.user["email"]` or `st.user.email` to access the email attribute.

**Important**
Identity tokens include an issuance and expiration time. Streamlit does not implicitly check these. If you want to automatically expire a user's authentication, check these values manually and programmatically log out your user (`st.logout()`) when needed.

#### Class description
[View st.user source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/user_info.py#L382)

#### Methods
##### st.user()
Get user info as a dictionary.

#### Attributes
* `is_logged_in` (bool): Whether a user is logged in. For a locally running app, this attribute is only available when authentication (`st.login()`) is configured in `secrets.toml`. Otherwise, it does not exist.

#### Examples
##### Example 1: Google's identity token
If you configure a basic Google OIDC connection as shown in Example 1 of `st.login()`, the following data is available in `st.user`. Streamlit adds the `is_logged_in` attribute. Additional attributes may be available depending on the configuration of the user's Google account. For more information about Google's identity tokens, see [Obtain user information from the ID token](https://developers.google.com/identity/openid-connect/openid-connect#obtainuserinfo) in Google's docs.

```python
import streamlit as st

if st.user.is_logged_in:
    st.write(st.user)
```

Displayed data when a user is logged in:
```json
{
    "is_logged_in": true,
    "iss": "https://accounts.google.com",
    "azp": "{client_id}.apps.googleusercontent.com",
    "aud": "{client_id}.apps.googleusercontent.com",
    "sub": "{unique_user_id}",
    "email": "{user}@gmail.com",
    "email_verified": true,
    "at_hash": "{access_token_hash}",
    "nonce": "{nonce_string}",
    "name": "{full_name}",
    "picture": "https://lh3.googleusercontent.com/a/{content_path}",
    "given_name": "{given_name}",
    "family_name": "{family_name}",
    "iat": {issued_time},
    "exp": {expiration_time}
}
```

##### Example 2: Microsoft's identity token
If you configure a basic Microsoft OIDC connection as shown in Example 2 of `st.login()`, the following data is available in `st.user`. For more information about Microsoft's identity tokens, see [ID token claims reference](https://learn.microsoft.com/en-us/entra/identity-platform/id-token-claims-reference) in Microsoft's docs.

```python
import streamlit as st

if st.user.is_logged_in:
    st.write(st.user)
```

Displayed data when a user is logged in:
```json
{
    "is_logged_in": true,
    "ver": "2.0",
    "iss": "https://login.microsoftonline.com/{tenant_id}/v2.0",
    "sub": "{application_user_id}",
    "aud": "{application_id}",
    "exp": {expiration_time},
    "iat": {issued_time},
    "nbf": {start_time},
    "name": "{full_name}",
    "preferred_username": "{username}",
    "oid": "{user_GUID}",
    "email": "{email}",
    "tid": "{tenant_id}",
    "nonce": "{nonce_string}",
    "aio": "{opaque_string}"
}
```

### Community Cloud
Starting from Streamlit version 1.42.0, you can't use `st.user` to retrieve a user's Community Cloud account email. To access user information, you must set up an identity provider and configure authentication (`[auth]`) in your app's secrets. Remember to update your identity provider's configuration and your app's secrets to allow your new domain. A list of [IP addresses](/deploy/streamlit-community-cloud/status#ip-addresses) used by Community Cloud is available if needed. An authentication-configured app counts as your single allowed private app.

### st.user.to_dict
#### Streamlit Version
1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Get user info as a dictionary.

This method primarily exists for internal use and is not needed for most cases. `st.user` returns an object that inherits from dict by default.

#### Function signature
[View st.to_dict source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/user_info.py#L517)

#### st.user.to_dict()
Returns a dictionary of the current user's information.

```python
st.user.to_dict()
```

Returns
```python
Dict[str, str]
```

A dictionary of the current user's information.

[Previous: st.logout](/develop/api-reference/user/st.logout)
[Next: Navigation and pages](/develop/api-reference/navigation)

Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit)
[YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
[Twitter](https://twitter.com/streamlit)
[LinkedIn](https://www.linkedin.com/company/streamlit)
[Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

2025 Snowflake Inc.
[Cookie policy](https://www.streamlit.io/cookie-policy)