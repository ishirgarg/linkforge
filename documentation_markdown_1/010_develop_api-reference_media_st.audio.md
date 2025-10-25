# st.audio

[Original URL](https://docs.streamlit.io/develop/api-reference/media/st.audio)

This page documents the `st.audio` function in the Streamlit API.


### Parameters

*   **data** (`str`, `Path`, `bytes`, `BytesIO`, `numpy.ndarray`, or `file`): The audio to play. This can be one of the following:
    *   A URL (string) for a hosted audio file.
    *   A path to a local audio file. The path can be a `str` or `Path` object. Paths can be absolute or relative to the working directory (where you execute `streamlit run`).
    *   Raw audio data. Raw data formats must include all necessary file headers to match the file format specified via `format`.

    If `data` is a NumPy array, it must either be a 1D array of the waveform or a 2D array of shape `(C, S)` where `C` is the number of channels and `S` is the number of samples. See the default channel order at [http://msdn.microsoft.com/en-us/library/windows/hardware/dn653308(v=vs.85).aspx](http://msdn.microsoft.com/en-us/library/windows/hardware/dn653308(v=vs.85).aspx).

*   **format** (`str`): The MIME type for the audio file. This defaults to `"audio/wav"`. For more information about MIME types, see [https://www.iana.org/assignments/media-types/media-types.xhtml](https://www.iana.org/assignments/media-types/media-types.xhtml).

*   **start\_time** (`int`, `float`, `timedelta`, `str`, or `None`): The time from which the element should start playing. This can be one of the following:
    *   `None` (default): The element plays from the beginning.
    *   An `int` or `float` specifying the time in seconds. `float` values are rounded down to whole seconds.
    *   A string specifying the time in a format supported by [Pandas' Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html), e.g. `"2 minute"`, `"20s"`, or `"1m14s"`.
    *   A `timedelta` object from [Python's built-in `datetime` library](https://docs.python.org/3/library/datetime.html#timedelta-objects), e.g. `timedelta(seconds=70)`.

*   **sample\_rate** (`int` or `None`): The sample rate of the audio data in samples per second. This is only required if `data` is a NumPy array.

*   **end\_time** (`int`, `float`, `timedelta`, `str`, or `None`): The time at which the element should stop playing. This can be one of the following:
    *   `None` (default): The element plays through to the end.
    *   An `int` or `float` specifying the time in seconds. `float` values are rounded down to whole seconds.
    *   A string specifying the time in a format supported by [Pandas' Timedelta constructor](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html), e.g. `"2 minute"`, `"20s"`, or `"1m14s"`.
    *   A `timedelta` object from [Python's built-in `datetime` library](https://docs.python.org/3/library/datetime.html#timedelta-objects), e.g. `timedelta(seconds=70)`.

*   **loop** (`bool`): Whether the audio should loop playback.

*   **autoplay** (`bool`): Whether the audio file should start playing automatically. This is `False` by default. Browsers will not autoplay audio files if the user has not interacted with the page by clicking somewhere.

*   **width** (`"stretch"` or `int`): The width of the audio player element. This can be one of the following:
    *   `"stretch"` (default): The width of the element matches the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

### Examples

To display an audio player for a local file, specify the file's string path and format.

```python
import streamlit as st

st.audio("cat-purr.mp3", format="audio/mpeg", loop=True)
```

You can also pass bytes or numpy.ndarray objects to `st.audio`.

```python
import streamlit as st
import numpy as np

audio_file = open("myaudio.ogg", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/ogg")

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)
```

### Conclusion

The `st.audio` function provides a versatile way to embed audio playback within your Streamlit applications. It supports various input formats, including URLs, local files, raw bytes, and NumPy arrays, making it adaptable to different audio sources. You can control playback behavior with parameters like `start_time`, `end_time`, `loop`, and `autoplay`, and customize the player's appearance with the `width` parameter. When working with raw audio data or NumPy arrays, specifying the `format` and `sample_rate` is crucial for correct playback.

### Further Resources

*   **Previous:** [Media elements](/develop/api-reference/media)
*   **Next:** [st.image](/develop/api-reference/media/st.image)
*   **Forums:** For further questions and community support, visit the [Streamlit forums](https://discuss.streamlit.io).