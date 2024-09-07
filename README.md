# Weekly Sales Prediction Web App

This repository contains a Streamlit web app designed to predict weekly sales based on historical sales data, weather, and economic information. 

## Features
- **Data Exploration**: View and analyze the sales data and summary statistics.
- **Data Visualization**: Explore interactive charts to understand sales trends, temperature, fuel prices, and other factors.
- **Predictions**: Forecast future sales using machine learning models.
- **Insights**: Gain insights from various sales trends and economic indicators.

## How to Use
1. Navigate through the app using the sidebar.
2. Data and visualizations are displayed in the main window.
3. Interact with tables and charts for detailed analysis.

## Column Descriptions
- **store**: Store identification number.
- **weekly_sales**: Total sales in USD for the specified week.
- **holiday_flag**: Indicator if the week includes a holiday (1 for holiday, 0 for no holiday).
- **temperature**: Average temperature during the week (Fahrenheit).
- **fuel_price**: Price per gallon of fuel (USD).
- **cpi**: Consumer Price Index, a measure of inflation.
- **unemployment**: Unemployment rate (%) for the week.
- **year**: Year the sales were recorded.
- **month**: Month the sales were recorded.
- **day**: Day the sales were recorded.

## Installation
1. Clone this repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the app with `streamlit run app.py`.
