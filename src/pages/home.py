import streamlit as st
from PIL import Image as imging
def main():
    img = imging.open("x.jpeg")
    st.image(img)
    st.title("Covid-19 DASHBOARD")
    txt = """
    This web application will serve to analyze, visualize, the spread of Covid-19.
    Coronavirus disease 2019 (COVID-19) is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).
    The first known case was identified in Wuhan, China, in December 2019.
    The disease has since spread worldwide, leading to an ongoing pandemic.
    """
    txt
    st.markdown('Symptoms')
    st.markdown(("* Respiratory symptoms\n""* Fever\n""* Cough\n""* Shortness of breath\n"))
    st.markdown("Vaccines")
    st.markdown("Track [here](https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-vaccine-tracker)")