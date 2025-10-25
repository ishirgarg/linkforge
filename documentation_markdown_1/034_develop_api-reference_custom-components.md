# Custom Components

[Original URL](https://docs.streamlit.io/develop/api-reference/custom-components)

#### Declare a component

Create and register a custom component.

```python
from st.components.v1 import declare_component
declare_component(
    "custom_slider",
    "/frontend",
)
```

#### HTML

Display an HTML string in an iframe.

```python
from st.components.v1 import html
html(
    "<p>Foo bar.</p>"
)
```

#### iframe

Load a remote URL in an iframe.

```python
from st.components.v1 import iframe
iframe(
    "docs.streamlit.io"
)
```
