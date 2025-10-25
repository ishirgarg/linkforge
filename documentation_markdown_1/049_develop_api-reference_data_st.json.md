# Streamlit `st.json` API Reference

**Original URL:** https://docs.streamlit.io/develop/api-reference/data/st.json

## st.json

Display an object or string as a pretty-printed, interactive JSON string.

### Function signature

```python
st.json(body, *, expanded=True, width="stretch")
```

[View st.json source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/json.py#L48)

### Parameters

*   **body** (object or str)
    The object to print as JSON. All referenced objects should be serializable to JSON as well. If object is a string, we assume it contains serialized JSON.

*   **expanded** (bool or int)
    The initial expansion state of the JSON element. This can be one of the following:
    *   `True` (default): The element is fully expanded.
    *   `False`: The element is fully collapsed.
    *   An integer: The element is expanded to the depth specified. The integer must be non-negative. `expanded=0` is equivalent to `expanded=False`.

    Regardless of the initial expansion state, users can collapse or expand any key-value pair to show or hide any part of the object.

*   **width** ("stretch" or int)
    The width of the JSON element. This can be one of the following:
    *   `"stretch"` (default): The width of the element matches the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Example

```python
import streamlit as st

st.json(
    {
        "foo": "bar",
        "stuff": [
            "stuff 1",
            "stuff 2",
            "stuff 3",
        ],
        "level1": {"level2": {"level3": {"a": "b"}}},
    },
    expanded=2,
)
```