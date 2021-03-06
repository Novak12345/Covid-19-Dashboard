import streamlit as st
import os
import webbrowser
import src.pages.home
import src.pages.data
import src.pages.dashboard
import src.pages.conclusions
from background import set_png_as_page_bg
st.set_page_config(
        page_title="Covid-19 Dashboard",
        page_icon=":microscope:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
set_png_as_page_bg('ribbons.png')
STREAMLIT_URL = os.getenv("STREAMLIT_URL", "/")
st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
query_params = st.experimental_get_query_params()
tabs = [
    "Home",
    "Data",
    "Dashboard",
    "Conclusions"
]
if "tab" in query_params:
    active_tab = query_params["tab"][0]
else:
    active_tab = "Data"

if active_tab not in tabs:
    st.experimental_set_query_params(tab="Data")
    active_tab = "Data"

li_items = "".join(
    f"""
    <li class="nav-item">
        <a class="nav-link{' active' if t==active_tab else ''}" href="{STREAMLIT_URL}?tab={t}">{t}</a>
    </li>
    """
    for t in tabs
)
tabs_html = f"""
    <ul class="nav nav-tabs">
    {li_items}
    </ul>
"""

st.markdown(tabs_html, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if active_tab == "Home":
    webbrowser.open("https://share.streamlit.io/novak12345/covid-19-dashboard/main/app.py")
elif active_tab == "Conclusions":
    webbrowser.open("https://share.streamlit.io/novak12345/covid-19-dashboard/main/conclusions_page.py")
elif active_tab == "Data":
    src.pages.data.main()
elif active_tab == "Dashboard":
    webbrowser.open("https://share.streamlit.io/novak12345/covid-19-dashboard/main/dashboard_page.py")
else:
    st.error("Something has gone terribly wrong.")
