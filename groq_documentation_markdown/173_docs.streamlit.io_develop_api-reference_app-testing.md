Here is the HTML converted to clean markdown:

# App testing - Streamlit Docs
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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [App testing](/develop/api-reference/app-testing)

Here is the HTML converted to clean Markdown:
### App Testing
Streamlit app testing framework enables developers to build and run headless tests that execute their app code directly, simulate user input, and inspect rendered outputs for correctness.

The provided class, `AppTest`, simulates a running app and provides methods to set up, manipulate, and inspect the app contents via API instead of a browser UI. It can be used to write automated tests of an app in various scenarios. These can then be run using a tool like pytest. A typical pattern is to build a suite of tests for an app that ensure consistent functionality as the app evolves, and run the tests locally and/or in a CI environment like Github Actions.

#### The AppTest Class
`st.testing.v1.AppTest` simulates a running Streamlit app for testing.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."
```

### AppTest Methods
#### AppTest.from_file
`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

#### AppTest.from_string
`st.testing.v1.AppTest.from_string` initializes a simulated app from a string.

```python
from streamlit.testing.v1 import AppTest
app_script = """
import streamlit as st
word_of_the_day = st.text_input("What's the word of the day?", key="word")
if word_of_the_day == st.secrets["WORD"]:
    st.success("That's right!")
elif word_of_the_day and word_of_the_day != st.secrets["WORD"]:
    st.warn("Try again.")
"""
at = AppTest.from_string(app_script)
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

#### AppTest.from_function
`st.testing.v1.AppTest.from_function` initializes a simulated app from a function.

```python
from streamlit.testing.v1 import AppTest
def app_script():
    import streamlit as st
    word_of_the_day = st.text_input("What's the word of the day?", key="word")
    if word_of_the_day == st.secrets["WORD"]:
        st.success("That's right!")
    elif word_of_the_day and word_of_the_day != st.secrets["WORD"]:
        st.warn("Try again.")
at = AppTest.from_function(app_script)
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

### Testing Element Classes
The following classes represent different Streamlit elements:

* `Block`: A representation of container elements, including `st.chat_message`, `st.columns`, `st.sidebar`, `st.tabs`, and the main body of the app.
* `Element`: The base class for representation of all elements, including `st.title`, `st.header`, `st.markdown`, and `st.dataframe`.
* `Button`: A representation of `st.button` and `st.form_submit_button`.
* `ChatInput`: A representation of `st.chat_input`.
* `Checkbox`: A representation of `st.checkbox`.
* `ColorPicker`: A representation of `st.color_picker`.
* `DateInput`: A representation of `st.date_input`.
* `Multiselect`: A representation of `st.multiselect`.
* `NumberInput`: A representation of `st.number_input`.
* `Radio`: A representation of `st.radio`.
* `SelectSlider`: A representation of `st.select_slider`.
* `Selectbox`: A representation of `st.selectbox`.
* `Slider`: A representation of `st.slider`.
* `TextArea`: A representation of `st.text_area`.
* `TextInput`: A representation of `st.text_input`.
* `TimeInput`: A representation of `st.time_input`.
* `Toggle`: A representation of `st.toggle`.

Example usage:
```python
at.button[0].click().run()
at.chat_input[0].set_value("What is Streamlit?").run()
at.checkbox[0].check().run()
```