The provided text is an HTML document containing API reference for Streamlit, a Python library for building web applications. Here is the cleaned-up version of the text in markdown format:

API Reference
==========

Streamlit Docs
--------------

### Documentation

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

API Reference
-------------

### Display almost anything

* [Write and magic](#write-and-magic)
	+ `st.write()`: Write arguments to the app.
	+ `st.write_stream()`: Write generators or streams to the app with a typewriter effect.
	+ [Magic](#magic): Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`.
* [Text elements](#text-elements)
	+ `st.markdown()`: Display string formatted as Markdown.
	+ `st.title()`: Display text in title formatting.
	+ `st.header()`: Display text in header formatting.
	+ `st.subheader()`: Display text in subheader formatting.
	+ `st.badge()`: Display a small, colored badge.
	+ `st.caption()`: Display text in small font.
	+ `st.code()`: Display a code block with optional syntax highlighting.
	+ `st.echo()`: Display some code in the app, then execute it.
	+ `st.latex()`: Display mathematical expressions formatted as LaTeX.
	+ `st.text()`: Write fixed-width and preformatted text.
	+ `st.divider()`: Display a horizontal rule.
	+ `st.help()`: Display object’s doc string, nicely formatted.
	+ `st.html()`: Renders HTML strings to your app.

### Data elements

* [Dataframes](#dataframes): Display a dataframe as an interactive table.
* [Data editor](#data-editor): Display a data editor widget.
* [Column configuration](#column-configuration): Configure the display and editing behavior of dataframes and data editors.
* [Static tables](#static-tables): Display a static table.
* [Metrics](#metrics): Display a metric in big bold font, with an optional indicator of how the metric changed.
* [Dicts and JSON](#dicts-and-json): Display object or string as a pretty-printed JSON string.

### Chart elements

* [Simple area charts](#simple-area-charts): Display an area chart.
* [Simple bar charts](#simple-bar-charts): Display a bar chart.
* [Simple line charts](#simple-line-charts): Display a line chart.
* [Simple scatter charts](#simple-scatter-charts): Display a line chart.
* [Scatterplots on maps](#scatterplots-on-maps): Display a map with points on it.
* [Matplotlib](#matplotlib): Display a matplotlib.pyplot figure.
* [Altair](#altair): Display a chart using the Altair library.
* [Vega-Lite](#vega-lite): Display a chart using the Vega-Lite library.
* [Plotly](#plotly): Display an interactive Plotly chart.
* [Bokeh](#bokeh): Display an interactive Bokeh chart.
* [PyDeck](#pydeck): Display a chart using the PyDeck library.
* [GraphViz](#graphviz): Display a graph using the dagre-d3 library.

### Input widgets

* [Button](#button): Display a button widget.
* [Download button](#download-button): Display a download button widget.
* [Form button](#form-button): Display a form submit button.
* [Link button](#link-button): Display a link button.
* [Page link](#page-link): Display a link to another page in a multipage app.
* [Checkbox](#checkbox): Display a checkbox widget.
* [Color picker](#color-picker): Display a color picker widget.
* [Feedback](#feedback): Display a rating or sentiment button group.
* [Multiselect](#multiselect): Display a multiselect widget.
* [Pills](#pills): Display a pill-button selection widget.
* [Radio](#radio): Display a radio button widget.
* [Segmented control](#segmented-control): Display a segmented-button selection widget.
* [Selectbox](#selectbox): Display a select widget.
* [Select-slider](#select-slider): Display a slider widget to select items from a list.
* [Toggle](#toggle): Display a toggle widget.
* [Number input](#number-input): Display a numeric input widget.
* [Slider](#slider): Display a slider widget.
* [Date input](#date-input): Display a date input widget.
* [Time input](#time-input): Display a time input widget.
* [Chat input](#chat-input): Display a chat input widget.
* [Text-area](#text-area): Display a multi-line text input widget.
* [Text input](#text-input): Display a single-line text input widget.
* [Audio input](#audio-input): Display a widget that allows users to record with their microphone.
* [File uploader](#file-uploader): Display a file uploader widget.
* [Camera input](#camera-input): Display a widget that allows users to upload images directly from a camera.

### Media elements

* [Image](#image): Display an image or list of images.
* [Logo](#logo): Display a logo in the upper-left corner of your app and its sidebar.
* [PDF](#pdf): Display a PDF file.
* [Audio](#audio): Display an audio player.
* [Video](#video): Display a video player.

### Layouts and containers

* [Columns](#columns): Insert containers laid out as side-by-side columns.
* [Container](#container): Insert a multi-element container.
* [Modal dialog](#modal-dialog): Insert a modal dialog that can rerun independently from the rest of the script.
* [Empty](#empty): Insert a single-element container.
* [Expander](#expander): Insert a multi-element container that can be expanded/collapsed.
* [Popover](#popover): Insert a multi-element popover container that can be opened/closed.
* [Sidebar](#sidebar): Display items in a sidebar.
* [Tabs](#tabs): Insert containers separated into tabs.

### Chat elements

* [Chat input](#chat-input): Display a chat input widget.
* [Chat message](#chat-message): Insert a chat message container.

### Status elements

* [Progress bar](#progress-bar): Display a progress bar.
* [Spinner](#spinner): Temporarily displays a message while executing a block of code.
* [Status container](#status-container): Display output of long-running tasks in a container.
* [Toast](#toast): Briefly displays a toast message in the bottom-right corner.
* [Balloons](#balloons): Display celebratory balloons!
* [Snowflakes](#snowflakes): Display celebratory snowflakes!
* [Success box](#success-box): Display a success message.
* [Info box](#info-box): Display an informational message.
* [Warning box](#warning-box): Display warning message.
* [Error box](#error-box): Display error message.
* [Exception output](#exception-output): Display an exception.

### App logic and configuration

* [Authentication and user info](#authentication-and-user-info)
	+ [Log in a user](#log-in-a-user): Start an authentication flow with an identity provider.
	+ [Log out a user](#log-out-a-user): Removes a user's identity information.
	+ [User info](#user-info): Returns information about a logged-in user.
* [Navigation and pages](#navigation-and-pages)
	+ [Navigation](#navigation): Configure the available pages in a multipage app.
	+ [Page](#page): Define a page in a multipage app.
	+ [Page link](#page-link): Display a link to another page in a multipage app.
	+ [Switch page](#switch-page): Programmatically navigates to a specified page.
* [Execution flow](#execution-flow)
	+ [Modal dialog](#modal-dialog): Insert a modal dialog that can rerun independently from the rest of the script.
	+ [Forms](#forms): Create a form that batches elements together with a “Submit" button.
	+ [Fragments](#fragments): Define a fragment to rerun independently from the rest of the script.
	+ [Rerun script](#rerun-script): Rerun the script immediately.
	+ [Stop execution](#stop-execution): Stops execution immediately.
* [Caching and state](#caching-and-state)
	+ [Cache data](#cache-data): Function decorator to cache functions that return data.
	+ [Cache resource](#cache-resource): Function decorator to cache functions that return global resources.
	+ [Session state](#session-state): Session state is a way to share variables between reruns, for each user session.
	+ [Query parameters](#query-parameters): Get, set, or clear the query parameters that are shown in the browser's URL bar.
	+ [Context](#context): Provides a read-only interface to access cookies, headers, locale, and other browser-session information.
* [Connections and databases](#connections-and-databases)
	+ [Setup your connection](#setup-your-connection): Connect to a data source or API.
	+ [Built-in connections](#built-in-connections)
		- [SnowflakeConnection](#snowflakeconnection): A connection to Snowflake.
		- [SQLConnection](#sqlconnection): A connection to a SQL database using SQLAlchemy.
	+ [Build your own connections](#build-your-own-connections)
		- [Connection base class](#connection-base-class): Build your own connection with `BaseConnection`.
		- [Secrets management](#secrets-management): Access secrets from a local TOML file.
* [Custom components](#custom-components)
	+ [Declare a component](#declare-a-component): Create and register a custom component.
	+ [HTML](#html): Display an HTML string in an iframe.
	+ [Iframe](#iframe): Load a remote URL in an iframe.
* [Configuration](#configuration)
	+ [Configuration file](#configuration-file): Configures the default settings for your app.
	+ [Get config option](#get-config-option): Retrieve a single configuration option.
	+ [Set config option](#set-config-option): Set a single configuration option.
	+ [Set page title, favicon, and more](#set-page-title-favicon-and-more): Configures the default settings of the page.

### Developer tools

* [App testing](#app-testing)
	+ [AppTest](#apptest): Simulates a running Streamlit app for testing.
	+ [AppTest.from_file](#apptestfrom_file): Initializes a simulated app from a file.
	+ [AppTest.from_string](#apptestfrom_string): Initializes a simulated app from a string.
	+ [AppTest.from_function](#apptestfrom_function): Initializes a simulated app from a function.
	+ [Block](#block): A representation of container elements.
	+ [Element](#element): The base class for representation of all elements.
	+ [Button](#button): A representation of `st.button` and `st.form_submit_button`.
	+ [ChatInput](#chatinput): A representation of `st.chat_input`.
	+ [Checkbox](#checkbox): A representation of `st.checkbox`.
	+ [ColorPicker](#colorpicker): A representation of `st.color_picker`.
	+ [DateInput](#dateinput): A representation of `st.date_input`.
	+ [Multiselect](#multiselect): A representation of `st.multiselect`.
	+ [NumberInput](#numberinput): A representation of `st.number_input`.
	+ [Radio](#radio): A representation of `st.radio`.
	+ [SelectSlider](#selectslider): A representation of `st.select_slider`.
	+ [Selectbox](#selectbox): A representation of `st.selectbox`.
	+ [Slider](#slider): A representation of `st.slider`.
	+ [TextArea](#textarea): A representation of `st.text_area`.
	+ [TextInput](#textinput): A representation of `st.text_input`.
	+ [TimeInput](#timeinput): A representation of `st.time_input`.
	+ [Toggle](#toggle): A representation of `st.toggle`.