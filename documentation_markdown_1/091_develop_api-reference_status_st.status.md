```markdown
# st.status - Streamlit API Reference

[Original URL](https://docs.streamlit.io/develop/api-reference/status/st.status)

## st.status

This section of the documentation covers the `st.status` element in the Streamlit API.
```

Inserts a container into your app that is typically used to show the status and details of a process or task. The container can hold multiple elements and can be expanded or collapsed by the user similar to `st.expander`. When collapsed, all that is visible is the status icon and label.

The label, state, and expanded state can all be updated by calling `.update()` on the returned object. To add elements to the returned container, you can use `with` notation (preferred) or just call methods directly on the returned object.

By default, `st.status()` initializes in the "running" state. When called using `with` notation, it automatically updates to the "complete" state at the end of the "with" block. See examples below for more details.

**Note:**
All content within the status container is computed and sent to the frontend, even if the status container is closed.

To follow best design practices and maintain a good appearance on all screen sizes, don't nest status containers.

### Function signature

```python
st.status(label, *, expanded=False, state="running", width="stretch")
```

#### Parameters

*   **label** (`str`)
    The initial label of the status container. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the `body` parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

*   **expanded** (`bool`)
    If `True`, initializes the status container in "expanded" state. Defaults to `False` (collapsed).

*   **state** (`"running"`, `"complete"`, or `"error"`)
    The initial state of the status container which determines which icon is shown:
    *   `running` (default): A spinner icon is shown.
    *   `complete`: A checkmark icon is shown.
    *   `error`: An error icon is shown.

*   **width** (`"stretch"` or `int`)
    The width of the status container. This can be one of the following:
    *   `"stretch"` (default): The width of the container matches the width of the parent container.
    *   An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container.

#### Returns

*   (`StatusContainer`)
    A mutable status container that can hold multiple elements. The label, state, and expanded state can be updated after creation via `.update()`.

### Examples

You can use the `with` notation to insert any element into an status container:

```python
import time
import streamlit as st

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button("Rerun")
```

You can also use `.update()` on the container to change the label, state, or expanded state:

```python
import time
import streamlit as st

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(
        label="Download complete!", state="complete", expanded=False
    )

st.button("Rerun")
```

### `StatusContainer.update`

Update the status container.

Only specified arguments are updated. Container contents and unspecified arguments remain unchanged.

#### Function signature

```python
StatusContainer.update(*, label=None, expanded=None, state=None)
```

#### Parameters

*   **label** (`str` or `None`)
    A new label of the status container. If `None`, the label is not changed.

*   **expanded** (`bool` or `None`)
    The new expanded state of the status container. If `None`, the expanded state is not changed.

*   **state** (`"running"`, `"complete"`, `"error"`, or `None`)
    The new state of the status container. This mainly changes the icon. If `None`, the state is not changed.

---

**Previous:** [st.spinner](/develop/api-reference/status/st.spinner)
**Next:** [st.toast](/develop/api-reference/status/st.toast)

---

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.