# st.html

[Original URL](https://docs.streamlit.io/develop/api-reference/text/st.html)

Insert HTML into your app.

Adding custom HTML to your app impacts safety, styling, and maintainability. We sanitize HTML with [DOMPurify](https://github.com/cure53/DOMPurify), but inserting HTML remains a developer risk. Passing untrusted code to st.html or dynamically loading external code can increase the risk of vulnerabilities in your app.

`st.html` content is **not** iframed. Executing JavaScript is not supported at this time.

## Function signature

```python
st.html(body, *, width="stretch")
```

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/html.py#L39 "View st.html source code on GitHub")

### Parameters

#### body (any)

The HTML code to insert. This can be one of the following:

*   A string of HTML code.
*   A path to a local file with HTML code. The path can be a `str` or `Path` object. Paths can be absolute or relative to the working directory (where you execute `streamlit run`).
*   Any object. If `body` is not a string or path, Streamlit will convert the object to a string. `body._repr_html_()` takes precedence over `str(body)` when available.

If the resulting HTML content is empty, Streamlit will raise an error.

If `body` is a path to a CSS file, Streamlit will wrap the CSS content in `<style>` tags automatically. When the resulting HTML content only contains style tags, Streamlit will send the content to the event container instead of the main container to avoid taking up space in the app.

#### width ("stretch", "content", or int)

The width of the HTML element. This can be one of the following:

*   `"stretch"` (default): The width of the element matches the width of the parent container.
*   `"content"`: The width of the element matches the width of its content, but doesn't exceed the width of the parent container.
*   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

## Example

```python
import streamlit as st

st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)
```


### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit) | [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q) | [Twitter](https://twitter.com/streamlit) | [LinkedIn](https://www.linkedin.com/company/streamlit) | [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

© 2025 Snowflake Inc. [Cookie policy](https://streamlit.io/cookie-policy)