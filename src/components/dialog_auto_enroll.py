import streamlit as st

from src.database.config import supabase
from src.database.db import enroll_student_to_subject


@st.dialog("Join Class")
def auto_enroll_dialog(join_code):

    # Get logged-in student
    student_data = st.session_state.get("student_data")

    if not student_data:
        st.warning("Please login as a student first.")
        return

    # student_data can be a list because create_student()
    # returns Supabase response.data
    if isinstance(student_data, list):
        if not student_data:
            st.error("Student information not found.")
            return

        student_data = student_data[0]

    student_id = student_data.get("student_id")

    if not student_id:
        st.error("Student ID not found.")
        return

    # Clean subject code
    join_code = str(join_code).strip().upper()

    # Find subject
    try:
        response = (
            supabase
            .table("subjects")
            .select("subject_id, name, subject_code")
            .eq("subject_code", join_code)
            .execute()
        )
    except Exception as e:
        st.error("Unable to find the subject.")
        st.error(str(e))
        return

    if not response.data:
        st.error(f"Subject code '{join_code}' was not found.")
        return

    subject = response.data[0]
    subject_id = subject["subject_id"]

    st.write(f"**Subject:** {subject['name']}")
    st.write(f"**Code:** {subject['subject_code']}")

    # Check whether student is already enrolled
    try:
        existing = (
            supabase
            .table("subject_students")
            .select("student_id, subject_id")
            .eq("student_id", student_id)
            .eq("subject_id", subject_id)
            .execute()
        )
    except Exception as e:
        st.error("Unable to check enrollment.")
        st.error(str(e))
        return

    if existing.data:
        st.info("You are already enrolled in this subject.")

        if st.button("Continue", type="primary", width="stretch"):
            st.session_state.pop("join_code", None)
            st.rerun()

        return

    # Enroll student
    if st.button("Join Class", type="primary", width="stretch"):

        try:
            enroll_student_to_subject(
                student_id,
                subject_id
            )

            st.success(
                f"Successfully enrolled in {subject['name']}!"
            )

            # Remove join code so dialog does not appear again
            st.session_state.pop("join_code", None)

            st.rerun()

        except Exception as e:
            st.error("Enrollment failed.")
            st.error(str(e))