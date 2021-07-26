import streamlit as st
from dashes.home import main as hm
from dashes.data import main as dt
from dashes.dashboard import main as dash
from dashes.about import main as abt
from background import set_png_as_page_bg
st.set_page_config(
        page_title="Covid-19 Dashboard",
        page_icon=":Microbe:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
set_png_as_page_bg('ribbons.png')
st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
    unsafe_allow_html=True,
)
query_params = st.experimental_get_query_params()
tabs = {
    "Home": src.pages.home,
    "Data": src.pages.data,
    "Dashboard": src.pages.dashboard,
    "About": src.pages.about
}
if "tab" in query_params:
    active_tab = query_params["tab"][0]
else:
    active_tab = "Home"

if active_tab not in tabs:
    st.experimental_set_query_params(tab="Home")
    active_tab = "Home"

li_items = "".join(
    f"""
    <li class="nav-item">
        <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
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
    hm()
elif active_tab == "About":
   abt.main()
elif active_tab == "Data":
    dt()
elif active_tab == "Dashboard":
    dash()
else:
    st.error("Something has gone terribly wrong.")
