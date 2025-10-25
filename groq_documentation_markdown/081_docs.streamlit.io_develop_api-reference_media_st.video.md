Here is the converted markdown:

# st.video - Streamlit Docs
![logo](/logo.svg)

## Documentation
### Search
Search

### Navigation
* **Get started**
	+ [Installation](/get-started/installation)
	+ [Fundamentals](/get-started/fundamentals)
	+ [First steps](/get-started/tutorials)
* **Develop**
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
* **Deploy**
	+ [Concepts](/deploy/concepts)
	+ [Streamlit Community Cloud](/deploy/streamlit-community-cloud)
	+ [Snowflake](/deploy/snowflake)
	+ [Other platforms](/deploy/tutorials)
* **Knowledge base**
	+ [FAQ](/knowledge-base/using-streamlit)
	+ [Installing dependencies](/knowledge-base/dependencies)
	+ [Deployment issues](/knowledge-base/deploy)

### Links
* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Media elements](/develop/api-reference/media)
* [st.video](/develop/api-reference/media/st.video)

Here is the HTML content converted to clean Markdown:
### st.video
#### Streamlit Version
 Version 1.50.0, Version 1.49.0, Version 1.48.0, Version 1.47.0, Version 1.46.0, Version 1.45.0, Version 1.44.0, Version 1.43.0, Version 1.42.0, Version 1.41.0, Version 1.40.0, Version 1.39.0, Version 1.38.0, Version 1.37.0, Version 1.36.0, Version 1.35.0, Version 1.34.0, Version 1.33.0, Version 1.32.0, Version 1.31.0, Version 1.30.0, Version 1.29.0, Version 1.28.0, Version 1.27.0, Version 1.26.0, Version 1.25.0, Version 1.24.0, Version 1.23.0, Version 1.22.0

Display a video player.

#### Function signature
[View st.video source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/media.py#L226)

```python
st.video(data, format="video/mp4", start_time=0, *, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False, width="stretch")
```

#### Parameters

* **data**: The video to play. This can be one of the following:
	+ A URL (string) for a hosted video file, including YouTube URLs.
	+ A path to a local video file. The path can be a str or Path object. Paths can be absolute or relative to the working directory (where you execute streamlit run).
	+ Raw video data. Raw data formats must include all necessary file headers to match the file format specified via format.
* **format**: The MIME type for the video file. This defaults to "video/mp4". For more information about MIME types, see [https://www.iana.org/assignments/media-types/media-types.xhtml](https://www.iana.org/assignments/media-types/media-types.xhtml).
* **start_time**: The time from which the element should start playing. This can be one of the following:
	+ None (default): The element plays from the beginning.
	+ An int or float specifying the time in seconds. float values are rounded down to whole seconds.
	+ A string specifying the time in a format supported by [Pandas' Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html), e.g. "2 minute", "20s", or "1m14s".
	+ A timedelta object from [Python's built-in datetime library](https://docs.python.org/3/library/datetime.html#timedelta-objects), e.g. timedelta(seconds=70).
* **subtitles**: Optional subtitle data for the video, supporting several input types:
	+ None (default): No subtitles.
	+ A string, bytes, or Path: File path to a subtitle file in .vtt or .srt formats, or the raw content of subtitles conforming to these formats. Paths can be absolute or relative to the working directory (where you execute streamlit run). If providing raw content, the string must adhere to the WebVTT or SRT format specifications.
	+ io.BytesIO: A BytesIO stream that contains valid .vtt or .srt formatted subtitle data.
	+ A dictionary: Pairs of labels and file paths or raw subtitle content in .vtt or .srt formats to enable multiple subtitle tracks. The label will be shown in the video player. Example: {"English": "path/to/english.vtt", "French": "path/to/french.srt"}
* **end_time**: The time at which the element should stop playing. This can be one of the following:
	+ None (default): The element plays through to the end.
	+ An int or float specifying the time in seconds. float values are rounded down to whole seconds.
	+ A string specifying the time in a format supported by [Pandas' Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html), e.g. "2 minute", "20s", or "1m14s".
	+ A timedelta object from [Python's built-in datetime library](https://docs.python.org/3/library/datetime.html#timedelta-objects), e.g. timedelta(seconds=70).
* **loop**: Whether the video should loop playback.
* **autoplay**: Whether the video should start playing automatically. This is False by default. Browsers will not autoplay unmuted videos if the user has not interacted with the page by clicking somewhere. To enable autoplay without user interaction, you must also set muted=True.
* **muted**: Whether the video should play with the audio silenced. This is False by default. Use this in conjunction with autoplay=True to enable autoplay without user interaction.
* **width**: The width of the video player element. This can be one of the following:
	+ "stretch" (default): The width of the element matches the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

#### Example
```python
import streamlit as st

video_file = open("myvideo.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)
```

#### Subtitle Example
Here is a simple VTT file (subtitles.vtt):
```
WEBVTT

0:00:01.000 --> 0:00:02.000
Look!

0:00:03.000 --> 0:00:05.000
Look at the pretty stars!
```
If the above VTT file lives in the same directory as your app, you can add subtitles like so:
```python
import streamlit as st

VIDEO_URL = "https://example.com/not-youtube.mp4"
st.video(VIDEO_URL, subtitles="subtitles.vtt")
```
See additional examples of supported subtitle input types in our [video subtitles feature demo](https://doc-video-subtitle-inputs.streamlit.app/).

#### Note
Some videos may not display if they are encoded using MP4V (which is an export option in OpenCV), as this codec is not widely supported by browsers. Converting your video to H.264 will allow the video to be displayed in Streamlit. See this [StackOverflow post](https://stackoverflow.com/a/49535220/2394542) or this [Streamlit forum post](https://discuss.streamlit.io/t/st-video-doesnt-show-opencv-generated-mp4/3193/2) for more information.