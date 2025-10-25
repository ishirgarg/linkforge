# Navigation and Pages - Streamlit

> Source: [https://docs.streamlit.io/develop/api-reference/navigation](https://docs.streamlit.io/develop/api-reference/navigation)

## Navigation

Configure the available pages in a multipage app.

```python
st.navigation({
    "Your account" : [log_out, settings],
    "Reports" : [overview, usage],
    "Tools" : [search]
})
```

## st.navigation

## Page

Define a page in a multipage app.

```python
home = st.Page( "home.py", title="Home", icon=":material/home:" )
```

## st.page\_link

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="Profile")
```

## st.switch\_page

Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```
