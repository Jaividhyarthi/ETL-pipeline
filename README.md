# Task 1 – Data Preprocessing Pipeline (ETL)

This repository contains Task 1 of my Data Science Internship at CODTECH.

## ✅ Objective

To build an ETL (Extract, Transform, Load) pipeline using Python libraries such as **Pandas** and **Scikit-Learn** for data preprocessing and transformation.

---

## 📊 Dataset Used

**Titanic Dataset**  
Source: [Kaggle / DataScienceDojo GitHub](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)

---

## 🧪 Tools & Libraries

- Python
- pandas
- scikit-learn (LabelEncoder, StandardScaler)

---

## ⚙️ What This Script Does

1. **Loads raw data** from the Titanic dataset
2. **Drops irrelevant columns** like `Name`, `Ticket`, and `Cabin`
3. **Handles missing values** in `Age` and `Embarked`
4. **Encodes categorical variables** (`Sex`, `Embarked`) using LabelEncoder
5. **Scales numerical features** (`Age`, `Fare`) using StandardScaler
6. **Saves the cleaned dataset** into a CSV file `cleaned_titanic_data.csv`

---

## 🚀 How to Run

If you're using GitHub Codespace or local Python environment:

```bash
python task1_etl_pipeline.py
├── task1_etl_pipeline.py
├── cleaned_titanic_data.csv
├── README.md
