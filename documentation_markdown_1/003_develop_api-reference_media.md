```markdown
# Media elements

> Source: [https://docs.streamlit.io/develop/api-reference/media](https://docs.streamlit.io/develop/api-reference/media)

This section of the Streamlit API reference covers the media elements available for use in your Streamlit applications. These elements allow you to display various media types, enhancing the visual and interactive aspects of your apps.
```


It's easy to embed images, videos, and audio files directly into your Streamlit apps.

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

### Third-party components

These are featured components created by our lovely community. For more examples and inspiration, check out our [Components Gallery](https://streamlit.io/components) and [Streamlit Extras](https://extras.streamlit.app)!

#### Streamlit Cropper

[A simple image cropper for Streamlit. Created by](https://github.com/turner-anderson/streamlit-cropper) [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper
st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

#### Image Coordinates

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
streamlit_image_coordinates("https://placekitten.com/200/300")
```

#### Streamlit Lottie

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

#### Streamlit Webrtc

[Handling and transmitting real-time video/audio streams with Streamlit. Created by](https://github.com/whitphx/streamlit-webrtc) [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer
webrtc_streamer(key="sample")
```

#### Drawable Canvas

[Provides a sketching canvas using](https://github.com/andfanilo/streamlit-drawable-canvas) [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

#### Image Comparison

[Compare images with a slider using](https://github.com/fcakyon/streamlit-image-comparison) [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison
image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

#### Streamlit Cropper

[A simple image cropper for Streamlit. Created by](https://github.com/turner-anderson/streamlit-cropper) [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper
st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

#### Image Coordinates

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
streamlit_image_coordinates("https://placekitten.com/200/300")
```

#### Streamlit Lottie

[Integrate](https://github.com/andfanilo/streamlit-lottie) [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

#### Streamlit Webrtc

[Handling and transmitting real-time video/audio streams with Streamlit. Created by](https://github.com/whitphx/streamlit-webrtc) [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer
webrtc_streamer(key="sample")
```

#### Drawable Canvas

[Provides a sketching canvas using](https://github.com/andfanilo/streamlit-drawable-canvas) [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

#### Image Comparison

[Compare images with a slider using](https://github.com/fcakyon/streamlit-image-comparison) [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison
image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

#### Streamlit Cropper

[A simple image cropper for Streamlit. Created by](https://github.com/turner-anderson/streamlit-cropper) [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper
st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

#### Image Coordinates

[Get the coordinates of clicks on an image. Created by](https://github.com/blackary/streamlit-image-coordinates) [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
streamlit_image_coordinates("https://placekitten.com/200/300")
```


### Streamlit Lottie

Integrate Lottie animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
st_lottie(lottie_hello, key="hello")
```

[Previous: Input widgets](/develop/api-reference/widgets) [Next: st.audio](/develop/api-reference/media/st.audio)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

***

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

© 2025 Snowflake Inc.
[Cookie policy](/)

_forum_ Ask A