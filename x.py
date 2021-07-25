# Global Choropleth Map of COVID 19 Infections & Casualties
def data_preprocess():
    # Importing libraries
    import pandas as pd
    from src.pages.utils.load_data import load_data
    import numpy as np
    # Importing dataset
    ds = load_data("https://raw.githubusercontent.com/shraddha-an/covid-choro-map/master/WHO-COVID-19-global-data.csv")
    ds = ds.drop(columns = ['WHO_region', 'New_cases', 'New_deaths'])
    cases_df = ds.groupby('Country').max().reset_index()
    cases = cases_df.drop(columns = ['Country_code', 'Cumulative_deaths'])
    deaths = cases_df.drop(columns = ['Country_code', 'Cumulative_cases'])
    return cases,deaths
def figcasesprov():
    from plotly.offline import plot
    import plotly.graph_objects as go
    import plotly.io as pio
    cases,deaths=data_preprocess()
    # 1) Infection Rates
    fig_cases = go.Figure(data = go.Choropleth(locations = cases['Country'],
                                         z = cases['Cumulative_cases'].astype(int),
                                         locationmode = 'country names',
                                         colorscale = 'ylorrd',
                                         colorbar_title = "Infections"))

    fig_cases.update_layout(title_text = 'COVID 19: Global Infections Count',
                      geo = dict(showframe = True,
                               showcoastlines = True,
                               projection_type = 'equirectangular'),

                      annotations = [dict(x = 0.5,
                                        y = 0.1,
                                        text='Source: <a href="https://covid19.who.int/info">\
                                        WHO</a>',
                                        showarrow = False)])
    return fig_cases