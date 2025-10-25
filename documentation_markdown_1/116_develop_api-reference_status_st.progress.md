# st.progress

**URL:** https://docs.streamlit.io/develop/api-reference/status/st.progress

Display a progress bar.

---

## Function Signature

[\[source\]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/elements/progress.py#L94 "View st.progress source code on GitHub")

```python
st.progress(value, text=None, width="stretch")
```

## Parameters

*   **`value`** (`int` or `float`)
    *   `0 <= value <= 100` for `int`
    *   `0.0 <= value <= 1.0` for `float`

*   **`text`** (`str` or `None`)
    A message to display above the progress bar. The text can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

*   **`width`** (`"stretch"` or `int`)
    The width of the progress element. This can be one of the following:
    *   `"stretch"` (default): The width of the element matches the width of the parent container.
    *   An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.

---

## Example

Here is an example of a progress bar increasing over time and disappearing when it reaches completion:

```python
import streamlit as st
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Rerun")
```

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---

[Home](/)[Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)[Community](https://discuss.streamlit.io)

[GitHub](https://github.com/streamlit "GitHub") [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q "YouTube") [Twitter](https://twitter.com/streamlit "Twitter") [LinkedIn](https://www.linkedin.com/company/streamlit "LinkedIn") [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html "Newsletter")

© 2025 Snowflake Inc. [Cookie policy](_forum_ Ask)