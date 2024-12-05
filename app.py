import streamlit as st

st.set_page_config(
    page_title="Faculty Selector",
    page_icon="book",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Faculty information
faculty_data = {
    "College of Interdisciplinary Studies": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/19/%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A5%E0%B8%B1%E0%B8%A2%E0%B8%AA%E0%B8%AB%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3.jpg",  # Replace with actual image links
        "website": "https://cis.tu.ac.th/cis-eng",
    },
    "Science and Technology": {
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZdRQej9m6Tlx0KGZaCzNXUqrDsOIWqQsZVA&s",
        "website": "https://sci.tu.ac.th/",
    },
    "Sirindhorn International Institute of Technology": {
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjLQIlqpmsRo9UzpR7ypkwqokP-kUt7bFIIA&s",
        "website": "https://www.siit.tu.ac.th/",
    },
    "College of Innovation": {
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT95Jv2GVzes_Q4AMgJ_175P0HKE3Ufy6g5QA&s",
        "website": "https://www.citu.tu.ac.th/eng/",
    },
    "Thammasat School of Engineering": {
        "image": "https://yt3.googleusercontent.com/ytc/AIdro_mc0QZyRM4AVHG72dReblab2bmtArgkDErS_FHewIoS4jY=s900-c-k-c0x00ffffff-no-rj",
        "website": "https://en.engr.tu.ac.th/",
    },
}

# Sidebar: Two dropdowns for faculty selection
st.sidebar.header("Select Faculties")
faculty_1 = st.sidebar.selectbox("Choose Faculty 1:", list(faculty_data.keys()), key="faculty_1")
faculty_2 = st.sidebar.selectbox("Choose Faculty 2:", list(faculty_data.keys()), key="faculty_2")

# Header
st.title("Thammasat University Faculties")
st.write("Explore the faculties below by clicking on their respective websites.")

# Split faculties into two groups for layout
faculties_top = list(faculty_data.items())[:3]  # First 3 faculties
faculties_bottom = list(faculty_data.items())[3:]  # Remaining 2 faculties

# CSS for uniform box and image sizes
st.markdown(
    """
    <style>
    .faculty-box {
        border: 2px solid #d9d9d9;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        width: 250px; /* Fixed width for uniform box size */
        height: 350px; /* Fixed height for uniform box size */
        display: inline-block;
        vertical-align: top;
    }
    .faculty-image {
        border-radius: 10px;
        width: 200px; /* Fixed width for uniform image size */
        height: 150px; /* Fixed height for uniform image size */
        object-fit: cover; /* Ensures images maintain aspect ratio */
        margin-bottom: 10px;
    }
    h4 {
        margin-top: 10px;
        font-size: 16px;
        color: #333;
    }
    a {
        text-decoration: none;
        color: #007BFF;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display faculties in consistent boxes
cols = st.columns(3)
for i, (faculty, data) in enumerate(faculty_data.items()):
    with cols[i % 3]:  # Ensure wrapping after every 3 items
        st.markdown(
            f"""
            <div class="faculty-box">
                <img src="{data['image']}" alt="{faculty}" class="faculty-image" />
                <h4>{faculty}</h4>
                <a href="{data['website']}" target="_blank">Visit {faculty} Website</a>
            </div>
            """,
            unsafe_allow_html=True,
        )