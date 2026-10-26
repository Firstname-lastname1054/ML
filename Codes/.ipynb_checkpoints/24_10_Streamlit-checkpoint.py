import streamlit as st
import pickle
import pandas as pd
import numpy as np

infile = open("wisc_model.pkl", 'rb')
objLoad = pickle.load(infile)

infile.close()

st.title("Breast Cancer")
col1, col2, col3, = st.columns([0.3, 0.3, 0.3])

with col1:
    Clump = st.slider(label="Clump Thickness:",
                      min_value = 1, max_value = 10, step=1)
    UniCell_Size = st.slider(label="Uniformity of Cell Size:",
                      min_value = 1, max_value = 10, step=1)
    Uni_CellShape = st.slider(label="Uniformity of Cell Shape:",
                      min_value = 1, max_value = 10, step=1)

with col2:
    MargAdh = st.slider(label="Marginal Adhesion:",
                      min_value = 1, max_value = 10, step=1)
    SEpith = st.slider(label="Single Epithelial Cell",
                      min_value = 1, max_value = 10, step=1)
    BareN = st.slider(label="Bare Nuclei",
                      min_value = 1, max_value = 10, step=1)

with col3:
    BChromtin = st.slider(label="Bland CHromatin:",
                      min_value = 1, max_value = 10, step=1)
    NoemN = st.slider(label="Normal Nucleoli",
                      min_value = 1, max_value = 10, step=1)
    Mitoses = st.slider(label="Mitoses:",
                      min_value = 1, max_value = 10, step=1)

df = pd.DataFrame({
    'Clump' : [Clump],
    'UniCell_Size' : [UniCell_Size],
    'Uni_CellShape' : [Uni_CellShape],
    'MargAdh':[MargAdh],
    'SEpith':[SEpith],
    'BareN':[BareN],
    'BChromatin':[BChromtin],
    'NoemN' : [NoemN],
    'Mitoses':[Mitoses]
})
pred = objLoad.predict(df)[0]
st.write('Predicted Class : {}' .format(pred))

