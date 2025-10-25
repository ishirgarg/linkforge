```markdown
# st.set_page_config

[Original URL](https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config)

## st.set_page_config
```


Configure the default settings of the page.

This command can be called multiple times in a script run to dynamically change the page configuration. The calls are additive, with each successive call overriding only the parameters that are specified.

### Function signature
[[source]](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/commands/page_config.py#L112 "View st.set_page_config source code on GitHub")

```python
st.set_page_config(page_title=None, page_icon=None, layout=None, initial_sidebar_state=None, menu_items=None)
```

### Parameters

*   **page_title** (`str` or `None`)
    The page title, shown in the browser tab. If this is `None` (default), the page title is inherited from the previous call of `st.set_page_config`. If this is `None` and no previous call exists, the page title is inferred from the page source.

    If a page source is a Python file, its inferred title is derived from the filename. If a page source is a callable object, its inferred title is derived from the callable's name.

*   **page_icon** (`Anything supported by st.image (except list)`, `str`, or `None`)
    The page favicon. If `page_icon` is `None` (default), the page icon is inherited from the previous call of `st.set_page_config`. If this is `None` and no previous call exists, the favicon is a monochrome Streamlit logo.

    In addition to the types supported by [st.image](https://docs.streamlit.io/develop/api-reference/media/st.image) (except list), the following strings are valid:

    *   A single-character emoji. For example, you can set `page_icon="🦈"`.
    *   An emoji short code. For example, you can set `page_icon=":shark:"`. For a list of all supported codes, see [https://share.streamlit.io/streamlit/emoji-shortcodes](https://share.streamlit.io/streamlit/emoji-shortcodes).
    *   The string literal, `"random"`. You can set `page_icon="random"` to set a random emoji from the supported list above.
    *   An icon from the Material Symbols library (rounded style) in the format `":material/icon_name:"` where `"icon_name"` is the name of the icon in snake case.

        For example, `page_icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.

    > **Note**
    > Colors are not supported for Material icons. When you use a Material icon for favicon, it will be black, regardless of browser theme.

*   **layout** (`"centered"`, `"wide"`, or `None`)
    How the page content should be laid out. If this is `None` (default), the page layout is inherited from the previous call of `st.set_page_config`. If this is `None` and no previous call exists, the page layout is `"centered"`.

    `"centered"` constrains the elements into a centered column of fixed width. `"wide"` uses the entire screen.

*   **initial_sidebar_state** (`"auto"`, `"expanded"`, `"collapsed"`, or `None`)
    How the sidebar should start out. If this is `None` (default), the sidebar state is inherited from the previous call of `st.set_page_config`. If no previous call exists, the sidebar state is `"auto"`.

    The following states are supported:

    *   `"auto"`: The sidebar is hidden on small devices and shown otherwise.
    *   `"expanded"`: The sidebar is shown initially.
    *   `"collapsed"`: The sidebar is hidden initially.

    In most cases, `"auto"` provides the best user experience across devices of different sizes.

*   **menu_items** (`dict`)
    Configure the menu that appears on the top-right side of this app. The keys in this dict denote the menu item to configure. The following keys can have string or `None` values:

    *   `"Get help"`: The URL this menu item should point to.
    *   `"Report a Bug"`: The URL this menu item should point to.
    *   `"About"`: A markdown string to show in the About dialog.

    A URL may also refer to an email address e.g. `mailto:john@example.com`.

    If you do not include a key, its menu item will be hidden (unless it was set by a previous call to `st.set_page_config`). To remove an item that was specified in a previous call to `st.set_page_config`, set its value to `None` in the dictionary.

#### Example

```python
import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
```

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.