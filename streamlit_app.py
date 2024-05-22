import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
fl_data = pd.read_csv('fltanggalperfebsortedbytanggalawal.csv')
qty_data = pd.read_csv('qtylostpertanggal.csv')
lost_products_data = pd.read_csv('lostproductsqty.csv')
fl_produk_data = pd.read_csv('flprodukperfebsortedbyangka.csv')
fl_mesin_data = pd.read_csv('flmesinperfebsortedbyangka.csv')
fl_tanggal_data = pd.read_csv('fltanggalperfebsortedbyangka.csv')

# Preprocess financial loss dataset
fl_data['Date'] = pd.to_datetime(fl_data['Date'])
fl_data['Financial Loss'] = fl_data['Financial Loss'].str.replace(',', '').astype(float)

# Calculate total lost products
total_lost_products = lost_products_data['Qty Lost'].sum()

# Calculate total financial loss
total_financial_loss = fl_data['Financial Loss'].sum()

# Display summary
st.header('Financial Loss Data for February 2024')
st.write(f'Total Lost Products: {total_lost_products}')
st.write(f'Total Financial Loss: Rp{total_financial_loss:,.2f}')

# Add "Home" option
if st.button('Home'):
    st.markdown('[Click here to go to home page](https://22ndmay-dpn5dfogubnbsunxhffucm.streamlit.app/)')

# Plot Time Series for Financial Losses
fig_fl = px.line(fl_data, x='Date', y='Financial Loss', title='Financial Losses')
fig_fl.update_layout(plot_bgcolor='#ffffe0')  # Soft background color (krem)
fig_fl.update_traces(line=dict(color='#00008b'))  # Soft line color (warna biru tua)
st.plotly_chart(fig_fl, use_container_width=True)

# Display Top 5 Lost Products table
st.subheader('Top 5 Lost Products')
top_5_lost_products = lost_products_data.head(5).reset_index(drop=True)
top_5_lost_products.index += 1
st.write(top_5_lost_products)

# Display option for more details on Top 5 Lost Products table
if st.button('Click here for more details', key='lost_products_detail'):
    lost_products_data.index += 1
    st.write(lost_products_data)

# Display Top 5 Financial Losses table by Products
st.subheader('Top 5 Financial Losses by Products')
top_5_fl_produk = fl_produk_data.head(5).reset_index(drop=True)
top_5_fl_produk.index += 1  # Start index from 1
st.write(top_5_fl_produk)

# Display option for more details on Top 5 Financial Losses table by Products
if st.button('Click here for more details (by Products)', key='fl_produk_detail'):
    fl_produk_data.index +=1
    st.write(fl_produk_data)

# Display Top 5 Financial Losses table by Machine
st.subheader('Top 5 Financial Losses by Machine')
top_5_fl_mesin = fl_mesin_data.head(5).reset_index(drop=True)
top_5_fl_mesin.index += 1  # Start index from 1
st.write(top_5_fl_mesin)

# Display option for more details on Top 5 Financial Losses table by Machine
if st.button('Click here for more details (by Machine)', key='fl_mesin_detail'):
    fl_mesin_data.index += 1
    st.write(fl_mesin_data)

# Display Top 5 Financial Losses table by Date
st.subheader('Top 5 Financial Losses by Date')
top_5_fl_tanggal = fl_tanggal_data.head(5).reset_index(drop=True)
top_5_fl_tanggal.index += 1  # Start index from 1
st.write(top_5_fl_tanggal)

# Display option for more details on Top 5 Financial Losses table by Date
if st.button('Click here for more details (by Date)', key='fl_tanggal_detail'):
    fl_tanggal_data.index += 1
    st.write(fl_tanggal_data)