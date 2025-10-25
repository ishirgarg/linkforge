Here is the HTML content converted to clean Markdown:

API Reference - Streamlit Docs
==========================

## Table of Contents

* [Getting Started](#getting-started)
* [Develop](#develop)
* [Deploy](#deploy)
* [Knowledge Base](#knowledge-base)
* [API Reference](#api-reference)

## Getting Started
------------

* [Installation](/get-started/installation)
* [Fundamentals](/get-started/fundamentals)
* [First steps](/get-started/tutorials)

## Develop
---------

* [Concepts](/develop/concepts)
* [API reference](/develop/api-reference)
* [Tutorials](/develop/tutorials)
* [Quick reference](/develop/quick-reference)

## Deploy
---------

* [Concepts](/deploy/concepts)
* [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
* [Snowflake](/deploy/snowflake)
* [Other platforms](/deploy/tutorials)

## Knowledge Base
----------------

* [FAQ](/knowledge-base/using-streamlit)
* [Installing dependencies](/knowledge-base/dependencies)
* [Deployment issues](/knowledge-base/deploy)

## API Reference
--------------

### Display almost anything

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

#### Dataframes

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

### Chart elements

#### Simple area charts

Display an area chart.

```python
st.area_chart(my_data_frame)
```

### Input widgets

#### Button

Display a button widget.

```python
clicked = st.button("Click me")
```

### Media elements

#### Image

Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

### Layouts and containers

#### Columns

Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

### Chat elements

#### Chat input

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

### Status elements

#### Progress bar

Display a progress bar.

```python
for i in range(101):
    st.progress(i)
    do_something_slow()
```

### App logic and configuration

#### Authentication and user info

Log in a user.

```python
st.login()
```

#### Navigation and pages

Configure the available pages in a multipage app.

```python
st.navigation({"Your account": [log_out, settings], "Reports": [overview, usage], "Tools": [search]})
```

### Developer tools

#### App testing

Simulate a running Streamlit app for testing.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```