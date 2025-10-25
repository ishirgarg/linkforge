# Testing Element Classes - Streamlit API Reference

**URL:** https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes

This section of the Streamlit documentation details the testing element classes available in `st.testing.v1.element_tree`. These classes provide a structured way to interact with and assert the state of various Streamlit elements within your tests.

## `st.testing.v1.element_tree.Block`

The `Block` class mirrors the functionality of `AppTest`, but it represents a container of elements within the Streamlit app, rather than the entire app itself. This allows for more granular testing of specific sections or layouts.

Methods and attributes available on `AppTest` are also available on `Block`. For instance, `Block.button` will return a `WidgetList` of `Button` elements, similar to how `AppTest.button` operates.

Container elements like `ChatMessage`, `Column`, and `Tab` inherit from `Block`. For these container classes, parameters of the original Streamlit element can be accessed as properties. For example, you can get the avatar of a `ChatMessage` using `ChatMessage.avatar` or the label of a `Tab` using `Tab.label`.

## `st.testing.v1.element_tree.Element`

**Streamlit Versions:** 1.22.0 - 1.50.0

`Element` is the base class for all elements within the Streamlit testing framework. It provides universal methods and attributes applicable to any testable element.

**Class Description:**
[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L103 "View st.Element source code on GitHub")

**Constructor:**
`st.testing.v1.element_tree.Element(proto, root)`

**Methods:**

*   **`run(*, timeout=None)`**: Executes the `AppTest` script that contains the element.
    *   `timeout`: An optional timeout for the script execution.

**Attributes:**

*   **`value`**: Represents the value or content of the element.

## `st.testing.v1.element_tree.Button`

**Streamlit Versions:** 1.22.0 - 1.50.0

This class represents `st.button` and `st.form_submit_button` for testing purposes.

**Class Description:**
[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L302 "View st.Button source code on GitHub")

**Constructor:**
`st.testing.v1.element_tree.Button(proto, root)`

**Methods:**

*   **`click()`**: Simulates a click on the button, setting its value to `True`.
*   **`run(*, timeout=None)`**: Executes the `AppTest` script that contains the button.
    *   `timeout`: An optional timeout for the script execution.
*   **`set_value(v)`**: Sets the value of the button to `v`.

**Attributes:**

*   **`value`**: The current value of the button, which is a boolean (`bool`).

### `st.testing.v1.element_tree.ChatInput`

A representation of `st.chat_input`.

**Class description**
[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L344 "View st.ChatInput source code on GitHub")

```python
st.testing.v1.element_tree.ChatInput(proto, root)
```

**Methods**

*   `run(*, timeout=None)`: Run the AppTest script which contains the element.
*   `set_value(v)`: Set the value of the widget.

**Attributes**

*   `value`: The value of the widget. (str)

### `st.testing.v1.element_tree.Checkbox`

A representation of `st.checkbox`.

**Class description**
[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L379 "View st.Checkbox source code on GitHub")

```python
st.testing.v1.element_tree.Checkbox(proto, root)
```

**Methods**

*   `check()`: Set the value of the widget to `True`.
*   `run(*, timeout=None)`: Run the AppTest script which contains the element.
*   `set_value(v)`: Set the value of the widget.
*   `uncheck()`: Set the value of the widget to `False`.

**Attributes**

*   `value`: The value of the widget. (bool)

### `st.testing.v1.element_tree.ColorPicker`

A representation of `st.color_picker`.

**Class description**
[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L446 "View st.ColorPicker source code on GitHub")

```python
st.testing.v1.element_tree.ColorPicker(proto, root)
```

**Methods**

*   `pick(v)`: Set the value of the widget as a hex string. May omit the "#" prefix.
*   `run(*, timeout=None)`: Run the AppTest script which contains the element.
*   `set_value(v)`: Set the value of the widget as a hex string.

**Attributes**

*   `value`: The currently selected value as a hex string. (str)

### `st.testing.v1.element_tree.DateInput`

A representation of `st.date_input`.

**Class description**
[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L512 "View st.DateInput source code on GitHub")

```python
st.testing.v1.element_tree.DateInput(proto, root)
```

**Methods**

*   `run(*, timeout=None)`: Run the AppTest script which contains the element.
*   `set_value(v)`: Set the value of the widget.

