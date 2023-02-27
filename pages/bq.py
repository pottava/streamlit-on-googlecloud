import pandas as pd
import streamlit as st
from google.cloud import bigquery

import firebase


@st.cache_resource()
def bq():
    client = bigquery.Client()
    return client


@st.cache_data(ttl=60 * 10)
def query(sql) -> pd.DataFrame:
    return bq().query(sql).to_dataframe()


def index():
    if not firebase.refresh():
        st.experimental_rerun()
        return

    st.subheader("Open Source Insights")
    sql = """
    SELECT p.System, License, COUNT(DISTINCT p.Name) AS Packages
    FROM `bigquery-public-data.deps_dev_v1.PackageVersionsLatest` AS p,
         p.Licenses AS License
    GROUP BY System, License ORDER BY Packages DESC LIMIT 10
    """
    st.dataframe(query(sql))


if "user" not in st.session_state:
    st.text("左のメニュー [home] からログインしてください")
else:
    index()
