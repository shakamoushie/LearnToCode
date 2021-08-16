import streamlit as st
from streamlit import caching
import pandas as pd
import altair as alt
from st_aggrid import AgGrid

st.set_page_config(page_title = "Test App", layout = "wide", initial_sidebar_state = "expanded")

# dataframe settings
pd.set_option("display.max_columns", None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# ------------------------------------------------------------------------------------------------------------------------------------------
caching.clear_cache()
df = (pd.read_excel(("./vtmp.xlsx"), "wsdta"))

sidlst = df["Region"].values.tolist()
sidlst = list(set(sidlst))    # rmv dupes
sidlst = [item for item in sidlst if not(pd.isnull(item)) == True]   # rmv NaN from a list
sidlst.sort()
sidlst.insert(0, "")     # insert blank entry to the top of the list

tmpsid = st.selectbox("Choose a Region ID: ", sidlst, index=0)
if tmpsid != "":
    AgGrid(df[(df["Region"] == tmpsid)])

    cht1 = alt.Chart(df[(df["Region"] == tmpsid)])
    cht1 = cht1.mark_line(color = "blue", point = True)
    cht1 = cht1.encode(alt.X("Vaccine", title = "Vaccine"), alt.Y("Units", title = "Vaccine Value"))
    cht1 = cht1.properties(width = 800, height = 300, title = "Reading per Vaccine")
    st.write(cht1)