**Attributes**

*   `value`: The value of the widget. (date or Tuple of date)

### `st.testing.v1.element_tree.Multiselect`

### `st.testing.v1.element_tree.Multiselect`

A representation of `st.multiselect`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L774 "View st.Multiselect source code on GitHub")

`st.testing.v1.element_tree.Multiselect(proto, root)`

**Methods**

*   `run(*, timeout=None)`
    Run the `AppTest` script which contains the element.
*   `select(v)`
    Add a selection to the widget. Do nothing if the value is already selected. If testing a multiselect widget with repeated options, use `set_value` instead.
*   `set_value(v)`
    Set the value of the multiselect widget. (`list`)
*   `unselect(v)`
    Remove a selection from the widget. Do nothing if the value is not already selected. If a value is selected multiple times, the first instance is removed.

**Attributes**

*   `format_func`
    The widget's formatting function for displaying options. (`callable`)
*   `indices`
    The indices of the currently selected values from the options. (`list`)
*   `value`
    The currently selected values from the options. (`list`)
*   `values`
    The currently selected values from the options. (`list`)

### `st.testing.v1.element_tree.NumberInput`

A representation of `st.number_input`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L867 "View st.NumberInput source code on GitHub")

`st.testing.v1.element_tree.NumberInput(proto, root)`

**Methods**

*   `decrement()`
    Decrement the `st.number_input` widget as if the user clicked "-".
*   `increment()`
    Increment the `st.number_input` widget as if the user clicked "+".
*   `run(*, timeout=None)`
    Run the `AppTest` script which contains the element.
*   `set_value(v)`
    Set the value of the `st.number_input` widget.

**Attributes**

*   `value`
    Get the current value of the `st.number_input` widget.

### `st.testing.v1.element_tree.Radio`

A representation of `st.radio`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L928 "View st.Radio source code on GitHub")

`st.testing.v1.element_tree.Radio(proto, root)`

**Methods**

*   `run(*, timeout=None)`
    Run the `AppTest` script which contains the element.
*   `set_value(v)`
    Set the selection by value.

**Attributes**

*   `format_func`
    The widget's formatting function for displaying options. (`callable`)
*   `index`
    The index of the current selection. (`int`)
*   `value`
    The currently selected value from the options. (`Any`)

### `st.testing.v1.element_tree.SelectSlider`

A representation of `st.select_slider`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1058 "View st.SelectSlider source code on GitHub")

`st.testing.v1.element_tree.SelectSlider(proto, root)`

**Methods**

*   `run(*, timeout=None)`
    Run the `AppTest` script which contains the element.
*   `set_range(lower, upper)`
    Set the ranged selection by values.
*   `set_value(v)`
    Set the (single) selection by value.

**Attributes**

*   `format_func`
    The widget's formatting function for displaying options. (`callable`)
*   `value`
    The currently selected value or range. (`Any` or `Sequence` of `Any`)

### `st.testing.v1.element_tree.Selectbox`

