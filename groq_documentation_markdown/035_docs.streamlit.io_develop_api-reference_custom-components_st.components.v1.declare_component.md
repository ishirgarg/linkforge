## st.components.v1.declare_component
### Overview
Create a custom component and register it if there is a ScriptRunContext.

The component is not registered when there is no ScriptRunContext. This can happen when a CustomComponent is executed as standalone command (e.g. for testing).

### Warning
Using st.components.v1.declare_component directly (instead of importing its module) is deprecated and will be disallowed in a later version.

### Function Signature
```python
st.components.v1.declare_component(name, path=None, url=None)
```

### Parameters
* `name` (str): A short, descriptive name for the component, like "slider".
* `path` (str, Path, or None): The path to serve the component's frontend files from. The path should be absolute. If path is None (default), Streamlit will serve the component from the location in url. Either path or url must be specified. If both are specified, then url will take precedence.
* `url` (str or None): The URL that the component is served from. If url is None (default), Streamlit will serve the component from the location in path. Either path or url must be specified. If both are specified, then url will take precedence.

### Returns
* `(CustomComponent)`: A CustomComponent that can be called like a function. Calling the component will create a new instance of the component in the Streamlit app.

### Example Use Cases
To use this function, import it from the streamlit.components.v1 module.

### Still have questions?
Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

### Version History
* Version 1.50.0
* Version 1.49.0
* Version 1.48.0
* Version 1.47.0
* Version 1.46.0
* Version 1.45.0
* Version 1.44.0
* Version 1.43.0
* Version 1.42.0
* Version 1.41.0
* Version 1.40.0
* Version 1.39.0
* Version 1.38.0
* Version 1.37.0
* Version 1.36.0
* Version 1.35.0
* Version 1.34.0
* Version 1.33.0
* Version 1.32.0
* Version 1.31.0
* Version 1.30.0
* Version 1.29.0
* Version 1.28.0
* Version 1.27.0
* Version 1.26.0
* Version 1.25.0
* Version 1.24.0
* Version 1.23.0
* Version 1.22.0

### Related Topics
* [Custom components](/develop/api-reference/custom-components)
* [st.components.v1.html](/develop/api-reference/custom-components/st.components.v1.html)