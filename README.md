# Hate Speech Detection

A machine learning project for detecting and classifying hate speech in social media tweets using natural language processing (NLP) and binary classification algorithms.
by...
     krishna kumar 
---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Machine Learning Model](#machine-learning-model)
- [Tools & Libraries](#tools--libraries)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Data Preprocessing](#data-preprocessing)
- [Algorithm Details](#algorithm-details)
- [Usage](#usage)
- [Results & Evaluation](#results--evaluation)
- [Requirements](#requirements)

---

## 🎯 Project Overview

This project implements a hate speech detection system that analyzes tweets and classifies them as:
- **Class 0**: Normal/Non-offensive tweets
- **Class 1**: Hate Speech/Offensive tweets

The system uses natural language processing techniques to preprocess tweets and machine learning algorithms to perform binary classification.

---

## 🤖 Machine Learning Model

### Model: Logistic Regression

**Algorithm**: Binary Logistic Regression with Sigmoid Function

#### Mathematical Foundation:
```
Sigmoid Function: P(y=1) = 1 / (1 + e^(-z))
Linear Combination: z = w·x + b
Loss Function: Binary Cross-Entropy: loss = -[y·log(p) + (1-y)·log(1-p)]
Optimization: Gradient Descent
Threshold: 0.3 probability for classification
```

#### Model Hyperparameters:
- **max_iter**: 1000 (maximum iterations for convergence)
- **random_state**: 42 (for reproducibility)
- **solver**: Default (lbfgs)
- **Threshold**: 0.3 (probability cutoff for positive class)

#### Training Data Split:
- Training Set: 70%
- Validation Set: 30%

#### Evaluation Metrics:
- **Accuracy**: Percentage of correct predictions
- **Precision**: True Positives / (True Positives + False Positives)
- **Recall**: True Positives / (True Positives + False Negatives)
- **F1-Score**: Harmonic mean of Precision and Recall

---

## 🛠️ Tools & Libraries

### Core Data Processing
| Tool | Version | Purpose |
|------|---------|---------|
| **pandas** | 2.3.2 | Data manipulation and analysis |
| **numpy** | 2.2.3 | Numerical computing |
| **re** | Built-in | Regular expressions for text cleaning |

### Natural Language Processing (NLP)
| Tool | Version | Purpose |
|------|---------|---------|
| **nltk** | 3.9.1 | Natural Language Toolkit for text processing |
| **PorterStemmer** | (nltk) | Reduces words to root form |
| **WordCloud** | Latest | Visualization of word frequency |
| **Tokenization** | (nltk) | Breaking text into individual words |

### Machine Learning & Feature Extraction
| Tool | Version | Purpose |
|------|---------|---------|
| **scikit-learn** | 1.7.1 | ML algorithms and utilities |
| **CountVectorizer** | (sklearn) | Bag of Words feature extraction |
| **TfidfVectorizer** | (sklearn) | TF-IDF feature extraction |
| **LogisticRegression** | (sklearn) | Binary classification model |
| **train_test_split** | (sklearn) | Data splitting utility |

### Evaluation & Metrics
| Tool | Version | Purpose |
|------|---------|---------|
| **f1_score** | (sklearn) | F1 metric calculation |
| **accuracy_score** | (sklearn) | Accuracy calculation |
| **precision_score** | (sklearn) | Precision calculation |
| **recall_score** | (sklearn) | Recall calculation |

### Visualization
| Tool | Version | Purpose |
|------|---------|---------|
| **matplotlib** | 3.10.6 | Static plotting library |
| **seaborn** | 0.13.2 | Statistical data visualization |
| **WordCloud** | Latest | Word cloud visualizations |

---

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Steps

1. **Clone or download the project**
```bash
cd "Hate speech detection"
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn wordcloud
```

3. **Download NLTK data**
```python
import nltk
nltk.download('punkt')  # For tokenization
```

---

## 📁 Project Structure

```
Hate speech detection/
├── README.md                          # Project documentation
├── hatespeech.ipynb                  # Main Jupyter notebook
├── hate_speech_new.ipynb             # Alternative implementation
├── test_tweets_anuFYb8.csv          # Test dataset
├── train_E6oV3lV.csv                # Training dataset (if available)
└── requirements.txt                  # Python dependencies
```

---

## 🔧 Data Preprocessing Pipeline

### Step 1: Text Cleaning
- Remove Twitter handles (@mentions)
- Remove special characters and numbers
- Keep only alphabetic characters and hashtags

### Step 2: Length Filtering
- Remove words with length ≤ 3 characters

### Step 3: Tokenization
- Split text into individual words
  ```
  "Hello World" → ["Hello", "World"]
  ```

### Step 4: Stemming (Porter Stemmer)
- Reduce words to root form
  ```
  "running" → "run"
  "happily" → "happi"
  ```

### Step 5: Feature Extraction

#### Option A: Bag of Words (BoW)
- Creates sparse matrix of word counts
- Parameters: max_df=0.90, min_df=2, max_features=1000
- Removes stop words in English

#### Option B: TF-IDF
- Weights terms by importance across corpus
- Parameters: max_df=0.90, min_df=2, max_features=1000
- Formula: TF-IDF(t,d) = TF(t,d) × log(N/DF(t))

---

## 🧠 Algorithm Details

### Logistic Regression Algorithm

#### How It Works:

1. **Initialization**
   - Initialize weights (w) and bias (b) to small random values

2. **Forward Propagation**
   - Compute linear combination: z = w·x + b
   - Apply sigmoid: P(y=1) = 1/(1 + e^(-z))

3. **Loss Calculation**
   - Binary cross-entropy: loss = -[y·log(p) + (1-y)·log(1-p)]

4. **Backpropagation**
   - Compute gradients: ∂loss/∂w, ∂loss/∂b

5. **Weight Update (Gradient Descent)**
   - w = w - α·∂loss/∂w
   - b = b - α·∂loss/∂b
   - (where α is learning rate)

6. **Repeat** until convergence or max iterations

#### Classification Decision:
```
If P(hate_speech) ≥ 0.3 → Classify as Hate Speech (1)
If P(hate_speech) < 0.3 → Classify as Normal (0)
```

#### Advantages:
- ✅ Fast training and prediction
- ✅ Works well with sparse text features
- ✅ Interpretable model weights
- ✅ Low computational overhead

---

## 🚀 Usage

### Running the Jupyter Notebook

```bash
jupyter notebook hatespeech.ipynb
```

### Training the Model (when train data available)

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, accuracy_score

# Split data
xtrain_bow, xvalid_bow, ytrain, yvalid = train_test_split(
    train_bow, train['label'], random_state=42, test_size=0.3
)

# Train model
lreg = LogisticRegression(max_iter=1000, random_state=42)
lreg.fit(xtrain_bow, ytrain)

# Predict
predictions = (lreg.predict_proba(xvalid_bow)[:, 1] >= 0.3).astype(int)

# Evaluate
print(f"F1-Score: {f1_score(yvalid, predictions):.4f}")
print(f"Accuracy: {accuracy_score(yvalid, predictions):.4f}")
```

### Making Predictions on New Tweets

```python
# Preprocess new tweet
new_tweet = "example tweet text"
# ... apply same preprocessing steps ...

# Predict
probability = lreg.predict_proba([processed_tweet])[:, 1]
prediction = 1 if probability >= 0.3 else 0
print(f"Hate Speech Probability: {probability[0]:.2%}")
```

---

## 📊 Results & Evaluation

### Expected Performance Metrics

| Metric | Range | Interpretation |
|--------|-------|-----------------|
| **Accuracy** | 0.0 - 1.0 | Percentage of correct predictions |
| **Precision** | 0.0 - 1.0 | Of detected hate speech, how many correct |
| **Recall** | 0.0 - 1.0 | Of actual hate speech, how many detected |
| **F1-Score** | 0.0 - 1.0 | Balance between precision and recall |

### Confusion Matrix Interpretation
```
                 Predicted
               Neg    Pos
Actual Neg     TN     FP
       Pos     FN     TP
```

---

## 📋 Requirements

### Python Version
- Python 3.10+

### Core Dependencies
```
pandas==2.3.2
numpy==2.2.3
matplotlib==3.10.6
seaborn==0.13.2
nltk==3.9.1
scikit-learn==1.7.1
wordcloud
```

### Install Requirements
```bash
pip install -r requirements.txt
```

---

## 🔍 Key Features

✅ **Text Preprocessing**: Comprehensive cleaning and normalization
✅ **Multiple Feature Extraction**: BoW and TF-IDF options
✅ **Visualizations**: Word clouds and hashtag frequency charts
✅ **Modular Design**: Reusable preprocessing and model functions
✅ **Evaluation Metrics**: Multiple metrics for model assessment
✅ **Scalable**: Handles large tweet datasets efficiently

---

## 📝 Input Data Format

### Required CSV Columns:
```
id,tweet
31963,"#studiolife #aislife #requires #passion..."
31964,"@user #white #supremacists want everyone..."
```

### With Labels (for training):
```
id,tweet,label
1,"normal tweet here",0
2,"hate speech tweet here",1
```

---

## 🐛 Troubleshooting

### Issue: "train_E6oV3lV.csv" not found
**Solution**: Provide the training data file or use only the test_tweets file

### Issue: WordCloud import error
**Solution**: `pip install wordcloud`

### Issue: NLTK data missing
**Solution**: Run `nltk.download('punkt')` in Python

---

## 📚 References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [NLTK Documentation](https://www.nltk.org/)
- [Logistic Regression Theory](https://en.wikipedia.org/wiki/Logistic_regression)
- [TF-IDF Explanation](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

---

## 📄 License

This project is provided as-is for educational and research purposes.

---

## 👤 Author

Hate Speech Detection Project - (KRISHNA KUMAR)February 2026

---

## 🤝 Contributing

For improvements or bug fixes, please update the notebook cells and document changes.

---

**Last Updated**: February 19, 2026
#   h a t e - o f - s p e e c h  
 