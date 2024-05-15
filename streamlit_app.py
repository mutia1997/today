import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
fltanggalperfebsortedbytanggalawal = pd.read_csv('fltanggalperfebsortedbytanggalawal.csv')
qtylostpertanggal = pd.read_csv('qtylostpertanggal.csv')
lostproductsqty = pd.read_csv('lostproductsqty.csv')
flprodukperfebsortedbyhuruf = pd.read_csv('flprodukperfebsortedbyhuruf.csv')
flmesinperfebsortedbyangka = pd.read_csv('flmesinperfebsortedbyangka.csv')
fltanggalperfebsortedbyangka = pd.read_csv('fltanggalperfebsortedbyangka.csv')

# Preprocess data
fltanggalperfebsortedbytanggalawal['Date'] = pd.to_datetime(fltanggalperfebsortedbytanggalawal['Date'])
fltanggalperfebsortedbytanggalawal['Financial Loss'] = fltanggalperfebsortedbytanggalawal['Financial Loss'].str.replace(',', '').astype(float)

qtylostpertanggal['Date'] = pd.to_datetime(qtylostpertanggal['Date'])

# Set Dashboard Title
st.title('Dashboard for February')

# Time Series plot for Financial Losses
st.subheader('Financial Losses Time Series')
fig_fl = px.line(fltanggalperfebsortedbytanggalawal, x='Date', y='Financial Loss', title='Financial Losses')
st.plotly_chart(fig_fl)

# Time Series plot for Quantity Lost
st.subheader('Quantity Lost Time Series')
fig_qty = px.line(qtylostpertanggal, x='Date', y='Qty Lost', title='Quantity Lost')
st.plotly_chart(fig_qty)

# Top 5 Lost Products table
st.subheader('Top 5 Lost Products')
top5_lost_products = lostproductsqty.head(5)
st.write(top5_lost_products)
if st.button('Click here for more detail'):
    st.write(lostproductsqty)

# Top 5 Financial Losses table
st.subheader('Top 5 Financial Losses')
st.write('By Products:')
top5_fl_by_products = flprodukperfebsortedbyhuruf.head(5)
st.write(top5_fl_by_products)
if st.button('Click here for more detail (By Products)'):
    st.write(flprodukperfebsortedbyhuruf)

st.write('By Machine:')
top5_fl_by_machine = flmesinperfebsortedbyangka.head(5)
st.write(top5_fl_by_machine)
if st.button('Click here for more detail (By Machine)'):
    st.write(flmesinperfebsortedbyangka)

st.write('By Date:')
top5_fl_by_date = fltanggalperfebsortedbyangka.head(5)
st.write(top5_fl_by_date)
if st.button('Click here for more detail (By Date)'):
    st.write(fltanggalperfebsortedbyangka) 