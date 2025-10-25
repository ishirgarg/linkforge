```markdown
# st.logo

[Original URL](https://docs.streamlit.io/develop/api-reference/media/st.logo)

## st.logo

```


Renders a logo in the upper-left corner of your app and its sidebar.

If `st.logo` is called multiple times within a page, Streamlit will render the image passed in the last call. For the most consistent results, call `st.logo` early in your page script and choose an image that works well in both light and dark mode. Avoid empty margins around your image.

If your logo does not work well for both light and dark mode, consider setting the theme and hiding the settings menu from users with the [configuration option](https://docs.streamlit.io/develop/api-reference/configuration/config.toml) `client.toolbarMode="minimal"`.

## Function signature

[`[source]`](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/commands/logo.py#L38 "View st.logo source code on GitHub")

`st.logo(image, *, size="medium", link=None, icon_image=None)`

## Parameters

### image (Anything supported by st.image (except list))

The image to display in the upper-left corner of your app and its sidebar. This can be any of the types supported by [`st.image`](https://docs.streamlit.io/develop/api-reference/media/st.image) except a list. If `icon_image` is also provided, then Streamlit will only display `image` in the sidebar.

Streamlit scales the image to a max height set by `size` and a max width to fit within the sidebar.

### size ("small", "medium", or "large")

The size of the image displayed in the upper-left corner of the app and its sidebar. The possible values are as follows:

*   "small": 20px max height
*   "medium" (default): 24px max height
*   "large": 32px max height

### link (str or None)

The external URL to open when a user clicks on the logo. The URL must start with "http://" or "https://". If `link` is `None` (default), the logo will not include a hyperlink.

### icon_image (Anything supported by st.image (except list) or None)

An optional, typically smaller image to replace `image` in the upper-left corner when the sidebar is closed. This can be any of the types supported by `st.image` except a list. If `icon_image` is `None` (default), Streamlit will always display `image` in the upper-left corner, regardless of whether the sidebar is open or closed. Otherwise, Streamlit will render `icon_image` in the upper-left corner of the app when the sidebar is closed.

Streamlit scales the image to a max height set by `size` and a max width to fit within the sidebar. If the sidebar is closed, the max width is retained from when it was last open.

For best results, pass a wide or horizontal image to `image` and a square image to `icon_image`. Or, pass a square image to `image` and leave `icon_image=None`.

## Examples

A common design practice is to use a wider logo in the sidebar, and a smaller, icon-styled logo in your app's main body.

```python
import streamlit as st

st.logo(
    LOGO_URL_LARGE,
    link="https://streamlit.io/gallery",
    icon_image=LOGO_URL_SMALL,
)
```

Try switching logos around in the following example:

```python
import streamlit as st

HORIZONTAL_RED = "images/horizontal_red.png"
ICON_RED = "images/icon_red.png"
HORIZONTAL_BLUE = "images/horizontal_blue.png"
ICON_BLUE = "images/icon_blue.png"

options = [HORIZONTAL_RED, ICON_RED, HORIZONTAL_BLUE, ICON_BLUE]
sidebar_logo = st.selectbox("Sidebar logo", options, 0)
main_body_logo = st.selectbox("Main body logo", options, 1)

st.logo(sidebar_logo, icon_image=main_body_logo)
st.sidebar.markdown("Hi!")
```

[Built with Streamlit 🎈](https://streamlit.io)

[Fullscreen _open\_in\_new_](https://doc-logo.streamlit.app//?utm_medium=oembed&)

[_arrow\_back_Previous: st.image](/develop/api-reference/media/st.image)
[_arrow\_forward_Next: st.pdf](/develop/api-reference/media/st.pdf)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
