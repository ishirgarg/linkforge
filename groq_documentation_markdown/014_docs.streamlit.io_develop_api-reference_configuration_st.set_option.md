Here is the cleaned-up markdown version of the provided HTML:

# st.set_option
## Streamlit Version
Version 1.50.0, Version 1.49.0, Version 1.48.0, Version 1.47.0, Version 1.46.0, Version 1.45.0, Version 1.44.0, Version 1.43.0, Version 1.42.0, Version 1.41.0, Version 1.40.0, Version 1.39.0, Version 1.38.0, Version 1.37.0, Version 1.36.0, Version 1.35.0, Version 1.34.0, Version 1.33.0, Version 1.32.0, Version 1.31.0, Version 1.30.0, Version 1.29.0, Version 1.28.0, Version 1.27.0, Version 1.26.0, Version 1.25.0, Version 1.24.0, Version 1.23.0, Version 1.22.0

Set a configuration option.

Currently, only client configuration options can be set within the script itself:

* `client.showErrorDetails`
* `client.showSidebarNavigation`
* `client.toolbarMode`

Calling `st.set_option` with any other option will raise a `StreamlitAPIException`. When changing a configuration option in a running app, you may need to trigger a rerun after changing the option to see the effects.

Run `streamlit config show` in a terminal to see all available options.

### Function signature
```python
st.set_option(key, value)
```
### Parameters

* `key` (str): The config option key of the form "section.optionName". To see all available options, run `streamlit config show` in a terminal.
* `value` (null): The new value to assign to this config option.

### Example
```python
import streamlit as st
st.set_option("client.showErrorDetails", True)
```
[Previous: st.get_option](/develop/api-reference/configuration/st.get_option)
[Next: st.set_page_config](/develop/api-reference/configuration/st.set_page_config)

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Footer
[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit)
[YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
[Twitter](https://twitter.com/streamlit)
[LinkedIn](https://www.linkedin.com/company/streamlit)
[Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc.
[Cookie policy](https://www.streamlit.io/cookie-policy)