## st.sidebar
### Overview

The `st.sidebar` function in Streamlit allows you to add interactivity to your app by organizing widgets into a sidebar. You can pass elements to `st.sidebar` using object notation or `with` notation.

### Adding Widgets to Sidebar

The following two snippets are equivalent:

```python
# Object notation
st.sidebar.element_name

# "with" notation
with st.sidebar:
    st.element_name
```

Each element passed to `st.sidebar` is pinned to the left, allowing users to focus on the content in your app.

#### Tip

The sidebar is resizable! Drag and drop the right border of the sidebar to resize it. 

### Example Usage

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

Here's an example of how you'd add `st.echo` and `st.spinner` to your sidebar:

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

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Navigation

* [Previous: st.popover](/develop/api-reference/layout/st.popover)
* [Next: st.tabs](/develop/api-reference/layout/st.tabs)

### Contact and Community

* [Home](/)
* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc. [Cookie policy](https://www.snowflake.com/cookie-policy/)