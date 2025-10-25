Here is the converted markdown document:

# API Reference - Streamlit Docs
## Table of Contents
1. [Display almost anything](#display-almost-anything)
2. [Text elements](#text-elements)
3. [Data elements](#data-elements)
4. [Chart elements](#chart-elements)
5. [Input widgets](#input-widgets)
6. [Media elements](#media-elements)
7. [Layouts and containers](#layouts-and-containers)
8. [Chat elements](#chat-elements)
9. [Status elements](#status-elements)
10. [App logic and configuration](#app-logic-and-configuration)
11. [Caching and state](#caching-and-state)
12. [Connections and databases](#connections-and-databases)
13. [Custom components](#custom-components)
14. [Configuration](#configuration)
15. [Developer tools](#developer-tools)

## Display almost anything
### Write and magic
You can use `st.write()` to write arguments to the app.

```python
import streamlit as st

st.write("Hello **world**!")
```

You can also use `st.write()` to write data frames, matplotlib figures, and more.

## Text elements
### Markdown
You can use `st.markdown()` to display string formatted as Markdown.

```python
import streamlit as st

st.markdown("Hello **world**!")
```

You can also use other text elements such as `st.title()`, `st.header()`, `st.subheader()`, `st.caption()`, `st.code()`, and more.

## Data elements
### Dataframes
You can use `st.dataframe()` to display a dataframe as an interactive table.

```python
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
})

st.dataframe(df)
```

You can also use `st.table()` to display a static table, and `st.metric()` to display a metric in big bold font.

## Chart elements
### Simple area charts
You can use `st.area_chart()` to display an area chart.

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
})

st.area_chart(df)
```

You can also use `st.bar_chart()`, `st.line_chart()`, `st.scatter_chart()`, and more to display different types of charts.

## Input widgets
### Button
You can use `st.button()` to display a button widget.

```python
import streamlit as st

if st.button('Click me'):
    st.write('Button clicked!')
```

You can also use `st.checkbox()`, `st.selectbox()`, `st.multiselect()`, `st.slider()`, and more to display different types of input widgets.

## Media elements
### Image
You can use `st.image()` to display an image.

```python
import streamlit as st

st.image('image.jpg')
```

You can also use `st.audio()` to display an audio player, `st.video()` to display a video player, and more.

## Layouts and containers
### Columns
You can use `st.columns()` to insert containers laid out as side-by-side columns.

```python
import streamlit as st

col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')
```

You can also use `st.container()` to insert a multi-element container, `st.sidebar()` to display items in a sidebar, and more.

## Chat elements
### Chat input
You can use `st.chat_input()` to display a chat input widget.

```python
import streamlit as st

prompt = st.chat_input('Say something')
if prompt:
    st.write(f'The user has sent: {prompt}')
```

You can also use `st.chat_message()` to insert a chat message container.

## Status elements
### Progress bar
You can use `st.progress()` to display a progress bar.

```python
import streamlit as st
import time

for i in range(101):
    st.progress(i)
    time.sleep(0.01)
```

You can also use `st.spinner()` to temporarily display a message while executing a block of code, `st.status()` to display output of long-running tasks in a container, and more.

## App logic and configuration
### Authentication and user info
You can use `st.login()` to log in a user, and `st.user` to retrieve information about a logged-in user.

```python
import streamlit as st

if st.login():
    st.write(f'Welcome back, {st.user.name}!')
```

You can also use `st.logout()` to log out a user.

## Caching and state
### Cache data
You can use `@st.cache_data` to cache functions that return data.

```python
import streamlit as st

@st.cache_data
def long_function(param1, param2):
    # Perform expensive computation here or
    # fetch data from the web here
    return data

data = long_function(param1, param2)
st.write(data)
```

You can also use `st.session_state` to share variables between reruns, for each user session.

## Connections and databases
### Create a connection
You can use `st.connection()` to connect to a data source or API.

```python
import streamlit as st

conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

You can also use `st.secrets` to access secrets from a local TOML file.

## Custom components
### Declare a component
You can use `st.components.v1.declare_component` to create and register a custom component.

```python
import streamlit as st
from st.components.v1 import declare_component

declare_component("custom_slider", "/frontend")
```

You can also use `st.components.v1.html` to display an HTML string in an iframe, and `st.components.v1.iframe` to load a remote URL in an iframe.

## Configuration
### Configuration file
You can configure the default settings for your app using a TOML file.

```toml
[theme]
primaryColor = "#00698f"
```

You can also use `st.get_option()` to retrieve a single configuration option, and `st.set_option()` to set a single configuration option.

## Developer tools
### App testing
You can use `st.testing.v1.AppTest` to simulate a running Streamlit app for testing.

```python
import streamlit as st
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py")
at.run()
assert not at.exception
```