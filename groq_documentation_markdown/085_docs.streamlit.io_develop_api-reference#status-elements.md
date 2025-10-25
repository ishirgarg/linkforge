Below is the content rewritten in clean Markdown:

API Reference - Streamlit Docs
================================

### Table of Contents

1. [Introduction](#introduction)
2. [Streamlit API Reference](#streamlit-api-reference)
3. [Display Almost Anything](#display-almost-anything)
4. [Text Elements](#text-elements)
5. [Data Elements](#data-elements)
6. [Chart Elements](#chart-elements)
7. [Input Widgets](#input-widgets)
8. [Media Elements](#media-elements)
9. [Layouts and Containers](#layouts-and-containers)
10. [Chat Elements](#chat-elements)
11. [Status Elements](#status-elements)
12. [App Logic and Configuration](#app-logic-and-configuration)
13. [Developer Tools](#developer-tools)

### Introduction

Streamlit makes it easy to visualize, mutate, and share data.

### Streamlit API Reference

Streamlit API is organized by activity type, like displaying data or optimizing performance.

### Display Almost Anything

#### Write and Magic

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

#### Magic

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`.

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

### Text Elements

#### Markdown

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

#### Title

Display text in title formatting.

```python
st.title("The app title")
```

#### Header

Display text in header formatting.

```python
st.header("This is a header")
```

#### Subheader

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```

### Data Elements

#### Dataframes

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

#### Data Editor

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

### Chart Elements

#### Simple Area Charts

Display an area chart.

```python
st.area_chart(my_data_frame)
```

#### Simple Bar Charts

Display a bar chart.

```python
st.bar_chart(my_data_frame)
```

### Input Widgets

#### Button

Display a button widget.

```python
clicked = st.button("Click me")
```

#### Download Button

Display a download button widget.

```python
st.download_button("Download file", file)
```

### Media Elements

#### Image

Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

### Layouts and Containers

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

### Chat Elements

#### Chat Input

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

### Status Elements

#### Progress Bar

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

### App Logic and Configuration

#### Authentication and User Info

```python
st.login()
st.logout()
if st.user.is_logged_in:
    st.write(f"Welcome back, {st.user.name}!")
```

#### Navigation and Pages

```python
st.navigation({
    "Your account": [log_out, settings],
    "Reports": [overview, usage],
    "Tools": [search]
})
```

### Developer Tools

#### App Testing

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."
```