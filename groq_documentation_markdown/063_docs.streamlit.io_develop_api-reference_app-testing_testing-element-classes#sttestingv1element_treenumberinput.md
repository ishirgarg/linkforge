Here is the clean markdown version:

# Testing element classes - Streamlit Docs
## Documentation
### Search
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

Note: I removed the unnecessary `_add_`, `_remove_`, and `_rocket_launch_` symbols, as well as the logo and other unnecessary HTML elements. I also reformatted the text to follow standard markdown formatting conventions. Let me know if you have any further requests!

# Testing Element Classes
Testing element classes are used to interact with Streamlit elements in a testing environment.

## st.testing.v1.element_tree.Block
The `Block` class has the same methods and attributes as `AppTest`. A `Block` instance represents a container of elements just as `AppTest` represents the entire app.

* `ChatMessage`, `Column`, and `Tab` all inherit from `Block`.
* For all container classes, parameters of the original element can be obtained as properties.

## st.testing.v1.element_tree.Element
Element base class for testing.

* This class's methods and attributes are universal for all elements implemented in testing.
* For example, `Caption`, `Code`, `Text`, and `Title` inherit from `Element`.
* All widget classes also inherit from `Element`, but have additional methods specific to each widget type.

## st.testing.v1.element_tree.Button
A representation of `st.button` and `st.form_submit_button`.

* Methods:
	+ `click()`: Set the value of the button to True.
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the button.
* Attributes:
	+ `value`: The value of the button. (bool)

## st.testing.v1.element_tree.ChatInput
A representation of `st.chat_input`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the widget.
* Attributes:
	+ `value`: The value of the widget. (str)

## st.testing.v1.element_tree.Checkbox
A representation of `st.checkbox`.

* Methods:
	+ `check()`: Set the value of the widget to True.
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the widget.
	+ `uncheck()`: Set the value of the widget to False.
* Attributes:
	+ `value`: The value of the widget. (bool)

## st.testing.v1.element_tree.ColorPicker
A representation of `st.color_picker`.

* Methods:
	+ `pick(v)`: Set the value of the widget as a hex string.
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the widget as a hex string.
* Attributes:
	+ `value`: The currently selected value as a hex string. (str)

## st.testing.v1.element_tree.DateInput
A representation of `st.date_input`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the widget.
* Attributes:
	+ `value`: The value of the widget. (date or Tuple of date)

## st.testing.v1.element_tree.Multiselect
A representation of `st.multiselect`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `select(v)`: Add a selection to the widget.
	+ `set_value(v)`: Set the value of the multiselect widget.
	+ `unselect(v)`: Remove a selection from the widget.
* Attributes:
	+ `format_func`: The widget's formatting function for displaying options. (callable)
	+ `indices`: The indices of the currently selected values from the options. (list)
	+ `value`: The currently selected values from the options. (list)
	+ `values`: The currently selected values from the options. (list)

## st.testing.v1.element_tree.NumberInput
A representation of `st.number_input`.

* Methods:
	+ `decrement()`: Decrement the `st.number_input` widget as if the user clicked "-".
	+ `increment()`: Increment the `st.number_input` widget as if the user clicked "+".
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the `st.number_input` widget.
* Attributes:
	+ `value`: Get the current value of the `st.number_input` widget.

## st.testing.v1.element_tree.Radio
A representation of `st.radio`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the selection by value.
* Attributes:
	+ `format_func`: The widget's formatting function for displaying options. (callable)
	+ `index`: The index of the current selection. (int)
	+ `value`: The currently selected value from the options. (Any)

## st.testing.v1.element_tree.SelectSlider
A representation of `st.select_slider`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_range(lower, upper)`: Set the ranged selection by values.
	+ `set_value(v)`: Set the (single) selection by value.
* Attributes:
	+ `format_func`: The widget's formatting function for displaying options. (callable)
	+ `value`: The currently selected value or range. (Any or Sequence of Any)

## st.testing.v1.element_tree.Selectbox
A representation of `st.selectbox`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `select(v)`: Set the selection by value.
	+ `select_index(index)`: Set the selection by index.
	+ `set_value(v)`: Set the selection by value.
* Attributes:
	+ `format_func`: The widget's formatting function for displaying options. (callable)
	+ `index`: The index of the current selection. (int)
	+ `value`: The currently selected value from the options. (Any)

## st.testing.v1.element_tree.Slider
A representation of `st.slider`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_range(lower, upper)`: Set the ranged value of the slider.
	+ `set_value(v)`: Set the (single) value of the slider.
* Attributes:
	+ `value`: The currently selected value or range. (Any or Sequence of Any)

## st.testing.v1.element_tree.TextArea
A representation of `st.text_area`.

* Methods:
	+ `input(v)`: Set the value of the widget only if the value does not exceed the maximum allowed characters.
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the widget.
* Attributes:
	+ `value`: The current value of the widget. (str)

## st.testing.v1.element_tree.TextInput
A representation of `st.text_input`.

* Methods:
	+ `input(v)`: Set the value of the widget only if the value does not exceed the maximum allowed characters.
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the widget.
* Attributes:
	+ `value`: The current value of the widget. (str)

## st.testing.v1.element_tree.TimeInput
A representation of `st.time_input`.

* Methods:
	+ `decrement()`: Select the previous available time.
	+ `increment()`: Select the next available time.
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the widget.
* Attributes:
	+ `value`: The current value of the widget. (time)

## st.testing.v1.element_tree.Toggle
A representation of `st.toggle`.

* Methods:
	+ `run(*, timeout=None)`: Run the AppTest script which contains the element.
	+ `set_value(v)`: Set the value of the widget.
* Attributes:
	+ `value`: The current value of the widget. (bool)