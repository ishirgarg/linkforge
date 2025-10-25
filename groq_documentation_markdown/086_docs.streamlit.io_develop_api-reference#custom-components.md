Here is the rewritten text in clean Markdown format:

API Reference
================

## Introduction

Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

## Display Almost Anything

### Write and Magic

You can use `st.write` to write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

### Text Elements

You can use `st.markdown` to display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

## Chart Elements

### Simple Area Charts

You can use `st.area_chart` to display an area chart.

```python
st.area_chart(my_data_frame)
```

### Simple Bar Charts

You can use `st.bar_chart` to display a bar chart.

```python
st.bar_chart(my_data_frame)
```

### Simple Line Charts

You can use `st.line_chart` to display a line chart.

```python
st.line_chart(my_data_frame)
```

## Input Widgets

### Button

You can use `st.button` to display a button widget.

```python
clicked = st.button("Click me")
```

### Checkbox

You can use `st.checkbox` to display a checkbox widget.

```python
selected = st.checkbox("I agree")
```

### Color Picker

You can use `st.color_picker` to display a color picker widget.

```python
color = st.color_picker("Pick a color")
```

## Media Elements

### Image

You can use `st.image` to display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```

### Logo

You can use `st.logo` to display a logo in the upper-left corner of your app and its sidebar.

```python
st.logo("logo.jpg")
```

## Layouts and Containers

### Columns

You can use `st.columns` to insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

### Container

You can use `st.container` to insert a multi-element container.

```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

## Chat Elements

### Chat Input

You can use `st.chat_input` to display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```

### Chat Message

You can use `st.chat_message` to insert a chat message container.

```python
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

## Status Elements

### Progress Bar

You can use `st.progress` to display a progress bar.

```python
for i in range(101):
    st.progress(i)
    do_something_slow()
```

### Spinner

You can use `st.spinner` to temporarily display a message while executing a block of code.

```python
with st.spinner("Please wait..."):
    do_something_slow()
```

## App Logic and Configuration

### Authentication and User Info

You can use `st.login` to start an authentication flow with an identity provider.

```python
st.login()
```

### Navigation and Pages

You can use `st.navigation` to configure the available pages in a multipage app.

```python
st.navigation({
    "Your account": [log_out, settings],
    "Reports": [overview, usage],
    "Tools": [search]
})
```

### Execution Flow

You can use `st.dialog` to insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

### Caching and State

You can use `st.cache_data` to cache functions that return data.

```python
@st.cache_data
def long_function(param1, param2):
    # Perform expensive computation here or
    # fetch data from the web here
    return data
```

### Connections and Databases

You can use `st.connection` to connect to a data source or API.

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

### Custom Components

You can use `st.components.v1.declare_component` to create and register a custom component.

```python
from st.components.v1 import declare_component
declare_component("custom_slider", "/frontend")
```

### Configuration

You can use `st.get_option` to retrieve a single configuration option.

```python
st.get_option("theme.primaryColor")
```

## Developer Tools

### App Testing

You can use `st.testing.v1.AppTest` to simulate a running Streamlit app for testing.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.run()
```

Note: This is not a complete conversion, as the original text had many images and links that are not included in this rewritten version. Additionally, some sections were not converted as they seemed to be duplicates or not relevant to the main content.