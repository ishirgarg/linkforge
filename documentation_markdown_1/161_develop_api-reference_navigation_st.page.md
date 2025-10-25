```markdown
# st.Page - Streamlit Docs

> Source: [https://docs.streamlit.io/develop/api-reference/navigation/st.page](https://docs.streamlit.io/develop/api-reference/navigation/st.page)

## st.Page
```


Configure a page for `st.navigation` in a multipage app.

Call `st.Page` to initialize a `StreamlitPage` object, and pass it to `st.navigation` to declare a page in your app.

When a user navigates to a page, `st.navigation` returns the selected `StreamlitPage` object. Call `.run()` on the returned `StreamlitPage` object to execute the page. You can only run the page returned by `st.navigation`, and you can only run it once per app rerun.

A page can be defined by a Python file or Callable.

### Function signature

```python
st.Page(page, *, title=None, icon=None, url_path=None, default=False)
```

### Parameters

*   **page** (`str`, `Path`, or `callable`)
    The page source as a Callable or path to a Python file. If the page source is defined by a Python file, the path can be a string or `pathlib.Path` object. Paths can be absolute or relative to the entrypoint file. If the page source is defined by a Callable, the Callable can't accept arguments.

*   **title** (`str` or `None`)
    The title of the page. If this is `None` (default), the page title (in the browser tab) and label (in the navigation menu) will be inferred from the filename or callable name in `page`. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-labels).

*   **icon** (`str` or `None`)
    An optional emoji or icon to display next to the page title and label. If `icon` is `None` (default), no icon is displayed next to the page label in the navigation menu, and a Streamlit icon is displayed next to the title (in the browser tab). If `icon` is a string, the following options are valid:
    *   A single-character emoji. For example, you can set `icon="🔥"`. Emoji short codes are not supported.
    *   An icon from the Material Symbols library (rounded style) in the format `":material/icon_name:"` where `"icon_name"` is the name of the icon in snake case. For example, `icon=":material/thumb_up:"` will display the Thumb Up icon. Find additional icons in the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded) font library.

*   **url_path** (`str` or `None`)
    The page's URL pathname, which is the path relative to the app's root URL. If this is `None` (default), the URL pathname will be inferred from the filename or callable name in `page`. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-urls).

    The default page will have a pathname of `""`, indicating the root URL of the app. If you set `default=True`, `url_path` is ignored. `url_path` can't include forward slashes; paths can't include subdirectories.

*   **default** (`bool`)
    Whether this page is the default page to be shown when the app is loaded. If `default` is `False` (default), the page will have a nonempty URL pathname. However, if no default page is passed to `st.navigation` and this is the first page, this page will become the default page. If `default` is `True`, then the page will have an empty pathname and `url_path` will be ignored.

### Returns

*   (`StreamlitPage`)
    The page object associated to the given script.

#### Example

```python
import streamlit as st

def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("page1.py", title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
])
pg.run()
```

## StreamlitPage

A page within a multipage Streamlit app.

Use `st.Page` to initialize a `StreamlitPage` object.

### Class description

```python
StreamlitPage(page, *, title=None, icon=None, url_path=None, default=False)
```

### Methods

*   [run()](/develop/api-reference/navigation/st.page#stpagerun)()
    Execute the page.

### Attributes

*   **icon** (`str`)
    The icon of the page. If no icon was declared in `st.Page`, this property returns `""`.

*   **title** (`str`)
    The title of the page. Unless declared otherwise in `st.Page`, the page title is inferred from the filename or callable name. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-labels).

*   **url_path** (`str`)
    The page's URL pathname, which is the path relative to the app's root URL. Unless declared otherwise in `st.Page`, the URL pathname is inferred from the filename or callable name. For more information, see [Overview of multipage apps](https://docs.streamlit.io/st.page.automatic-page-urls).

    The default page will always have a `url_path` of `""` to indicate the root URL (e.g., homepage).

## StreamlitPage.run

Execute the page.

When a page is returned by `st.navigation`, use the `.run()` method within your entrypoint file to render the page. You can only call this method on the page returned by `st.navigation`. You can only call this method once per run of your entrypoint file.

### Function signature

```python
StreamlitPage.run()
```

---

[_arrow_back_Previous: st.navigation](/develop/api-reference/navigation/st.navigation) [_arrow_forward_Next: st.page_link](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link)

---

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.