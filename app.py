import streamlit as st


def main():

    st.set_page_config(
        page_title="SnapClass - Making Attendance faster using AI",
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )

    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    join_code = st.query_params.get("join-code")

    if join_code:
        st.write("Join code received:", join_code)

    login_type = st.session_state["login_type"]

    if login_type == "teacher":

        from src.screens.teacher_screen import teacher_screen

        teacher_screen()

    elif login_type == "student":

        from src.screens.student_screen import student_screen

        student_screen()

    else:

        from src.screens.home_screen import home_screen

        home_screen()


if __name__ == "__main__":
    main()