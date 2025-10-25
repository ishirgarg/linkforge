Below is the converted text from HTML to clean markdown.

API Reference - Streamlit Docs
================================

## Table of Contents

*   [Introduction](#introduction)
*   [Display Almost Anything](#display-almost-anything)
*   [Text Elements](#text-elements)
*   [Data Elements](#data-elements)
*   [Chart Elements](#chart-elements)
*   [Input Widgets](#input-widgets)
*   [Media Elements](#media-elements)
*   [Layouts and Containers](#layouts-and-containers)
*   [Chat Elements](#chat-elements)
*   [Status Elements](#status-elements)
*   [App Logic and Configuration](#app-logic-and-configuration)
*   [Developer Tools](#developer-tools)

## Introduction
Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

## Display Almost Anything
### Write and Magic

*   `st.write`: Write arguments to the app.
    ```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```
*   `st.write_stream`: Write generators or streams to the app with a typewriter effect.
    ```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```
*   Magic: Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`
    ```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

## Text Elements
### Markdown
Display string formatted as Markdown.
```python
st.markdown("Hello **world**!")
```
### Title
Display text in title formatting.
```python
st.title("The app title")
```
### Header
Display text in header formatting.
```python
st.header("This is a header")
```
### Subheader
Display text in subheader formatting.
```python
st.subheader("This is a subheader")
```
### Badge
Display a small, colored badge.
```python
st.badge("New")
```
### Caption
Display text in small font.
```python
st.caption("This is written small caption text")
```
### Code Block
Display a code block with optional syntax highlighting.
```python
st.code("a = 1234")
```
### Echo
Display some code in the app, then execute it. Useful for tutorials.
```python
with st.echo():
    st.write('This code will be printed')
```
### LaTeX
Display mathematical expressions formatted as LaTeX.
```python
st.latex("\int a x^2 \,dx")
```
### Preformatted Text
Write fixed-width and preformatted text.
```python
st.text("Hello world")
```
### Divider
Display a horizontal rule.
```python
st.divider()
```
### Get Help
Display object’s doc string, nicely formatted.
```python
st.help(st.write)
st.help(pd.DataFrame)
```
### Render HTML
Renders HTML strings to your app.
```python
st.html("<p>Foo bar.</p>")
```

## Data Elements
### Dataframes
Display a dataframe as an interactive table.
```python
st.dataframe(my_data_frame)
```
### Data Editor
Display a data editor widget.
```python
edited = st.data_editor(df, num_rows="dynamic")
```
### Column Configuration
Configure the display and editing behavior of dataframes and data editors.
```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```
### Static Tables
Display a static table.
```python
st.table(my_data_frame)
```
### Metrics
Display a metric in big bold font, with an optional indicator of how the metric changed.
```python
st.metric("My metric", 42, 2)
```
### Dicts and JSON
Display object or string as a pretty-printed JSON string.
```python
st.json(my_dict)
```

## Chart Elements
### Simple Area Charts
Display an area chart.
```python
st.area_chart(my_data_frame)
```
### Simple Bar Charts
Display a bar chart.
```python
st.bar_chart(my_data_frame)
```
### Simple Line Charts
Display a line chart.
```python
st.line_chart(my_data_frame)
```
### Simple Scatter Charts
Display a line chart.
```python
st.scatter_chart(my_data_frame)
```
### Scatterplots on Maps
Display a map with points on it.
```python
st.map(my_data_frame)
```
### Matplotlib
Display a matplotlib.pyplot figure.
```python
st.pyplot(my_mpl_figure)
```
### Altair
Display a chart using the Altair library.
```python
st.altair_chart(my_altair_chart)
```
### Vega-Lite
Display a chart using the Vega-Lite library.
```python
st.vega_lite_chart(my_vega_lite_chart)
```
### Plotly
Display an interactive Plotly chart.
```python
st.plotly_chart(my_plotly_chart)
```
### Bokeh
Display an interactive Bokeh chart.
```python
st.bokeh_chart(my_bokeh_chart)
```
### PyDeck
Display a chart using the PyDeck library.
```python
st.pydeck_chart(my_pydeck_chart)
```
### GraphViz
Display a graph using the dagre-d3 library.
```python
st.graphviz_chart(my_graphviz_spec)
```

## Input Widgets
### Button
Display a button widget.
```python
clicked = st.button("Click me")
```
### Download Button
Display a download button widget.
```python
st.download_button("Download file", file)
```
### Form Button
Display a form submit button. For use with `st.form`.
```python
st.form_submit_button("Sign up")
```
### Link Button
Display a link button.
```python
st.link_button("Go to gallery", url)
```
### Page Link
Display a link to another page in a multipage app.
```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```
### Checkbox
Display a checkbox widget.
```python
selected = st.checkbox("I agree")
```
### Color Picker
Display a color picker widget.
```python
color = st.color_picker("Pick a color")
```
### Feedback
Display a rating or sentiment button group.
```python
st.feedback("stars")
```
### Multiselect
Display a multiselect widget. The multiselect widget starts as empty.
```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```
### Pills
Display a pill-button selection widget.
```python
st.pills("Tags", ["Sports", "AI", "Politics"])
```
### Radio
Display a radio button widget.
```python
choice = st.radio("Pick one", ["cats", "dogs"])
```
### Segmented Control
Display a segmented-button selection widget.
```python
st.segmented_control("Filter", ["Open", "Closed", "All"])
```
### Selectbox
Display a select widget.
```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```
### Select Slider
Display a slider widget to select items from a list.
```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```
### Toggle
Display a toggle widget.
```python
activated = st.toggle("Activate")
```
### Number Input
Display a numeric input widget.
```python
choice = st.number_input("Pick a number", 0, 10)
```
### Slider
Display a slider widget.
```python
number = st.slider("Pick a number", 0, 100)
```
### Date Input
Display a date input widget.
```python
date = st.date_input("Your birthday")
```
### Time Input
Display a time input widget.
```python
time = st.time_input("Meeting time")
```
### Chat Input
Display a chat input widget.
```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```
### Text Area
Display a multi-line text input widget.
```python
text = st.text_area("Text to translate")
```
### Text Input
Display a single-line text input widget.
```python
name = st.text_input("First name")
```
### Audio Input
Display a widget that allows users to record with their microphone.
```python
speech = st.audio_input("Record a voice message")
```
### Data Editor
Display a data editor widget.
```python
edited = st.data_editor(df, num_rows="dynamic")
```
### File Uploader
Display a file uploader widget.
```python
data = st.file_uploader("Upload a CSV")
```
### Camera Input
Display a widget that allows users to upload images directly from a camera.
```python
image = st.camera_input("Take a picture")
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
### Logo
Display a logo in the upper-left corner of your app and its sidebar.
```python
st.logo("logo.jpg")
```
### PDF
Display a PDF file.
```python
st.pdf("my_document.pdf")
```
### Audio
Display an audio player.
```python
st.audio(numpy_array)
st.audio(audio_bytes)
st.audio(file)
st.audio("https://example.com/myaudio.mp3", format="audio/mp3")
```
### Video
Display a video player.
```python
st.video(numpy_array)
st.video(video_bytes)
st.video(file)
st.video("https://example.com/myvideo.mp4", format="video/mp4")
```

## Layouts and Containers
### Columns
Insert containers laid out as side-by-side columns.
```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```
### Container
Insert a multi-element container.
```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```
### Modal Dialog
Insert a modal dialog that can rerun independently from the rest of the script.
```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```
### Empty
Insert a single-element container.
```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```
### Expander
Insert a multi-element container that can be expanded/collapsed.
```python
with st.expander("Open to see more"):
    st.write("This is more content")
```
### Popover
Insert a multi-element popover container that can be opened/closed.
```python
with st.popover("Settings"):
    st.checkbox("Show completed")
```
### Sidebar
Display items in a sidebar.
```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```
### Tabs
Insert containers separated into tabs.
```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

## Chat Elements
Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

### Chat Input
Display a chat input widget.
```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```
### Chat Message
Insert a chat message container.
```python
import numpy as np
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

## Status Elements
### Progress Bar
Display a progress bar.
```python
for i in range(101):
    st.progress(i)
    do_something_slow()
```
### Spinner
Temporarily displays a message while executing a block of code.
```python
with st.spinner("Please wait..."):
    do_something_slow()
```
### Status Container
Display output of long-running tasks in a container.
```python
with st.status('Running'):
    do_something_slow()
```
### Toast
Briefly displays a toast message in the bottom-right corner.
```python
st.toast('Butter!', icon='🧈')
```
### Balloons
Display celebratory balloons!
```python
do_something()  # Celebrate when all done!
st.balloons()
```
### Snowflakes
Display celebratory snowflakes!
```python
do_something()  # Celebrate when all done!
st.snow()
```
### Success Box
Display a success message.
```python
st.success("Match found!")
```
### Info Box
Display an informational message.
```python
st.info("Dataset is updated every day at midnight.")
```
### Warning Box
Display warning message.
```python
st.warning("Unable to fetch image. Skipping...")
```
### Error Box
Display error message.
```python
st.error("We encountered an error")
```
### Exception Output
Display an exception.
```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

## App Logic and Configuration
### Authentication and User Info
#### Log in a User
`st.login()` starts an authentication flow with an identity provider.
```python
st.login()
```
#### Log out a User
`st.logout()` removes a user's identity information.
```python
st.logout()
```
#### User Info
`st.user` returns information about a logged-in user.
```python
if st.user.is_logged_in:
    st.write(f"Welcome back, {st.user.name}!")
```
### Navigation and Pages
#### Navigation
Configure the available pages in a multipage app.
```python
st.navigation({
    "Your account": [log_out, settings],
    "Reports": [overview, usage],
    "Tools": [search]
})
```
#### Page
Define a page in a multipage app.
```python
home = st.Page("home.py", title="Home", icon=":material/home:")
```
#### Page Link
Display a link to another page in a multipage app.
```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```
#### Switch Page
Programmatically navigates to a specified page.
```python
st.switch_page("pages/my_page.py")
```
### Execution Flow
#### Modal Dialog
Insert a modal dialog that can rerun independently from the rest of the script.
```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```
#### Forms
Create a form that batches elements together with a “Submit" button.
```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```
#### Fragments
Define a fragment to rerun independently from the rest of the script.
```python
@st.fragment(run_every="10s")
def fragment():
    df = get_data()
    st.line_chart(df)
```
#### Rerun Script
Rerun the script immediately.
```python
st.rerun()
```
#### Stop Execution
Stops execution immediately.
```python
st.stop()
```
### Caching and State
#### Cache Data
Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).
```python
@st.cache_data
def long_function(param1, param2):
    # Perform expensive computation here or
    # fetch data from the web here
    return data
```
#### Cache Resource
Function decorator to cache functions that return global resources (e.g. database connections, ML models).
```python
@st.cache_resource
def init_model():
    # Return a global resource here
    return pipeline(
        "sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english"
    )
```
#### Session State
Session state is a way to share variables between reruns, for each user session.
```python
st.session_state['key'] = value
```
#### Query Parameters
Get, set, or clear the query parameters that are shown in the browser's URL bar.
```python
st.query_params[key] = value
st.query_params.clear()
```
#### Context
`st.context` provides a read-only interface to access cookies, headers, locale, and other browser-session information.
```python
st.context.cookies
st.context.headers
```
### Connections and Databases
#### Setup Your Connection
Connect to a data source or API
```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```
#### Built-in Connections
##### SnowflakeConnection
A connection to Snowflake.
```python
conn = st.connection('snowflake')
```
##### SQLConnection
A connection to a SQL database using SQLAlchemy.
```python
conn = st.connection('sql')
```
#### Build Your Own Connections
##### Connection Base Class
Build your own connection with `BaseConnection`.
```python
class MyConnection(BaseConnection[myconn.MyConnection]):
    def _connect(self, **kwargs) -> MyConnection:
        return myconn.connect(**self._secrets, **kwargs)

    def query(self, query):
        return self._instance.query(query)
```
#### Secrets Management
##### Secrets Singleton
Access secrets from a local TOML file.
```python
key = st.secrets["OpenAI_key"]
```
##### Secrets File
Save your secrets in a per-project or per-profile TOML file.
```toml
OpenAI_key = "<YOUR_SECRET_KEY>"
```
### Custom Components
#### Declare a Component
Create and register a custom component.
```python
from st.components.v1 import declare_component
declare_component(
    "custom_slider", 
    "/frontend", 
)
```
#### HTML
Display an HTML string in an iframe.
```python
from st.components.v1 import html
html("<p>Foo bar.</p>")
```
#### iframe
Load a remote URL in an iframe.
```python
from st.components.v1 import iframe
iframe("docs.streamlit.io")
```
### Configuration
#### Configuration File
Configures the default settings for your app.
```toml
your-project/
├── .streamlit/
│   └── config.toml
└── your_app.py
```
#### Get Config Option
Retrieve a single configuration option.
```python
st.get_option("theme.primaryColor")
```
#### Set Config Option
Set a single configuration option. (This is very limited.)
```python
st.set_option("deprecation.showPyplotGlobalUse", False)
```
#### Set Page Title, Favicon, and More
Configures the default settings of the page.
```python
st.set_page_config(
    page_title="My app",
    page_icon=":shark:",
)
```
## Developer Tools
### App Testing
#### st.testing.v1.AppTest
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
#### AppTest.from_file
`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.
```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.run()
```
#### AppTest.from_string
`st.testing.v1.AppTest.from_string` initializes a simulated app from a string.
```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_string(app_script_as_string)
at.run()
```
#### AppTest.from_function
`st.testing.v1.AppTest.from_function` initializes a simulated app from a function.
```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_function(app_script_as_callable)
at.run()
```
#### Block
A representation of container elements, including:
*   `st.chat_message`
*   `st.columns`
*   `st.sidebar`
*   `st.tabs`
*   The main body of the app.
```python
# at.sidebar returns a Block
at.sidebar.button[0].click().run()
assert not at.exception
```
#### Element
The base class for representation of all elements, including:
*   `st.title`
*   `st.header`
*   `st.markdown`
*   `st.dataframe`
```python
# at.title returns a sequence of Title
# Title inherits from Element
assert at.title[0].value == "My awesome app"
```