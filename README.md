# 📊 Customer Segmentation with RFM & K-Means

---

## 🧠 Project Overview

This project focuses on **customer segmentation** using transactional data, combining **RFM analysis** (Recency, Frequency, Monetary) with **unsupervised learning (K-Means)**.

We used Kaggle's [Online Retail II dataset](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) which contains transactions from a UK-based online retailer between 2009 and 2011.

The goal is to:
- Identify meaningful customer segments from a **business perspective**
- Build a **clean, modular, and production-oriented data pipeline** using Python

At this stage, the project covers **data preparation, feature engineering, RFM construction, and customer segmentation**.

---

## 📁 Project Structure

```text
.
├── data/
│   ├──  raw/                 # Raw transactional data (csv)
│   ├──  curated/             # Cleaned dataset (parquet)
│   ├──features/              # Featured & segmented datasets (parquet)
│   ├── rfm/                  # RFM datasets (parquet)
│
├── app/
│   ├── config/ 
│   │   └── settings.py        # Configuration settings
│   ├── etl/ 
│   │   └── download_data.py         # Data extraction
│   │   └── clean_data.py            # Data cleaning
│   │   └── save_cleaned_data.py     # Save cleaned data
│   │   └── extract_features.py      # Feature extraction
│   │   └── save_featured_data.py    # Save featured data
│   │   └── build_rfm_features.py    # RFM aggregation
│   │   └── save_rfm_data.py         # Save RFM data
│   │   └── scale_features.py        # Feature scaling
│   │   └── run_rfm_segmentation.py  # RFM scoring + K-Means clustering
│   │   └── save_rfm_seg_results.py  # Save segmentation results
│
├── notebooks/
│   └── eda.ipynb              # Exploratory Data Analysis
│   └── eda_rfm.ipynb          # EDA on RFM features
│   └── kmeans.ipynb           # K-Means clustering analysis
│
└── README.md
└── requirements.txt
```

## Prerequisites & Installation

- Python 3.12+
- Clone the repository:
```
git clone <paste_your_repo_url_here>
```
- Install required packages:
```
pip install -r requirements.txt
```
---

## Data Pipeline (Current State) 

### 1. Data Cleaning & Preparation
- Removal of invalid or inconsistent transactions
- Parsing and standardization of timestamps

### 2. Feature Engineering (extract_features.py)
Transaction-level enrichment with:

**Temporal features:**
- Day of week 
- Month 
- Cyclical encoding (sin / cos)

**Behavioral features:**
- High season indicator (September–November)
- Weekend purchase indicator 
- Time gap between consecutive invoices per customer (DaysSincePrevInvoice)

### 3. RFM Feature Construction (build_rfm_features.py)
Customer-level aggregation including:

- **Recency**: days since last purchase (snapshot-based)
- **Frequency**: number of unique invoices 
- **Monetary**: total spend (price × quantity)
- Customer Lifespan: time between first and last purchase
- Purchase gap statistics: average / median / max gap 
- Seasonality indicators:
  - % of purchases during high season 
  - % of purchases on weekends

Due to highly skewed distributions:
- Features are log-transformed 
- Scaling is applied using RobustScaler

### 4. K-Means Clustering (run_rfm_segmentation.py)

In parallel, a K-Means clustering is performed:
- Features used: Recency, Frequency, Monetary
- Optimal number of clusters evaluated using:
  - Elbow method 
  - Silhouette score
- Final model trained with K = 4

Each customer receives a cluster label (unsupervised).

### 📈 Results & Insights

The clustering reveals four distinct customer profiles:
- Cluster 0: One-shot or lost customers (low frequency, low monetary, high recency)
- Cluster 1: New or early-stage customers (recent purchases, limited history)
- Cluster 2: At-risk customers (historically active but disengaging)
- Cluster 3: Champions / high-value customers (frequent and high spenders)

Marketing strategies can be adapted accordingly:
- Win-back campaigns for lost customers
- Onboarding and engagement for new customers
- Retention strategies for at-risk customers
- Loyalty and VIP programs for champions

---
## Conclusion

This project demonstrates how to effectively segment customers using RFM analysis combined with K-Means clustering. The modular pipeline allows for easy data processing and feature engineering, making it suitable for production environments. Future work could include integrating additional clustering algorithms, enhancing feature sets, and deploying the pipeline for real-time customer segmentation.

---

## Next steps

To complete the project from a data engineering and production perspective, upcoming steps include:

- Data modeling (SQL)
- Loading data into PostgreSQL (via Docker)
- Spark-based ETL for scalability
- Workflow orchestration with Airflow

---

## License

This project is licensed under the [MIT License](LICENSE).
