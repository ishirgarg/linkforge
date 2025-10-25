Here is the converted text to clean Markdown:

# API Reference - Streamlit Docs
## Table of Contents
* [Get started](#get-started)
* [Develop](#develop)
* [API reference](#api-reference)
* [App logic and configuration](#app-logic-and-configuration)
* [Developer tools](#developer-tools)

## Get started
* [Installation](#installation)
* [Fundamentals](#fundamentals)
* [First steps](#first-steps)

## Develop
* [Concepts](#concepts)
* [API reference](#api-reference)
* [Tutorials](#tutorials)
* [Quick reference](#quick-reference)

## API Reference
Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

### Display almost anything
* [Write and magic](#write-and-magic)
* [Text elements](#text-elements)

#### Write and magic
Write arguments to the app.
```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

#### Text elements
Display string formatted as Markdown.
```python
st.markdown("Hello **world**!")
```

### Data elements
* [Dataframes](#dataframes)
* [Data editors](#data-editors)

#### Dataframes
Display a dataframe as an interactive table.
```python
st.dataframe(my_data_frame)
```

#### Data editors
Display a data editor widget.
```python
edited = st.data_editor(df, num_rows="dynamic")
```

### Chart elements
* [Simple area charts](#simple-area-charts)
* [Simple bar charts](#simple-bar-charts)

#### Simple area charts
Display an area chart.
```python
st.area_chart(my_data_frame)
```

#### Simple bar charts
Display a bar chart.
```python
st.bar_chart(my_data_frame)
```

### Input widgets
* [Button](#button)
* [Download button](#download-button)

#### Button
Display a button widget.
```python
clicked = st.button("Click me")
```

#### Download button
Display a download button widget.
```python
st.download_button("Download file", file)
```

### Media elements
* [Image](#image)
* [Logo](#logo)

#### Image
Display an image or list of images.
```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

#### Logo
Display a logo in the upper-left corner of your app and its sidebar.
```python
st.logo("logo.jpg")
```

### Layouts and containers
* [Columns](#columns)
* [Container](#container)

#### Columns
Insert containers laid out as side-by-side columns.
```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

#### Container
Insert a multi-element container.
```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

### Chat elements
* [Chat input](#chat-input)
* [Chat message](#chat-message)

#### Chat input
Display a chat input widget.
```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

#### Chat message
Insert a chat message container.
```python
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

### Status elements
* [Progress bar](#progress-bar)
* [Spinner](#spinner)

#### Progress bar
Display a progress bar.
```python
for i in range(101):
    st.progress(i)
    do_something_slow()
```

#### Spinner
Temporarily displays a message while executing a block of code.
```python
with st.spinner("Please wait..."):
    do_something_slow()
```

### App logic and configuration
* [Authentication and user info](#authentication-and-user-info)
* [Navigation and pages](#navigation-and-pages)

#### Authentication and user info
Log in a user.
```python
st.login()
```

#### Navigation and pages
Configure the available pages in a multipage app.
```python
st.navigation({
    "Your account" : [log_out, settings],
    "Reports" : [overview, usage],
    "Tools" : [search]
})
```

### Developer tools
* [App testing](#app-testing)

#### App testing
Simulates a running Streamlit app for testing.
```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

Note: This is not an exhaustive conversion, and you may need to reformat some sections to better fit the Markdown format. Additionally, some links and images may not translate directly to Markdown.