```markdown
## `st.testing.v1.element_tree.Selectbox`

Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A representation of `st.selectbox`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L987)

`st.testing.v1.element_tree.Selectbox(proto, root)`

**Methods**

*   [`run`](/develop/api-reference/app-testing/testing-element-classes#selectboxrun)(*, timeout=None)

    Run the AppTest script which contains the element.
*   [`select`](/develop/api-reference/app-testing/testing-element-classes#selectboxselect)(v)

    Set the selection by value.
*   [`select_index`](/develop/api-reference/app-testing/testing-element-classes#selectboxselect_index)(index)

    Set the selection by index.
*   [`set_value`](/develop/api-reference/app-testing/testing-element-classes#selectboxset_value)(v)

    Set the selection by value.

**Attributes**

*   [`format_func`](/develop/api-reference/app-testing/testing-element-classes#selectboxformat_func)

    The widget's formatting function for displaying options. (callable)
*   [`index`](/develop/api-reference/app-testing/testing-element-classes#selectboxindex)

    The index of the current selection. (int)
*   [`value`](/develop/api-reference/app-testing/testing-element-classes#selectboxvalue)

    The currently selected value from the options. (Any)

## `st.testing.v1.element_tree.Slider`

Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A representation of `st.slider`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1121)

`st.testing.v1.element_tree.Slider(proto, root)`

**Methods**

*   [`run`](/develop/api-reference/app-testing/testing-element-classes#sliderrun)(*, timeout=None)

    Run the AppTest script which contains the element.
*   [`set_range`](/develop/api-reference/app-testing/testing-element-classes#sliderset_range)(lower, upper)

    Set the ranged value of the slider.
*   [`set_value`](/develop/api-reference/app-testing/testing-element-classes#sliderset_value)(v)

    Set the (single) value of the slider.

**Attributes**

*   [`value`](/develop/api-reference/app-testing/testing-element-classes#slidervalue)

    The currently selected value or range. (Any or Sequence of Any)

## `st.testing.v1.element_tree.TextArea`

Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A representation of `st.text_area`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1207)

`st.testing.v1.element_tree.TextArea(proto, root)`

**Methods**

*   [`input`](/develop/api-reference/app-testing/testing-element-classes#textareainput)(v)

    Set the value of the widget only if the value does not exceed the maximum allowed characters.
*   [`run`](/develop/api-reference/app-testing/testing-element-classes#textarearun)(*, timeout=None)

    Run the AppTest script which contains the element.
*   [`set_value`](/develop/api-reference/app-testing/testing-element-classes#textareaset_value)(v)

    Set the value of the widget.

**Attributes**

*   [`value`](/develop/api-reference/app-testing/testing-element-classes#textareavalue)

    The current value of the widget. (str)

## `st.testing.v1.element_tree.TextInput`

Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A representation of `st.text_input`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1259)

`st.testing.v1.element_tree.TextInput(proto, root)`

**Methods**

*   [`input`](/develop/api-reference/app-testing/testing-element-classes#textinputinput)(v)

    Set the value of the widget only if the value does not exceed the maximum allowed characters.
*   [`run`](/develop/api-reference/app-testing/testing-element-classes#textinputrun)(*, timeout=None)

    Run the AppTest script which contains the element.
*   [`set_value`](/develop/api-reference/app-testing/testing-element-classes#textinputset_value)(v)

    Set the value of the widget.

**Attributes**

*   [`value`](/develop/api-reference/app-testing/testing-element-classes#textinputvalue)

    The current value of the widget. (str)

## `st.testing.v1.element_tree.TimeInput`

Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A representation of `st.time_input`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1314)

`st.testing.v1.element_tree.TimeInput(proto, root)`

**Methods**

*   [`decrement`](/develop/api-reference/app-testing/testing-element-classes#timeinputdecrement)()

    Select the previous available time.
*   [`increment`](/develop/api-reference/app-testing/testing-element-classes#timeinputincrement)()

    Select the next available time.
*   [`run`](/develop/api-reference/app-testing/testing-element-classes#timeinputrun)(*, timeout=None)

    Run the AppTest script which contains the element.
*   [`set_value`](/develop/api-reference/app-testing/testing-element-classes#timeinputset_value)(v)

    Set the value of the widget.

**Attributes**

*   [`value`](/develop/api-reference/app-testing/testing-element-classes#timeinputvalue)

    The current value of the widget. (time)

## `st.testing.v1.element_tree.Toggle`
```

### `st.testing.v1.element_tree.Toggle`

A representation of `st.toggle`.

[View `st.Toggle` source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1387)

**`st.testing.v1.element_tree.Toggle(proto, root)`**

#### Methods

*   **`run(*, timeout=None)`**: Run the `AppTest` script which contains the element.
*   **`set_value(v)`**: Set the value of the widget.

#### Attributes

*   **`value`**: The current value of the widget. (bool)

***

### Conclusion

This section of the documentation covered the `st.testing.v1.element_tree.Toggle` class, which is used for testing Streamlit toggle widgets. It detailed the class's constructor, available methods for interacting with the toggle (like `run` and `set_value`), and its attributes, specifically the `value` attribute which represents the current state of the toggle.

***

### Navigation

*   [Previous: `st.testing.v1.AppTest`](/develop/api-reference/app-testing/st.testing.v1.apptest)
*   [Next: Command line](/develop/api-reference/cli)

***

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

***

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)