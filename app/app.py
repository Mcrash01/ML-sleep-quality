import pandas as pd
import streamlit as st
from homepage import *
from data_analysis import *
from ml_models import *

st.title('Sleep Quality Analysis')


display_page = st.sidebar.selectbox('Quelle page souhaitez-vous visiter ?',('HOMEPAGE', 'DATA ANALYSIS', 'ML MODELS'))
# HOMEPAGE STUFF
if display_page == 'HOMEPAGE':
    homepage()
    if st.button('Load Data'):
        df_train = pd.read_csv('./data/Sleep_health_and_lifestyle_dataset.csv')
        st.write("Data Successfully loaded")
        st.dataframe(data=df_train)
# DATA ANALYSIS STUFF
elif display_page == 'DATA ANALYSIS':
    data_analysis()
# ML MODELS STUFF
elif display_page == 'ML MODELS':
    ml_models()



