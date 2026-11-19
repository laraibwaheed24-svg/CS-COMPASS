
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CS Compass",
    page_icon="🎓",
    layout="wide"
)

# Application title
st.title("🎓 CS Compass")

st.subheader("Your Computer Science Learning Companion")

st.write(
    "Explore your UET Peshawar BS Computer Science curriculum, "
    "understand difficult concepts, and practice with AI-powered tools."
)

st.divider()

# Sidebar navigation
st.sidebar.title("CS Compass")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "My Curriculum",
        "My Study Materials",
        "AI Study Assistant",
        "Practice & Revision"
    ]
)

# Dashboard
if page == "Dashboard":

    st.header("Welcome to CS Compass 👋")

    st.write(
        "Your complete Computer Science learning journey starts here."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Degree Duration", "4 Years")

    with col2:
        st.metric("Semesters", "8")

    with col3:
        st.metric("Current Semester", "Semester 1")

    st.divider()

    st.subheader("Your Learning Journey")

    st.info(
        "We will begin with Semester 1 and complete each subject "
        "before moving to the next semester."
    )

    st.subheader("Core Subjects")

    subject1, subject2, subject3 = st.columns(3)

    with subject1:
        st.markdown("### Applications of ICT")
        st.caption("CS-101")

    with subject2:
        st.markdown("### Programming Fundamentals")
        st.caption("CS-102")

    with subject3:
        st.markdown("### Discrete Structures")
        st.caption("CS-103")

# Curriculum
elif page == "My Curriculum":

    st.header("My Curriculum")

    st.write("Explore your eight-semester BSCS degree.")

    for semester in range(1, 9):
        with st.expander(f"Semester {semester}"):
            st.write("Curriculum subjects will be added here.")

# Study materials
elif page == "My Study Materials":

    st.header("My Study Materials")

    st.write(
        "Upload lecture PDFs and organize them by subject."
    )

    uploaded_files = st.file_uploader(
        "Upload your PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(f"{len(uploaded_files)} PDF file(s) uploaded.")

        for file in uploaded_files:
            st.write("📄", file.name)

# AI assistant
elif page == "AI Study Assistant":

    st.header("AI Study Assistant")

    st.info(
        "Gemini-powered explanations and document-based "
        "question answering will be implemented in a later phase."
    )

# Practice
elif page == "Practice & Revision":

    st.header("Practice & Revision")

    st.info(
        "Quizzes, solved examples, flashcards and book-based "
        "practice will be added here."
    )

