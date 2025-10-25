```markdown
# st.form

> **Tip**
> This page only contains information on the `st.forms` API. For a deeper dive into creating and using forms within Streamlit apps, read our guide on [Using forms](/develop/concepts/architecture/forms).

## st.form

---
*Original URL: https://docs.streamlit.io/develop/api-reference/execution-flow/st.form*
```

Create a form that batches elements together with a "Submit" button.

A form is a container that visually groups other elements and widgets together, and contains a Submit button. When the form's Submit button is pressed, all widget values inside the form will be sent to Streamlit in a batch.

To add elements to a form object, you can use `with` notation (preferred) or just call methods directly on the form. See examples below.

Forms have a few constraints:

*   Every form must contain a `st.form_submit_button`.
*   `st.button` and `st.download_button` cannot be added to a form.
*   Forms can appear anywhere in your app (sidebar, columns, etc), but they cannot be embedded inside other forms.
*   Within a form, the only widget that can have a callback function is `st.form_submit_button`.

## Function signature
[source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/form.py#L71 "View st.form source code on GitHub")

```python
st.form(key, clear_on_submit=False, *, enter_to_submit=True, border=True, width="stretch", height="content")
```

## Parameters

*   **key** (`str`)
    A string that identifies the form. Each form must have its own key. (This key is not displayed to the user in the interface.)

*   **clear_on_submit** (`bool`)
    If `True`, all widgets inside the form will be reset to their default values after the user presses the Submit button. Defaults to `False`. (Note that Custom Components are unaffected by this flag, and will not be reset to their defaults on form submission.)

*   **enter_to_submit** (`bool`)
    Whether to submit the form when a user presses Enter while interacting with a widget inside the form.

    If this is `True` (default), pressing Enter while interacting with a form widget is equivalent to clicking the first `st.form_submit_button` in the form.

    If this is `False`, the user must click an `st.form_submit_button` to submit the form.

    If the first `st.form_submit_button` in the form is disabled, the form will override submission behavior with `enter_to_submit=False`.

*   **border** (`bool`)
    Whether to show a border around the form. Defaults to `True`.

    > Note
    > Not showing a border can be confusing to viewers since interacting with a widget in the form will do nothing. You should only remove the border if there's another border (e.g. because of an expander) or the form is small (e.g. just a text input and a submit button).

*   **width** (`"stretch"`, `"content"`, or `int`)
    The width of the form container. This can be one of the following:
    *   `"stretch"` (default): The width of the container matches the width of the parent container.
    *   `"content"`: The width of the container matches the width of its content, but doesn't exceed the width of the parent container.
    *   An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container.

*   **height** (`"content"`, `"stretch"`, or `int`)
    The height of the form container. This can be one of the following:
    *   `"content"` (default): The height of the container matches the height of its content.
    *   `"stretch"`: The height of the container matches the height of its content or the height of the parent container, whichever is larger. If the container is not in a parent container, the height of the container matches the height of its content.
    *   An integer specifying the height in pixels: The container has a fixed height. If the content is larger than the specified height, scrolling is enabled.

    > Note
    > Use scrolling containers sparingly. If you use scrolling containers, avoid heights that exceed 500 pixels. Otherwise, the scroll surface of the container might cover the majority of the screen on mobile devices, which makes it hard to scroll the rest of the app.

## Examples

### Inserting elements using with notation:

```python
import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")
```

### Inserting elements out of order:

```python
import streamlit as st

form = st.form("my_form")
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")
```