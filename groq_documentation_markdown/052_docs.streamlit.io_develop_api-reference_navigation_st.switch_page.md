Here is the clean markdown version of the provided HTML:

# st.switch_page
Streamlit Version: 1.50.0, 1.49.0, 1.48.0, 1.47.0, 1.46.0, 1.45.0, 1.44.0, 1.43.0, 1.42.0, 1.41.0, 1.40.0, 1.39.0, 1.38.0, 1.37.0, 1.36.0, 1.35.0, 1.34.0, 1.33.0, 1.32.0, 1.31.0, 1.30.0, 1.29.0, 1.28.0, 1.27.0, 1.26.0, 1.25.0, 1.24.0, 1.23.0, 1.22.0

Programmatically switch the current page in a multipage app.

When `st.switch_page` is called, the current page execution stops and the specified page runs as if the user clicked on it in the sidebar navigation. The specified page must be recognized by Streamlit's multipage architecture (your main Python file or a Python file in a `pages/` folder). Arbitrary Python scripts cannot be passed to `st.switch_page`.

## Function signature
```python
st.switch_page(page)
```
### Parameters

* `page` (str, Path, or st.Page): The file path (relative to the main script) or an `st.Page` indicating the page to switch to.

## Example

Consider the following example given this file structure:
```markdown
your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py
```
```python
import streamlit as st

if st.button("Home"):
    st.switch_page("your_app.py")
if st.button("Page 1"):
    st.switch_page("pages/page_1.py")
if st.button("Page 2"):
    st.switch_page("pages/page_2.py")
```
### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Links

* [Home](/)
* [Develop](/develop)
* [API reference](/develop/api-reference)
* [Navigation and pages](/develop/api-reference/navigation)
* [st.switch_page](/develop/api-reference/navigation/st.switch_page)
* [Previous: st.page_link](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link)
* [Next: Execution flow](/develop/api-reference/execution-flow)

### Contact

* [Contact Us](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
* [Community](https://discuss.streamlit.io)
* [GitHub](https://github.com/streamlit)
* [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
* [Twitter](https://twitter.com/streamlit)
* [LinkedIn](https://www.linkedin.com/company/streamlit)
* [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

&copy; 2025 Snowflake Inc.