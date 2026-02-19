from logging import disable

import streamlit as st

def display_form(form_fields):
    st.title("Autofilled Supplier Form")

    for field in form_fields:
        st.text(field["question_text"])
        st.text_input(
            "Answer",
            value=field.get("value", ""),
            disabled=True,
            key=field["form_question_id"]
        )
        st.caption(f"Status: {field['status']}")
        st.divider()