Here is the converted markdown:
### st.audio - Streamlit Docs

![logo](/logo.svg)

#### Documentation

### Search

* [Get started](/get-started)
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* [Develop](/develop)
	+ [Concepts](/develop/concepts)
	+ [API reference](/develop/api-reference)
		- PAGE ELEMENTS
		- [Write and magic](/develop/api-reference/write-magic)
		- [Text elements](/develop/api-reference/text)
		- [Data elements](/develop/api-reference/data)
		- [Chart elements](/develop/api-reference/charts)
		- [Input widgets](/develop/api-reference/widgets)
		- [Media elements](/develop/api-reference/media)
			- [st.audio](/develop/api-reference/media/st.audio)
			- [st.image](/develop/api-reference/media/st.image)
			- [st.logo](/develop/api-reference/media/st.logo)
			- [st.pdf](/develop/api-reference/media/st.pdf)
			- [st.video](/develop/api-reference/media/st.video)
		- [Layouts and containers](/develop/api-reference/layout)
		- [Chat elements](/develop/api-reference/chat)
		- [Status elements](/develop/api-reference/status)
		- [Third-party components](https://streamlit.io/components)
		- APPLICATION LOGIC
		- [Authentication and user info](/develop/api-reference/user)
		- [Navigation and pages](/develop/api-reference/navigation)
		- [Execution flow](/develop/api-reference/execution-flow)
		- [Caching and state](/develop/api-reference/caching-and-state)
		- [Connections and secrets](/develop/api-reference/connections)
		- [Custom components](/develop/api-reference/custom-components)
		- [Configuration](/develop/api-reference/configuration)
		- TOOLS
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

### Links

* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Media elements](/develop/api-reference/media)
* [st.audio](/develop/api-reference/media/st.audio)

## st.audio
### Display an audio player

#### Function signature
```python
st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None, end_time=None, loop=False, autoplay=False, width="stretch")
```
#### Parameters

* **data**: The audio to play. This can be a URL, a path to a local audio file, or raw audio data.
	+ If `data` is a NumPy array, it must be a 1D array of the waveform or a 2D array of shape (C, S) where C is the number of channels and S is the number of samples.
* **format**: The MIME type for the audio file. Defaults to "audio/wav".
* **start_time**: The time from which the element should start playing. Can be `None`, an int or float, a string, or a `timedelta` object.
* **sample_rate**: The sample rate of the audio data in samples per second. Required if `data` is a NumPy array.
* **end_time**: The time at which the element should stop playing. Can be `None`, an int or float, a string, or a `timedelta` object.
* **loop**: Whether the audio should loop playback.
* **autoplay**: Whether the audio file should start playing automatically.
* **width**: The width of the audio player element. Can be "stretch" or an integer.

#### Examples

To display an audio player for a local file:
```python
import streamlit as st
st.audio("cat-purr.mp3", format="audio/mpeg", loop=True)
```
You can also pass bytes or NumPy arrays to `st.audio`:
```python
import streamlit as st
import numpy as np

audio_file = open("myaudio.ogg", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/ogg")

sample_rate = 44100
seconds = 2
frequency_la = 440
t = np.linspace(0, seconds, seconds * sample_rate, False)
note_la = np.sin(frequency_la * t * 2 * np.pi)
st.audio(note_la, sample_rate=sample_rate)
```