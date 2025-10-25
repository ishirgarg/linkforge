Here is the content rewritten in Markdown format:

# API Reference - Streamlit Docs
Streamlit makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance. Each section includes methods associated with the activity type, including examples.

## Display Almost Anything
### Write and Magic
Write arguments to the app.

* `st.write`: Write arguments to the app.
* `st.write_stream`: Write generators or streams to the app with a typewriter effect.
* `Magic`: Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`.

### Text Elements
Display text in various formats.

* `st.markdown`: Display string formatted as Markdown.
* `st.title`: Display text in title formatting.
* `st.header`: Display text in header formatting.
* `st.subheader`: Display text in subheader formatting.
* `st.badge`: Display a small, colored badge.
* `st.caption`: Display text in small font.
* `st.code`: Display a code block with optional syntax highlighting.
* `st.echo`: Display some code in the app, then execute it. Useful for tutorials.
* `st.latex`: Display mathematical expressions formatted as LaTeX.
* `st.text`: Write fixed-width and preformatted text.
* `st.divider`: Display a horizontal rule.
* `st.help`: Display object’s doc string, nicely formatted.
* `st.html`: Renders HTML strings to your app.

## Data Elements
Display data in various formats.

* `st.dataframe`: Display a dataframe as an interactive table.
* `st.data_editor`: Display a data editor widget.
* `st.column_config`: Configure the display and editing behavior of dataframes and data editors.
* `st.table`: Display a static table.
* `st.metric`: Display a metric in big bold font, with an optional indicator of how the metric changed.
* `st.json`: Display object or string as a pretty-printed JSON string.

## Chart Elements
Display charts and graphs.

* `st.area_chart`: Display an area chart.
* `st.bar_chart`: Display a bar chart.
* `st.line_chart`: Display a line chart.
* `st.scatter_chart`: Display a scatter chart.
* `st.map`: Display a map with points on it.
* `st.pyplot`: Display a matplotlib.pyplot figure.
* `st.altair_chart`: Display a chart using the Altair library.
* `st.vega_lite_chart`: Display a chart using the Vega-Lite library.
* `st.plotly_chart`: Display an interactive Plotly chart.
* `st.bokeh_chart`: Display an interactive Bokeh chart.
* `st.pydeck_chart`: Display a chart using the PyDeck library.
* `st.graphviz_chart`: Display a graph using the dagre-d3 library.

## Input Widgets
Display input widgets.

* `st.button`: Display a button widget.
* `st.download_button`: Display a download button widget.
* `st.form_submit_button`: Display a form submit button.
* `st.link_button`: Display a link button.
* `st.page_link`: Display a link to another page in a multipage app.
* `st.checkbox`: Display a checkbox widget.
* `st.color_picker`: Display a color picker widget.
* `st.feedback`: Display a rating or sentiment button group.
* `st.multiselect`: Display a multiselect widget.
* `st.pills`: Display a pill-button selection widget.
* `st.radio`: Display a radio button widget.
* `st.segmented_control`: Display a segmented-button selection widget.
* `st.selectbox`: Display a select widget.
* `st.select_slider`: Display a slider widget to select items from a list.
* `st.toggle`: Display a toggle widget.
* `st.number_input`: Display a numeric input widget.
* `st.slider`: Display a slider widget.
* `st.date_input`: Display a date input widget.
* `st.time_input`: Display a time input widget.
* `st.chat_input`: Display a chat input widget.
* `st.text_area`: Display a multi-line text input widget.
* `st.text_input`: Display a single-line text input widget.
* `st.audio_input`: Display a widget that allows users to record with their microphone.
* `st.file_uploader`: Display a file uploader widget.
* `st.camera_input`: Display a widget that allows users to upload images directly from a camera.

## Media Elements
Display media.

* `st.image`: Display an image or list of images.
* `st.logo`: Display a logo in the upper-left corner of your app and its sidebar.
* `st.pdf`: Display a PDF file.
* `st.audio`: Display an audio player.
* `st.video`: Display a video player.

## Layouts and Containers
Display layouts and containers.

* `st.columns`: Insert containers laid out as side-by-side columns.
* `st.container`: Insert a multi-element container.
* `st.dialog`: Insert a modal dialog that can rerun independently from the rest of the script.
* `st.empty`: Insert a single-element container.
* `st.expander`: Insert a multi-element container that can be expanded/collapsed.
* `st.popover`: Insert a multi-element popover container that can be opened/closed.
* `st.sidebar`: Display items in a sidebar.
* `st.tabs`: Insert containers separated into tabs.

## Chat Elements
Display chat elements.

* `st.chat_input`: Display a chat input widget.
* `st.chat_message`: Insert a chat message container.

## Status Elements
Display status elements.

* `st.progress`: Display a progress bar.
* `st.spinner`: Temporarily displays a message while executing a block of code.
* `st.status`: Display output of long-running tasks in a container.
* `st.toast`: Briefly displays a toast message in the bottom-right corner.
* `st.balloons`: Display celebratory balloons!
* `st.snow`: Display celebratory snowflakes!
* `st.success`: Display a success message.
* `st.info`: Display an informational message.
* `st.warning`: Display warning message.
* `st.error`: Display error message.
* `st.exception`: Display an exception.

## App Logic and Configuration
Configure app logic and configuration.

* `st.login`: Log in a user.
* `st.logout`: Log out a user.
* `st.user`: Returns information about a logged-in user.
* `st.navigation`: Configure the available pages in a multipage app.
* `st.page`: Define a page in a multipage app.
* `st.page_link`: Display a link to another page in a multipage app.
* `st.switch_page`: Programmatically navigates to a specified page.

## Caching and State
Configure caching and state.

* `st.cache_data`: Function decorator to cache functions that return data.
* `st.cache_resource`: Function decorator to cache functions that return global resources.
* `st.session_state`: Session state is a way to share variables between reruns, for each user session.
* `st.query_params`: Get, set, or clear the query parameters that are shown in the browser's URL bar.
* `st.context`: Provides a read-only interface to access cookies, headers, locale, and other browser-session information.

## Connections and Databases
Configure connections and databases.

* `st.connection`: Connect to a data source or API
* `st.secrets`: Access secrets from a local TOML file.

## Custom Components
Create custom components.

* `st.components.v1.declare_component`: Create and register a custom component.
* `st.components.v1.html`: Display an HTML string in an iframe.
* `st.components.v1.iframe`: Load a remote URL in an iframe.

## Configuration
Configure the app.

* `st.get_option`: Retrieve a single configuration option.
* `st.set_option`: Set a single configuration option.
* `st.set_page_config`: Configures the default settings of the page.

## Developer Tools
Use developer tools.

* `st.testing.v1.AppTest`: Simulates a running Streamlit app for testing.
* `st.testing.v1.AppTest.from_file`: Initializes a simulated app from a file.
* `st.testing.v1.AppTest.from_string`: Initializes a simulated app from a string.
* `st.testing.v1.AppTest.from_function`: Initializes a simulated app from a function.
* `st.testing.v1.Element`: The base class for representation of all elements.
* `st.testing.v1.Block`: A representation of container elements.
* `st.testing.v1.Button`: A representation of `st.button` and `st.form_submit_button`.
* `st.testing.v1.ChatInput`: A representation of `st.chat_input`.
* `st.testing.v1.Checkbox`: A representation of `st.checkbox`.
* `st.testing.v1.ColorPicker`: A representation of `st.color_picker`.
* `st.testing.v1.DateInput`: A representation of `st.date_input`.
* `st.testing.v1.Multiselect`: A representation of `st.multiselect`.
* `st.testing.v1.NumberInput`: A representation of `st.number_input`.
* `st.testing.v1.Radio`: A representation of `st.radio`.
* `st.testing.v1.SelectSlider`: A representation of `st.select_slider`.
* `st.testing.v1.Selectbox`: A representation of `st.selectbox`.
* `st.testing.v1.TextArea`: A representation of `st.text_area`.
* `st.testing.v1.TextInput`: A representation of `st.text_input`.
* `st.testing.v1.TimeInput`: A representation of `st.time_input`.
* `st.testing.v1.Toggle`: A representation of `st.toggle`.