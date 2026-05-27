# Customer Sentiment & Marketing Performance Analytics Dashboard

This project is a full end-to-end data analytics pipeline combining **SQL Server**, **Python (NLTK VADER)**, and **Power BI** to analyze customer sentiment and marketing performance for a fictional e-commerce business.

---

## 1. Project Overview

This project builds a complete analytics pipeline that ingests raw customer and marketing data, enriches it with sentiment analysis using Python, and visualizes insights in an interactive Power BI dashboard published to Power BI Service. The goal is to help stakeholders understand how customer sentiment relates to marketing channel performance, product engagement, and customer geography.

---

## 2. Business Problem

A mid-sized e-commerce company is seeking to better understand:

- Why customer satisfaction scores may be declining despite increased marketing spend
- Which products are receiving the most negative reviews
- How engagement across different marketing channels compares
- Where geographically customers are most and least satisfied

This project addresses those questions by combining structured SQL data with NLP-powered sentiment scoring, all surfaced through a business-ready Power BI dashboard.

---

## 3. Tools Used

| Tool | Purpose |
|------|---------|
| **SQL Server (Docker on macOS)** | Data storage, cleaning, and transformation using T-SQL |
| **VS Code SQL Server Extension** | Writing and executing SQL queries against the Docker-hosted database |
| **Python 3** | Sentiment analysis and data enrichment |
| **NLTK VADER** | Natural language sentiment scoring of customer reviews |
| **pandas** | Data manipulation and CSV export |
| **pyodbc** | Python-to-SQL Server database connection |
| **Power BI Service** | Interactive dashboard and data visualization (web-based) |
| **Power Query / Dataflow Gen2** | Data transformation and loading within Power BI |
| **GitHub** | Version control and project sharing |

---

## 4. Dataset Overview

All datasets represent a fictional e-commerce company and are stored in the `CSVs/` folder:

| File | Description |
|------|-------------|
| `customer_reviews.csv` | Raw customer reviews with ratings and review text |
| `customers_and_geography.csv` | Customer demographic and location data |
| `Customer_journey.csv` | Customer funnel stages and drop-off points |
| `engagement_data.csv` | Marketing channel engagement metrics |
| `products.csv` | Product catalog with categories and pricing |
| `customer_reviews_with_sentiment.csv` | Enriched reviews with VADER sentiment scores (output) |

---

## 5. Project Workflow

```
Raw CSV Data
     │
     ▼
SQL Server (Docker on macOS)
  - Import & clean data
  - Write transformation queries via VS Code SQL Extension
  - Join tables for analysis
     │
     ▼
Python (pandas + NLTK VADER + pyodbc)
  - Connect to SQL Server
  - Pull customer reviews
  - Run VADER sentiment analysis
  - Classify: Positive / Negative / Neutral
  - Export enriched CSV
     │
     ▼
Power BI Service (Power Query / Dataflow Gen2)
  - Load enriched data
  - Build relationships across tables
  - Create KPIs, visuals, and filters
  - Publish interactive dashboard to Power BI Service
```

---

## 6. SQL Work

The SQL layer handles all foundational data work using SQL Server running in Docker on macOS, with queries written and executed through the VS Code SQL Server extension:

- **Data Import:** Raw CSVs imported into a SQL Server database
- **Data Cleaning:** Handling nulls, fixing data types, standardizing text fields
- **Transformations:** Joining customer, product, journey, and engagement tables
- **Views:** Creating reusable views to feed into Python and Power BI
- **Aggregations:** Summarizing ratings, engagement counts, and conversion metrics by product, category, and region

> 📌 *The `.bak` database backup file is excluded from this repository via `.gitignore`.*

---

## 7. Python Sentiment Analysis

**Script:** `customer_reviews_enrichment.py`

