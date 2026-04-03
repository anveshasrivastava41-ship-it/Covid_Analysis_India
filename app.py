import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌍 COVID-19 Analytics & Prediction Dashboard")
st.markdown("### Data Analysis • Machine Learning • Interactive Dashboard") 

st.sidebar.markdown("## 📊 COVID Dashboard Controls")
st.set_page_config(layout="wide")

# Load data
df = pd.read_csv("covid_19_clean_complete.csv")

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("Filters")

# Country selector
countries = df['Country/Region'].unique()
selected_country = st.sidebar.selectbox("Select Country", countries)

# Date range
start_date = st.sidebar.date_input("Start Date", df['Date'].min())
end_date = st.sidebar.date_input("End Date", df['Date'].max())

# Metric selector
metric = st.sidebar.selectbox("Select Metric", ["Confirmed", "Deaths", "Recovered", "Active"])

# ---------------- FILTER DATA ---------------- #
filtered = df[(df['Country/Region'] == selected_country) &
              (df['Date'] >= pd.to_datetime(start_date)) &
              (df['Date'] <= pd.to_datetime(end_date))]

# Group by date
filtered = filtered.groupby('Date').sum().reset_index()

# ---------------- KPI SECTION ---------------- #
st.subheader(f"📊 Key Metrics for {selected_country}")

col1, col2, col3 = st.columns(3)

col1.metric("Total Cases", int(filtered['Confirmed'].max()))
col2.metric("Total Deaths", int(filtered['Deaths'].max()))
col3.metric("Total Recovered", int(filtered['Recovered'].max()))

# ---------------- LINE CHART ---------------- #
st.subheader(f"{metric} Trend")

plt.figure()
plt.plot(filtered['Date'], filtered[metric])
plt.title(f"{metric} Over Time")
plt.xlabel("Date")
plt.ylabel(metric)

st.pyplot(plt)

# ---------------- TOP COUNTRIES ---------------- #
st.subheader("🌍 Top 5 Countries Comparison")

top_countries = df.groupby('Country/Region')['Confirmed'].max().sort_values(ascending=False).head(5)

plt.figure()
top_countries.plot(kind='bar')
plt.title("Top 5 Countries by Cases")

st.pyplot(plt)

# ---------------- PIE CHART ---------------- #
st.subheader("📊 Distribution of Cases")

latest = df[df['Date'] == df['Date'].max()]
top5 = latest.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False).head(5)

plt.figure()
top5.plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")

st.pyplot(plt)

# ---------------- ML PREDICTION (OPTIONAL) ---------------- #
st.subheader("🤖 Prediction (Linear Regression)")

from sklearn.linear_model import LinearRegression

filtered['Date_Ordinal'] = filtered['Date'].map(pd.Timestamp.toordinal)

X = filtered[['Date_Ordinal']]
y = filtered['Confirmed']

model = LinearRegression()
model.fit(X, y)

future_dates = pd.date_range(start=filtered['Date'].max() + pd.Timedelta(days=1), periods=30)
future_ordinal = future_dates.map(pd.Timestamp.toordinal)

future_df = pd.DataFrame({'Date_Ordinal': future_ordinal})

predictions = model.predict(future_df)

plt.figure()
plt.plot(filtered['Date'], filtered['Confirmed'], label='Actual')
plt.plot(future_dates, predictions, linestyle='dashed', label='Predicted')

plt.legend()
plt.title("Prediction")

st.pyplot(plt)

# ---------------- DATA TABLE ---------------- #
st.subheader("📄 Data Preview")
st.dataframe(filtered.tail())

st.markdown("""
---
### 📌 About This Project
This dashboard analyzes COVID-19 trends using data analytics and machine learning techniques.  
It includes prediction models and interactive visualizations to derive insights.
""")
