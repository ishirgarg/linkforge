## Testing Element Classes - Streamlit Docs
![Logo](/logo.svg)

### Documentation
#### Search
Search

### Menu
* [Get Started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First Steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API Reference](/develop/api-reference)
		- PAGE ELEMENTS
			- [Write and Magic](/develop/api-reference/write-magic)
			- [Text Elements](/develop/api-reference/text)
			- [Data Elements](/develop/api-reference/data)
			- [Chart Elements](/develop/api-reference/charts)
			- [Input Widgets](/develop/api-reference/widgets)
			- [Media Elements](/develop/api-reference/media)
			- [Layouts and Containers](/develop/api-reference/layout)
			- [Chat Elements](/develop/api-reference/chat)
			- [Status Elements](/develop/api-reference/status)
			- [Third-party Components](https://streamlit.io/components)
		- APPLICATION LOGIC
			- [Authentication and User Info](/develop/api-reference/user)
			- [Navigation and Pages](/develop/api-reference/navigation)
			- [Execution Flow](/develop/api-reference/execution-flow)
			- [Caching and State](/develop/api-reference/caching-and-state)
			- [Connections and Secrets](/develop/api-reference/connections)
			- [Custom Components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- TOOLS
			- [App Testing](/develop/api-reference/app-testing)
				- [Testing Element Classes](/develop/api-reference/app-testing/testing-element-classes)
			- [Command Line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick Reference](/develop/quick-reference)
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other Platforms](/deploy/tutorials)
* [Knowledge Base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing Dependencies](/knowledge-base/dependencies)
	+ [Deployment Issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API Reference](/develop/api-reference)
* [App Testing](/develop/api-reference/app-testing)
* [Testing Element Classes](/develop/api-reference/app-testing/testing-element-classes)

Here is the provided HTML content converted to Markdown:

# Testing Element Classes
## st.testing.v1.element_tree.Block
The `Block` class has the same methods and attributes as `AppTest`. A `Block` instance represents a container of elements just as `AppTest` represents the entire app. For example, `Block.button` will produce a `WidgetList` of `Button` in the same manner as [`AppTest.button`](/develop/api-reference/testing/st.testing.v1.apptest#apptestbutton).

`ChatMessage`, `Column`, and `Tab` all inherit from `Block`. For all container classes, parameters of the original element can be obtained as properties. For example, `ChatMessage.avatar` and `Tab.label`.

## st.testing.v1.element_tree.Element
Element base class for testing.

This class's methods and attributes are universal for all elements implemented in testing. For example, Caption, Code, Text, and Title inherit from Element. All widget classes also inherit from Element, but have additional methods specific to each widget type. See the AppTest class for the full list of supported elements.

For all element classes, parameters of the original element can be obtained as properties. For example, Button.label, Caption.help, and Toast.icon.

### Class Description
[View st.Element source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L103)

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
### Attributes
* `value`: The value or contents of the element.

## st.testing.v1.element_tree.Button
A representation of st.button and st.form_submit_button.

### Class Description
[View st.Button source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L302)

### Methods
* `click()`: Set the value of the button to True.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the button.
### Attributes
* `value`: The value of the button. (bool)

## st.testing.v1.element_tree.ChatInput
A representation of st.chat_input.

### Class Description
[View st.ChatInput source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L344)

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
### Attributes
* `value`: The value of the widget. (str)

## st.testing.v1.element_tree.Checkbox
A representation of st.checkbox.

### Class Description
[View st.Checkbox source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L379)

### Methods
* `check()`: Set the value of the widget to True.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
* `uncheck()`: Set the value of the widget to False.
### Attributes
* `value`: The value of the widget. (bool)

## st.testing.v1.element_tree.ColorPicker
A representation of st.color_picker.

### Class Description
[View st.ColorPicker source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L446)

### Methods
* `pick(v)`: Set the value of the widget as a hex string. May omit the "#" prefix.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget as a hex string.
### Attributes
* `value`: The currently selected value as a hex string. (str)

## st.testing.v1.element_tree.DateInput
A representation of st.date_input.

### Class Description
[View st.DateInput source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L512)

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
### Attributes
* `value`: The value of the widget. (date or Tuple of date)

## st.testing.v1.element_tree.Multiselect
A representation of st.multiselect.

### Class Description
[View st.Multiselect source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L774)

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `select(v)`: Add a selection to the widget. Do nothing if the value is already selected. If testing a multiselect widget with repeated options, use set_value instead.
* `set_value(v)`: Set the value of the multiselect widget. (list)
* `unselect(v)`: Remove a selection from the widget. Do nothing if the value is not already selected. If a value is selected multiple times, the first instance is removed.
### Attributes
* `format_func`: The widget's formatting function for displaying options. (callable)
* `indices`: The indices of the currently selected values from the options. (list)
* `value`: The currently selected values from the options. (list)
* `values`: The currently selected values from the options. (list)

## st.testing.v1.element_tree.NumberInput
A representation of st.number_input.

### Class Description
[View st.NumberInput source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L867)

### Methods
* `decrement()`: Decrement the st.number_input widget as if the user clicked "-".
* `increment()`: Increment the st.number_input widget as if the user clicked "+".
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the st.number_input widget.
### Attributes
* `value`: Get the current value of the st.number_input widget.

## st.testing.v1.element_tree.Radio
A representation of st.radio.

### Class Description
[View st.Radio source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L928)

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the selection by value.
### Attributes
* `format_func`: The widget's formatting function for displaying options. (callable)
* `index`: The index of the current selection. (int)
* `value`: The currently selected value from the options. (Any)

## st.testing.v1.element_tree.SelectSlider
A representation of st.select_slider.

### Class Description
[View st.SelectSlider source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1058)

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_range(lower, upper)`: Set the ranged selection by values.
* `set_value(v)`: Set the (single) selection by value.
### Attributes
* `format_func`: The widget's formatting function for displaying options. (callable)
* `value`: The currently selected value or range. (Any or Sequence of Any)

## st.testing.v1.element_tree.Selectbox
A representation of st.selectbox.

### Class Description
[View st.Selectbox source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L987)

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `select(v)`: Set the selection by value.
* `select_index(index)`: Set the selection by index.
* `set_value(v)`: Set the selection by value.
### Attributes
* `format_func`: The widget's formatting function for displaying options. (callable)
* `index`: The index of the current selection. (int)
* `value`: The currently selected value from the options. (Any)

## st.testing.v1.element_tree.Slider
A representation of st.slider.

### Class Description
[View st.Slider source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1121)

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_range(lower, upper)`: Set the ranged value of the slider.
* `set_value(v)`: Set the (single) value of the slider.
### Attributes
* `value`: The currently selected value or range. (Any or Sequence of Any)

## st.testing.v1.element_tree.TextArea
A representation of st.text_area.

### Class Description
[View st.TextArea source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1207)

### Methods
* `input(v)`: Set the value of the widget only if the value does not exceed the maximum allowed characters.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
### Attributes
* `value`: The current value of the widget. (str)

## st.testing.v1.element_tree.TextInput
A representation of st.text_input.

### Class Description
[View st.TextInput source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1259)

### Methods
* `input(v)`: Set the value of the widget only if the value does not exceed the maximum allowed characters.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
### Attributes
* `value`: The current value of the widget. (str)

## st.testing.v1.element_tree.TimeInput
A representation of st.time_input.

### Class Description
[View st.TimeInput source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1314)

### Methods
* `decrement()`: Select the previous available time.
* `increment()`: Select the next available time.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
### Attributes
* `value`: The current value of the widget. (time)

## st.testing.v1.element_tree.Toggle
A representation of st.toggle.

### Class Description
[View st.Toggle source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/testing/v1/element_tree.py#L1387)

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
### Attributes
* `value`: The current value of the widget. (bool)