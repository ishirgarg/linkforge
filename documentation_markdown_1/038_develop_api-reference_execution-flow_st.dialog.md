```markdown
# st.dialog - Streamlit Docs

**Source:** [https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog](https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog)

## st.dialog
```


Function decorator to create a modal dialog.

A function decorated with `@st.dialog` becomes a dialog function. When you call a dialog function, Streamlit inserts a modal dialog into your app. Streamlit element commands called within the dialog function render inside the modal dialog.

The dialog function can accept arguments that can be passed when it is called. Any values from the dialog that need to be accessed from the wider app should generally be stored in Session State.

If a dialog is dismissible, a user can dismiss it by clicking outside of it, clicking the "**X**" in its upper-right corner, or pressing ESC on their keyboard. You can configure whether this triggers a rerun of the app by setting the `on_dismiss` parameter.

If a dialog is not dismissible, it must be closed programmatically by calling `st.rerun()` inside the dialog function. This is useful when you want to ensure that the dialog is always closed programmatically, such as when the dialog contains a form that must be submitted before closing.

`st.dialog` inherits behavior from [st.fragment](https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment). When a user interacts with an input widget created inside a dialog function, Streamlit only reruns the dialog function instead of the full script.

Calling `st.sidebar` in a dialog function is not supported.

Dialog code can interact with Session State, imported modules, and other Streamlit elements created outside the dialog. Note that these interactions are additive across multiple dialog reruns. You are responsible for handling any side effects of that behavior.

**Warning**

Only one dialog function may be called in a script run, which means that only one dialog can be open at any given time.

### Function signature

```python
st.dialog(title, *, width="small", dismissible=True, on_dismiss="ignore")
```

### Parameters

*   **title** (`str`)

    The title to display at the top of the modal dialog. It cannot be empty.

    The title can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.
*   **width** (`"small"`, `"medium"`, `"large"`)

    The width of the modal dialog. This can be one of the following:

    *   `"small"` (default): The modal dialog will be a maximum of 500 pixels wide.
    *   `"medium"`: The modal dialog will be up to 750 pixels wide.
    *   `"large"`: The modal dialog will be up to 1280 pixels wide.
*   **dismissible** (`bool`)

    Whether the modal dialog can be dismissed by the user. If this is `True` (default), the user can dismiss the dialog by clicking outside of it, clicking the "**X**" in its upper-right corner, or pressing ESC on their keyboard. If this is `False`, the "**X**" in the upper-right corner is hidden and the dialog must be closed programmatically by calling `st.rerun()` inside the dialog function.

    **Note**

    Setting `dismissible` to `False` does not guarantee that all interactions in the main app are blocked. Don't rely on `dismissible` for security-critical checks.
*   **on_dismiss** (`"ignore"`, `"rerun"`, or callable)

    How the dialog should respond to dismissal events. This can be one of the following:

    *   `"ignore"` (default): Streamlit will not rerun the app when the user dismisses the dialog.
    *   `"rerun"`: Streamlit will rerun the app when the user dismisses the dialog.
    *   A callable: Streamlit will rerun the app when the user dismisses the dialog and execute the callable as a callback function before the rest of the app.

#### Examples

The following example demonstrates the basic usage of `@st.dialog`. In this app, clicking "**A**" or "**B**" will open a modal dialog and prompt you to enter a reason for your vote. In the modal dialog, click "**Submit**" to record your vote into Session State and rerun the app. This will close the modal dialog since the dialog function is not called during the full-script rerun.

```python
import streamlit as st

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"
```
