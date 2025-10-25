```markdown
# Authentication and User Info

[Original URL](https://docs.streamlit.io/develop/api-reference/user)

Streamlit provides native support for user authentication so you can personalize your apps. You can also directly read headers and cookies.

## Log in a user

[`st.login()`](/develop/api-reference/user/st.login) starts an authentication flow with an identity provider.

```python
st.login()
```

## Log out a user

[`st.logout()`](/develop/api-reference/user/st.logout) removes a user's identity information.

```python
st.logout()
```

## User info

[`st.user`](/develop/api-reference/user/st.user) returns information about a logged-in user.

```python
if st.user.is_logged_in:
    st.write(f"Welcome back, {st.user.name}!")
```
```