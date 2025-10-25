Here is the content rewritten in clean Markdown:

# st.image
## Display an image or list of images

### Function signature
```python
st.image(image, caption=None, width="content", use_column_width=None, clamp=False, channels="RGB", output_format="auto")
```
### Parameters

* `image`: The image to display. This can be one of the following:
	+ A URL (string) for a hosted image.
	+ A path to a local image file. The path can be a str or Path object. Paths can be absolute or relative to the working directory (where you execute `streamlit run`).
	+ An SVG string like `<svg xmlns=...</svg>`.
	+ A byte array defining an image.
	+ A list of any of the above. Streamlit displays the list as a row of images that overflow to additional rows as needed.
* `caption`: Image caption(s). If this is `None` (default), no caption is displayed. If `image` is a list of multiple images, `caption` must be a list of captions (one caption for each image) or `None`.
* `width`: The width of the image element. This can be one of the following:
	+ "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
	+ "stretch": The width of the element matches the width of the parent container.
	+ An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.
* `use_column_width`: **Deprecated**. Please use the `width` parameter instead.
* `clamp`: Whether to clamp image pixel values to a valid range (0-255 per channel). This is only used for byte array images; the parameter is ignored for image URLs and files.
* `channels`: The color format when `image` is an nd.array. This is ignored for other image types. If this is "RGB" (default), `image[:, :, 0]` is the red channel, `image[:, :, 1]` is the green channel, and `image[:, :, 2]` is the blue channel.
* `output_format`: The output format to use when transferring the image data. If this is "auto" (default), Streamlit identifies the compression type based on the type and format of the image.

### Example
```python
import streamlit as st
st.image("sunrise.jpg", caption="Sunrise by the mountains")
```
Note: I removed the unnecessary HTML tags, links, and images, and reformatted the content to be more readable in Markdown. Let me know if you have any further requests!