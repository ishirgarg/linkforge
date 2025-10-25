Below is the provided text rewritten in clean markdown:

# API Reference - Streamlit Docs
Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

## Display almost anything
### Write and magic
Write arguments to the app.

* `st.write("Hello **world**!")`
* `st.write(my_data_frame)`
* `st.write(my_mpl_figure)`

### Text elements
Display string formatted as Markdown.

* `st.markdown("Hello **world**!")`
* `st.title("The app title")`
* `st.header("This is a header")`
* `st.subheader("This is a subheader")`
* `st.badge("New")`
* `st.caption("This is written small caption text")`
* `st.code("a = 1234")`
* `st.echo()` 
* `st.latex("\int a x^2 \,dx")"`
* `st.text("Hello world")`
* `st.divider()`
* `st.help(st.write)`
* `st.html("<p>Foo bar.</p>")"`

## Data elements
### Dataframes
Display a dataframe as an interactive table.

* `st.dataframe(my_data_frame)`
* `st.data_editor(df, num_rows="dynamic")`
* `st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")`
* `st.table(my_data_frame)`
* `st.metric("My metric", 42, 2)`
* `st.json(my_dict)`

## Chart elements
### Simple area charts
Display an area chart.

* `st.area_chart(my_data_frame)`
* `st.bar_chart(my_data_frame)`
* `st.line_chart(my_data_frame)`
* `st.scatter_chart(my_data_frame)`
* `st.map(my_data_frame)`
* `st.pyplot(my_mpl_figure)`
* `st.altair_chart(my_altair_chart)`
* `st.vega_lite_chart(my_vega_lite_chart)`
* `st.plotly_chart(my_plotly_chart)`
* `st.bokeh_chart(my_bokeh_chart)`
* `st.pydeck_chart(my_pydeck_chart)`
* `st.graphviz_chart(my_graphviz_spec)`

## Input widgets
### Button
Display a button widget.

* `st.button("Click me")`
* `st.download_button("Download file", file)`
* `st.form_submit_button("Sign up")`
* `st.link_button("Go to gallery", url)`
* `st.page_link("app.py", label="Home", icon="")`
* `st.checkbox("I agree")`
* `st.color_picker("Pick a color")`
* `st.feedback("stars")`
* `st.multiselect("Buy", ["milk", "apples", "potatoes"])`
* `st.pills("Tags", ["Sports", "AI", "Politics"])`
* `st.radio("Pick one", ["cats", "dogs"])`
* `st.segmented_control("Filter", ["Open", "Closed", "All"])`
* `st.selectbox("Pick one", ["cats", "dogs"])`
* `st.select_slider("Pick a size", ["S", "M", "L"])`
* `st.toggle("Activate")`
* `st.number_input("Pick a number", 0, 10)`
* `st.slider("Pick a number", 0, 100)`
* `st.date_input("Your birthday")`
* `st.time_input("Meeting time")`
* `st.chat_input("Say something")`
* `st.text_area("Text to translate")`
* `st.text_input("First name")`
* `st.audio_input("Record a voice message")`
* `st.file_uploader("Upload a CSV")`
* `st.camera_input("Take a picture")`

## Media elements
### Image
Display an image or list of images.

* `st.image(numpy_array)`
* `st.logo("logo.jpg")`
* `st.pdf("my_document.pdf")`
* `st.audio(numpy_array)`
* `st.video(numpy_array)`

## Layouts and containers
### Columns
Insert containers laid out as side-by-side columns.

* `col1, col2 = st.columns(2)`
* `st.container()`
* `st.dialog("Sign up")`
* `st.empty()`
* `st.expander("Open to see more")`
* `st.popover("Settings")`
* `st.sidebar.write("This lives in the sidebar")`
* `st.tabs(["Tab 1", "Tab2"])`

## Chat elements
### Chat input
Display a chat input widget.

* `prompt = st.chat_input("Say something")`
* `st.chat_message("user")`

## Status elements
### Progress bar
Display a progress bar.

* `st.progress(i)`
* `st.spinner("Please wait...")`
* `st.status('Running')`
* `st.toast('Butter!', icon='')`
* `st.balloons()`
* `st.snow()`
* `st.success("Match found!")`
* `st.info("Dataset is updated every day at midnight.")`
* `st.warning("Unable to fetch image. Skipping...")`
* `st.error("We encountered an error")`
* `st.exception(e)`

## App logic and configuration
### Authentication and user info
#### Log in a user
Start an authentication flow with an identity provider.

* `st.login()`

#### Log out a user
Remove a user's identity information.

* `st.logout()`

#### User info
Return information about a logged-in user.

* `st.user`

### Navigation and pages
#### Navigation
Configure the available pages in a multipage app.

* `st.navigation({"Your account" : [log_out, settings], "Reports" : [overview, usage], "Tools" : [search] })`

#### Page
Define a page in a multipage app.

* `home = st.Page("home.py", title="Home", icon="")`

#### Page link
Display a link to another page in a multipage app.

* `st.page_link("app.py", label="Home", icon="")`

### Execution flow
#### Modal dialog
Insert a modal dialog that can rerun independently from the rest of the script.

* `@st.dialog("Sign up")`

#### Forms
Create a form that batches elements together with a “Submit" button.

* `with st.form(key='my_form'):`

#### Fragments
Define a fragment to rerun independently from the rest of the script.

* `@st.fragment(run_every="10s")`

#### Rerun script
Rerun the script immediately.

* `st.rerun()`

#### Stop execution
Stops execution immediately.

* `st.stop()`

### Caching and state
#### Cache data
Function decorator to cache functions that return data.

* `@st.cache_data`

#### Cache resource
Function decorator to cache functions that return global resources.

* `@st.cache_resource`

#### Session state
Session state is a way to share variables between reruns, for each user session.

* `st.session_state['key'] = value`

#### Query parameters
Get, set, or clear the query parameters that are shown in the browser's URL bar.

* `st.query_params[key] = value`

### Custom components
#### Declare a component
Create and register a custom component.

* `from st.components.v1 import declare_component`

### Configuration
#### Configuration file
Configures the default settings for your app.

* `your-project/ ├── .streamlit/ │ └── config.toml └── your_app.py`

#### Get config option
Retrieve a single configuration option.

* `st.get_option("theme.primaryColor")`

#### Set config option
Set a single configuration option.

* `st.set_option("deprecation.showPyplotGlobalUse", False)`

#### Set page title, favicon, and more
Configures the default settings of the page.

* `st.set_page_config(page_title="My app", page_icon="")`

## Developer tools
### App testing
#### st.testing.v1.AppTest
Simulates a running Streamlit app for testing.

* `from streamlit.testing.v1 import AppTest`