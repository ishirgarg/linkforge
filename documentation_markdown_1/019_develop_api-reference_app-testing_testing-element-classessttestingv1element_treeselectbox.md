```markdown
# Testing Element Classes

> **Source:** [https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes](https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes)

## Introduction

This document provides information on testing element classes within the Streamlit framework. It covers the `Block` class, the base `Element` class, and the `Button` class, detailing their methods, attributes, and how they are used in testing Streamlit applications.

## st.testing.v1.element_tree.Block

The `Block` class mirrors the methods and attributes of `AppTest`. It represents a container of elements, similar to how `AppTest` represents the entire application. For instance, `Block.button` returns a `WidgetList` of `Button` instances, mirroring the behavior of [`AppTest.button`](/develop/api-reference/testing/st.testing.v1.apptest#apptestbutton).

Classes like `ChatMessage`, `Column`, and `Tab` inherit from `Block`.  Parameters of the original element can be accessed as properties. For example, `ChatMessage.avatar` and `Tab.label`.
```

## st.testing.v1.element_tree.ChatInput

A representation of `st.chat_input`.

**Class description** ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L344))

```python
st.testing.v1.element_tree.ChatInput(proto, root)
```

**Methods**

*   [run](/develop/api-reference/app-testing/testing-element-classes#chatinputrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set_value](/develop/api-reference/app-testing/testing-element-classes#chatinputset_value)(v)

    Set the value of the widget.

**Attributes**

*   [value](/develop/api-reference/app-testing/testing-element-classes#chatinputvalue)

    The value of the widget. (str)

## st.testing.v1.element_tree.Checkbox

A representation of `st.checkbox`.

**Class description** ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L379))

```python
st.testing.v1.element_tree.Checkbox(proto, root)
```

**Methods**

