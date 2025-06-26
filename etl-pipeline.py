# task1_etl_pipeline.py

# 🚀 Task 1: ETL Pipeline using Pandas & Scikit-Learn
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(url):
    return pd.read_csv(url)

def preprocess_data(df):
    df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    
    le = LabelEncoder()
    df['Sex'] = le.fit_transform(df['Sex'])
    df['Embarked'] = le.fit_transform(df['Embarked'])

    scaler = StandardScaler()
    df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
    return df

def save_data(df, filename):
    df.to_csv(filename, index=False)

# Run the pipeline
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = load_data(url)
clean_data = preprocess_data(data)
save_data(clean_data, "cleaned_titanic_data.csv")

print("✅ Data pipeline complete. File saved: cleaned_titanic_data.csv")
