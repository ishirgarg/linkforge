Here is the converted HTML to clean markdown:

# Testing element classes - Streamlit Docs

## Documentation
### Search
[Get started](/get-started)
* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

### Develop
[Develop](/develop)
* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
	+ PAGE ELEMENTS
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
	+ APPLICATION LOGIC
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
	+ TOOLS
		- [App testing](/develop/api-reference/app-testing)
			- [st.testing.v1.AppTest](/develop/api-reference/app-testing/st.testing.v1.apptest)
			- [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)
		- [Command line](/develop/api-reference/cli)
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

### Deploy
[Deploy](/deploy)
* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

### Knowledge base
[Knowledge base](/knowledge-base)
* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [App testing](/develop/api-reference/app-testing)
* [Testing element classes](/develop/api-reference/app-testing/testing-element-classes)

# Testing Element Classes
Testing element classes are used to represent and interact with Streamlit app elements in a testing environment.

## st.testing.v1.element_tree.Block
The `Block` class represents a container of elements, similar to `AppTest` representing the entire app. It has the same methods and attributes as `AppTest`.

* Inheritance: `ChatMessage`, `Column`, and `Tab` inherit from `Block`.
* Attributes: Parameters of the original element can be obtained as properties, e.g., `ChatMessage.avatar` and `Tab.label`.

## st.testing.v1.element_tree.Element
The `Element` class is the base class for all elements in testing.

* Inheritance: `Caption`, `Code`, `Text`, `Title`, and all widget classes inherit from `Element`.
* Attributes: Parameters of the original element can be obtained as properties, e.g., `Button.label`, `Caption.help`, and `Toast.icon`.

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `value`: The value or contents of the element.

## st.testing.v1.element_tree.Button
The `Button` class represents a button element.

### Methods
* `click()`: Set the value of the button to True.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the button.

### Attributes
* `value`: The value of the button (bool).

## st.testing.v1.element_tree.ChatInput
The `ChatInput` class represents a chat input element.

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.

### Attributes
* `value`: The value of the widget (str).

## st.testing.v1.element_tree.Checkbox
The `Checkbox` class represents a checkbox element.

### Methods
* `check()`: Set the value of the widget to True.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.
* `uncheck()`: Set the value of the widget to False.

### Attributes
* `value`: The value of the widget (bool).

## st.testing.v1.element_tree.ColorPicker
The `ColorPicker` class represents a color picker element.

### Methods
* `pick(v)`: Set the value of the widget as a hex string.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget as a hex string.

### Attributes
* `value`: The currently selected value as a hex string (str).

## st.testing.v1.element_tree.DateInput
The `DateInput` class represents a date input element.

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.

### Attributes
* `value`: The value of the widget (date or Tuple of date).

## st.testing.v1.element_tree.Multiselect
The `Multiselect` class represents a multiselect element.

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `select(v)`: Add a selection to the widget.
* `set_value(v)`: Set the value of the multiselect widget (list).
* `unselect(v)`: Remove a selection from the widget.

### Attributes
* `format_func`: The widget's formatting function for displaying options (callable).
* `indices`: The indices of the currently selected values from the options (list).
* `value`: The currently selected values from the options (list).
* `values`: The currently selected values from the options (list).

## st.testing.v1.element_tree.NumberInput
The `NumberInput` class represents a number input element.

### Methods
* `decrement()`: Decrement the st.number_input widget.
* `increment()`: Increment the st.number_input widget.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the st.number_input widget.

### Attributes
* `value`: The current value of the widget.

## st.testing.v1.element_tree.Radio
The `Radio` class represents a radio element.

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the selection by value.

### Attributes
* `format_func`: The widget's formatting function for displaying options (callable).
* `index`: The index of the current selection (int).
* `value`: The currently selected value from the options (Any).

## st.testing.v1.element_tree.SelectSlider
The `SelectSlider` class represents a select slider element.

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_range(lower, upper)`: Set the ranged selection by values.
* `set_value(v)`: Set the (single) selection by value.

### Attributes
* `format_func`: The widget's formatting function for displaying options (callable).
* `value`: The currently selected value or range (Any or Sequence of Any).

## st.testing.v1.element_tree.Selectbox
The `Selectbox` class represents a selectbox element.

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `select(v)`: Set the selection by value.
* `select_index(index)`: Set the selection by index.
* `set_value(v)`: Set the selection by value.

### Attributes
* `format_func`: The widget's formatting function for displaying options (callable).
* `index`: The index of the current selection (int).
* `value`: The currently selected value from the options (Any).

## st.testing.v1.element_tree.Slider
The `Slider` class represents a slider element.

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_range(lower, upper)`: Set the ranged value of the slider.
* `set_value(v)`: Set the (single) value of the slider.

### Attributes
* `value`: The currently selected value or range (Any or Sequence of Any).

## st.testing.v1.element_tree.TextArea
The `TextArea` class represents a text area element.

### Methods
* `input(v)`: Set the value of the widget only if the value does not exceed the maximum allowed characters.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.

### Attributes
* `value`: The current value of the widget (str).

## st.testing.v1.element_tree.TextInput
The `TextInput` class represents a text input element.

### Methods
* `input(v)`: Set the value of the widget only if the value does not exceed the maximum allowed characters.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.

### Attributes
* `value`: The current value of the widget (str).

## st.testing.v1.element_tree.TimeInput
The `TimeInput` class represents a time input element.

### Methods
* `decrement()`: Select the previous available time.
* `increment()`: Select the next available time.
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.

### Attributes
* `value`: The current value of the widget (time).

## st.testing.v1.element_tree.Toggle
The `Toggle` class represents a toggle element.

### Methods
* `run(*, timeout=None)`: Run the AppTest script which contains the element.
* `set_value(v)`: Set the value of the widget.

### Attributes
* `value`: The current value of the widget (bool).