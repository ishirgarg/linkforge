```markdown
# st.sidebar - Streamlit

> This document provides information on the `st.sidebar` function in Streamlit, which allows you to add widgets and other elements to a sidebar in your application.
>
> **Reference:** [https://docs.streamlit.io/develop/api-reference/layout/st.sidebar](https://docs.streamlit.io/develop/api-reference/layout/st.sidebar)

## Add widgets to sidebar

You can organize widgets into a sidebar to add interactivity to your app. Elements can be passed to `st.sidebar` using object notation and `with` notation.

The following two snippets are equivalent:

```python
# Object notation
st.sidebar.[element_name]
```

```python
# "with" notation
with st.sidebar:
    st.[element_name]
```

Each element that's passed to `st.sidebar` is pinned to the left, allowing users to focus on the content in your app.

#### Tip

The sidebar is resizable! Drag and drop the right border of the sidebar to resize it! ↔️

Here's an example of how you'd add a selectbox and a radio button to your sidebar:

```python
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
```

#### Important

The only elements that aren't supported using object notation are `st.echo`, `st.spinner`, and `st.toast`. To use these elements, you must use `with` notation.

Here's an example of how you'd add [`st.echo`](/develop/api-reference/text/st.echo) and [`st.spinner`](/develop/api-reference/status/st.spinner) to your sidebar:

```python
import streamlit as st
import time

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")
    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
```
```
