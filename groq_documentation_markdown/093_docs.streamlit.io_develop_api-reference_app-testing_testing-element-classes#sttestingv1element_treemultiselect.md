# Testing Element Classes - Streamlit Docs

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
Testing element classes are used to interact with and test Streamlit apps.

## st.testing.v1.element_tree.Block
The `Block` class has the same methods and attributes as `AppTest`. A `Block` instance represents a container of elements, just like `AppTest` represents the entire app.

### Example
```python
block = st.testing.v1.element_tree.Block(proto, root)
```

## st.testing.v1.element_tree.Element
The `Element` class is the base class for all elements in Streamlit. It has methods and attributes that are common to all elements.

### Methods
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the element.

### Attributes
* `value`: The value or contents of the element.

### Example
```python
element = st.testing.v1.element_tree.Element(proto, root)
element.run()
```

## st.testing.v1.element_tree.Button
The `Button` class represents a button element in Streamlit.

### Methods
* `click()`: Click the button.
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the button.

### Attributes
* `value`: The value of the button (bool).

### Example
```python
button = st.testing.v1.element_tree.Button(proto, root)
button.click()
```

## st.testing.v1.element_tree.ChatInput
The `ChatInput` class represents a chat input element in Streamlit.

### Methods
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the chat input.

### Attributes
* `value`: The value of the chat input (str).

### Example
```python
chat_input = st.testing.v1.element_tree.ChatInput(proto, root)
chat_input.set_value("Hello, world!")
```

## st.testing.v1.element_tree.Checkbox
The `Checkbox` class represents a checkbox element in Streamlit.

### Methods
* `check()`: Check the checkbox.
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the checkbox.
* `uncheck()`: Uncheck the checkbox.

### Attributes
* `value`: The value of the checkbox (bool).

### Example
```python
checkbox = st.testing.v1.element_tree.Checkbox(proto, root)
checkbox.check()
```

## st.testing.v1.element_tree.ColorPicker
The `ColorPicker` class represents a color picker element in Streamlit.

### Methods
* `pick(v)`: Pick a color.
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the color picker.

### Attributes
* `value`: The value of the color picker (str).

### Example
```python
color_picker = st.testing.v1.element_tree.ColorPicker(proto, root)
color_picker.pick("#FF0000")
```

## st.testing.v1.element_tree.DateInput
The `DateInput` class represents a date input element in Streamlit.

### Methods
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the date input.

### Attributes
* `value`: The value of the date input (date or tuple of date).

### Example
```python
date_input = st.testing.v1.element_tree.DateInput(proto, root)
date_input.set_value("2022-01-01")
```

## st.testing.v1.element_tree.Multiselect
The `Multiselect` class represents a multiselect element in Streamlit.

### Methods
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `select(v)`: Select an option.
* `set_value(v)`: Set the value of the multiselect.
* `unselect(v)`: Unselect an option.

### Attributes
* `format_func`: The widget's formatting function for displaying options (callable).
* `indices`: The indices of the currently selected values from the options (list).
* `value`: The currently selected values from the options (list).
* `values`: The currently selected values from the options (list).

### Example
```python
multiselect = st.testing.v1.element_tree.Multiselect(proto, root)
multiselect.select("Option 1")
```

## st.testing.v1.element_tree.NumberInput
The `NumberInput` class represents a number input element in Streamlit.

### Methods
* `decrement()`: Decrement the number input.
* `increment()`: Increment the number input.
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the number input.

### Attributes
* `value`: The current value of the number input.

### Example
```python
number_input = st.testing.v1.element_tree.NumberInput(proto, root)
number_input.increment()
```

## st.testing.v1.element_tree.Radio
The `Radio` class represents a radio element in Streamlit.

### Methods
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the selection by value.

### Attributes
* `format_func`: The widget's formatting function for displaying options (callable).
* `index`: The index of the current selection (int).
* `value`: The currently selected value from the options (any).

### Example
```python
radio = st.testing.v1.element_tree.Radio(proto, root)
radio.set_value("Option 1")
```

## st.testing.v1.element_tree.SelectSlider
The `SelectSlider` class represents a select slider element in Streamlit.

### Methods
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_range(lower, upper)`: Set the ranged selection by values.
* `set_value(v)`: Set the (single) selection by value.

### Attributes
* `format_func`: The widget's formatting function for displaying options (callable).
* `value`: The currently selected value or range (any or sequence of any).

### Example
```python
select_slider = st.testing.v1.element_tree.SelectSlider(proto, root)
select_slider.set_value("Option 1")
```

## st.testing.v1.element_tree.Selectbox
The `Selectbox` class represents a selectbox element in Streamlit.

### Methods
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `select(v)`: Set the selection by value.
* `select_index(index)`: Set the selection by index.
* `set_value(v)`: Set the selection by value.

### Attributes
* `format_func`: The widget's formatting function for displaying options (callable).
* `index`: The index of the current selection (int).
* `value`: The currently selected value from the options (any).

### Example
```python
selectbox = st.testing.v1.element_tree.Selectbox(proto, root)
selectbox.select("Option 1")
```

## st.testing.v1.element_tree.Slider
The `Slider` class represents a slider element in Streamlit.

### Methods
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_range(lower, upper)`: Set the ranged value of the slider.
* `set_value(v)`: Set the (single) value of the slider.

### Attributes
* `value`: The currently selected value or range (any or sequence of any).

### Example
```python
slider = st.testing.v1.element_tree.Slider(proto, root)
slider.set_value(5)
```

## st.testing.v1.element_tree.TextArea
The `TextArea` class represents a text area element in Streamlit.

### Methods
* `input(v)`: Set the value of the text area only if the value does not exceed the maximum allowed characters.
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the text area.

### Attributes
* `value`: The current value of the text area (str).

### Example
```python
text_area = st.testing.v1.element_tree.TextArea(proto, root)
text_area.input("Hello, world!")
```

## st.testing.v1.element_tree.TextInput
The `TextInput` class represents a text input element in Streamlit.

### Methods
* `input(v)`: Set the value of the text input only if the value does not exceed the maximum allowed characters.
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the text input.

### Attributes
* `value`: The current value of the text input (str).

### Example
```python
text_input = st.testing.v1.element_tree.TextInput(proto, root)
text_input.input("Hello, world!")
```

## st.testing.v1.element_tree.TimeInput
The `TimeInput` class represents a time input element in Streamlit.

### Methods
* `decrement()`: Select the previous available time.
* `increment()`: Select the next available time.
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the time input.

### Attributes
* `value`: The current value of the time input (time).

### Example
```python
time_input = st.testing.v1.element_tree.TimeInput(proto, root)
time_input.set_value("12:00:00")
```

## st.testing.v1.element_tree.Toggle
The `Toggle` class represents a toggle element in Streamlit.

### Methods
* `run(*, timeout=None)`: Run the AppTest script that contains the element.
* `set_value(v)`: Set the value of the toggle.

### Attributes
* `value`: The current value of the toggle (bool).

### Example
```python
toggle = st.testing.v1.element_tree.Toggle(proto, root)
toggle.set_value(True)
```