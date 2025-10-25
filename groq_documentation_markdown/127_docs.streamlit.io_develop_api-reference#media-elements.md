Below is the provided HTML content converted to Markdown:

# API Reference - Streamlit Docs
[![Logo](/logo.svg)](/)

## Navigation Menu
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
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

## API Reference
Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

### Display Almost Anything
#### Write and Magic
Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

#### Magic
Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

#### Text Elements
Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

### Text Elements
Display a title.

```python
st.title("The app title")
```

Display a header.

```python
st.header("This is a header")
```

Display a subheader.

```python
st.subheader("This is a subheader")
```

Display a badge.

```python
st.badge("New")
```

Display text in small font.

```python
st.caption("This is written small caption text")
```

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```

Display some code in the app, then execute it.

```python
with st.echo():
    st.write('This code will be printed')
```

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\int a x^2 \,dx")
```

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```

Display a horizontal rule.

```python
st.divider()
```

Display object’s doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

Renders HTML strings to your app.

```python
st.html("<p>Foo bar.</p>")
```

### Data Elements
Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

Display a static table.

```python
st.table(my_data_frame)
```

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```

### Chart Elements
Display an area chart.

```python
st.area_chart(my_data_frame)
```

Display a bar chart.

```python
st.bar_chart(my_data_frame)
```

Display a line chart.

```python
st.line_chart(my_data_frame)
```

Display a scatter chart.

```python
st.scatter_chart(my_data_frame)
```

Display a map with points on it.

```python
st.map(my_data_frame)
```

Display a matplotlib.pyplot figure.

```python
st.pyplot(my_mpl_figure)
```

Display a chart using the Altair library.

```python
st.altair_chart(my_altair_chart)
```

Display a chart using the Vega-Lite library.

```python
st.vega_lite_chart(my_vega_lite_chart)
```

Display an interactive Plotly chart.

```python
st.plotly_chart(my_plotly_chart)
```

Display an interactive Bokeh chart.

```python
st.bokeh_chart(my_bokeh_chart)
```

Display a chart using the PyDeck library.

```python
st.pydeck_chart(my_pydeck_chart)
```

Display a graph using the dagre-d3 library.

```python
st.graphviz_chart(my_graphviz_spec)
```

### Input Widgets
Display a button widget.

```python
clicked = st.button("Click me")
```

Display a download button widget.

```python
st.download_button("Download file", file)
```

Display a form submit button.

```python
st.form_submit_button("Sign up")
```

Display a link button.

```python
st.link_button("Go to gallery", url)
```

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
```

Display a checkbox widget.

```python
selected = st.checkbox("I agree")
```

Display a color picker widget.

```python
color = st.color_picker("Pick a color")
```

Display a rating or sentiment button group.

```python
st.feedback("stars")
```

### Media Elements
Display an image or list of images.

```python
st.image(numpy_array)
```

Display a logo in the upper-left corner of your app and its sidebar.

```python
st.logo("logo.jpg")
```

Display a PDF file.

```python
st.pdf("my_document.pdf")
```

Display an audio player.

```python
st.audio(numpy_array)
```

Display a video player.

```python
st.video(numpy_array)
```

### Layouts and Containers
Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
```

Insert a multi-element container.

```python
c = st.container()
```

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

Insert a single-element container.

```python
c = st.empty()
```

Insert a multi-element container that can be expanded/collapsed.

```python
with st.expander("Open to see more"):
    st.write("This is more content")
```

Insert a multi-element popover container that can be opened/closed.

```python
with st.popover("Settings"):
    st.checkbox("Show completed")
```

Display items in a sidebar.

```python
st.sidebar.write("This lives in the sidebar")
```

Insert containers separated into tabs.

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
```

### Chat Elements
Display a chat input widget.

```python
prompt = st.chat_input("Say something")
```

Insert a chat message container.

```python
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

### Status Elements
Display a progress bar.

```python
for i in range(101):
    st.progress(i)
    do_something_slow()
```

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
    do_something_slow()
```

Display output of long-running tasks in a container.

```python
with st.status('Running'):
    do_something_slow()
```

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='🧈')
```

Display celebratory balloons!

```python
st.balloons()
```

Display celebratory snowflakes!

```python
st.snow()
```

Display a success message.

```python
st.success("Match found!")
```

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

Display error message.

```python
st.error("We encountered an error")
```

Display an exception.

```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

### App Logic and Configuration
#### Authentication and User Info
Log in a user.

```python
st.login()
```

Log out a user.

```python
st.logout()
```

User info.

```python
st.user
```

#### Navigation and Pages
Configure the available pages in a multipage app.

```python
st.navigation({
    "Your account": [log_out, settings],
    "Reports": [overview, usage],
    "Tools": [search]
})
```

Define a page in a multipage app.

```python
home = st.Page("home.py", title="Home", icon=":material/home:")
```

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
```

Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```

#### Execution Flow
Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

Create a form that batches elements together with a “Submit" button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

Define a fragment to rerun independently from the rest of the script.

```python
@st.fragment(run_every="10s")
def fragment():
    df = get_data()
    st.line_chart(df)
```

Rerun the script immediately.

```python
st.rerun()
```

Stops execution immediately.

```python
st.stop()
```

#### Caching and State
Function decorator to cache functions that return data.

```python
@st.cache_data
def long_function(param1, param2):
    # Perform expensive computation here or
    # fetch data from the web here
    return data
```

Function decorator to cache functions that return global resources.

```python
@st.cache_resource
def init_model():
    # Return a global resource here
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
```

Session state is a way to share variables between reruns, for each user session.

```python
st.session_state['key'] = value
```

Get, set, or clear the query parameters that are shown in the browser's URL bar.

```python
st.query_params[key] = value
st.query_params.clear()
```

`st.context` provides a read-only interface to access cookies, headers, locale, and other browser-session information.

```python
st.context.cookies
st.context.headers
```

#### Connections and Databases
Connect to a data source or API.

```python
conn = st.connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)
```

#### Custom Components
Create and register a custom component.

```python
from st.components.v1 import declare_component
declare_component("custom_slider", "/frontend")
```

Display an HTML string in an iframe.

```python
from st.components.v1 import html
html("<p>Foo bar.</p>")
```

Load a remote URL in an iframe.

```python
from st.components.v1 import iframe
iframe("docs.streamlit.io")
```

### Developer Tools
#### App Testing
`st.testing.v1.AppTest` simulates a running Streamlit app for testing.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
```

`st.testing.v1.AppTest.from_file` initializes a simulated app from a file.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.run()
```

`st.testing.v1.AppTest.from_string` initializes a simulated app from a string.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_string(app_script_as_string)
at.run()
```

`st.testing.v1.AppTest.from_function` initializes a simulated app from a function.

```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_function(app_script_as_callable)
at.run()
```

A representation of container elements.

```python
# at.sidebar returns a Block
at.sidebar.button[0].click().run()
```

The base class for representation of all elements.

```python
# at.title returns a sequence of Title
# Title inherits from Element
assert at.title[0].value == "My awesome app"
```

A representation of `st.button` and `st.form_submit_button`.

```python
at.button[0].click().run()
```

A representation of `st.chat_input`.

```python
at.chat_input[0].set_value("What is Streamlit?").run()
```