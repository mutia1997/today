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

# Preprocess quantity lost dataset
qty_data['Date'] = pd.to_datetime(qty_data['Date'])

# Define color options
color_options = {
    'Black': '#000000',
    'White': '#ffffff',
    'Red': '#ff0000',
    'Green': '#008000',
    'Blue': '#0000ff',
    'Yellow': '#ffff00',
    'Purple': '#800080',
    'Orange': '#ffa500',
    'Cyan': '#00ffff',
    'Pink': '#ffc0cb'
}

# Select background color
background_color = st.sidebar.selectbox('Select background color:', options=list(color_options.keys()))

# Select line color
line_color = st.sidebar.selectbox('Select line color:', options=list(color_options.keys()))

# Plot Time Series for Financial Losses
fig_fl = px.line(fl_data, x='Date', y='Financial Loss', title='Financial Losses')
fig_fl.update_layout(plot_bgcolor=color_options[background_color])
fig_fl.update_traces(line=dict(color=color_options[line_color]))
st.plotly_chart(fig_fl, use_container_width=True)

# Plot Time Series for Quantity Lost
fig_qty = px.line(qty_data, x='Date', y='Qty Lost', title='Quantity Lost')
fig_qty.update_layout(plot_bgcolor=color_options[background_color])
fig_qty.update_traces(line=dict(color=color_options[line_color]))
st.plotly_chart(fig_qty, use_container_width=True)

# Display Top 5 Lost Products table
st.subheader('Top 5 Lost Products')
top_5_lost_products = lost_products_data.head(5).reset_index(drop=True)
top_5_lost_products.index += 1
st.write(top_5_lost_products)

# Display option for more detail on Top 5 Lost Products table
if st.button('Click here for more detail'):
    st.write(lost_products_data)

# Display Top 5 Financial Losses table by Products
st.subheader('Top 5 Financial Losses by Products')
top_5_fl_produk = fl_produk_data.head(5).reset_index(drop=True)
top_5_fl_produk.index += 1  # Start index from 1
st.write(top_5_fl_produk)

# Display option for more detail on Top 5 Financial Losses table by Products
if st.button('Click here for more detail (by Products)'):
    st.write(fl_produk_data)

# Display Top 5 Financial Losses table by Machine
st.subheader('Top 5 Financial Losses by Machine')
top_5_fl_mesin = fl_mesin_data.head(5).reset_index(drop=True)
top_5_fl_mesin.index += 1  # Start index from 1
st.write(top_5_fl_mesin)

# Display option for more detail on Top 5 Financial Losses table by Machine
if st.button('Click here for more detail (by Machine)'):
    st.write(fl_mesin_data)

# Display Top 5 Financial Losses table by Date
st.subheader('Top 5 Financial Losses by Date')
top_5_fl_tanggal = fl_tanggal_data.head(5).reset_index(drop=True)
top_5_fl_tanggal.index += 1  # Start index from 1
st.write(top_5_fl_tanggal)

# Display option for more detail on Top 5 Financial Losses table by Date
if st.button('Click here for more detail (by Date)'):
    st.write(fl_tanggal_data) 