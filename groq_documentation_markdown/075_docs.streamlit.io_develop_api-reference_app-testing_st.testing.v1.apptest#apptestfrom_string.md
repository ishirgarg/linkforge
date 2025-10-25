Here is the HTML content converted to clean markdown:
### st.testing.v1.AppTest
#### Streamlit Version: 1.50.0
A simulated Streamlit app to check the correctness of displayed elements and outputs.

An instance of AppTest simulates a running Streamlit app. This class provides methods to set up, manipulate, and inspect the app contents via API instead of a browser UI. It can be used to write automated tests of an app in various scenarios. These can then be run using a tool like pytest.

### Initialization
AppTest can be initialized by one of three class methods:
* `st.testing.v1.AppTest.from_file` (recommended)
* `st.testing.v1.AppTest.from_string`
* `st.testing.v1.AppTest.from_function`

Once initialized, Session State and widget values can be updated and the script can be run. Unlike an actual live-running Streamlit app, you need to call AppTest.run() explicitly to re-run the app after changing a widget value. Switching pages also requires an explicit, follow-up call to AppTest.run().

### Methods
#### AppTest.run
Run the script from the current state.
#### AppTest.switch_page
Switch to another page of the app.

### Getting Elements
The main value of `AppTest` is providing an API to programmatically inspect and interact with the elements and widgets produced by a running Streamlit app. Using the `AppTest.<element type>` properties or `AppTest.get()` method returns a collection of all the elements or widgets of the specified type that would have been displayed by running the app.

### Available Elements
* `AppTest.button`: Sequence of all st.button and st.form_submit_button widgets.
* `AppTest.caption`: Sequence of all st.caption elements.
* `AppTest.chat_input`: Sequence of all st.chat_input widgets.
* `AppTest.chat_message`: Sequence of all st.chat_message elements.
* `AppTest.checkbox`: Sequence of all st.checkbox widgets.
* `AppTest.code`: Sequence of all st.code elements.
* `AppTest.color_picker`: Sequence of all st.color_picker widgets.
* `AppTest.columns`: Sequence of all columns within st.columns elements.
* `AppTest.dataframe`: Sequence of all st.dataframe elements.
* `AppTest.date_input`: Sequence of all st.date_input widgets.
* `AppTest.divider`: Sequence of all st.divider elements.
* `AppTest.error`: Sequence of all st.error elements.
* `AppTest.exception`: Sequence of all st.exception elements.
* `AppTest.expander`: Sequence of all st.expander elements.
* `AppTest.header`: Sequence of all st.header elements.
* `AppTest.info`: Sequence of all st.info elements.
* `AppTest.json`: Sequence of all st.json elements.
* `AppTest.latex`: Sequence of all st.latex elements.
* `AppTest.main`: Sequence of elements within the main body of the app.
* `AppTest.markdown`: Sequence of all st.markdown elements.
* `AppTest.metric`: Sequence of all st.metric elements.
* `AppTest.multiselect`: Sequence of all st.multiselect widgets.
* `AppTest.number_input`: Sequence of all st.number_input widgets.
* `AppTest.radio`: Sequence of all st.radio widgets.
* `AppTest.select_slider`: Sequence of all st.select_slider widgets.
* `AppTest.selectbox`: Sequence of all st.selectbox widgets.
* `AppTest.sidebar`: Sequence of all elements within st.sidebar.
* `AppTest.slider`: Sequence of all st.slider widgets.
* `AppTest.subheader`: Sequence of all st.subheader elements.
* `AppTest.success`: Sequence of all st.success elements.
* `AppTest.status`: Sequence of all st.status elements.
* `AppTest.table`: Sequence of all st.table elements.
* `AppTest.tabs`: Sequence of all tabs within st.tabs elements.
* `AppTest.text`: Sequence of all st.text elements.
* `AppTest.text_area`: Sequence of all st.text_area widgets.
* `AppTest.text_input`: Sequence of all st.text_input widgets.
* `AppTest.time_input`: Sequence of all st.time_input widgets.
* `AppTest.title`: Sequence of all st.title elements.
* `AppTest.toast`: Sequence of all st.toast elements.
* `AppTest.toggle`: Sequence of all st.toggle widgets.
* `AppTest.warning`: Sequence of all st.warning elements.

### Previous
[App testing](/develop/api-reference/app-testing)
### Next
[Testing element classes](/develop/api-reference/app-testing/testing-element-classes)