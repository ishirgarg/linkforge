Here is the converted HTML to clean markdown:

# Streamlit Docs
## Documentation

### Search
Search

### Navigation
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
				+ [st.button](/develop/api-reference/widgets/st.button)
				+ [st.download_button](/develop/api-reference/widgets/st.download_button)
				+ [st.form_submit_button](/develop/api-reference/execution-flow/st.form_submit_button)
				+ [st.link_button](/develop/api-reference/widgets/st.link_button)
				+ [st.page_link](/develop/api-reference/widgets/st.page_link)
			- [SELECTIONS](#)
				+ [st.checkbox](/develop/api-reference/widgets/st.checkbox)
				+ [st.color_picker](/develop/api-reference/widgets/st.color_picker)
				+ [st.feedback](/develop/api-reference/widgets/st.feedback)
				+ [st.multiselect](/develop/api-reference/widgets/st.multiselect)
				+ [st.pills](/develop/api-reference/widgets/st.pills)
				+ [st.radio](/develop/api-reference/widgets/st.radio)
				+ [st.segmented_control](/develop/api-reference/widgets/st.segmented_control)
				+ [st.selectbox](/develop/api-reference/widgets/st.selectbox)
				+ [st.select_slider](/develop/api-reference/widgets/st.select_slider)
				+ [st.toggle](/develop/api-reference/widgets/st.toggle)
			- [NUMERIC](#)
				+ [st.number_input](/develop/api-reference/widgets/st.number_input)
				+ [st.slider](/develop/api-reference/widgets/st.slider)
			- [DATE AND TIME](#)
				+ [st.date_input](/develop/api-reference/widgets/st.date_input)
				+ [st.time_input](/develop/api-reference/widgets/st.time_input)
			- [TEXT](#)
				+ [st.chat_input](/develop/api-reference/chat/st.chat_input)
				+ [st.text_area](/develop/api-reference/widgets/st.text_area)
				+ [st.text_input](/develop/api-reference/widgets/st.text_input)
			- [MEDIA AND FILES](#)
				+ [st.audio_input](/develop/api-reference/widgets/st.audio_input)
				+ [st.camera_input](/develop/api-reference/widgets/st.camera_input)
				+ [st.data_editor](/develop/api-reference/data/st.data_editor)
				+ [st.file_uploader](/develop/api-reference/widgets/st.file_uploader)
		- [Media elements](/develop/api-reference/media)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- [APPLICATION LOGIC](#)
			+ [Authentication and user info](/develop/api-reference/user)
			+ [Navigation and pages](/develop/api-reference/navigation)
			+ [Execution flow](/develop/api-reference/execution-flow)
			+ [Caching and state](/develop/api-reference/caching-and-state)
			+ [Connections and secrets](/develop/api-reference/connections)
			+ [Custom components](/develop/api-reference/custom-components)
			+ [Configuration](/develop/api-reference/configuration)
		- [TOOLS](#)
			+ [App testing](/develop/api-reference/app-testing)
			+ [Command line](/develop/api-reference/cli)
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

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Input widgets](/develop/api-reference/widgets)
* [st.audio_input](/develop/api-reference/widgets/st.audio_input)

## st.audio_input
Display a widget that returns an audio recording from the user's microphone.

### Function Signature
```python
st.audio_input(label, *, sample_rate=16000, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")
```
### Parameters

* **label** (str): A short label explaining to the user what this widget is used for. The label can optionally contain GitHub-flavored Markdown.
* **sample_rate** (int or None): The target sample rate for the audio recording in Hz. Defaults to 16000 Hz, which is optimal for speech recognition.
* **key** (str or int): An optional string or integer to use as the unique key for the widget.
* **help** (str or None): A tooltip that gets displayed next to the widget label.
* **on_change** (callable): An optional callback invoked when this audio input's value changes.
* **args** (list or tuple): An optional list or tuple of args to pass to the callback.
* **kwargs** (dict): An optional dict of kwargs to pass to the callback.
* **disabled** (bool): An optional boolean that disables the audio input if set to True. Defaults to False.
* **label_visibility** ("visible", "hidden", or "collapsed"): The visibility of the label. Defaults to "visible".
* **width** ("stretch" or int): The width of the audio input widget.

### Returns
(None or UploadedFile): The UploadedFile class is a subclass of BytesIO, and therefore is "file-like". This means you can pass an instance of it anywhere a file is expected. The MIME type for the audio data is audio/wav.

### Examples

#### Example 1: Record a voice message and play it back.
```python
import streamlit as st

audio_value = st.audio_input("Record a voice message")

if audio_value:
    st.audio(audio_value)
```
#### Example 2: Record high-fidelity audio and play it back.
```python
import streamlit as st

audio_value = st.audio_input("Record high quality audio", sample_rate=48000)

if audio_value:
    st.audio(audio_value)
```
Note: The resulting UploadedFile is subject to the size limitation configured in server.maxUploadSize. If you expect large sound files, update the configuration option appropriately.