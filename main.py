import json

import streamlit as st


def render_main_page() -> None:
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h1>Upload data to train model</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="https://i.kym-cdn.com/photos/images/newsfeed/001/115/760/c37.gif" width="300" />
        </div>
        """,
        unsafe_allow_html=True
    )

    json_input = st.text_area("Enter your JSON here", height=100)

    if st.button("Send"):
        if json_input:
            try:
                parsed_json = json.loads(json_input)
                st.json(parsed_json)
                st.write("Parsed JSON object:")
                st.write(parsed_json)
                print(parsed_json)
            except json.JSONDecodeError:
                st.error("Invalid JSON! Please enter a valid JSON string.")
        else:
            st.error("Please enter JSON data before submitting.")


if __name__ == '__main__':
    render_main_page()
