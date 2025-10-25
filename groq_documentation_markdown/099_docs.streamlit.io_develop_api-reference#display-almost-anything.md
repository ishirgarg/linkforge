Below is the cleaned-up version of the provided API reference documentation in Markdown:

API Reference - Streamlit Docs
==========================

### Table of Contents

*   [Display Almost Anything](#display-almost-anything)
    *   [Write and Magic](#write-and-magic)
    *   [Text Elements](#text-elements)
*   [Data Elements](#data-elements)
*   [Chart Elements](#chart-elements)
*   [Input Widgets](#input-widgets)
*   [Media Elements](#media-elements)
*   [Layouts and Containers](#layouts-and-containers)
*   [Chat Elements](#chat-elements)
*   [Status Elements](#status-elements)
*   [App Logic and Configuration](#app-logic-and-configuration)
    *   [Authentication and User Info](#authentication-and-user-info)
    *   [Navigation and Pages](#navigation-and-pages)
    *   [Execution Flow](#execution-flow)
    *   [Caching and State](#caching-and-state)
    *   [Connections and Secrets](#connections-and-secrets)
    *   [Custom Components](#custom-components)
    *   [Configuration](#configuration)
*   [Developer Tools](#developer-tools)
    *   [App Testing](#app-testing)

### Display Almost Anything
#### Write and Magic

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

#### Text Elements

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
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

#### Number Input

Display a numeric input widget.

```python
choice = st.number_input("Pick a number", 0, 10)
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

### App Logic and Configuration

#### Authentication and User Info

```python
st.login()
st.logout()
st.user
```

#### Navigation and Pages

```python
st.navigation({"Your account": [log_out, settings], "Reports": [overview, usage], "Tools": [search]})
st.page("home.py", title="Home", icon=":material/home:")
st.page_link("app.py", label="Home", icon="🏠")
st.switch_page("pages/my_page.py")
```

#### Execution Flow

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

#### Caching and State

```python
@st.cache_data
def long_function(param1, param2):
    # Perform expensive computation here
    return data
```

#### Connections and Secrets

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

### Developer Tools

#### App Testing

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
```

Please note that the provided API reference documentation is extensive and the cleaned-up version only covers a portion of it. You can add more sections and details as needed.