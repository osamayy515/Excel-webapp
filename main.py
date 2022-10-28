import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2022')
st.subheader('Hope you find it useful')

### --- load dataframe

excel_file = 'Survey_Results.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='B:D', header=3)

df_participants = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='F:G', header=3)

df_participants.dropna(inplace=True)




st.dataframe(df)

pie_chart = px.pie(df_participants, title='Total No. of Participants', values='Participants', names='Departments')

st.plotly_chart(pie_chart)

image = Image.open('images/survey.jpg')

st.image(image, caption='Designed by pch.vector / Freepik',
use_column_width=True)