import os
import tkinter as tk
from tkinter import filedialog

import google.generativeai as genai
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

from utils import static_vars


class FileSeparator:
    def __init__(self) -> None:
        st.set_page_config(
            page_title=static_vars.APP_NAME,
            page_icon=static_vars.APP_ICON,
            initial_sidebar_state="collapsed",
        )

    def run(self) -> None:
        self.__display_form()

    def __display_form(self) -> None:
        with st.container():
            st.header(
                "File Separator",
                divider="gray",
            )
            add_vertical_space()
            path, open_path = st.columns([0.8, 0.2])
            with path:
                st.text_input(
                    label="File Path",
                    value=st.session_state.get("folder_path", None),
                )
            with open_path:
                add_vertical_space(2)
                if st.button("Select Folder"):
                    st.session_state.folder_path = self.select_folder()
                    st.rerun()

            st.checkbox(
                label="Rename Files?",
                value=True,
            )
            st.button("Start", on_click=self.execute)

    @staticmethod
    def select_folder():
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory(
            master=root,
            initialdir="D:/",
            title="Please select a directory",
        )
        root.destroy()
        return folder_path

    def execute(self):
        st.session_state.files_list = os.listdir(st.session_state.folder_path)
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        model = genai.GenerativeModel("gemini-pro")
        for file_name in st.session_state.files_list:
            response = model.generate_content(
                f"""{file_name}
    find name of series or movie from file name
    answer should be directly given with movie/series name nothing else"""
            )
            print(response.text)


if __name__ == "__main__":
    app = FileSeparator()
    app.run()
