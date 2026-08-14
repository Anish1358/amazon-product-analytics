
# Amazon Product Analytics

An end-to-end **Amazon Product Analytics project** focused on data cleaning, business analysis, review sentiment analysis, and dashboard development using **Python, SQL/MySQL, and Excel**.

## Project Overview

This project analyzes Amazon product data to understand **pricing, discounts, product ratings, review volume, categories, price ranges, and customer review sentiment**.

The workflow starts with raw Amazon product data, cleans and prepares the dataset using Python, performs business-oriented analysis using SQL/MySQL, applies sentiment analysis to review text, and presents the results through an Excel dashboard.

## Objectives

* Clean and preprocess the raw Amazon product dataset.
* Analyze product pricing, discounts, ratings, and review counts.
* Perform category-level business analysis using SQL.
* Analyze customer review sentiment using TextBlob.
* Identify highly rated, highly reviewed, and potentially problematic products.
* Create an Excel dashboard with KPIs and visualizations.

## Project Workflow

```text
Raw Amazon Dataset
        ↓
Data Cleaning & Preprocessing
        ↓
Cleaned Dataset
        ↓
SQL / MySQL Business Analysis
        ↓
Review Sentiment Analysis
        ↓
Final Analytical Dataset
        ↓
Excel Dashboard
```

## Technologies Used

* **Python**

  * Pandas
  * NumPy
  * TextBlob
  * OpenPyXL
* **SQL / MySQL**
* **Microsoft Excel**

## Project Components

### 1. Data Cleaning

The raw dataset is cleaned using Python and Pandas.

Key steps include:

* Converting price fields into numeric format.
* Removing ₹ symbols and comma separators.
* Converting discount percentages into numeric values.
* Cleaning rating and rating-count fields.
* Extracting main and sub-categories from the category hierarchy.
* Removing records with missing analytical values.
* Removing duplicate product IDs.
* Creating `savings_amount`.
* Creating price buckets for analysis.

The output is:

`amazon_cleaned.csv`

### 2. SQL / MySQL Analysis

The cleaned dataset is loaded into MySQL and analyzed using business-oriented SQL queries.

The analysis covers:

* Top categories using an estimated demand/revenue proxy.
* Average discount percentage by category.
* Best-rated categories based on review volume.
* Highly discounted but poorly rated products.
* Product distribution across price buckets.
* Highly rated products with strong review volume.

> **Note:** The estimated revenue/demand measure uses `discounted_price × rating_count` as a proxy based on the available dataset. It does not represent actual Amazon sales revenue.

### 3. Sentiment Analysis

Customer review text is analyzed using **TextBlob**.

Each review text receives a sentiment polarity score between **-1 and +1**.

The scores are classified as:

* **Positive**
* **Neutral**
* **Negative**

The sentiment results are then merged with the cleaned product dataset.

Output:

`amazon_with_sentiment.csv`

### 4. Excel Dashboard

An Excel dashboard is generated using Python and OpenPyXL.

The dashboard includes:

* Product-level data
* Category-level KPIs
* Average discounted price
* Average discount percentage
* Average rating
* Total review count
* Overall project KPIs
* Average rating by category chart
* Product count by category chart
* Sentiment analysis summary

Output:

`Amazon_Product_Analytics_Dashboard.xlsx`

## Repository Structure

```text
amazon-product-analytics/
│
├── amazon.csv
├── amazon_cleaned.csv
├── amazon_with_sentiment.csv
│
├── cleaning.py
├── sql_analysis.py
├── sentiment.py
├── dashboard.py
│
├── Amazon_Product_Analytics_Dashboard.xlsx
│
└── README.md
```

## Key Skills Demonstrated

* Data Cleaning & Preprocessing
* Exploratory Data Analysis
* Python / Pandas
* SQL & MySQL
* Sentiment Analysis
* Feature Engineering
* Business Analytics
* Data Visualization
* Excel Dashboard Development
* KPI Analysis

## Conclusion
This project demonstrates an end-to-end data analytics workflow, from raw data preparation to business insights and dashboard reporting, combining Python, SQL/MySQL, sentiment analysis, and Excel.
This project demonstrates an end-to-end data analytics workflow, from **raw data preparation to business insights and dashboard reporting**, combining Python, SQL/MySQL, sentiment analysis, and Excel.
