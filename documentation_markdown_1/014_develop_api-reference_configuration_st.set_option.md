# st.set_option

**Source URL:** [https://docs.streamlit.io/develop/api-reference/configuration/st.set_option](https://docs.streamlit.io/develop/api-reference/configuration/st.set_option)

---

`st.set_option` allows you to set a configuration option.

Currently, only client configuration options can be set within the script itself:

-   `client.showErrorDetails`
-   `client.showSidebarNavigation`
-   `client.toolbarMode`

Calling `st.set_option` with any other option will raise a `StreamlitAPIException`. When changing a configuration option in a running app, you may need to trigger a rerun after changing the option to see the effects.

Run `streamlit config show` in a terminal to see all available options.

## Function signature

[source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/config.py#L129)

```python
st.set_option(key, value)
```

## Parameters

-   **key** (str)
    The config option key of the form "section.optionName". To see all available options, run `streamlit config show` in a terminal.

-   **value** (any)
    The new value to assign to this config option.

## Example

```python
import streamlit as st

st.set_option("client.showErrorDetails", True)
```