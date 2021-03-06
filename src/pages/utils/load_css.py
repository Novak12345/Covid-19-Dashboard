import streamlit as st


def local_css():
    """
    Function loads the css stylesheet
    :param file_name: str
    :return: None
    """
    stylesheet="""
    highlight {
  border-radius: 0.4rem;
  color: white;
  padding: 0.5rem;
  margin-bottom: 1rem;
  padding-right: 2rem;
}
.bold {
  padding-left: 1rem;
  font-weight: 700;
}
.blue {
  background-color: #1F77B4;
}
.orange {
  background-color: #FF7F0E;
}
.green {
  background-color: #2CA02C;
}
.red {
  background-color: #D62728;
}
span.highlight.blue{
    margin: 0px 40px 40px 120px;
    display: inline-block;
}
span.highlight.red{
    margin: 0px 40px 40px 120px;
    display: inline-block;
}
span.highlight.green{
    margin: 0px 40px 40px 40px;
    display: inline-block;
}
span.highlight.orange{
    margin: 0px 40px 40px 80px;
    display: inline-block;
}
    """
    st.markdown("<style>{}</style>".format(stylesheet), unsafe_allow_html=True)
