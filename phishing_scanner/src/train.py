# src/train.py

import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
from features import get_url_features


def load_data():
    """
    Load phishing and legitimate URL data, assign labels, and shuffle.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    phishing_path = os.path.join(base_dir, 'data', 'phishing.csv')
    legitimate_path = os.path.join(base_dir, 'data', 'legitimate.csv')

    # Load phishing URLs (PhishTank CSV) - select 'url' column
    phish = pd.read_csv(phishing_path, usecols=['url'], dtype=str)
    phish['label'] = 1

    # Load legitimate URLs (Majestic Millions CSV) - select 'Domain' column
    legit = pd.read_csv(legitimate_path, usecols=['Domain'], header=0, dtype=str)
    legit = legit.rename(columns={'Domain': 'url'})
    legit['label'] = 0

    # Combine and shuffle
    df = pd.concat([phish, legit]).sample(frac=1, random_state=42).reset_index(drop=True)
    return df


def extract_features(df):
    """
    Extract features for each URL in df using get_url_features.
    """
    X = df['url'].apply(lambda u: pd.Series(get_url_features(u)))
    y = df['label']
    return X, y


def main():
    # 1. Load data
    df = load_data()
    # Sample a subset to speed up training and avoid excessive WHOIS lookups
    df = df.sample(n=2000, random_state=42).reset_index(drop=True)

    # 2. Extract features
    X, y = extract_features(df)

    # 3. Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Train model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # 5. Evaluate model
    y_pred = clf.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # 6. Save model
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    model_dir = os.path.join(base_dir, 'models')
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, 'phish_detector.pkl')
    joblib.dump(clf, model_path)
    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    main()
