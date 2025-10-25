# st.get_option - Streamlit Docs

**URL:** https://docs.streamlit.io/develop/api-reference/configuration/st.get_option

---

## st.get_option

Return the current value of a given Streamlit configuration option.

Run `streamlit config show` in a terminal to see all available options.

### Function signature

[Source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/config.py#L178 "View st.get_option source code on GitHub")

```python
st.get_option(key)
```

### Parameters

*   **key** (`str`)
    The config option key of the form "section.optionName". To see all available options, run `streamlit config show` in a terminal.

### Example

```python
import streamlit as st

color = st.get_option("theme.primaryColor")
```

---

**Previous:** [config.toml](/develop/api-reference/configuration/config.toml) | **Next:** [st.set_option](/develop/api-reference/configuration/st.set_option)

---

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.