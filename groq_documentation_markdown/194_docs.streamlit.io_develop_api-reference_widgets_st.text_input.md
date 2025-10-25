### st.text_input
#### Display a single-line text input widget.

##### Function Signature
```python
st.text_input(
    label, 
    value="", 
    max_chars=None, 
    key=None, 
    type="default", 
    help=None, 
    autocomplete=None, 
    on_change=None, 
    args=None, 
    kwargs=None, 
    placeholder=None, 
    disabled=False, 
    label_visibility="visible", 
    icon=None, 
    width="stretch"
)
```

##### Parameters
* `label` (str): A short label explaining to the user what this input is for.
* `value` (object or None): The text value of this widget when it first renders.
* `max_chars` (int or None): Max number of characters allowed in text input.
* `key` (str or int): An optional string or integer to use as the unique key for the widget.
* `type` ("default" or "password"): The type of the text input.
* `help` (str or None): A tooltip that gets displayed next to the widget label.
* `autocomplete` (str): An optional value that will be passed to the `<input>` element's autocomplete property.
* `on_change` (callable): An optional callback invoked when this text input's value changes.
* `args` (list or tuple): An optional list or tuple of args to pass to the callback.
* `kwargs` (dict): An optional dict of kwargs to pass to the callback.
* `placeholder` (str or None): An optional string displayed when the text input is empty.
* `disabled` (bool): An optional boolean that disables the text input if set to True.
* `label_visibility` ("visible", "hidden", or "collapsed"): The visibility of the label.
* `icon` (str, None): An optional emoji or icon to display within the input field to the left of the value.
* `width` ("stretch" or int): The width of the text input widget.

##### Returns
* (str or None): The current value of the text input widget or None if no value has been provided by the user.

##### Example
```python
import streamlit as st

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)
```

Text input widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Text input widgets can also be disabled with the `disabled` parameter, and can display an optional placeholder text when the text input is empty using the `placeholder` parameter:
```python
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
st.session_state.disabled = False

col1, col2 = st.columns(2)
with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility ",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text ",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
    if text_input:
        st.write("You entered: ", text_input)
```