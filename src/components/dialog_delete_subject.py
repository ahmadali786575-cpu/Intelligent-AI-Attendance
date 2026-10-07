import streamlit as st
import time

from src.database.db import delete_subject


@st.dialog("Delete Subject")
def delete_subject_dialog(subject_id, subject_name):

    st.markdown(
        f"### Are you sure you want to delete **{subject_name}**?"
    )

    st.write("This action cannot be undone.")

    st.warning(
        "All students enrolled in this subject and their "
        "attendance records will also be deleted."
    )

    st.write("")

    col1, col2 = st.columns(2)

    # ==========================================
    # CANCEL
    # ==========================================

    with col1:

        if st.button(
            "Cancel",
            key=f"cancel_delete_{subject_id}",
            width="stretch"
        ):
            st.session_state.pop("delete_subject_id", None)
            st.rerun()

    # ==========================================
    # DELETE
    # ==========================================

    with col2:

        if st.button(
            "Delete Subject",
            key=f"confirm_delete_{subject_id}",
            type="primary",
            icon=":material/delete:",
            width="stretch"
        ):

            success = delete_subject(subject_id)

            if success:

                st.session_state.pop("delete_subject_id", None)

                st.toast(
                    "Subject deleted successfully!",
                    icon="✅"
                )

                time.sleep(1)

                st.rerun()

            else:

                st.error(
                    "Unable to delete the subject. "
                    "Please try again."
                )