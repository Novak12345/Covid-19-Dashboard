import streamlit as st
from datetime import datetime, timedelta
from utils.load_data import load_data
from utils.fetch_url import fetch_url
# from PIL import Image
# from x import figcasesprov
def main():
    from background import set_png_as_page_bg
    set_png_as_page_bg('x.png')
    st.title("Conclusions")
    date = datetime.today()
    df = None
    while True:
        try:
            df = load_data(fetch_url(date))
        except Exception as e:
            date = date - timedelta(days=1)
            continue
        break
    st.subheader("The numbers so far")
    st.markdown("* There are **{}** countries that have been affected by the COVID-19 virus.".format(len(df["Country_Region"].unique())))
    st.markdown("* The virus has affected **{:.2f}M** people and caused the death of **{:.2f}K**.".format(df["Confirmed"].sum()/1000000,
                                                                                                df["Deaths"].sum()/1000))
    h_confirmed = df.groupby("Country_Region").agg({"Confirmed": "sum"}).nlargest(1,"Confirmed")
    st.markdown("* **{}** has the largest number of confirmed cases with **{:.2f}M** confirmed cases.".format(h_confirmed.index.values[0],
                                                                                      h_confirmed["Confirmed"].values[0]/1000000))
    h_deaths = df.groupby("Country_Region").agg({"Deaths": "sum"}).nlargest(1,"Deaths")
    st.markdown("* **{}** has the largest number of deaths with **{:.2f}K** deaths.".format(h_deaths.index.values[0],
                                                                                                      h_deaths["Deaths"].values[0]/1000))
    h_recovered = df.groupby("Country_Region").agg({"Recovered": "sum"}).nlargest(1,"Recovered")
    st.markdown("* **{}** has the largest number of recoveries with **{:.2f}M** recovered.".format(h_recovered.index.values[0],
                                                                                           h_recovered["Recovered"].values[0]/1000000))
