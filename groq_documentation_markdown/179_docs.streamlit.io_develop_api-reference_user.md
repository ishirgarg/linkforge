Here is the HTML content converted to clean Markdown:

## Authentication and User Info
Streamlit provides native support for user authentication so you can personalize your apps. You can also directly read headers and cookies.

### Log in a user
`st.login()` starts an authentication flow with an identity provider.

### Log out a user
`st.logout()` removes a user's identity information.

### User Info
`st.user` returns information about a logged-in user.
```python
if st.user.is_logged_in: 
    st.write(f"Welcome back, {st.user.name}!")
```
Still have questions? Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Navigation
* [Home](/)
* [Develop](/develop)
* [API Reference](/develop/api-reference)
* [Authentication and User Info](/develop/api-reference/user)

### External Links
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. [Cookie policy](/)