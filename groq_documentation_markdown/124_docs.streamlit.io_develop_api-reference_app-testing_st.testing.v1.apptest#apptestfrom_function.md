# Introduction to AppTest
The `AppTest` class in Streamlit allows you to simulate a running Streamlit app and test its elements and widgets. This is useful for writing automated tests for your app, ensuring it works as expected, and catching any bugs or errors.

## Initializing AppTest
There are three ways to initialize `AppTest`:
1. **From a file**: Use `AppTest.from_file()` to create an instance of `AppTest` from a Python script file.
2. **From a string**: Use `AppTest.from_string()` to create an instance of `AppTest` from a string containing Python code.
3. **From a function**: Use `AppTest.from_function()` to create an instance of `AppTest` from a Python function.

## Running the App
To run the app, use the `AppTest.run()` method. This will execute the app's script and update the app's state.

## Switching Pages
If your app has multiple pages, you can switch between them using the `AppTest.switch_page()` method.

## Getting App Elements
You can get the elements of the app using the `AppTest.get()` method or by accessing the element properties directly, such as `AppTest.button`, `AppTest.checkbox`, etc.

## Element Properties
The following element properties are available:
* `button`: Sequence of all `st.button` and `st.form_submit_button` widgets.
* `caption`: Sequence of all `st.caption` elements.
* `chat_input`: Sequence of all `st.chat_input` widgets.
* `chat_message`: Sequence of all `st.chat_message` elements.
* `checkbox`: Sequence of all `st.checkbox` widgets.
* `code`: Sequence of all `st.code` elements.
* `color_picker`: Sequence of all `st.color_picker` widgets.
* `columns`: Sequence of all columns within `st.columns` elements.
* `dataframe`: Sequence of all `st.dataframe` elements.
* `date_input`: Sequence of all `st.date_input` widgets.
* `divider`: Sequence of all `st.divider` elements.
* `error`: Sequence of all `st.error` elements.
* `exception`: Sequence of all `st.exception` elements.
* `expander`: Sequence of all `st.expander` elements.
* `header`: Sequence of all `st.header` elements.
* `info`: Sequence of all `st.info` elements.
* `json`: Sequence of all `st.json` elements.
* `latex`: Sequence of all `st.latex` elements.
* `main`: Sequence of elements within the main body of the app.
* `markdown`: Sequence of all `st.markdown` elements.
* `metric`: Sequence of all `st.metric` elements.
* `multiselect`: Sequence of all `st.multiselect` widgets.
* `number_input`: Sequence of all `st.number_input` widgets.
* `radio`: Sequence of all `st.radio` widgets.
* `select_slider`: Sequence of all `st.select_slider` widgets.
* `selectbox`: Sequence of all `st.selectbox` widgets.
* `sidebar`: Sequence of all elements within `st.sidebar`.
* `slider`: Sequence of all `st.slider` widgets.
* `status`: Sequence of all `st.status` elements.
* `subheader`: Sequence of all `st.subheader` elements.
* `success`: Sequence of all `st.success` elements.
* `table`: Sequence of all `st.table` elements.
* `tabs`: Sequence of all tabs within `st.tabs` elements.
* `text`: Sequence of all `st.text` elements.
* `text_area`: Sequence of all `st.text_area` widgets.
* `text_input`: Sequence of all `st.text_input` widgets.
* `time_input`: Sequence of all `st.time_input` widgets.
* `title`: Sequence of all `st.title` elements.
* `toast`: Sequence of all `st.toast` elements.
* `toggle`: Sequence of all `st.toggle` widgets.
* `warning`: Sequence of all `st.warning` elements.

These properties allow you to access and interact with the elements of your app, making it easier to write tests and ensure your app works as expected.