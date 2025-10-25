# st.user

**URL:** https://docs.streamlit.io/develop/api-reference/user/st.user

This document describes the `st.user` function in Streamlit, which provides information about the currently logged-in user.

---

**Note:** This is the first part of the conversion. The subsequent parts will cover the detailed API reference for `st.user`.

A read-only, dict-like object for accessing information about the current user.

`st.user` is dependent on the host platform running your Streamlit app. If your host platform has not configured the object, `st.user` will behave as it does in a locally running app.

When authentication is configured in `secrets.toml`, Streamlit will parse the OpenID Connect (OIDC) identity token and copy the attributes to `st.user`. Check your provider's documentation for their available attributes (known as claims).

When authentication is not configured, `st.user` has no attributes.

You can access values via key or attribute notation. For example, use `st.user["email"]` or `st.user.email` to access the email attribute.

> **Important**
> Identity tokens include an issuance and expiration time. Streamlit does not implicitly check these. If you want to automatically expire a user's authentication, check these values manually and programmatically log out your user (`st.logout()`) when needed.

### Class description [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/user_info.py#L382 "View st.user source code on GitHub")

`st.user()`

### Methods

*   [to\_dict](/develop/api-reference/user/st.user#userto_dict)()
    Get user info as a dictionary.

### Attributes

*   `is_logged_in` (bool)
    Whether a user is logged in. For a locally running app, this attribute is only available when authentication (`st.login()`) is configured in `secrets.toml`. Otherwise, it does not exist.

#### Examples

**Example 1: Google's identity token**

If you configure a basic Google OIDC connection as shown in Example 1 of `st.login()`, the following data is available in `st.user`. Streamlit adds the `is_logged_in` attribute. Additional attributes may be available depending on the configuration of the user's Google account. For more information about Google's identity tokens, see [Obtain user information from the ID token](https://developers.google.com/identity/openid-connect/openid-connect#obtainuserinfo) in Google's docs.

Your app code:

```python
import streamlit as st

if st.user.is_logged_in:
    st.write(st.user)
```

Displayed data when a user is logged in:

```json
{
    "is_logged_in":true,
    "iss":"https://accounts.google.com",
    "azp":"{client_id}.apps.googleusercontent.com",
    "aud":"{client_id}.apps.googleusercontent.com",
    "sub":"{unique_user_id}",
    "email":"{user}@gmail.com",
    "email_verified":true,
    "at_hash":"{access_token_hash}",
    "nonce":"{nonce_string}",
    "name":"{full_name}",
    "picture":"https://lh3.googleusercontent.com/a/{content_path}",
    "given_name":"{given_name}",
    "family_name":"{family_name}",
    "iat":{issued_time},
    "exp":{expiration_time}
}
```

**Example 2: Microsoft's identity token**

If you configure a basic Microsoft OIDC connection as shown in Example 2 of `st.login()`, the following data is available in `st.user`. For more information about Microsoft's identity tokens, see [ID token claims reference](https://learn.microsoft.com/en-us/entra/identity-platform/id-token-claims-reference) in Microsoft's docs.

Your app code:

```python
import streamlit as st

if st.user.is_logged_in:
    st.write(st.user)
```

Displayed data when a user is logged in:

```json
{
    "is_logged_in":true,
    "ver":"2.0",
    "iss":"https://login.microsoftonline.com/{tenant_id}/v2.0",
    "sub":"{application_user_id}",
    "aud":"{application_id}",
    "exp":{expiration_time},
    "iat":{issued_time},
    "nbf":{start_time},
    "name":"{full_name}",
    "preferred_username":"{username}",
    "oid":"{user_GUID}",
    "email":"{email}",
    "tid":"{tenant_id}",
    "nonce":"{nonce_string}",
    "aio":"{opaque_string}"
}
```

### Community Cloud

Starting from Streamlit version 1.42.0, you can't use `st.user` to retrieve a user's Community Cloud account email. To access user information, you must set up an identity provider and configure authentication (`[auth]`) in your app's `secrets`. Remember to update your identity provider's configuration and your app's `secrets` to allow your new domain. A list of [IP addresses](/deploy/streamlit-community-cloud/status#ip-addresses) used by Community Cloud is available if needed. An authentication-configured app counts as your single allowed private app.

## st.user.to\_dict

Get user info as a dictionary.

This method primarily exists for internal use and is not needed for most cases. `st.user` returns an object that inherits from `dict` by default.

### Function signature [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/user_info.py#L517 "View st.to_dict source code on GitHub")

`st.user.to_dict()`

### Returns

(`Dict[str,str]`)

A dictionary of the current user's information.