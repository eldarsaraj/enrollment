import streamlit as st
import pandas as pd

st.set_page_config(page_title='College Enrollment in the US, 2003-2021',
                   page_icon=':school:', layout="centered", initial_sidebar_state="auto",
                   menu_items=None)

st.title('College Enrollment in the US, 2003-2021')

df = pd.read_csv('enrollment.csv')

st.markdown('### Data')

st.dataframe(df[['Type', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
          '2015', '2016', '2017', '2018', '2019', '2020', '2021']])


st.markdown('### Charts')

years = ('2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
          '2015', '2016', '2017', '2018', '2019', '2020', '2021')

options = st.selectbox(label='Select a year', options=years)
st.bar_chart(data=df, x='Type', y=options)

df2 = pd.pivot_table(df, columns='Type', values=['2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
          '2015', '2016', '2017', '2018', '2019', '2020', '2021'])

colleges = ('Overall', 'All 4-year Institutions', 'All 2-year Institutions', 'All Public Institutions', 'All Private not-for-profit Institutions',
            'All Private for-profit Institutions')

options2 = st.selectbox(label='Select a type of college', options=colleges)

st.line_chart(df2[options2])

