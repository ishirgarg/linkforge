```markdown
# st.stop - Streamlit

> **Reference:** [https://docs.streamlit.io/develop/api-reference/execution-flow/st.stop](https://docs.streamlit.io/develop/api-reference/execution-flow/st.stop)

## `st.stop`

Stops execution immediately.

Streamlit will not run any statements after `st.stop()`. We recommend rendering a message to explain why the script has stopped.

### Function signature

```python
st.stop()
```

[Source code](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/commands/execution_control.py#L34)

### Example

```python
import streamlit as st

name = st.text_input("Name")
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success("Thank you for inputting a name.")
```

---

**Previous:** [`st.rerun`](/develop/api-reference/execution-flow/st.rerun)
**Next:** [`st.experimental_rerun`](/develop/api-reference/execution-flow/st.experimental_rerun)
```