*   [check](/develop/api-reference/app-testing/testing-element-classes#checkboxcheck)()

    Set the value of the widget to True.
*   [run](/develop/api-reference/app-testing/testing-element-classes#checkboxrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set_value](/develop/api-reference/app-testing/testing-element-classes#checkboxset_value)(v)

    Set the value of the widget.
*   [uncheck](/develop/api-reference/app-testing/testing-element-classes#checkboxuncheck)()

    Set the value of the widget to False.

**Attributes**

*   [value](/develop/api-reference/app-testing/testing-element-classes#checkboxvalue)

    The value of the widget. (bool)

## st.testing.v1.element_tree.ColorPicker

A representation of `st.color_picker`.

**Class description** ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L446))

```python
st.testing.v1.element_tree.ColorPicker(proto, root)
```

**Methods**

*   [pick](/develop/api-reference/app-testing/testing-element-classes#colorpickerpick)(v)

    Set the value of the widget as a hex string. May omit the "#" prefix.
*   [run](/develop/api-reference/app-testing/testing-element-classes#colorpickerrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set_value](/develop/api-reference/app-testing/testing-element-classes#colorpickerset_value)(v)

    Set the value of the widget as a hex string.

**Attributes**

*   [value](/develop/api-reference/app-testing/testing-element-classes#colorpickervalue)

    The currently selected value as a hex string. (str)

## st.testing.v1.element_tree.DateInput

A representation of `st.date_input`.

**Class description** ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L512))

```python
st.testing.v1.element_tree.DateInput(proto, root)
```

**Methods**

*   [run](/develop/api-reference/app-testing/testing-element-classes#dateinputrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set_value](/develop/api-reference/app-testing/testing-element-classes#dateinputset_value)(v)

    Set the value of the widget.

**Attributes**

*   [value](/develop/api-reference/app-testing/testing-element-classes#dateinputvalue)

    The value of the widget. (date or Tuple of date)

## st.testing.v1.element_tree.Multiselect


## st.testing.v1.element_tree.Multiselect

A representation of `st.multiselect`.

**Class description** ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L774 "View st.Multiselect source code on GitHub"))

`st.testing.v1.element_tree.Multiselect(proto, root)`

**Methods**

*   [run](/develop/api-reference/app-testing/testing-element-classes#multiselectrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [select](/develop/api-reference/app-testing/testing-element-classes#multiselectselect)(v)

    Add a selection to the widget. Do nothing if the value is already selected. If testing a multiselect widget with repeated options, use `set_value` instead.
*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#multiselectset_value)(v)

    Set the value of the multiselect widget. (list)
*   [unselect](/develop/api-reference/app-testing/testing-element-classes#multiselectunselect)(v)

    Remove a selection from the widget. Do nothing if the value is not already selected. If a value is selected multiple times, the first instance is removed.

**Attributes**

*   [format\_func](/develop/api-reference/app-testing/testing-element-classes#multiselectformat_func)

    The widget's formatting function for displaying options. (callable)
*   [indices](/develop/api-reference/app-testing/testing-element-classes#multiselectindices)

    The indices of the currently selected values from the options. (list)
*   [value](/develop/api-reference/app-testing/testing-element-classes#multiselectvalue)

    The currently selected values from the options. (list)
*   [values](/develop/api-reference/app-testing/testing-element-classes#multiselectvalues)

    The currently selected values from the options. (list)

## st.testing.v1.element_tree.NumberInput

A representation of `st.number_input`.

**Class description** ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L867 "View st.NumberInput source code on GitHub"))

`st.testing.v1.element_tree.NumberInput(proto, root)`

**Methods**

*   [decrement](/develop/api-reference/app-testing/testing-element-classes#numberinputdecrement)()

    Decrement the `st.number_input` widget as if the user clicked "-".
*   [increment](/develop/api-reference/app-testing/testing-element-classes#numberinputincrement)()

    Increment the `st.number_input` widget as if the user clicked "+".
*   [run](/develop/api-reference/app-testing/testing-element-classes#numberinputrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#numberinputset_value)(v)

    Set the value of the `st.number_input` widget.

**Attributes**

*   [value](/develop/api-reference/app-testing/testing-element-classes#numberinputvalue)

    Get the current value of the `st.number_input` widget.

## st.testing.v1.element_tree.Radio

A representation of `st.radio`.

**Class description** ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L928 "View st.Radio source code on GitHub"))

`st.testing.v1.element_tree.Radio(proto, root)`

**Methods**

*   [run](/develop/api-reference/app-testing/testing-element-classes#radiorun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#radioset_value)(v)

    Set the selection by value.

**Attributes**

*   [format\_func](/develop/api-reference/app-testing/testing-element-classes#radioformat_func)

    The widget's formatting function for displaying options. (callable)
*   [index](/develop/api-reference/app-testing/testing-element-classes#radioindex)

    The index of the current selection. (int)
*   [value](/develop/api-reference/app-testing/testing-element-classes#radiovalue)

    The currently selected value from the options. (Any)

## st.testing.v1.element_tree.SelectSlider

A representation of `st.select_slider`.

**Class description** ([source](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1058 "View st.SelectSlider source code on GitHub"))

`st.testing.v1.element_tree.SelectSlider(proto, root)`

**Methods**

*   [run](/develop/api-reference/app-testing/testing-element-classes#selectsliderrun)(\*, timeout=None)

    Run the AppTest script which contains the element.
*   [set\_range](/develop/api-reference/app-testing/testing-element-classes#selectsliderset_range)(lower, upper)

    Set the ranged selection by values.
*   [set\_value](/develop/api-reference/app-testing/testing-element-classes#selectsliderset_value)(v)

    Set the (single) selection by value.

**Attributes**

*   [format\_func](/develop/api-reference/app-testing/testing-element-classes#selectsliderformat_func)

    The widget's formatting function for displaying options. (callable)
*   [value](/develop/api-reference/app-testing/testing-element-classes#selectslidervalue)

    The currently selected value or range. (Any or Sequence of Any)

## st.testing.v1.element_tree.Selectbox


## `st.testing.v1.element_tree.Selectbox`

A representation of `st.selectbox`.

### Class description [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L987 "View st.Selectbox source code on GitHub")

```python
st.testing.v1.element_tree.Selectbox(proto, root)
```

### Methods

*   `run(*, timeout=None)`
    Run the AppTest script which contains the element.
*   `select(v)`
    Set the selection by value.
*   `select_index(index)`
    Set the selection by index.
*   `set_value(v)`
    Set the selection by value.

### Attributes

*   `format_func`
    The widget's formatting function for displaying options. (callable)
*   `index`
    The index of the current selection. (int)
*   `value`
    The currently selected value from the options. (Any)

## `st.testing.v1.element_tree.Slider`

A representation of `st.slider`.

### Class description [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1121 "View st.Slider source code on GitHub")

```python
st.testing.v1.element_tree.Slider(proto, root)
```

### Methods

*   `run(*, timeout=None)`
    Run the AppTest script which contains the element.
*   `set_range(lower, upper)`
    Set the ranged value of the slider.
*   `set_value(v)`
    Set the (single) value of the slider.

### Attributes

*   `value`
    The currently selected value or range. (Any or Sequence of Any)

## `st.testing.v1.element_tree.TextArea`

A representation of `st.text_area`.

### Class description [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1207 "View st.TextArea source code on GitHub")

```python
st.testing.v1.element_tree.TextArea(proto, root)
```

### Methods

*   `input(v)`
    Set the value of the widget only if the value does not exceed the maximum allowed characters.
*   `run(*, timeout=None)`
    Run the AppTest script which contains the element.
*   `set_value(v)`
    Set the value of the widget.

### Attributes

*   `value`
    The current value of the widget. (str)

## `st.testing.v1.element_tree.TextInput`

A representation of `st.text_input`.

### Class description [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1259 "View st.TextInput source code on GitHub")

```python
st.testing.v1.element_tree.TextInput(proto, root)
```

### Methods

*   `input(v)`
    Set the value of the widget only if the value does not exceed the maximum allowed characters.
*   `run(*, timeout=None)`
    Run the AppTest script which contains the element.
*   `set_value(v)`
    Set the value of the widget.

### Attributes

*   `value`
    The current value of the widget. (str)

## `st.testing.v1.element_tree.TimeInput`

A representation of `st.time_input`.

### Class description [[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1314 "View st.TimeInput source code on GitHub")

```python
st.testing.v1.element_tree.TimeInput(proto, root)
```

### Methods

*   `decrement()`
    Select the previous available time.
*   `increment()`
    Select the next available time.
*   `run(*, timeout=None)`
    Run the AppTest script which contains the element.
*   `set_value(v)`
    Set the value of the widget.

### Attributes

*   `value`
    The current value of the widget. (time)

## `st.testing.v1.element_tree.Toggle`

### `st.testing.v1.element_tree.Toggle`

A representation of `st.toggle`.

**Class Description**

[View `st.Toggle` source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1387 "View st.Toggle source code on GitHub")

```python
st.testing.v1.element_tree.Toggle(proto, root)
```

**Methods**

*   **`run(*, timeout=None)`**
    Run the `AppTest` script which contains the element.

*   **`set_value(v)`**
    Set the value of the widget.

**Attributes**

*   **`value`**
    The current value of the widget. (bool)

***

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.