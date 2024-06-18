import streamlit as st
import shelve
from acd_stream import get_course_outline, modify_course_outline, gen_full_course

# Customizing the page configuration
st.set_page_config(
    page_title="Automated Course Content Generator",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Automated Course Development (ACD) Model 🤖")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

# Load chat history from shelve file
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])

# Example of using columns for advanced layouts
col1, col2 = st.columns(2)

col1, col_divider, col2 = st.columns([3.0, 0.1, 7.0])

with col1:
    st.header("Course Details 📋")
    
    # Function to create mandatory label with red asterisk
    def mandatory_label(label):
        return f"{label} <span style='color:red;'>*</span>"

    # Interactive widgets for course details
    st.markdown(mandatory_label("Course Name"), unsafe_allow_html=True)
    course_name = st.text_input("Enter the name of the course you'd like to generate")
    
    target_audience_edu_level = st.selectbox(
        "Target Audience Edu Level",
        ["N/A", "Primary", "High School", "Diploma", "Bachelors", "Masters"]
    )
    
    difficulty_level = st.radio(
        "Course Difficulty Level",
        ["N/A", "Beginner", "Intermediate", "Advanced"]
    )
    
    st.markdown(mandatory_label("No. of Modules"), unsafe_allow_html=True)
    num_modules = st.slider(
        "Use the slider to choose the number of modules (Max. 15)",
        min_value=1, max_value=15,
    )
    
    course_duration = st.text_input("Course Duration")
    course_credit = st.text_input("Course Credit")

    # Save widget states in session_state
    st.session_state.course_name = course_name
    st.session_state.target_audience_edu_level = target_audience_edu_level
    st.session_state.difficulty_level = difficulty_level
    st.session_state.num_modules = num_modules
    st.session_state.course_duration = course_duration
    st.session_state.course_credit = course_credit

    # Check if mandatory fields are filled
    if not course_name:
        st.warning("Please enter the Course Name.")
    if num_modules is None or num_modules < 1:
        st.warning("Please select the Number of Modules.")

    button1, button2 = st.columns([1, 0.8])
    with button1:
        generate_button = st.button("Generate Course Outline", help="Click me to generate course outline!😁")
    with button2:
        if "pdf" in st.session_state:
            new_course_button = st.button("Start a New Course", help="Click me to start a new course!💡")
            if new_course_button:
                st.session_state.course_name = ""
                st.session_state.target_audience_edu_level = ""
                st.session_state.difficulty_level = ""
                st.session_state.num_modules = 1
                st.session_state.course_duration = ""
                st.session_state.course_credit = ""
                st.session_state.pdf = False
                st.experimental_rerun()
                
    
with col2:
    st.header("Generated Course Content 📝")
    # Display the generated content here
    if generate_button and "pdf" not in st.session_state:

        with st.spinner("Generating course outline..."):
            
            course_outline = get_course_outline(course_name, target_audience_edu_level, difficulty_level, num_modules, course_duration, course_credit)

            st.success("Course outline generated successfully!")

            st.session_state['course_outline'] = course_outline
            st.session_state['buttons_visible'] = True

    if 'course_outline' in st.session_state and "pdf" not in st.session_state:
        st.session_state['modifications'] = True

        with st.expander("Course Outline", expanded=True):
            st.write(st.session_state['course_outline'])

            if 'buttons_visible' in st.session_state and st.session_state['buttons_visible']:
                complete_course_button = st.button(
                    "Looks good. Generate complete course!",
                    help="Click here to generate complete course!😍",
                    key="complete_course_button"
                )
                modifications_button = st.button(
                    "Wait! I need to make some modifications.",
                    help="Click here to modify the course outline!🧐",
                    key="modifications_button"
                )

                if modifications_button or st.session_state.get('modifications_pending', False):
                    modifications = st.text_area("Please enter the modifications you'd like to make:", key="modifications_input")
                    submit_modifications = st.button("Submit Modifications", key="submit_modifications")

                    if submit_modifications:
                        st.session_state['course_outline'] = modify_course_outline(
                            st.session_state['course_outline'], modifications
                        )
                        st.session_state['modifications_pending'] = False
                        st.rerun()  # Comment this line to avoid full reload

                    # Keep showing the modifications text area until they are submitted
                    st.session_state['modifications_pending'] = True
  
                if complete_course_button:
                    st.session_state['complete_course'] = True
                    st.session_state['modifications'] = False

        if 'complete_course' in st.session_state and st.session_state['complete_course']:
            with st.spinner("Generating complete course..."):
                gen_full_course(course_name, st.session_state['course_outline'])
                    
    else:
        st.write("Your generated content will appear here.")

# Save chat history after each interaction
save_chat_history(st.session_state.messages)
