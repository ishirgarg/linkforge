# Layouts and Containers

This section of the Streamlit API reference covers elements that help you structure your application's layout and organize content into containers.

**URL:** https://docs.streamlit.io/develop/api-reference/layout

## Complex layouts

This part of the documentation will detail how to create complex layouts using Streamlit.

---

**(This is the first part of the content. The next part will continue with specific layout elements.)**

### Columns

Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

### Container

Insert a multi-element container.

```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

### Modal dialog

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

### Empty

Insert a single-element container.

```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```

### Expander

Insert a multi-element container that can be expanded/collapsed.

```python
with st.expander("Open to see more"):
    st.write("This is more content")
```

### Popover

Insert a multi-element popover container that can be opened/closed.

```python
with st.popover("Settings"):
    st.checkbox("Show completed")
```

### Sidebar

Display items in a sidebar.

```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```

### Tabs

Insert containers separated into tabs.

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

### Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Streamlit Elements

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
    mui.Typography("Hello world")
```

#### Pydantic

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form", model=ExampleModel)
```

#### Streamlit Pages

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([
    Page("streamlit_app.py", "Home", "🏠"),
    Page("other_pages/page2.py", "Page 2", ":books:"),
])
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.