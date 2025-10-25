Here is the HTML converted to clean Markdown:

# Testing element classes - Streamlit Docs

## Documentation

### Search
Search

### Menu
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
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
				- [st.testing.v1.AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest)
				- [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)
			- [Command line](/develop/api-reference/cli)
	+ [Tutorials](/develop/tutorials)
	+ [Quick reference](/develop/quick-reference)
* [Deploy](/deploy)
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* [Knowledge base](/knowledge-base)
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [App testing](/develop/api-reference/app-testing)
* [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)

# Testing Element Classes
Testing element classes are used to represent and interact with various Streamlit elements in a testing context.

## st.testing.v1.element_tree.Block
A `Block` instance represents a container of elements, similar to how `AppTest` represents the entire app.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
* Attributes:
	+ Various attributes corresponding to the original element's parameters.

## st.testing.v1.element_tree.Element
The base class for testing elements.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
* Attributes:
	+ `value`: The value or contents of the element.

## st.testing.v1.element_tree.Button
A representation of `st.button` and `st.form_submit_button`.

* Methods:
	+ `click()`: Set the button's value to True.
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the button's value.
* Attributes:
	+ `value`: The button's value (bool).

## st.testing.v1.element_tree.ChatInput
A representation of `st.chat_input`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the widget's value.
* Attributes:
	+ `value`: The widget's value (str).

## st.testing.v1.element_tree.Checkbox
A representation of `st.checkbox`.

* Methods:
	+ `check()`: Set the widget's value to True.
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the widget's value.
	+ `uncheck()`: Set the widget's value to False.
* Attributes:
	+ `value`: The widget's value (bool).

## st.testing.v1.element_tree.ColorPicker
A representation of `st.color_picker`.

* Methods:
	+ `pick(v)`: Set the widget's value as a hex string.
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the widget's value as a hex string.
* Attributes:
	+ `value`: The currently selected value as a hex string (str).

## st.testing.v1.element_tree.DateInput
A representation of `st.date_input`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the widget's value.
* Attributes:
	+ `value`: The widget's value (date or tuple of date).

## st.testing.v1.element_tree.Multiselect
A representation of `st.multiselect`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `select(v)`: Add a selection to the widget.
	+ `set_value(v)`: Set the widget's value.
	+ `unselect(v)`: Remove a selection from the widget.
* Attributes:
	+ `format_func`: The widget's formatting function for displaying options (callable).
	+ `indices`: The indices of the currently selected values (list).
	+ `value`: The currently selected values (list).
	+ `values`: The currently selected values (list).

## st.testing.v1.element_tree.NumberInput
A representation of `st.number_input`.

* Methods:
	+ `decrement()`: Decrement the widget's value.
	+ `increment()`: Increment the widget's value.
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the widget's value.
* Attributes:
	+ `value`: The widget's value.

## st.testing.v1.element_tree.Radio
A representation of `st.radio`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the selection by value.
* Attributes:
	+ `format_func`: The widget's formatting function for displaying options (callable).
	+ `index`: The index of the current selection (int).
	+ `value`: The currently selected value (Any).

## st.testing.v1.element_tree.SelectSlider
A representation of `st.select_slider`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_range(lower, upper)`: Set the ranged selection.
	+ `set_value(v)`: Set the single selection.
* Attributes:
	+ `format_func`: The widget's formatting function for displaying options (callable).
	+ `value`: The currently selected value or range (Any or Sequence of Any).

## st.testing.v1.element_tree.Selectbox
A representation of `st.selectbox`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `select(v)`: Set the selection by value.
	+ `select_index(index)`: Set the selection by index.
	+ `set_value(v)`: Set the selection by value.
* Attributes:
	+ `format_func`: The widget's formatting function for displaying options (callable).
	+ `index`: The index of the current selection (int).
	+ `value`: The currently selected value (Any).

## st.testing.v1.element_tree.Slider
A representation of `st.slider`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_range(lower, upper)`: Set the ranged value.
	+ `set_value(v)`: Set the single value.
* Attributes:
	+ `value`: The currently selected value or range (Any or Sequence of Any).

## st.testing.v1.element_tree.TextArea
A representation of `st.text_area`.

* Methods:
	+ `input(v)`: Set the widget's value if it does not exceed the maximum allowed characters.
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the widget's value.
* Attributes:
	+ `value`: The widget's current value (str).

## st.testing.v1.element_tree.TextInput
A representation of `st.text_input`.

* Methods:
	+ `input(v)`: Set the widget's value if it does not exceed the maximum allowed characters.
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the widget's value.
* Attributes:
	+ `value`: The widget's current value (str).

## st.testing.v1.element_tree.TimeInput
A representation of `st.time_input`.

* Methods:
	+ `decrement()`: Select the previous available time.
	+ `increment()`: Select the next available time.
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the widget's value.
* Attributes:
	+ `value`: The widget's current value (time).

## st.testing.v1.element_tree.Toggle
A representation of `st.toggle`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script containing the element.
	+ `set_value(v)`: Set the widget's value.
* Attributes:
	+ `value`: The widget's current value (bool).