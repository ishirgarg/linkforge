```markdown
# st.image - Streamlit

> Source: [https://docs.streamlit.io/develop/api-reference/media/st.image](https://docs.streamlit.io/develop/api-reference/media/st.image)

## st.image

Display an image or list of images.

### Function signature

```python
st.image(image, caption=None, width="content", use_column_width=None, clamp=False, channels="RGB", output_format="auto", *, use_container_width=None)
```

### Parameters

*   **image** (numpy.ndarray, BytesIO, str, Path, or list of these)

    The image to display. This can be one of the following:

    *   A URL (string) for a hosted image.
    *   A path to a local image file. The path can be a str or Path object. Paths can be absolute or relative to the working directory (where you execute streamlit run).
    *   An SVG string like `<svg xmlns=...</svg>`.
    *   A byte array defining an image. This includes monochrome images of shape (w,h) or (w,h,1), color images of shape (w,h,3), or RGBA images of shape (w,h,4), where w and h are the image width and height, respectively.
    *   A list of any of the above. Streamlit displays the list as a row of images that overflow to additional rows as needed.
*   **caption** (str or list of str)

    Image caption(s). If this is None (default), no caption is displayed. If image is a list of multiple images, caption must be a list of captions (one caption for each image) or None.

    Captions can optionally contain GitHub-flavored Markdown. Syntax information can be found at: [https://github.github.com/gfm](https://github.github.com/gfm).

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.
*   **width** ("content", "stretch", or int)

    The width of the image element. This can be one of the following:

    *   "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
    *   "stretch": The width of the element matches the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

    When using an SVG image without a default width, use "stretch" or an integer.
*   **use\_column\_width** ("auto", "always", "never", or bool)

    `use_column_width` is deprecated and will be removed in a future release. Please use the `width` parameter instead.

    If "auto", set the image's width to its natural size, but do not exceed the width of the column. If "always" or True, set the image's width to the column width. If "never" or False, set the image's width to its natural size. Note: if set, `use_column_width` takes precedence over the `width` parameter.
*   **clamp** (bool)

    Whether to clamp image pixel values to a valid range (0-255 per channel). This is only used for byte array images; the parameter is ignored for image URLs and files. If this is False (default) and an image has an out-of-range value, a RuntimeError will be raised.
*   **channels** ("RGB" or "BGR")
```


The color format when image is an nd.array. This is ignored for other image types. If this is "RGB" (default), `image[:, :, 0]` is the red channel, `image[:, :, 1]` is the green channel, and `image[:, :, 2]` is the blue channel. For images coming from libraries like OpenCV, you should set this to "BGR" instead.

`output_format` ("JPEG", "PNG", or "auto")
The output format to use when transferring the image data. If this is "auto" (default), Streamlit identifies the compression type based on the type and format of the image. Photos should use the "JPEG" format for lossy compression while diagrams should use the "PNG" format for lossless compression.

`use_container_width` (bool)
> **Deprecated:** `use_container_width` is deprecated and will be removed in a future release. For `use_container_width=True`, use `width="stretch"`. For `use_container_width=False`, use `width="content"`.
Whether to override width with the width of the parent container. If `use_container_width` is `False` (default), Streamlit sets the image's width according to `width`. If `use_container_width` is `True`, Streamlit sets the width of the image to match the width of the parent container.

#### Example

```python
import streamlit as st
st.image("sunrise.jpg", caption="Sunrise by the mountains")
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---