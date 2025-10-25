Here is the provided HTML content converted to clean markdown:
### API Reference - Streamlit Docs
#### Documentation
* [Get started](/get-started)
  * [Installation](/get-started/installation)
  * [Fundamentals](/get-started/fundamentals)
  * [First steps](/get-started/tutorials)
* [Develop](/develop)
  * [Concepts](/develop/concepts)
  * [API reference](/develop/api-reference)
* [Deploy](/deploy)
  * [Concepts](/deploy/concepts)
  * [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
  * [Snowflake](/deploy/snowflake)
  * [Other platforms](/deploy/tutorials)
* [Knowledge base](/knowledge-base)
  * [FAQ](/knowledge-base/using-streamlit)
  * [Installing dependencies](/knowledge-base/dependencies)
  * [Deployment issues](/knowledge-base/deploy)

### API Reference
Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

### Display almost anything
#### Write and magic
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

### Text elements
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
#### Badge
Display a small, colored badge.
```python
st.badge("New")
```
#### Caption
Display text in small font.
```python
st.caption("This is written small caption text")
```
#### Code block
Display a code block with optional syntax highlighting.
```python
st.code("a = 1234")
```
#### Echo
Display some code in the app, then execute it. Useful for tutorials.
```python
with st.echo():
  st.write('This code will be printed')
```
#### LaTeX
Display mathematical expressions formatted as LaTeX.
```python
st.latex("\int a x^2 \,dx")
```
#### Preformatted text
Write fixed-width and preformatted text.
```python
st.text("Hello world")
```
#### Divider
Display a horizontal rule.
```python
st.divider()
```
#### Get help
Display object’s doc string, nicely formatted.
```python
st.help(st.write)
st.help(pd.DataFrame)
```
#### Render HTML
Renders HTML strings to your app.
```python
st.html("<p>Foo bar.</p>")
```

### Third-party components
These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

### Data elements
#### Dataframes
Display a dataframe as an interactive table.
```python
st.dataframe(my_data_frame)
```
#### Data editor
Display a data editor widget.
```python
edited = st.data_editor(df, num_rows="dynamic")
```
#### Column configuration
Configure the display and editing behavior of dataframes and data editors.
```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```
#### Static tables
Display a static table.
```python
st.table(my_data_frame)
```
#### Metrics
Display a metric in big bold font, with an optional indicator of how the metric changed.
```python
st.metric("My metric", 42, 2)
```
#### Dicts and JSON
Display object or string as a pretty-printed JSON string.
```python
st.json(my_dict)
```

### Chart elements
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
#### Simple line charts
Display a line chart.
```python
st.line_chart(my_data_frame)
```
#### Simple scatter charts
Display a line chart.
```python
st.scatter_chart(my_data_frame)
```
#### Scatterplots on maps
Display a map with points on it.
```python
st.map(my_data_frame)
```
#### Matplotlib
Display a matplotlib.pyplot figure.
```python
st.pyplot(my_mpl_figure)
```
#### Altair
Display a chart using the Altair library.
```python
st.altair_chart(my_altair_chart)
```
#### Vega-Lite
Display a chart using the Vega-Lite library.
```python
st.vega_lite_chart(my_vega_lite_chart)
```
#### Plotly
Display an interactive Plotly chart.
```python
st.plotly_chart(my_plotly_chart)
```
#### Bokeh
Display an interactive Bokeh chart.
```python
st.bokeh_chart(my_bokeh_chart)
```
#### PyDeck
Display a chart using the PyDeck library.
```python
st.pydeck_chart(my_pydeck_chart)
```
#### GraphViz
Display a graph using the dagre-d3 library.
```python
st.graphviz_chart(my_graphviz_spec)
```

### Input widgets
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
#### Form button
Display a form submit button. For use with `st.form`.
```python
st.form_submit_button("Sign up")
```
#### Link button
Display a link button.
```python
st.link_button("Go to gallery", url)
```
#### Page link
Display a link to another page in a multipage app.
```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
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
#### Logo
Display a logo in the upper-left corner of your app and its sidebar.
```python
st.logo("logo.jpg")
```
#### PDF
Display a PDF file.
```python
st.pdf("my_document.pdf")
```
#### Audio
Display an audio player.
```python
st.audio(numpy_array)
st.audio(audio_bytes)
st.audio(file)
st.audio("https://example.com/myaudio.mp3", format="audio/mp3")
```
#### Video
Display a video player.
```python
st.video(numpy_array)
st.video(video_bytes)
st.video(file)
st.video("https://example.com/myvideo.mp4", format="video/mp4")
```

### Layouts and containers
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
#### Modal dialog
Insert a modal dialog that can rerun independently from the rest of the script.
```python
@st.dialog("Sign up")
def email_form():
  name = st.text_input("Name")
  email = st.text_input("Email")
```

### Chat elements
Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

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
```python
st.login()
st.logout()
if st.user.is_logged_in:
  st.write(f"Welcome back, {st.user.name}!")
```

### Developer tools
#### App testing
```python
from streamlit.testing.v1 import AppTest
at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception
at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."
```