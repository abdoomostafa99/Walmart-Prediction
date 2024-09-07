import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_title='Home Page', page_icon='🏠')

df = pd.read_csv('Walmart_cleaned.csv')

st.title('Weekly Sales Prediction')
st.markdown('This is a simple web app that uses the Streamlit library to predicit weekly sales data. The dataset includes sales, weather, and economic information.')

st.image('https://th.bing.com/th/id/OIP.AndkjuHOJstOPpP_wM1a6AAAAA?rs=1&pid=ImgDetMain', width=700, caption='Weekly Sales Data Analysis')

st.markdown('''
## Welcome to the Weekly Sales Data Analysis Web App!
### Features:
- **Data Exploration:** View the sales data and its summary statistics.
- **Data Visualization:** Explore interactive visualizations of the sales data.
- **Predictions:** Use machine learning models to forecast sales.
- **Insights:** Extract insights from sales trends, temperature, fuel prices, and more.
### How to use this app:
1. Use the sidebar to navigate between pages.
2. Data and visualizations are shown in the main window.
3. You can interact with tables and charts.

### Column Descriptions:
- **store**: Store identification number.
- **weekly_sales**: Total sales in USD for the specified week.
- **holiday_flag**: Indicator of whether the week includes a holiday (1 for holiday, 0 for no holiday).
- **temperature**: Average temperature during the week (Fahrenheit).
- **fuel_price**: Price per gallon of fuel (USD).
- **cpi**: Consumer Price Index, a measure of inflation.
- **unemployment**: Unemployment rate (%) for the week.
- **year**: The year the sales were recorded.
- **month**: The month the sales were recorded.
- **day**: The day the sales were recorded.
''')

# Sample data display
st.title('Sample of Data')
if st.checkbox('View Sample of Data'):
    st.dataframe(df.head(10))
