# st.page_link

[Original URL](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link)

#### Tip

Check out our [tutorial](/develop/tutorials/multipage/st.page_link-nav) to learn about building custom, dynamic menus with `st.page_link`.

## st.page_link


Display a link to another page in a multipage app or to an external page.

If another page in a multipage app is specified, clicking `st.page_link` stops the current page execution and runs the specified page as if the user clicked on it in the sidebar navigation.

If an external page is specified, clicking `st.page_link` opens a new tab to the specified page. The current script run will continue if not complete.

## Function signature

```python
st.page_link(page, *, label=None, icon=None, help=None, disabled=False, use_container_width=None, width="content")
```

## Parameters

*   **page** (`str`, `Path`, or `StreamlitPage`)

    The file path (relative to the main script) or a `StreamlitPage` indicating the page to switch to. Alternatively, this can be the URL to an external page (must start with "http://" or "https://").
*   **label** (`str`)

    The label for the page link. Labels are required for external pages. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height.

    Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\\. Not an ordered list".

    See the body parameter of [`st.markdown`](https://docs.streamlit.io/develop/api-reference/text/st.markdown) for additional, supported Markdown directives.
*   **icon** (`str` or `None`)

    An optional emoji or icon to display next to the button label. If `icon` is `None` (default), the icon is inferred from the `StreamlitPage` object or no icon is displayed. If `icon` is a string, the following options are valid:

    *   A single-character emoji. For example, you can set `icon="🚨"` or `icon="🔥"`. Emoji short codes are not supported.
    *   An icon from the Material Symbols library (rounded style) in the format `":material/icon_name:"` where `"icon_name"` is the name of the icon in snake case.

        For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.
*   **help** (`str` or `None`)

    A tooltip that gets displayed when the link is hovered over. If this is `None` (default), no tooltip is displayed.

    The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of `st.markdown`.
*   **disabled** (`bool`)

    An optional boolean that disables the page link if set to `True`. The default is `False`.
*   **use_container_width** (`bool`)

    _delete_

    `use_container_width` is deprecated and will be removed in a future release. For `use_container_width=True`, use `width="stretch"`. For `use_container_width=False`, use `width="content"`.

    Whether to expand the link's width to fill its parent container. The default is `True` for page links in the sidebar and `False` for those in the main app.
*   **width** (`"content"`, `"stretch"`, or `int`)

    The width of the page-link button. This can be one of the following:

    *   `"content"` (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container.
    *   `"stretch"`: The width of the button matches the width of the parent container.
    *   An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container.

## Example

Consider the following example given this file structure:

```
your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py
```

```python
import streamlit as st

st.page_link("your_app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
```

The default navigation is shown here for comparison, but you can hide the default navigation using the [client.showSidebarNavigation](https://docs.streamlit.io/develop/api-reference/configuration/config.toml#client) configuration option. This allows you to create custom, dynamic navigation menus for your apps!

[Built with Streamlit 🎈](https://streamlit.io)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
