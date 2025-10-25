```markdown
# st.navigation

[Original URL](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation)

This section of the documentation covers the `st.navigation` element in Streamlit. Further content will be added in subsequent parts.
```


Configure the available pages in a multipage app.

Call `st.navigation` in your entrypoint file to define the available pages for your app. `st.navigation` returns the current page, which can be executed using the `.run()` method.

When using `st.navigation`, your entrypoint file (the file passed to `streamlit run`) acts like a router or frame of common elements around each of your pages. Streamlit executes the entrypoint file with every app rerun. To execute the current page, you must call the `.run()` method on the `StreamlitPage` object returned by `st.navigation`.

The set of available pages can be updated with each rerun for dynamic navigation. By default, `st.navigation` displays the available pages in the sidebar if there is more than one page. This behavior can be changed using the `position` keyword argument.

As soon as any session of your app executes the `st.navigation` command, your app will ignore the `pages/` directory (across all sessions).

### Function signature

```python
st.navigation(pages, *, position="sidebar", expanded=False)
```

### Parameters

*   **pages** (`Sequence[page-like], Mapping[str, Sequence[page-like]]`)

    The available pages for the app.

    To create a navigation menu with no sections or page groupings, `pages` must be a list of page-like objects. Page-like objects are anything that can be passed to `st.Page` or a `StreamlitPage` object returned by `st.Page`.

    To create labeled sections or page groupings within the navigation menu, `pages` must be a dictionary. Each key is the label of a section and each value is the list of page-like objects for that section. If you use `position="top"`, each grouping will be a collapsible item in the navigation menu. For top navigation, if you use an empty string as a section header, the pages in that section will be displayed at the beginning of the menu before the collapsible sections.

    When you use a string or path as a page-like object, they are internally passed to `st.Page` and converted to `StreamlitPage` objects. In this case, the page will have the default title, icon, and path inferred from its path or filename. To customize these attributes for your page, initialize your page with `st.Page`.

*   **position** (`"sidebar"`, `"top"`, or `"hidden"`)

    The position of the navigation menu. If this is `"sidebar"` (default), the navigation widget appears at the top of the sidebar. If this is `"top"`, the navigation appears in the top header of the app. If this is `"hidden"`, the navigation widget is not displayed.

    If there is only one page in `pages`, the navigation will be hidden for any value of `position`.

*   **expanded** (`bool`)

    Whether the navigation menu should be expanded. If this is `False` (default), the navigation menu will be collapsed and will include a button to view more options when there are too many pages to display. If this is `True`, the navigation menu will always be expanded; no button to collapse the menu will be displayed.

    If `st.navigation` changes from `expanded=True` to `expanded=False` on a rerun, the menu will stay expanded and a collapse button will be displayed.

    The parameter is only used when `position="sidebar"`.

### Returns

(`StreamlitPage`)

The current page selected by the user. To run the page, you must use the `.run()` method on it.

### Examples

The following examples show different possible entrypoint files, each named `streamlit_app.py`. An entrypoint file is passed to `streamlit run`. It manages your app's navigation and serves as a router between pages.

**Example 1: Use a callable or Python file as a page**

You can declare pages from callables or file paths. If you pass callables or paths to `st.navigation` as a page-like objects, they are internally converted to `StreamlitPage` objects using `st.Page`. In this case, the page titles, icons, and paths are inferred from the file or callable names.

`page_1.py` (in the same directory as your entrypoint file):

```python
import streamlit as st

st.title("Page 1")
```

`streamlit_app.py`:

```python
import streamlit as st

def page_2():
    st.title("Page 2")

pg = st.navigation(["page_1.py", page_2])
pg.run()
```

**Example 2: Group pages into sections and customize them with `st.Page`**

You can use a dictionary to create sections within your navigation menu. In the following example, each page is similar to Page 1 in Example 1, and all pages are in the same directory. However, you can use Python files from anywhere in your repository. `st.Page` is used to give each page a custom title. For more information, see [st.Page](https://docs.streamlit.io/develop/api-reference/navigation/st.page).

Directory structure:

```
your_repository/
├── create_account.py
├── learn.py
├── manage_account.py
├── streamlit_app.py
└── trial.py
```

`streamlit_app.py`:

```python
import streamlit as st

pages = {
    "Your account": [
        st.Page("create_account.py", title="Create your account"),
        st.Page("manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()
```

**Example 3: Use top navigation**

You can use the `position` parameter to place the navigation at the top of the app. This is useful for apps with a lot of pages because it allows you to create collapsible sections for each group of pages. The following example uses the same directory structure as Example 2 and shows how to create a top navigation menu.

`streamlit_app.py`:

```python
import streamlit as st

pages = {
    "Your account": [
        st.Page("create_account.py", title="Create your account"),
        st.Page("manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()
```

**Example 4: Stateful widgets across multiple pages**

Call widget functions in your entrypoint file when you want a widget to be stateful across pages. Assign keys to your common widgets and access their values through Session State within your pages.

`streamlit_app.py`:

```python
import streamlit as st

def page1():
    st.write(st.session_state.foo)

def page2():
    st.write(st.session_state.bar)

# Widgets shared by all the pages
st.sidebar.selectbox("Foo", ["A", "B", "C"], key="foo")
st.sidebar.checkbox("Bar", key="bar")

pg = st.navigation([page1, page2])
pg.run()
```


Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.
