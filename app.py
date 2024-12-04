import streamlit as st
import streamlit_shadcn_ui as ui
from streamlit_modal import Modal

st.set_page_config(
    page_title="DSI314",
    page_icon="book",
    layout="centered",
    initial_sidebar_state="collapsed",
)

if "show_modal" not in st.session_state:
    st.session_state["show_modal"] = True 

if "selected_faculty" not in st.session_state:
    st.session_state["selected_faculty"] = None 

def toggle_modal():
    st.session_state["show_modal"] = not st.session_state["show_modal"]

modal = Modal(key="Popup", padding=40, max_width=800, title="Choose the faculty")

if st.session_state["show_modal"]:
    with modal.container():
        add_selectbox = st.selectbox(
            "",
            (
                "College of Interdisciplinary Studies",
                "Science and Technology",
                "Sirindhorn International Institute of Technology",
                "College of Innovation",
                "Thammasat School of Engineering",
            ),
        )
        if add_selectbox:
            st.session_state["selected_faculty"] = add_selectbox
            toggle_modal()

if st.session_state["selected_faculty"]:
    st.header("งานนี้พี่ไปไหนต่อ")
    st.write(f"Current faculty: {st.session_state['selected_faculty']}")


# add_selectbox = st.selectbox(
#     "Current Major",
#     ("DSI", "Home phone", "Mobile phone")
# )

# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
