Here is the HTML converted to clean markdown:

# Testing Element Classes - Streamlit Docs

## Documentation

### Get Started
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)

### Develop
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- PAGE ELEMENTS
			- [Write and magic](/develop/api-reference/write-magic)
			- [Text elements](/develop/api-reference/text)
			- [Data elements](/develop/api-reference/data)
			- [Chart elements](/develop/api-reference/charts)
			- [Input widgets](/develop/api-reference/widgets)
			- [Media elements](/develop/api-reference/media)
			- [Layouts and containers](/develop/api-reference/layout)
			- [Chat elements](/develop/api-reference/chat)
			- [Status elements](/develop/api-reference/status)
			- [Third-party components](https://streamlit.io/components)
		- APPLICATION LOGIC
			- [Authentication and user info](/develop/api-reference/user)
			- [Navigation and pages](/develop/api-reference/navigation)
			- [Execution flow](/develop/api-reference/execution-flow)
			- [Caching and state](/develop/api-reference/caching-and-state)
			- [Connections and secrets](/develop/api-reference/connections)
			- [Custom components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- TOOLS
			- [App testing](/develop/api-reference/app-testing)
				- [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)
			- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)

### Deploy
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)

### Knowledge Base
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Navigation
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [App testing](/develop/api-reference/app-testing)
* [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)

Here is the markdown version of the provided HTML:
# Testing Element Classes
## st.testing.v1.element_tree.Block
The `Block` class has the same methods and attributes as `AppTest`. A `Block` instance represents a container of elements just as `AppTest` represents the entire app. For example, `Block.button` will produce a `WidgetList` of `Button` in the same manner as [`AppTest.button`](/develop/api-reference/testing/st.testing.v1.apptest#apptestbutton).

`ChatMessage`, `Column`, and `Tab` all inherit from `Block`. For all container classes, parameters of the original element can be obtained as properties. For example, `ChatMessage.avatar` and `Tab.label`.

## st.testing.v1.element_tree.Element
### Class Description
Element base class for testing.

This class's methods and attributes are universal for all elements implemented in testing. For example, Caption, Code, Text, and Title inherit from Element. All widget classes also inherit from Element, but have additional methods specific to each widget type. See the AppTest class for the full list of supported elements.

For all element classes, parameters of the original element can be obtained as properties. For example, Button.label, Caption.help, and Toast.icon.

#### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
#### Attributes
* `value`: The value or contents of the element.

## st.testing.v1.element_tree.Button
### Class Description
A representation of st.button and st.form_submit_button.

#### Methods
* `click()`: Set the value of the button to True.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the button.
#### Attributes
* `value`: The value of the button. (bool)

## st.testing.v1.element_tree.ChatInput
### Class Description
A representation of st.chat_input.

#### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
#### Attributes
* `value`: The value of the widget. (str)

## st.testing.v1.element_tree.Checkbox
### Class Description
A representation of st.checkbox.

#### Methods
* `check()`: Set the value of the widget to True.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
* `uncheck()`: Set the value of the widget to False.
#### Attributes
* `value`: The value of the widget. (bool)

## st.testing.v1.element_tree.ColorPicker
### Class Description
A representation of st.color_picker.

#### Methods
* `pick(v)`: Set the value of the widget as a hex string. May omit the "#" prefix.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget as a hex string.
#### Attributes
* `value`: The currently selected value as a hex string. (str)

## st.testing.v1.element_tree.DateInput
### Class Description
A representation of st.date_input.

#### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
#### Attributes
* `value`: The value of the widget. (date or Tuple of date)

## st.testing.v1.element_tree.Multiselect
### Class Description
A representation of st.multiselect.

#### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `select(v)`: Add a selection to the widget. Do nothing if the value is already selected. If testing a multiselect widget with repeated options, use set_value instead.
* `set_value(v)`: Set the value of the multiselect widget. (list)
* `unselect(v)`: Remove a selection from the widget. Do nothing if the value is not already selected. If a value is selected multiple times, the first instance is removed.
#### Attributes
* `format_func`: The widget's formatting function for displaying options. (callable)
* `indices`: The indices of the currently selected values from the options. (list)
* `value`: The currently selected values from the options. (list)
* `values`: The currently selected values from the options. (list)

## st.testing.v1.element_tree.NumberInput
### Class Description
A representation of st.number_input.

#### Methods
* `decrement()`: Decrement the st.number_input widget as if the user clicked "-".
* `increment()`: Increment the st.number_input widget as if the user clicked "+".
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the st.number_input widget.
#### Attributes
* `value`: Get the current value of the st.number_input widget.

## st.testing.v1.element_tree.Radio
### Class Description
A representation of st.radio.

#### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the selection by value.
#### Attributes
* `format_func`: The widget's formatting function for displaying options. (callable)
* `index`: The index of the current selection. (int)
* `value`: The currently selected value from the options. (Any)

## st.testing.v1.element_tree.SelectSlider
### Class Description
A representation of st.select_slider.

#### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_range(lower, upper)`: Set the ranged selection by values.
* `set_value(v)`: Set the (single) selection by value.
#### Attributes
* `format_func`: The widget's formatting function for displaying options. (callable)
* `value`: The currently selected value or range. (Any or Sequence of Any)

## st.testing.v1.element_tree.Selectbox
### Class Description
A representation of st.selectbox.

#### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `select(v)`: Set the selection by value.
* `select_index(index)`: Set the selection by index.
* `set_value(v)`: Set the selection by value.
#### Attributes
* `format_func`: The widget's formatting function for displaying options. (callable)
* `index`: The index of the current selection. (int)
* `value`: The currently selected value from the options. (Any)

## st.testing.v1.element_tree.Slider
### Class Description
A representation of st.slider.

#### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_range(lower, upper)`: Set the ranged value of the slider.
* `set_value(v)`: Set the (single) value of the slider.
#### Attributes
* `value`: The currently selected value or range. (Any or Sequence of Any)

## st.testing.v1.element_tree.TextArea
### Class Description
A representation of st.text_area.

#### Methods
* `input(v)`: Set the value of the widget only if the value does not exceed the maximum allowed characters.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
#### Attributes
* `value`: The current value of the widget. (str)

## st.testing.v1.element_tree.TextInput
### Class Description
A representation of st.text_input.

#### Methods
* `input(v)`: Set the value of the widget only if the value does not exceed the maximum allowed characters.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
#### Attributes
* `value`: The current value of the widget. (str)

## st.testing.v1.element_tree.TimeInput
### Class Description
A representation of st.time_input.

#### Methods
* `decrement()`: Select the previous available time.
* `increment()`: Select the next available time.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
#### Attributes
* `value`: The current value of the widget. (time)

## st.testing.v1.element_tree.Toggle
### Class Description
A representation of st.toggle.

#### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
#### Attributes
* `value`: The current value of the widget. (bool)