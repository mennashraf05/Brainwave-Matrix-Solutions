# src/scan.py

import os
import sys
import pandas as pd
import joblib
from features import get_url_features


def scan_url(url: str, model) -> str:
    """
    Extract features for a URL and predict using the trained model.
    Returns 'Phishing' or 'Legitimate'.
    """
    feats_dict = get_url_features(url)
    feats_df = pd.DataFrame([feats_dict])  # preserve feature names
    pred = model.predict(feats_df)[0]
    return "Phishing" if pred == 1 else "Legitimate"


def main():
    # Check arguments
    if len(sys.argv) < 2:
        print("Usage: python src/scan.py <url1> [url2 ...]")
        sys.exit(1)

    # Determine project root and load model
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    model_path = os.path.join(base_dir, 'models', 'phish_detector.pkl')
    model = joblib.load(model_path)

    # Scan each provided URL
    for url in sys.argv[1:]:
        result = scan_url(url, model)
        print(f"{url} ➜ {result}")


if __name__ == "__main__":
    main()
