# st.rerun

**URL:** https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun

Rerun the script immediately.

When `st.rerun()` is called, Streamlit halts the current script run and executes no further statements. Streamlit immediately queues the script to rerun.

When using `st.rerun` in a fragment, you can scope the rerun to the fragment. However, if a fragment is running as part of a full-app rerun, a fragment-scoped rerun is not allowed.

## Function signature

[Source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/commands/execution_control.py#L102)

```python
st.rerun(scope="app")
```

### Parameters

*   **scope** (`"app"` or `"fragment"`)
    Specifies what part of the app should rerun. If `scope` is `"app"` (default), the full app reruns. If `scope` is `"fragment"`, Streamlit only reruns the fragment from which this command is called.

    Setting `scope="fragment"` is only valid inside a fragment during a fragment rerun. If `st.rerun(scope="fragment")` is called during a full-app rerun or outside of a fragment, Streamlit will raise a `StreamlitAPIException`.

## Caveats for `st.rerun`

`st.rerun` is one of the tools to control the logic of your app. While it is great for prototyping, there can be adverse side effects:

*   Additional script runs may be inefficient and slower.
*   Excessive reruns may complicate your app's logic and be harder to follow.
*   If misused, infinite looping may crash your app.

In many cases where `st.rerun` works, [callbacks](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state) may be a cleaner alternative. [Containers](/develop/api-reference/layout) may also be helpful.

## A simple example in three variations

### Using `st.rerun` to update an earlier header

```python
import streamlit as st

if "value" not in st.session_state:
    st.session_state.value = "Title"

##### Option using st.rerun #####
st.header(st.session_state.value)

if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()
```

### Using a callback to update an earlier header

```python
##### Option using a callback #####
st.header(st.session_state.value)

def update_value():
    st.session_state.value = "Bar"

st.button("Bar", on_click=update_value)
```

### Using containers to update an earlier header

```python
##### Option using a container #####
container = st.container()

if st.button("Baz"):
    st.session_state.value = "Baz"

container.header(st.session_state.value)
```

## Conclusion

The `st.rerun()` function is a powerful tool for controlling the execution flow of your Streamlit applications. By understanding its behavior and when to use it, you can create more dynamic and responsive user interfaces. Remember to use it judiciously to avoid unintended consequences and ensure a smooth user experience.

---

### Further Resources

*   **Streamlit Forums:** [https://discuss.streamlit.io](https://discuss.streamlit.io)
*   **Contact Us:** [mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20](mailto:hello@streamlit.io?subject=Contact%20from%20documentation%20)
*   **Community:** [https://discuss.streamlit.io](https://discuss.streamlit.io)

---

### Connect with Streamlit

*   [GitHub](https://github.com/streamlit)
*   [YouTube](https://www.youtube.com/channel/UC3LD42rjj-Owtxsa6PwGU5Q)
*   [Twitter](https://twitter.com/streamlit)
*   [LinkedIn](https://www.linkedin.com/company/streamlit)
*   [Newsletter](https://info.snowflake.com/streamlit-newsletter-sign-up.html)

---

© 2025 Snowflake Inc.
[Cookie policy](https://www.snowflake.com/legal/cookie-policy/)