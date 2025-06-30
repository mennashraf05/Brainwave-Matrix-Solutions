# Phishing Link Scanner

I built this Python tool to detect phishing URLs and classify them as **Phishing** or **Legitimate** using a simple machine learning pipeline.

## 🔍 Project Overview

* **Objective:** Automatically scan URLs and flag suspicious links that may be used in phishing attacks.
* **Approach:**

  1. **Data Collection:** I gathered labeled URLs from PhishTank (phishing) and Majestic Million (legitimate).
  2. **Feature Engineering:** I wrote a function to extract characteristics like URL length, number of dots/hyphens, presence of `@`, suspicious TLDs, and more.
  3. **Model Training:** I trained a Random Forest classifier on a sample of 2,000 URLs and achieved 99% accuracy.
  4. **CLI Scanner:** I provided a simple command‑line script to scan any URL on demand.

## ⚙️ Installation

1. **Clone the repo**:

   ```bash
   git clone https://github.com/mennashraf05/Brainwave-Matrix-Solutions
   cd phishing‑scanner
   ```
2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: .\venv\Scripts\Activate.ps1
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### 1. Train the model

I start by training the model on my sample data:

```bash
python src/train.py
```

This script will:

* Load and preprocess data from `data/phishing.csv` and `data/legitimate.csv`
* Extract URL features
* Train a Random Forest and print evaluation metrics
* Save the trained model to `models/phish_detector.pkl`

### 2. Scan URLs

Once the model is saved, I can scan any URL directly from the terminal:

```bash
python src/scan.py <url1> [url2 ...]
```

**Examples:**

```bash
python src/scan.py http://example.com
# Output: Legitimate

python src/scan.py https://secure-login.tk/login?user=abc http://sub.test-site.ga/path/page.html
# Output:
# https://secure-login.tk/login?user=abc ➜ Legitimate
# http://sub.test-site.ga/path/page.html ➜ Phishing
```

## 📝 Project Structure

```
phishing-link-scanner/
├── data/                  # Raw CSV datasets
├── models/                # Saved ML model
├── src/
│   ├── features.py        # URL feature extraction
│   ├── train.py           # Model training script
│   └── scan.py            # CLI scanner
├── report.md              # Detailed project report
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

## 🔮 Future Improvements

* Restore WHOIS-based domain age feature with caching or API.
* Expand training data to tens of thousands of URLs.
* Add SSL certificate and page‑content analysis (forms, iframes).

## 👤 Author

I’m a Cyber Security intern who created this project as part of my hands‑on training. Feel free to open issues or suggest enhancements!
