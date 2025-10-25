```markdown
# Execution Flow

[Original URL](https://docs.streamlit.io/develop/api-reference/execution-flow)

By default, Streamlit apps execute the script entirely, but we allow some functionality to handle control flow in your applications.

## Change Execution

[![screenshot](/images/api/dialog.jpg)

#### Modal dialog

Insert a modal dialog that can rerun independently from the rest of the script.

`@st.dialog("Sign up") def email_form(): name = st.text_input("Name") email = st.text_input("Email")`

](/develop/api-reference/execution-flow/st.dialog)[

#### Fragments

Define a fragment to rerun independently from the rest of the script.

`@st.fragment(run_every="10s") def fragment(): df = get_data() st.line_chart(df)`

](/develop/api-reference/execution-flow/st.fragment)[

#### Rerun script

Rerun the script immediately.

`st.rerun()`

](/develop/api-reference/execution-flow/st.rerun)[

#### Stop execution

Stops execution immediately.

`st.stop()`

](/develop/api-reference/execution-flow/st.stop)

## Group Multiple Widgets

By default, Streamlit reruns your script everytime a user interacts with your app. However, sometimes it's a better user experience to wait until a group of related widgets is filled before actually rerunning the script. That's what `st.form` is for!

[

#### Forms

Create a form that batches elements together with a “Submit" button.

`with st.form(key='my_form'): name = st.text_input("Name") email = st.text_input("Email") st.form_submit_button("Sign up")`

](/develop/api-reference/execution-flow/st.form)[

#### Form submit button

Display a form submit button.

`with st.form(key='my_form'): name = st.text_input("Name") email = st.text_input("Email") st.form_submit_button("Sign up")`

](/develop/api-reference/execution-flow/st.form_submit_button)
```

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

---