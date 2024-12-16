import streamlit as st

# Initialize session state if it doesn't exist
if 'page' not in st.session_state:
    st.session_state.page = 'Page 1'


# Create a sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.selectbox('Select Page', ['Page 1', 'Page 2'])
st.session_state.page = page

# Define page content
if st.session_state.page == 'Page 1':
    st.title('Page 1')
    
    # Text input to modify shared variable
    shared_var = st.text_input('Set Shared Variable', key='z')

    if 'shared_var' not in st.session_state:
        st.session_state.shared_var = 'Initial Value'
    elif st.session_state.z:
        st.session_state.shared_var = st.session_state.z
    
    # Update shared variable only if user entered a new value
    if shared_var :
        st.session_state.shared_var = shared_var 
    
    st.button('Go to Page 2', on_click=lambda: st.experimental_rerun())

elif st.session_state.page == 'Page 2':
    st.title('Page 2')
    
    # Access the shared variable
    st.write('Shared Variable:', st.session_state.shared_var)