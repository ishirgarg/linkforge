```markdown
# Navigation and Pages

[Original URL](https://docs.streamlit.io/develop/api-reference/navigation)

Configure the available pages in a multipage app.

#### Navigation

[![screenshot](/images/api/navigation.jpg)](/develop/api-reference/navigation/st.navigation)

```python
st.navigation({
    "Your account": [log_out, settings],
    "Reports": [overview, usage],
    "Tools": [search]
})
```

#### Page

[![screenshot](/images/api/page.jpg)](/develop/api-reference/navigation/st.page)

Define a page in a multipage app.

```python
home = st.Page("home.py", title="Home", icon=":material/home:")
```

#### Page link

[![screenshot](/images/api/page_link.jpg)](/develop/api-reference/widgets/st.page_link)

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="Profile")
```

#### Switch page

Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```
```