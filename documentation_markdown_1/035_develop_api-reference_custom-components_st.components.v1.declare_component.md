# st.components.v1.declare_component

**Original URL:** https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.declare_component

Create a custom component and register it if there is a ScriptRunContext.

The component is not registered when there is no ScriptRunContext. This can happen when a CustomComponent is executed as standalone command (e.g. for testing).

To use this function, import it from the `streamlit.components.v1` module.

**Warning**
Using `st.components.v1.declare_component` directly (instead of importing its module) is deprecated and will be disallowed in a later version.

## Function signature

[View st.declare_component source code on GitHub](https://github.com/streamlit/streamlit/blob/1.50.0/lib/streamlit/components/v1/component_registry.py#L53)

```python
st.components.v1.declare_component(name, path=None, url=None)
```

## Parameters

*   **name** (`str`)
    A short, descriptive name for the component, like "slider".

*   **path** (`str`, `Path`, or `None`)
    The path to serve the component's frontend files from. The path should be absolute. If `path` is `None` (default), Streamlit will serve the component from the location in `url`. Either `path` or `url` must be specified. If both are specified, then `url` will take precedence.

*   **url** (`str` or `None`)
    The URL that the component is served from. If `url` is `None` (default), Streamlit will serve the component from the location in `path`. Either `path` or `url` must be specified. If both are specified, then `url` will take precedence.

## Returns

(`CustomComponent`)
A `CustomComponent` that can be called like a function. Calling the component will create a new instance of the component in the Streamlit app.