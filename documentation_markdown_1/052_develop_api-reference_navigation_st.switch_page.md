```markdown
# st.switch_page - Streamlit

> **Reference:** [https://docs.streamlit.io/develop/api-reference/navigation/st.switch_page](https://docs.streamlit.io/develop/api-reference/navigation/st.switch_page)

## `st.switch_page`

Programmatically switch the current page in a multipage app.

When `st.switch_page` is called, the current page execution stops and the specified page runs as if the user clicked on it in the sidebar navigation. The specified page must be recognized by Streamlit's multipage architecture (your main Python file or a Python file in a `pages/` folder). Arbitrary Python scripts cannot be passed to `st.switch_page`.

### Function signature

```python
st.switch_page(page)
```

[Source code](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/commands/execution_control.py#L157)

### Parameters

*   **page** (str, Path, or `st.Page`): The file path (relative to the main script) or an `st.Page` indicating the page to switch to.

### Example

Consider the following example given this file structure:

```
your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py
```

```python
import streamlit as st

if st.button("Home"):
    st.switch_page("your_app.py")
if st.button("Page 1"):
    st.switch_page("pages/page_1.py")
if st.button("Page 2"):
    st.switch_page("pages/page_2.py")
```
```
