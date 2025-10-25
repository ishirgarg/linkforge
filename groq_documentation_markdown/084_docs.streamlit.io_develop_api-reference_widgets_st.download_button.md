Here is the HTML converted to clean Markdown:
### Streamlit Docs
#### Documentation
* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
			- [BUTTONS](#)
				- [st.button](/develop/api-reference/widgets/st.button)
				- [st.download_button](/develop/api-reference/widgets/st.download_button)
				- [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
				- [st.link_button](/develop/api-reference/widgets/st.link_button)
				- [st.page_link](/develop/api-reference/widgets/st.page_link)
			- [SELECTIONS](#)
				- [st.checkbox](/develop/api-reference/widgets/st.checkbox)
				- [st.color_picker](/develop/api-reference/widgets/st.color_picker)
				- [st.feedback](/develop/api-reference/widgets/st.feedback)
				- [st.multiselect](/develop/api-reference/widgets/st.multiselect)
				- [st.pills](/develop/api-reference/widgets/st.pills)
				- [st.radio](/develop/api-reference/widgets/st.radio)
				- [st.segmented_control](/develop/api-reference/widgets/st.segmented_control)
				- [st.selectbox](/develop/api-reference/widgets/st.selectbox)
				- [st.select_slider](/develop/api-reference/widgets/st.select_slider)
				- [st.toggle](/develop/api-reference/widgets/st.toggle)
			- [NUMERIC](#)
				- [st.number_input](/develop/api-reference/widgets/st.number_input)
				- [st.slider](/develop/api-reference/widgets/st.slider)
			- [DATE AND TIME](#)
				- [st.date_input](/develop/api-reference/widgets/st.date_input)
				- [st.time_input](/develop/api-reference/widgets/st.time_input)
			- [TEXT](#)
				- [st.chat_input](/develop/api-reference/chat/st.chat_input)
				- [st.text_area](/develop/api-reference/widgets/st.text_area)
				- [st.text_input](/develop/api-reference/widgets/st.text_input)
			- [MEDIA AND FILES](#)
				- [st.audio_input](/develop/api-reference/widgets/st.audio_input)
				- [st.camera_input](/develop/api-reference/widgets/st.camera_input)
				- [st.data_editor](/develop/api-reference/data/st.data_editor)
				- [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [APPLICATION LOGIC](#)
			- [Authentication and user info](/develop/api-reference/user)
			- [Navigation and pages](/develop/api-reference/navigation)
			- [Execution flow](/develop/api-reference/execution-flow)
			- [Caching and state](/develop/api-reference/caching-and-state)
			- [Connections and secrets](/develop/api-reference/connections)
			- [Custom components](/develop/api-reference/custom-components)
			- [Configuration](/develop/api-reference/configuration)
		- [TOOLS](#)
			- [App testing](/develop/api-reference/app-testing)
			- [Command line](/develop/api-reference/cli)
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
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Input widgets](/develop/api-reference/widgets)
* [st.download_button](/develop/api-reference/widgets/st.download_button)

### st.download_button
#### Display a download button widget.

This is useful when you would like to provide a way for your users to download a file directly from your app.

**Note:** The data to be downloaded is stored in-memory while the user is connected, so it's a good idea to keep file sizes under a couple hundred megabytes to conserve memory.

If you want to prevent your app from rerunning when a user clicks the download button, wrap the download button in a [fragment](https://docs.streamlit.io/develop/concepts/architecture/fragments).

#### Function signature
```python
st.download_button(
    label, 
    data, 
    file_name=None, 
    mime=None, 
    key=None, 
    help=None, 
    on_click="rerun", 
    args=None, 
    kwargs=None, 
    type="secondary", 
    icon=None, 
    disabled=False, 
    use_container_width=None, 
    width="content"
)
```

#### Parameters

* **label** (str): A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown.
* **data** (str, bytes, or file): The contents of the file to be downloaded.
* **file_name** (str): An optional string to use as the name of the file to be downloaded.
* **mime** (str or None): The MIME type of the data.
* **key** (str or int): An optional string or integer to use as the unique key for the widget.
* **help** (str or None): A tooltip that gets displayed when the button is hovered over.
* **on_click** (callable, "rerun", "ignore", or None): How the button should respond to user interaction.
* **args** (list or tuple): An optional list or tuple of args to pass to the callback.
* **kwargs** (dict): An optional dict of kwargs to pass to the callback.
* **type** ("primary", "secondary", or "tertiary"): An optional string that specifies the button type.
* **icon** (str or None): An optional emoji or icon to display next to the button label.
* **disabled** (bool): An optional boolean that disables the download button if set to True.
* **width** ("content", "stretch", or int): The width of the download button.

#### Returns

* **bool**: True if the button was clicked on the last run of the app, False otherwise.

#### Examples

##### Example 1: Download a dataframe as a CSV file

When working with a large dataframe, it's recommended to fetch your data with a cached function. When working with a download button, it's similarly recommended to convert your data into a downloadable format with a cached function.

```python
import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
    )
    return df

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)
```

##### Example 2: Download a string as a text file

If you pass a string to the data argument, Streamlit will automatically use the "text/plain" MIME type.

```python
import streamlit as st

message = st.text_area("Message", value="Lorem ipsum.\nStreamlit is cool.")

if st.button("Prepare download"):
    st.download_button(
        label="Download text",
        data=message,
        file_name="message.txt",
        on_click="ignore",
        type="primary",
        icon=":material/download:",
    )
```

##### Example 3: Download a file

Use a context manager to open and read a local file on your Streamlit server. Pass the io.BufferedReader object directly to data.

```python
import streamlit as st

with open("flower.png", "rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="flower.png",
        mime="image/png",
    )
```