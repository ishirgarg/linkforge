# st.text_area

**URL:** https://docs.streamlit.io/develop/api-reference/widgets/st.text_area

This document describes the `st.text_area` function in Streamlit, which allows you to add a multi-line text input widget to your application.

## Overview

The `st.text_area` function creates a text input widget that supports multiple lines of text. This is useful for collecting longer text inputs from users, such as comments, descriptions, or code snippets.

---
**(This is the first part of the content. The next part will continue with the function signature, parameters, and examples.)**

```markdown
## Parameters

*   **label** (`str`)

    A short label explaining to the user what this input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the body parameter of [st.markdown](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.

    For accessibility reasons, you should never set an empty label, but you can hide it with `label_visibility` if needed. In the future, we may disallow empty labels by raising an exception.

*   **value** (`object` or `None`)

    The text value of this widget when it first renders. This will be cast to `str` internally. If `None`, will initialize empty and return `None` until the user provides input. Defaults to empty string.

*   **height** (`"content"`, `"stretch"`, `int`, or `None`)

    The height of the text area widget. This can be one of the following:

    *   `None` (default): The height of the widget fits three lines.
    *   `"content"`: The height of the widget matches the height of its content.
    *   `"stretch"`: The height of the widget matches the height of its content or the height of the parent container, whichever is larger. If the widget is not in a parent container, the height of the widget matches the height of its content.
    *   An integer specifying the height in pixels: The widget has a fixed height. If the content is larger than the specified height, scrolling is enabled.

    The widget's height can't be smaller than the height of two lines. When `label_visibility="collapsed"`, the minimum height is 68 pixels. Otherwise, the minimum height is 98 pixels.

*   **max\_chars** (`int` or `None`)

    Maximum number of characters allowed in text area.

*   **key** (`str` or `int`)

    An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key.

*   **help** (`str` or `None`)

    A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when `label_visibility="visible"`. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.

*   **on\_change** (`callable`)

    An optional callback invoked when this `text_area`'s value changes.

*   **args** (`list` or `tuple`)

    An optional list or tuple of args to pass to the callback.

*   **kwargs** (`dict`)

    An optional dict of kwargs to pass to the callback.

*   **placeholder** (`str` or `None`)

    An optional string displayed when the text area is empty. If `None`, no text is displayed.

*   **disabled** (`bool`)

    An optional boolean that disables the text area if set to `True`. The default is `False`.

*   **label\_visibility** (`"visible"`, `"hidden"`, or `"collapsed"`)

    The visibility of the label. The default is `"visible"`. If this is `"hidden"`, Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is `"collapsed"`, Streamlit displays no label or spacer.

*   **width** (`"stretch"` or `int`)

    The width of the text area widget. This can be one of the following:

    *   `"stretch"` (default): The width of the widget matches the width of the parent container.
    *   An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container.

## Returns

(`str` or `None`)

The current value of the text area widget or `None` if no value has been provided by the user.

## Example

```python
import streamlit as st

txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(f"You wrote {len(txt)} characters.")
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
