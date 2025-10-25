```markdown
# st.tabs - Streamlit API

[Original URL](https://docs.streamlit.io/develop/api-reference/layout/st.tabs)

## st.tabs

```


Inserts a number of multi-element containers as tabs. Tabs are a navigational element that allows users to easily move between groups of related content.

To add elements to the returned containers, you can use the `with` notation (preferred) or just call methods directly on the returned object. See the examples below.

**Note**

All content within every tab is computed and sent to the frontend, regardless of which tab is selected. Tabs do not currently support conditional rendering. If you have a slow-loading tab, consider using a widget like `st.segmented_control` to conditionally render content instead.

### Function signature

```python
st.tabs(tabs, *, width="stretch", default=None)
```

#### Parameters

*   **`tabs`** (`list` of `str`):
    Creates a tab for each string in the list. The first tab is selected by default. The string is used as the name of the tab and can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

*   **`width`** (`"stretch"` or `int`):
    The width of the tab container. This can be one of the following:
    *   `"stretch"` (default): The width of the container matches the width of the parent container.
    *   An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container.

*   **`default`** (`str` or `None`):
    The default tab to select. If this is `None` (default), the first tab is selected. If this is a string, it must be one of the tab labels. If two tabs have the same label as `default`, the first one is selected.

#### Returns

*   (`list` of `st.container`):
    A list of container objects.

### Examples

**Example 1: Use context management**

You can use `with` notation to insert any element into a tab:

```python
import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-tabs1.streamlit.app//?utm_medium=oembed&)

**Example 2: Call methods directly**

You can call methods directly on the returned objects:

```python
import streamlit as st
from numpy.random import default_rng as rng

df = rng(0).standard_normal((10, 1))

tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

tab1.subheader("A tab with a chart")
tab1.line_chart(df)

tab2.subheader("A tab with the data")
tab2.write(df)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-tabs2.streamlit.app//?utm_medium=oembed&)

**Example 3: Set the default tab and style the tab labels**

Use the `default` parameter to set the default tab. You can also use Markdown in the tab labels.

```python
import streamlit as st

tab1, tab2, tab3 = st.tabs(
    [":cat: Cat", ":dog: Dog", ":rainbow[Owl]"], default=":rainbow[Owl]"
)

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-tabs3.streamlit.app//?utm_medium=oembed&)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.