# API Reference
Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

## Display Almost Anything
### Write and Magic
Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

### Text Elements
Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

## Data Elements
### Dataframes
Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

## Chart Elements
### Simple Area Charts
Display an area chart.

```python
st.area_chart(my_data_frame)
```

## Input Widgets
### Button
Display a button widget.

```python
clicked = st.button("Click me")
```

## Media Elements
### Image
Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

## Layouts and Containers
### Columns
Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

## Chat Elements
### Chat Input
Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

## Status Elements
### Progress Bar
Display a progress bar.

```python
for i in range(101):
    st.progress(i)
    do_something_slow()
```

## App Logic and Configuration
### Authentication and User Info
Log in a user.

```python
st.login()
```

### Navigation and Pages
Configure the available pages in a multipage app.

```python
st.navigation({
    "Your account": [log_out, settings],
    "Reports": [overview, usage],
    "Tools": [search]
})
```

## Developer Tools
### App Testing
Simulate a running Streamlit app for testing.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."
```