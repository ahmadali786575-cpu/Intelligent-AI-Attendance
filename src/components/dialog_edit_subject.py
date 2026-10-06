import streamlit as st

from src.database.config import supabase


@st.dialog("Edit Subject")
def edit_subject_dialog(
    subject_id,
    subject_name,
    subject_code,
    section
):

    st.subheader("Edit Subject")

    # ==========================================
    # INPUT FIELDS
    # ==========================================

    new_name = st.text_input(
        "Subject Name",
        value=subject_name,
        key=f"edit_name_{subject_id}"
    )

    new_code = st.text_input(
        "Subject Code",
        value=subject_code,
        key=f"edit_code_{subject_id}"
    )

    new_section = st.text_input(
        "Section",
        value=section,
        key=f"edit_section_{subject_id}"
    )

    col1, col2 = st.columns(2)

    # ==========================================
    # SAVE CHANGES
    # ==========================================

    with col1:

        if st.button(
            "Save Changes",
            type="primary",
            width="stretch",
            icon=":material/save:"
        ):

            # ------------------------------
            # VALIDATION
            # ------------------------------

            if not new_name.strip():

                st.error(
                    "Subject name is required."
                )

                return

            if not new_code.strip():

                st.error(
                    "Subject code is required."
                )

                return

            if not new_section.strip():

                st.error(
                    "Section is required."
                )

                return

            try:

                # ------------------------------
                # UPDATE DATABASE
                # ------------------------------

                supabase.table("subjects").update({

                    "name": new_name.strip(),

                    "subject_code": new_code.strip(),

                    "section": new_section.strip()

                }).eq(
                    "subject_id",
                    subject_id
                ).execute()

                # ------------------------------
                # CLOSE EDIT MODE
                # ------------------------------

                st.session_state.pop(
                    "editing_subject",
                    None
                )

                st.session_state.pop(
                    f"edit_mode_{subject_id}",
                    None
                )

                # ------------------------------
                # SUCCESS MESSAGE
                # ------------------------------

                st.session_state[
                    "subject_success_message"
                ] = "Subject updated successfully!"

                # ------------------------------
                # REFRESH
                # ------------------------------

                st.rerun()

            except Exception as e:

                st.error(
                    f"Failed to update subject: {e}"
                )

    # ==========================================
    # CANCEL
    # ==========================================

    with col2:

        if st.button(
            "Cancel",
            width="stretch",
            icon=":material/close:"
        ):

            # ------------------------------
            # CLOSE EDIT MODE
            # ------------------------------

            st.session_state.pop(
                "editing_subject",
                None
            )
            st.session_state.pop(
                f"edit_mode_{subject_id}",
                None
            )

            # ------------------------------
            # CANCEL MESSAGE
            # ------------------------------

            st.session_state[
                "subject_cancel_message"
            ] = "Edit cancelled."

            # ------------------------------
            # REFRESH
            # ------------------------------

            st.rerun()