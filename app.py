import streamlit as st
import src.pages.home
import src.pages.data
import src.pages.dashboard
import src.pages.about


PAGES = {
    "Home": src.pages.home,
    "Data": src.pages.data,
    "Dashboard": src.pages.dashboard,
    "About": src.pages.about
}

def main():
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Navigate", list(PAGES.keys()))
    PAGES[choice].main()
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by Arohan Arora. You can learn more about me at
        https://sites.google.com/view/arohan/.
        """
    )

if __name__ == "__main__":
    main()