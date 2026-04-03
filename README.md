# 🌍 COVID-19 Analytics & Prediction Dashboard

## 📌 Overview

This project presents a comprehensive analysis of COVID-19 data using data analytics and machine learning techniques. It includes data cleaning, visualization, predictive modeling, and an interactive dashboard for real-time insights.

---

## 🚀 Live Dashboard

🔗 *[https://covid-analytics-dashboard.streamlit.app/]* <br>
✨ Features an interactive dashboard with real-time filtering and ML-based predictions.

---

## 📊 Features

### 🔹 Data Analysis

* Cleaned and processed COVID-19 dataset
* Handled missing values and formatted date columns
* Performed exploratory data analysis (EDA)

### 🔹 Visualizations

* Time-series trends of confirmed, deaths, recovered, and active cases
* Comparative analysis of top countries
* Bar charts, line graphs, and pie charts

### 🔹 Machine Learning

* **Linear Regression** → Predict future COVID-19 cases
* **ARIMA Model** → Time series forecasting
* **Classification Model** → Categorized risk levels (Low / Medium / High)

### 🔹 Interactive Dashboard

* Built using Streamlit
* Dynamic filters (country, date range, metrics)
* Real-time graph updates
* KPI metrics display

---

## 📸 Dashboard Preview

### 🔹 Main Dashboard
![Main Dashboard](image/main_dashboard.png)

### 🔹 Trend Visualization
![Trend](screenshot2.png)

### 🔹 ML Prediction
![Prediction](screenshot3.png)


## 🧠 Key Insights

* COVID-19 cases showed multiple waves with rapid spikes during peak periods
* Growth trends stabilized over time after initial fluctuations
* Fatality rates decreased due to improved healthcare response
* Machine learning models captured trends and enabled future predictions
* Risk classification helps in understanding severity levels

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy** → Data processing
* **Matplotlib** → Data visualization
* **Scikit-learn** → Machine learning
* **Statsmodels** → ARIMA forecasting
* **Streamlit** → Dashboard deployment

---

## 📂 Project Structure

```
CovidAnalysisIndia/
│── covid_analysis.ipynb        # Jupyter notebook (analysis + ML)
│── app.py                      # Streamlit dashboard
│── covid_19_clean_complete.csv # Dataset
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/anveshasrivastava41-ship-it/CovidAnalysisIndia.git
cd CovidAnalysisIndia
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```
streamlit run app.py
```

---

## 📈 Future Improvements

* Improve model accuracy with advanced time-series techniques
* Add vaccination and policy data
* Enhance dashboard UI/UX
* Deploy using cloud-based data pipelines

---

## 👩‍💻 Author

**Anvesha Srivastava**

---

## ⭐ Acknowledgment

Dataset sourced from publicly available COVID-19 datasets.

---
