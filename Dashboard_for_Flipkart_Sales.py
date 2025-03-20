import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Upload CSV file
#st.sidebar.title("Upload CSV File")
#uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

#if uploaded_file:
   # df = pd.read_csv(uploaded_file, parse_dates=['OrderDate'])  # Ensure OrderDate is parsed correctly
    #st.write("### Sales Data Preview")
    #st.dataframe(df.head())  # Display the first few rows

    #Read csv filr

df = pd.read_csv('flipkart_sales.csv')

#Display data

st.write(df)

    # Sidebar Filters
st.sidebar.title("Filter Data")

    # Filter by City
selected_city = st.sidebar.selectbox("Select City", df['City'].unique())
    
    # Filter by Region
selected_region = st.sidebar.selectbox("Select Region", df['Region'].unique())

    # Apply filters
filtered_df = df[(df['City'] == selected_city) & (df['Region'] == selected_region)]
st.write(f"### Filtered Data for {selected_city}, {selected_region}")
st.dataframe(filtered_df)

    # Order Count
st.write(f"### Number of Orders in {selected_city}")
order_count = filtered_df['OrderID'].count()
st.write(order_count)

    # Sales and Profit Statistics
st.write(f"### Sales & Profit in {selected_city}")

total_sales = filtered_df['Sales'].sum()
st.write(f"Total Sales: ₹{total_sales}")

average_sales = filtered_df['Sales'].mean()
st.write(f"Average Sales: ₹{average_sales:.2f}")

total_profit = filtered_df['Profit'].sum()
st.write(f"Total Profit: ₹{total_profit}")

    # Product Search
st.sidebar.subheader("Search Product")
search_product = st.sidebar.text_input("Enter Product Name")
    
if search_product:
 search_results = df[df['ProductName'].str.contains(search_product, case=False, na=False)]
 st.write("### Search Results")
 st.dataframe(search_results)

    # Pie Chart for Region
st.write("### Pie Chart: Sales by Region")
region_data = df['Region'].value_counts()
fig, ax = plt.subplots()
ax.pie(region_data, labels=region_data.index, autopct="%1.1f%%")
st.pyplot(fig)

    # Pie Chart for City
st.write("### Pie Chart: Sales by City")
city_data = df['City'].value_counts()
fig, ax = plt.subplots()
ax.pie(city_data, labels=city_data.index, autopct="%1.1f%%")
st.pyplot(fig)

    # Pie Chart for Category
st.write("### Pie Chart: Sales by Category")
category_data = df['SubCategory'].value_counts()
fig, ax = plt.subplots()
ax.pie(category_data, labels=category_data.index, autopct="%1.1f%%")
st.pyplot(fig)

    # Line Chart for Sales & Profit
st.write("### Line Chart: Sales & Profit Over Time")
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
line_data = df.groupby('OrderDate')[['Sales', 'Profit']].sum()
    
fig, ax = plt.subplots()
ax.plot(line_data.index, line_data['Sales'], label="Sales", color="blue")
ax.plot(line_data.index, line_data['Profit'], label="Profit", color="red")
ax.legend()
st.pyplot(fig)

    # Displaying Grouped Data
st.write("### Sales & Profit Summary by Date")
order_group = df.groupby('OrderDate')[['Sales', 'Profit']].sum()
st.dataframe(order_group)

st.write("### Sales Summary by Region")
region_group = df.groupby('Region')[['Sales']].sum()
st.dataframe(region_group)
