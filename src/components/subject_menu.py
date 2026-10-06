import streamlit as st


def subject_menu(
    subject_id,
    subject_name,
    subject_code,
    section
):

    # ==================================================
    # CHECK EDIT MODE
    # ==================================================

    edit_mode = st.session_state.get(
        f"edit_mode_{subject_id}",
        False
    )


    # ==================================================
    # COMMON CSS
    # ==================================================

    st.markdown(
        """
        <style>

        /* ==================================================
           OPTIONS BUTTON
        ================================================== */
        [class*="st-key-options_"],
        [class*="st-key-options_only_"] {
            transform: translateY(-18px) !important;
        }

        [class*="st-key-options_"] button,
        [class*="st-key-options_only_"] button {
            background-color: #4C5D87 !important;
            border-color: #4C5D87 !important;
            color: white !important;
        }

        [class*="st-key-options_"] button:hover,
        [class*="st-key-options_only_"] button:hover {
            background-color: #4752C4 !important;
            border-color: #4752C4 !important;
            color: white !important;
        }

        [class*="st-key-options_"] button svg,
        [class*="st-key-options_only_"] button svg {
            color: white !important;
            fill: white !important;
        }


        /* ==================================================
           POPUP
        ================================================== */

        [data-testid="stPopoverBody"] {
            background-color: #EEF1F7 !important;
            border: none !important;
        }


        /* ==================================================
           POPUP BUTTONS
        ================================================== */

        [data-testid="stPopoverBody"] button {
            background-color: transparent !important;
            border-color: transparent !important;
            color: #000000 !important;
        }

        [data-testid="stPopoverBody"] button p {
            color: #000000 !important;
        }

        [data-testid="stPopoverBody"] button svg {
            color: #000000 !important;
            fill: #000000 !important;
        }

        [data-testid="stPopoverBody"] button:hover {
            background-color: #D5DCEB !important;
            border-color: transparent !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # ==================================================
    # EDIT MODE
    # ONLY SHOW OPTIONS BUTTON
    # ==================================================

    if edit_mode:


        st.button(
            "Options",
            icon=":material/more_vert:",
            width="stretch",
            key=f"options_only_{subject_id}",
            type="secondary"
        )

        return


    # ==================================================
    # NORMAL OPTIONS POPOVER
    # ==================================================

    with st.popover(
        "Options",
        type="secondary",
        icon=":material/more_vert:",
        use_container_width=True,
        key=f"options_{subject_id}"
    ):

        # ==================================================
        # EDIT SUBJECT
        # ==================================================

        if st.button(
            "Edit Subject",
            icon=":material/edit:",
            width="stretch",
            key=f"edit_{subject_id}"
        ):

            st.session_state["editing_subject"] = {
                "subject_id": subject_id,
                "subject_name": subject_name,
                "subject_code": subject_code,
                "section": section
            }

            st.session_state[
                f"edit_mode_{subject_id}"
            ] = True

            st.rerun()


        # ==================================================
        # DELETE SUBJECT
        # ==================================================

        if st.button(
            "Delete Subject",
            icon=":material/delete:",
            width="stretch",
            key=f"delete_{subject_id}"
        ):

            st.session_state[
                f"edit_mode_{subject_id}"
            ] = True

            st.session_state[
                "delete_subject_id"
            ] = subject_id

            st.rerun()


        # ==================================================
        # STUDENT DETAILS
        # ==================================================

        if st.button(
            "Student Details",
            icon=":material/group:",
            width="stretch",
            key=f"students_{subject_id}"
        ):

            st.session_state[
                f"edit_mode_{subject_id}"
            ] = True

            st.session_state[
                "student_details_subject_id"
            ] = subject_id

            st.rerun()