```markdown
# Testing element classes

> **Source:** [https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes](https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes)

## Introduction

This document provides information on testing element classes within Streamlit.
```

## `st.testing.v1.element_tree.ChatInput`

Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A representation of `st.chat_input`.

**Class description** [\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L344 "View st.ChatInput source code on GitHub")

`st.testing.v1.element_tree.ChatInput(proto, root)`

**Methods**

*   [`run`](/develop/api-reference/app-testing/testing-element-classes#chatinputrun)(*, timeout=None)

    Run the AppTest script which contains the element.
*   [`set_value`](/develop/api-reference/app-testing/testing-element-classes#chatinputset_value)(v)

    Set the value of the widget.

**Attributes**

*   [`value`](/develop/api-reference/app-testing/testing-element-classes#chatinputvalue)

    The value of the widget. (str)

## `st.testing.v1.element_tree.Checkbox`

Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A representation of `st.checkbox`.

**Class description** [\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L379 "View st.Checkbox source code on GitHub")

`st.testing.v1.element_tree.Checkbox(proto, root)`

**Methods**

*   [`check`](/develop/api-reference/app-testing/testing-element-classes#checkboxcheck)()

    Set the value of the widget to True.
*   [`run`](/develop/api-reference/app-testing/testing-element-classes#checkboxrun)(*, timeout=None)

    Run the AppTest script which contains the element.
*   [`set_value`](/develop/api-reference/app-testing/testing-element-classes#checkboxset_value)(v)

    Set the value of the widget.
*   [`uncheck`](/develop/api-reference/app-testing/testing-element-classes#checkboxuncheck)()

    Set the value of the widget to False.

**Attributes**

*   [`value`](/develop/api-reference/app-testing/testing-element-classes#checkboxvalue)

    The value of the widget. (bool)

## `st.testing.v1.element_tree.ColorPicker`

Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A representation of `st.color_picker`.

**Class description** [\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L446 "View st.ColorPicker source code on GitHub")

`st.testing.v1.element_tree.ColorPicker(proto, root)`

**Methods**

*   [`pick`](/develop/api-reference/app-testing/testing-element-classes#colorpickerpick)(v)

    Set the value of the widget as a hex string. May omit the "#" prefix.
*   [`run`](/develop/api-reference/app-testing/testing-element-classes#colorpickerrun)(*, timeout=None)

    Run the AppTest script which contains the element.
*   [`set_value`](/develop/api-reference/app-testing/testing-element-classes#colorpickerset_value)(v)

    Set the value of the widget as a hex string.

**Attributes**

*   [`value`](/develop/api-reference/app-testing/testing-element-classes#colorpickervalue)

    The currently selected value as a hex string. (str)

## `st.testing.v1.element_tree.DateInput`

Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

A representation of `st.date_input`.

**Class description** [\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L512 "View st.DateInput source code on GitHub")

`st.testing.v1.element_tree.DateInput(proto, root)`

**Methods**

*   [`run`](/develop/api-reference/app-testing/testing-element-classes#dateinputrun)(*, timeout=None)

    Run the AppTest script which contains the element.
*   [`set_value`](/develop/api-reference/app-testing/testing-element-classes#dateinputset_value)(v)

    Set the value of the widget.

**Attributes**

*   [`value`](/develop/api-reference/app-testing/testing-element-classes#dateinputvalue)

    The value of the widget. (date or Tuple of date)

## `st.testing.v1.element_tree.Multiselect`


A representation of `st.multiselect`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L774 "View st.Multiselect source code on GitHub")

```python
st.testing.v1.element_tree.Multiselect(proto, root)
```

**Methods**

*   `run(*, timeout=None)`
    Run the AppTest script which contains the element.
*   `select(v)`
    Add a selection to the widget. Do nothing if the value is already selected. If testing a multiselect widget with repeated options, use `set_value` instead.
*   `set_value(v)`
    Set the value of the multiselect widget. (list)
*   `unselect(v)`
    Remove a selection from the widget. Do nothing if the value is not already selected. If a value is selected multiple times, the first instance is removed.

**Attributes**

*   `format_func`
    The widget's formatting function for displaying options. (callable)
*   `indices`
    The indices of the currently selected values from the options. (list)
*   `value`
    The currently selected values from the options. (list)
*   `values`
    The currently selected values from the options. (list)

## st.testing.v1.element\_tree.NumberInput

A representation of `st.number_input`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L867 "View st.NumberInput source code on GitHub")

```python
st.testing.v1.element_tree.NumberInput(proto, root)
```

**Methods**

*   `decrement()`
    Decrement the `st.number_input` widget as if the user clicked "-".
*   `increment()`
    Increment the `st.number_input` widget as if the user clicked "+".
*   `run(*, timeout=None)`
    Run the AppTest script which contains the element.
*   `set_value(v)`
    Set the value of the `st.number_input` widget.

**Attributes**

*   `value`
    Get the current value of the `st.number_input` widget.

## st.testing.v1.element\_tree.Radio

A representation of `st.radio`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L928 "View st.Radio source code on GitHub")

```python
st.testing.v1.element_tree.Radio(proto, root)
```

**Methods**

*   `run(*, timeout=None)`
    Run the AppTest script which contains the element.
*   `set_value(v)`
    Set the selection by value.

**Attributes**

*   `format_func`
    The widget's formatting function for displaying options. (callable)
*   `index`
    The index of the current selection. (int)
*   `value`
    The currently selected value from the options. (Any)

## st.testing.v1.element\_tree.SelectSlider

A representation of `st.select_slider`.

**Class description** [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1058 "View st.SelectSlider source code on GitHub")

```python
st.testing.v1.element_tree.SelectSlider(proto, root)
```

**Methods**

*   `run(*, timeout=None)`
    Run the AppTest script which contains the element.
*   `set_range(lower, upper)`
    Set the ranged selection by values.
*   `set_value(v)`
    Set the (single) selection by value.

**Attributes**

*   `format_func`
    The widget's formatting function for displaying options. (callable)
*   `value`
    The currently selected value or range. (Any or Sequence of Any)

## st.testing.v1.element\_tree.Selectbox

## st.testing.v1.element_tree.Selectbox

A representation of st.selectbox.

**Class description**[[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L987 "View st.Selectbox source code on GitHub")

`st.testing.v1.element_tree.Selectbox(proto, root)`

**Methods**

*   [run](/develop/api-reference/app-testing/testing-element-classes#selectboxrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [select](/develop/api-reference/app-testing/testing-element-classes#selectboxselect)(v)

    Set the selection by value.
*   [select\_index](/develop/api-reference/app-testing/testing-element-classes#selectboxselect_index)(index)

    Set the selection by index.
*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#selectboxset_value)(v)

    Set the selection by value.

**Attributes**

*   [format\_func](/develop/api-reference/app-testing/testing-element-classes#selectboxformat_func)

    The widget's formatting function for displaying options. (callable)
*   [index](/develop/api-reference/app-testing/testing-element-classes#selectboxindex)

    The index of the current selection. (int)
*   [value](/develop/api-reference/app-testing/testing-element-classes#selectboxvalue)

    The currently selected value from the options. (Any)

## st.testing.v1.element_tree.Slider

A representation of st.slider.

**Class description**[[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1121 "View st.Slider source code on GitHub")

`st.testing.v1.element_tree.Slider(proto, root)`

**Methods**

*   [run](/develop/api-reference/app-testing/testing-element-classes#sliderrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set\_range](/develop/api-reference/app-testing/testing-element-classes#sliderset_range)(lower, upper)

    Set the ranged value of the slider.
*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#sliderset_value)(v)

    Set the (single) value of the slider.

**Attributes**

*   [value](/develop/api-reference/app-testing/testing-element-classes#slidervalue)

    The currently selected value or range. (Any or Sequence of Any)

## st.testing.v1.element_tree.TextArea

A representation of st.text\_area.

**Class description**[[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1207 "View st.TextArea source code on GitHub")

`st.testing.v1.element_tree.TextArea(proto, root)`

**Methods**

*   [input](/develop/api-reference/app-testing/testing-element-classes#textareainput)(v)

    Set the value of the widget only if the value does not exceed the maximum allowed characters.
*   [run](/develop/api-reference/app-testing/testing-element-classes#textarearun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#textareaset_value)(v)

    Set the value of the widget.

**Attributes**

*   [value](/develop/api-reference/app-testing/testing-element-classes#textareavalue)

    The current value of the widget. (str)

## st.testing.v1.element_tree.TextInput

A representation of st.text\_input.

**Class description**[[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1259 "View st.TextInput source code on GitHub")

`st.testing.v1.element_tree.TextInput(proto, root)`

**Methods**

*   [input](/develop/api-reference/app-testing/testing-element-classes#textinputinput)(v)

    Set the value of the widget only if the value does not exceed the maximum allowed characters.
*   [run](/develop/api-reference/app-testing/testing-element-classes#textinputrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#textinputset_value)(v)

    Set the value of the widget.

**Attributes**

*   [value](/develop/api-reference/app-testing/testing-element-classes#textinputvalue)

    The current value of the widget. (str)

## st.testing.v1.element_tree.TimeInput

A representation of st.time\_input.

**Class description**[[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1314 "View st.TimeInput source code on GitHub")

`st.testing.v1.element_tree.TimeInput(proto, root)`

**Methods**

*   [decrement](/develop/api-reference/app-testing/testing-element-classes#timeinputdecrement)()

    Select the previous available time.
*   [increment](/develop/api-reference/app-testing/testing-element-classes#timeinputincrement)()

    Select the next available time.
*   [run](/develop/api-reference/app-testing/testing-element-classes#timeinputrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#timeinputset_value)(v)

    Set the value of the widget.

**Attributes**

*   [value](/develop/api-reference/app-testing/testing-element-classes#timeinputvalue)

    The current value of the widget. (time)

## st.testing.v1.element_tree.Toggle


A representation of `st.toggle`.

## Class description

[Source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1387 "View st.Toggle source code on GitHub")

`st.testing.v1.element_tree.Toggle(proto, root)`

## Methods

*   [run](/develop/api-reference/app-testing/testing-element-classes#togglerun)(\*, timeout=None)

    Run the AppTest script which contains the element.

*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#toggleset_value)(v)

    Set the value of the widget.

## Attributes

*   [value](/develop/api-reference/app-testing/testing-element-classes#togglevalue)

    The current value of the widget. (bool)

---

[_arrow\_back_Previous: st.testing.v1.AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest)
[_arrow\_forward_Next: Command line](/develop/api-reference/cli)

_forum_

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