The Python script connects to SQL Server via `pyodbc`, retrieves customer review text, and applies the **NLTK VADER** (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer — a lexicon-based model well-suited for short, informal text like product reviews.

**What the script does:**
1. Connects to SQL Server using `pyodbc`
2. Queries the `customer_reviews` table
3. Applies VADER's `SentimentIntensityAnalyzer` to each review
4. Generates a **compound score** (range: -1.0 to +1.0)
5. Classifies each review as:
   - ✅ `Positive` — compound score ≥ 0.05
   - ❌ `Negative` — compound score ≤ -0.05
   - ➖ `Neutral` — compound score between -0.05 and 0.05
6. Exports the enriched dataset to `customer_reviews_with_sentiment.csv`

**Output columns added:**
- `sentiment_score` — VADER compound score
- `sentiment_category` — Positive / Negative / Neutral

---

## 8. Power BI Dashboard

The dashboard is published to **Power BI Service** and built on top of the enriched CSV data. It consists of multiple report pages:

- **Overview Page** — High-level KPIs: total reviews, average rating, sentiment breakdown
- **Sentiment Analysis Page** — Sentiment distribution by product, category, and time
- **Customer Journey Page** — Funnel visualization showing drop-off at each stage
- **Marketing Engagement Page** — Channel-by-channel engagement comparison
- **Geographic Page** — Map visual showing sentiment and engagement by customer location

**Power Query** and **Dataflow Gen2** are used to load, clean, and merge the CSV files before visualization. Relationships are built across all five source tables.

---

## 9. Key Insights

- 📉 Sentiment scores vary across product categories, with some categories showing a higher proportion of negative reviews
- 📣 Engagement metrics differ across marketing channels, with social media showing high volume relative to other channels
- 🌍 Customer satisfaction patterns show some geographic variation across regions
- 🛒 The customer journey funnel highlights drop-off points between stages that may indicate areas for further investigation
- ⭐ Review text sentiment does not always align directly with star ratings, suggesting qualitative feedback adds context beyond numeric scores

---

## 10. Skills Demonstrated

- ✅ End-to-end data pipeline design (SQL → Python → Power BI)
- ✅ Running SQL Server in Docker on macOS
- ✅ Writing and executing T-SQL using the VS Code SQL Server extension
- ✅ Python scripting for data enrichment and NLP
- ✅ Sentiment analysis using NLTK VADER
- ✅ Database connectivity with `pyodbc`
- ✅ Data wrangling and transformation with `pandas`
- ✅ Interactive dashboard design in Power BI Service
- ✅ Data modeling and table relationships in Power BI
- ✅ Power Query and Dataflow Gen2 for ETL within Power BI
- ✅ Git version control and clean GitHub project structure

---

## 11. How to Run This Project

### Prerequisites

- Python 3.8+
- Docker Desktop (to run SQL Server on macOS)
- VS Code with the SQL Server extension
- A Power BI account (to view or republish the dashboard via Power BI Service)
- Required Python packages:

```bash
pip install pandas nltk pyodbc
```

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/your-username/sentiment-analysis.git
cd sentiment-analysis
```

2. **Set up the database**
   - Start SQL Server in Docker
   - Connect via the VS Code SQL Server extension
   - Import the CSVs from the `CSVs/` folder into your database
   - Run any provided SQL scripts to create and populate the tables

3. **Run the Python sentiment script**
   - Update the connection string in `customer_reviews_enrichment.py` with your SQL Server credentials

```bash
python customer_reviews_enrichment.py
```

   This will generate `customer_reviews_with_sentiment.csv`.

4. **View the dashboard**
   - Log in to [Power BI Service](https://app.powerbi.com)
   - Upload the enriched CSV and connect it as a data source
   - Explore the published dashboard

---

## 12. Project Files

```
sentiment-analysis/
│
├── CSVs/
│   ├── customer_reviews.csv
│   ├── customers_and_geography.csv
│   ├── Customer_journey.csv
│   ├── engagement_data.csv
│   └── products.csv
│
├── Files/
│   └── (project screenshots)
│
├── Github Link for reference/
│   └── Github_youtube.docx
│
├── customer_reviews_enrichment.py       ← Python sentiment analysis script
├── customer_reviews_with_sentiment.csv  ← Enriched output (generated by script)
├── .gitignore                           ← Excludes local/large files from GitHub
└── README.md                            ← This file
```

> 🔒 **Note:** The SQL Server database backup (`.bak`), installer files (`.dmg`, `.exe`), and Claude Code local settings (`.claude/`) are intentionally excluded from this repository via `.gitignore`. These are large local setup files that do not belong in version control.

---

## Author

**Himanshu Jain**
University of Massachusetts Dartmouth
[hjain@umassd.edu](mailto:hjain@umassd.edu)

---

*Built as a portfolio project demonstrating end-to-end data analytics skills across SQL, Python, and Power BI.*
