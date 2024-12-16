import streamlit as st
import ast 
import pandas as pd
import re

df = pd.read_csv("final_1.csv",usecols=["code","description","faculty","valid_pairs1","valid_pairs2","valid_pairs3"])

# Page Configuration
st.set_page_config(
    page_title="Faculty Selector",
    page_icon="book",
    layout="wide",
    initial_sidebar_state="auto",
)

# Initialize session state variables
if "page" not in st.session_state:
    st.session_state.page = "home"


# Faculty Data
faculty_data = {
    "College of Interdisciplinary Studies": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/19/%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A5%E0%B8%B1%E0%B8%A2%E0%B8%AA%E0%B8%AB%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3.jpg",
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

# Handle Query Params for Navigation
# query_params = st.query_params
# if "page" in query_params:
#     st.session_state["page"] = query_params["page"]

# Page Logic
if st.session_state["page"] == "home":
    list_sub = list(faculty_data.keys())
    list_sub.append(" ")
    list_sub = list_sub[::-1]
    # Main Page
    st.title("Thammasat University Faculties")
    st.write("Explore the faculties below by clicking on their respective websites.")

    # Sidebar for Faculty Selection
    st.sidebar.header("Faculty Selection")
    faculty_1 = st.sidebar.selectbox(
        "Choose your current faculty",
        list_sub,
        key="faculty_1",
    )
    faculty_2 = st.sidebar.selectbox(
        "Choose your interest faculty",
        list_sub,
        key="faculty_2",

    )

    # Button to proceed to the results page
    if faculty_2 and faculty_1 in faculty_data:
        # st.query_params.update(page="results")
        if "faculty_1" not in st.session_state:
            st.session_state.faculty_1 = faculty_1
        
        if "faculty_2" not in st.session_state:
            st.session_state.faculty_2 = faculty_2
        st.session_state["page"] = "results"

    # Display faculties
    cols = st.columns(3)
    for i, (faculty, data) in enumerate(faculty_data.items()):
        with cols[i % 3]:
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

elif st.session_state["page"] == "results":
    # Results Page
    # st.title("Selected Faculties")
    # st.subheader("Your Selection:")
    # st.write(f"**Current Faculty:** {st.session_state.faculty_1}")
    # st.write(f"**Interest Faculty:** {st.session_state.faculty_2}")

    dict_transform = {
        "College of Interdisciplinary Studies" : "cis",
        "Science and Technology" : "sci",
        "Sirindhorn International Institute of Technology" : "si",
        "College of Innovation" : "inno",
        "Thammasat School of Engineering" : "eng"
    }

    st.session_state.faculty_1 = dict_transform.get(st.session_state.faculty_1, "Unknown")
    st.session_state.faculty_2 = dict_transform.get(st.session_state.faculty_2, "Unknown")
    print(st.session_state.faculty_1,st.session_state.faculty_2)

    filtered_row = df[df["faculty"] == st.session_state["faculty_1"]]
    filtered_row2 = df[df["faculty"] == st.session_state["faculty_2"]]
    # st.write(filtered_row)

    matching_rows_curt = filtered_row[filtered_row['code'].apply(lambda x: any(x in sublist for sublist in filtered_row2['valid_pairs1']))]
    filtered_row2['matches'] = filtered_row2['valid_pairs1'].apply(lambda x: any(code in x for code in filtered_row['code']))
    filtered_row2 = filtered_row2[filtered_row2['matches'] == True]
    
    print(matching_rows_curt)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(filtered_row2)

    size = len(matching_rows_curt)
    rows_needed = (size + 2) // 3  

    rows = []
    for _ in range(rows_needed):
        rows.append(st.columns(3))

    index = 0  
    for row in rows:
        for col in row:
            if index < size:  

                item = matching_rows_curt.iloc[index]

                with col:
                    # st.container(border=True, height=120)
                    
                    cuurent_code = item["code"]                                                         #วิชาปัจจุบัน
                    
                    valid_pairs1 = item["valid_pairs1"]                                                 
                    if isinstance(valid_pairs1, str):
                        valid_pairs1 = ast.literal_eval(valid_pairs1) 
                    filtered = filtered_row2[filtered_row2['code'].isin(valid_pairs1)]


                    filtered_column_code = filtered['code']
                    print(filtered_column_code)
                    print(type(filtered_column_code))
                    pattern = r'\b[a-z]{2,3}\d{3}\b'
                    matches = filtered_column_code.apply(lambda x: re.findall(pattern, x) if isinstance(x, str) else [])
                    text = ": "
                    
                    matches_str = "; ".join([", ".join(match) for match in matches])                    #วิชาที่เทียบโอน
                    text_2 = cuurent_code + " : " + matches_str                                         #วิชาปัจจุบัน ที่เทียบโอน
                    
                    
                    st.subheader(text_2)
                    st.write(f"**Description:** {item['description']}")                                 #desc ของวิชาที่แรก
                    st.write(f"**Description:** {filtered['description'].iloc[0]}")                     #desc ของวิชาที่สอง
                    # st.write(f"**Faculty:** {item['faculty']}")
                index += 1



    # matching_rows_current = filtered_row2[common_values]
    # st.write("Matching Rows:")
    # st.write(matching_rows_current)
    


    # Faculty Details
    # if faculty_1 and faculty_1 in faculty_data:
    # data = faculty_data[st.session_state.faculty_1]
    # st.markdown(
    #     f"""
    #     <div class="faculty-box">
    #         <img src="{data['image']}" alt="{st.session_state.faculty_1}" class="faculty-image" />
    #         <h4>{st.session_state.faculty_1}</h4>
    #         <a href="{data['website']}" target="_blank">Visit {st.session_state.faculty_1} Website</a>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # # if faculty_2 and faculty_2 in faculty_data:
    # data = faculty_data[st.session_state.faculty_2]
    # st.markdown(
    #     f"""
    #     <div class="faculty-box">
    #         <img src="{data['image']}" alt="{st.session_state.faculty_2}" class="faculty-image" />
    #         <h4>{st.session_state.faculty_2}</h4>
    #         <a href="{data['website']}" target="_blank">Visit {st.session_state.faculty_2} Website</a>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # Back to Home Button
    # if st.button("Go Back"):
    #     st.session_state["page"] = "home"
        # st.query_params.update(page="home")
    

