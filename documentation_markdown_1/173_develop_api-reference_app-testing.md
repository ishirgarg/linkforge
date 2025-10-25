# App Testing

Streamlit app testing framework enables developers to build and run headless tests that execute their app code directly, simulate user input, and inspect rendered outputs for correctness.

The provided class, `AppTest`, simulates a running app and provides methods to set up, manipulate, and inspect the app contents via API instead of a browser UI. It can be used to write automated tests of an app in various scenarios. These can then be run using a tool like `pytest`. A typical pattern is to build a suite of tests for an app that ensure consistent functionality as the app evolves, and run the tests locally and/or in a CI environment like Github Actions.

## The AppTest class

### `st.testing.v1.AppTest`

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

### `AppTest.from_file`

`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

### `AppTest.from_string`

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

### `AppTest.from_function`

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

## Testing-element classes

---

*Original URL: https://docs.streamlit.io/develop/api-reference/app-testing*

### Element Classes

#### Block

A representation of container elements, including:

*   `st.chat_message`
*   `st.columns`
*   `st.sidebar`
*   `st.tabs`
*   The main body of the app.

```python
# at.sidebar returns a Block
# at.sidebar.button[0].click().run()
# assert not at.exception
```

[Link to Block documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeblock)

#### Element

The base class for representation of all elements, including:

*   `st.title`
*   `st.header`
*   `st.markdown`
*   `st.dataframe`

```python
# at.title returns a sequence of Title
# Title inherits from Element
# assert at.title[0].value == "My awesome app"
```

[Link to Element documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeelement)

#### Button

A representation of `st.button` and `st.form_submit_button`.

```python
# at.button[0].click().run()
```

[Link to Button documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treebutton)

#### ChatInput

A representation of `st.chat_input`.

```python
# at.chat_input[0].set_value("What is Streamlit?").run()
```

[Link to ChatInput documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treechatinput)

#### Checkbox

A representation of `st.checkbox`.

```python
# at.checkbox[0].check().run()
```

[Link to Checkbox documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecheckbox)

#### ColorPicker

A representation of `st.color_picker`.

```python
# at.color_picker[0].pick("#FF4B4B").run()
```

[Link to ColorPicker documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treecolorpicker)

#### DateInput

A representation of `st.date_input`.

```python
# release_date = datetime.date(2023, 10, 26)
# at.date_input[0].set_value(release_date).run()
```

[Link to DateInput documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treedateinput)

#### Multiselect

A representation of `st.multiselect`.

```python
# at.multiselect[0].select("New York").run()
```

[Link to Multiselect documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treemultiselect)

#### NumberInput

A representation of `st.number_input`.

```python
# at.number_input[0].increment().run()
```

[Link to NumberInput documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treenumberinput)

#### Radio

A representation of `st.radio`.

```python
# at.radio[0].set_value("New York").run()
```

[Link to Radio documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeradio)

#### SelectSlider

A representation of `st.select_slider`.

```python
# at.select_slider[0].set_range("A","C").run()
```

[Link to SelectSlider documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectslider)

#### Selectbox

A representation of `st.selectbox`.

```python
# at.selectbox[0].select("New York").run()
```

[Link to Selectbox documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeselectbox)

#### Slider

A representation of `st.slider`.

```python
# at.slider[0].set_range(2,5).run()
```

[Link to Slider documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treeslider)

#### TextArea

A representation of `st.text_area`.

```python
# at.text_area[0].input("Streamlit is awesome!").run()
```

[Link to TextArea documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextarea)

#### TextInput

A representation of `st.text_input`.

```python
# at.text_input[0].input("Streamlit").run()
```

[Link to TextInput documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetextinput)

#### TimeInput

A representation of `st.time_input`.

```python
# at.time_input[0].increment().run()
```

[Link to TimeInput documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetimeinput)

#### Toggle

A representation of `st.toggle`.

```python
# at.toggle[0].set_value("True").run()
```

[Link to Toggle documentation](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treetoggle)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
