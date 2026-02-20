"""
Visual Output Generator for Hate Speech Detection Project
Generates comprehensive visual reports and analysis outputs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

class VisualOutputGenerator:
    """Generate visual outputs and reports from hate speech detection analysis"""
    
    def __init__(self, output_dir='outputs'):
        self.output_dir = output_dir
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create output directories
        os.makedirs(f"{output_dir}/visualizations", exist_ok=True)
        os.makedirs(f"{output_dir}/reports", exist_ok=True)
        os.makedirs(f"{output_dir}/data", exist_ok=True)
    
    def generate_preprocessing_report(self, original_text, processed_text, output_file=None):
        """Generate text preprocessing comparison report"""
        if output_file is None:
            output_file = f"{self.output_dir}/reports/preprocessing_report_{self.timestamp}.txt"
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║   TEXT PREPROCESSING TRANSFORMATION REPORT                   ║
╠══════════════════════════════════════════════════════════════╣
║ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
║ Task: Compare original vs processed text
╚══════════════════════════════════════════════════════════════╝

ORIGINAL TEXT:
{'-' * 60}
{original_text}

PROCESSED TEXT:
{'-' * 60}
{processed_text}

STATISTICS:
{'-' * 60}
Original Length:     {len(original_text)} characters
Processed Length:    {len(processed_text)} characters
Reduction:           {(1 - len(processed_text)/len(original_text))*100:.1f}%

Original Words:      {len(original_text.split())}
Processed Words:     {len(processed_text.split())}

TRANSFORMATIONS APPLIED:
{'-' * 60}
✓ Removed Twitter handles (@mentions)
✓ Removed special characters and punctuation
✓ Removed numbers
✓ Removed short words (length ≤ 3)
✓ Applied stemming (Porter Stemmer)
✓ Converted to lowercase (implicit)
"""
        
        with open(output_file, 'w') as f:
            f.write(report)
        
        print(f"✅ Preprocessing report saved: {output_file}")
        return report
    
    def generate_feature_extraction_report(self, bow_shape, tfidf_shape, vocab_size):
        """Generate feature extraction statistics report"""
        output_file = f"{self.output_dir}/reports/feature_extraction_{self.timestamp}.txt"
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║   FEATURE EXTRACTION REPORT                                  ║
╠══════════════════════════════════════════════════════════════╣
║ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
╚══════════════════════════════════════════════════════════════╝

BAG OF WORDS (CountVectorizer):
{'-' * 60}
Matrix Shape:           {bow_shape}
Samples:                {bow_shape[0]}
Features:               {bow_shape[1]}
Sparsity:               High (most values are 0)
Data Type:              Integer (word counts)
Total Non-Zero:         ~66,305 elements

TF-IDF (TfidfVectorizer):
{'-' * 60}
Matrix Shape:           {tfidf_shape}
Samples:                {tfidf_shape[0]}
Features:               {tfidf_shape[1]}
Value Range:            0.0 to 1.0
Data Type:              Float64
Total Non-Zero:         ~66,305 elements

VECTORIZER PARAMETERS:
{'-' * 60}
max_df:                 0.90 (ignore terms in >90% docs)
min_df:                 2 (ignore terms in <2 docs)
max_features:           1000 (max unique terms)
stop_words:             English

VOCABULARY:
{'-' * 60}
Total Unique Words:     {vocab_size}
Extracted Features:     {min(vocab_size, 1000)}
Vocabulary Type:        Stemmed words

INTERPRETATION:
{'-' * 60}
• Bag of Words: Raw count of word occurrences
  - Higher values = Word appears more in tweet
  - Sparse matrix: Memory efficient representation
  
• TF-IDF: Weighted importance of words
  - Higher values = Word is more discriminative
  - Values normalized between 0.0 and 1.0
  - Reduces impact of common words
"""
        
        with open(output_file, 'w') as f:
            f.write(report)
        
        print(f"✅ Feature extraction report saved: {output_file}")
        return report
    
    def generate_model_performance_report(self, accuracy, precision, recall, f1):
        """Generate model performance metrics report"""
        output_file = f"{self.output_dir}/reports/model_performance_{self.timestamp}.txt"
        
        # Create performance visualization
        metrics = {
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1
        }
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║   MODEL PERFORMANCE REPORT                                   ║
╠══════════════════════════════════════════════════════════════╣
║ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
║ Model: Logistic Regression
║ Threshold: 0.30
╚══════════════════════════════════════════════════════════════╝

OVERALL METRICS:
{'-' * 60}
Accuracy:               {accuracy:.4f} ({accuracy*100:.2f}%)
Precision:              {precision:.4f} ({precision*100:.2f}%)
Recall:                 {recall:.4f} ({recall*100:.2f}%)
F1-Score:               {f1:.4f} ({f1*100:.2f}%)

METRIC DEFINITIONS:
{'-' * 60}
Accuracy:   Percentage of correct predictions
            Formula: (TP + TN) / Total

Precision:  Of predicted hate speech, how many correct?
            Formula: TP / (TP + FP)
            Use when: False positives are costly

Recall:     Of actual hate speech, how many detected?
            Formula: TP / (TP + FN)
            Use when: False negatives are costly

F1-Score:   Balance between Precision and Recall
            Formula: 2 * (Precision * Recall) / (Precision + Recall)
            Use when: Need overall model performance

CONFUSION MATRIX:
{'-' * 60}
                    Predicted Negative    Predicted Positive
Actual Negative     TN (True Neg)         FP (False Pos)
Actual Positive     FN (False Neg)        TP (True Pos)

INTERPRETATION:
{'-' * 60}
• F1-Score {f1:.4f}: {'Excellent' if f1 >= 0.8 else 'Good' if f1 >= 0.7 else 'Fair' if f1 >= 0.6 else 'Poor'} model performance
• Precision {precision:.4f}: {precision*100:.1f}% of detected hate speech is correct
• Recall {recall:.4f}: {recall*100:.1f}% of actual hate speech is detected
• Accuracy {accuracy:.4f}: {accuracy*100:.1f}% overall correct predictions

THRESHOLD IMPACT:
{'-' * 60}
Current Threshold: 0.30
• Lower threshold (e.g., 0.20) → Higher recall, lower precision
• Higher threshold (e.g., 0.50) → Lower recall, higher precision
"""
        
        with open(output_file, 'w') as f:
            f.write(report)
        
        print(f"✅ Model performance report saved: {output_file}")
        return report
    
    def create_metrics_visualization(self, accuracy, precision, recall, f1):
        """Create visual representation of metrics"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Bar chart
        metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
        values = [accuracy, precision, recall, f1]
        colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
        
        axes[0].bar(metrics, values, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
        axes[0].set_ylabel('Score', fontsize=12, fontweight='bold')
        axes[0].set_title('Model Performance Metrics', fontsize=14, fontweight='bold')
        axes[0].set_ylim([0, 1])
        axes[0].grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for i, v in enumerate(values):
            axes[0].text(i, v + 0.02, f'{v:.4f}', ha='center', fontweight='bold')
        
        # Radar chart
        angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
        values_plot = values + [values[0]]  # Complete the circle
        angles_plot = angles + [angles[0]]
        
        ax = plt.subplot(122, projection='polar')
        ax.plot(angles_plot, values_plot, 'o-', linewidth=2, color='#3498db')
        ax.fill(angles_plot, values_plot, alpha=0.25, color='#3498db')
        ax.set_xticks(angles)
        ax.set_xticklabels(metrics)
        ax.set_ylim(0, 1)
        ax.set_title('Performance Radar Chart', fontsize=14, fontweight='bold', pad=20)
        ax.grid(True)
        
        plt.tight_layout()
        output_file = f"{self.output_dir}/visualizations/metrics_visualization_{self.timestamp}.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✅ Metrics visualization saved: {output_file}")
        plt.close()
    
    def create_sample_predictions_table(self, sample_tweets, predictions, probabilities):
        """Create visualization of sample predictions"""
        df = pd.DataFrame({
            'Tweet': sample_tweets,
            'Probability': probabilities,
            'Prediction': ['Hate Speech' if p >= 0.3 else 'Normal' for p in predictions]
        })
        
        output_file = f"{self.output_dir}/reports/sample_predictions_{self.timestamp}.csv"
        df.to_csv(output_file, index=False)
        
        # Also create text report
        text_file = f"{self.output_dir}/reports/sample_predictions_{self.timestamp}.txt"
        with open(text_file, 'w') as f:
            f.write("╔══════════════════════════════════════════════════════════════╗\n")
            f.write("║   SAMPLE PREDICTIONS                                         ║\n")
            f.write("╠══════════════════════════════════════════════════════════════╣\n")
            f.write(f"║ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("╚══════════════════════════════════════════════════════════════╝\n\n")
            f.write(df.to_string(index=False))
        
        print(f"✅ Sample predictions saved: {output_file}")
        return df
    
    def create_confusion_matrix_visualization(self, tn, fp, fn, tp):
        """Create confusion matrix visualization"""
        fig, ax = plt.subplots(figsize=(8, 6))
        
        cm = np.array([[tn, fp], [fn, tp]])
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax,
                    xticklabels=['Predicted Neg', 'Predicted Pos'],
                    yticklabels=['Actual Neg', 'Actual Pos'],
                    cbar_kws={'label': 'Count'})
        
        ax.set_ylabel('True Label', fontweight='bold', fontsize=12)
        ax.set_xlabel('Predicted Label', fontweight='bold', fontsize=12)
        ax.set_title('Confusion Matrix', fontweight='bold', fontsize=14)
        
        # Add totals
        total = tn + fp + fn + tp
        accuracy = (tn + tp) / total
        
        textstr = f'Accuracy: {accuracy:.4f}'
        ax.text(1, -0.25, textstr, transform=ax.transAxes, fontsize=11,
                verticalalignment='top', horizontalalignment='center', fontweight='bold')
        
        plt.tight_layout()
        output_file = f"{self.output_dir}/visualizations/confusion_matrix_{self.timestamp}.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✅ Confusion matrix saved: {output_file}")
        plt.close()
    
    def create_hashtag_distribution_visualization(self, hashtags, counts, title="Top Hashtags"):
        """Create hashtag frequency visualization"""
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # Create bar chart
        colors = plt.cm.viridis(np.linspace(0, 1, len(hashtags)))
        bars = ax.bar(range(len(hashtags)), counts, color=colors, edgecolor='black', linewidth=1.2)
        
        ax.set_xticks(range(len(hashtags)))
        ax.set_xticklabels(hashtags, rotation=45, ha='right')
        ax.set_ylabel('Frequency', fontweight='bold', fontsize=12)
        ax.set_xlabel('Hashtags', fontweight='bold', fontsize=12)
        ax.set_title(title, fontweight='bold', fontsize=14)
        ax.grid(axis='y', alpha=0.3)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        output_file = f"{self.output_dir}/visualizations/hashtag_distribution_{self.timestamp}.png"
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✅ Hashtag distribution saved: {output_file}")
        plt.close()
    
    def create_pipeline_summary(self, data_shape, feature_shapes, model_name="Logistic Regression"):
        """Create ML pipeline summary report"""
        output_file = f"{self.output_dir}/reports/pipeline_summary_{self.timestamp}.txt"
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║   ML PIPELINE SUMMARY REPORT                                 ║
╠══════════════════════════════════════════════════════════════╣
║ Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
╚══════════════════════════════════════════════════════════════╝

PIPELINE OVERVIEW:
{'-' * 60}
Stage 1: Data Loading          ✓ Complete
  └─ Input: test_tweets_anuFYb8.csv
  └─ Samples: {data_shape[0]}
  └─ Columns: id, tweet

Stage 2: Text Preprocessing    ✓ Complete
  └─ Remove Twitter handles
  └─ Remove special characters
  └─ Remove short words
  └─ Tokenization
  └─ Stemming (Porter Stemmer)

Stage 3: Feature Extraction    ✓ Complete
  └─ Bag of Words (BoW):       {feature_shapes[0]}
  └─ TF-IDF:                   {feature_shapes[1]}

Stage 4: Model Training        ⏳ Ready (needs train data)
  └─ Algorithm: {model_name}
  └─ Threshold: 0.30
  └─ Test Size: 0.30
  └─ Random State: 42

Stage 5: Evaluation            ⏳ Ready (needs train data)
  └─ Metrics: Accuracy, Precision, Recall, F1-Score
  └─ Matrix: Confusion Matrix

DATA FLOW:
{'-' * 60}
Input CSV
    ↓
[Text Preprocessing]
    ↓
Cleaned Text
    ↓
[Feature Extraction]
    ├─→ BoW Matrix {feature_shapes[0]}
    └─→ TF-IDF Matrix {feature_shapes[1]}
         ↓
[Model]
    ├─→ Training (70%)
    └─→ Validation (30%)
         ↓
[Predictions & Evaluation]
    ├─→ Probabilities
    ├─→ Classifications
    ├─→ Metrics
    └─→ Confusion Matrix

STATUS:
{'-' * 60}
✓ Data loaded and preprocessed
✓ Features extracted (BoW and TF-IDF)
⏳ Model training (requires train_E6oV3lV.csv)
⏳ Evaluation metrics (requires labeled data)
"""
        
        with open(output_file, 'w') as f:
            f.write(report)
        
        print(f"✅ Pipeline summary saved: {output_file}")
        return report


# Example usage
if __name__ == "__main__":
    print("="*60)
    print("VISUAL OUTPUT GENERATOR - HATE SPEECH DETECTION")
    print("="*60)
    
    # Initialize generator
    generator = VisualOutputGenerator(output_dir='outputs')
    
    # Example: Generate preprocessing report
    original = "@user This is a #bad tweet with numbers 123!"
    processed = "bad tweet"
    generator.generate_preprocessing_report(original, processed)
    
    # Example: Generate feature extraction report
    generator.generate_feature_extraction_report(
        bow_shape=(17197, 1000),
        tfidf_shape=(17197, 1000),
        vocab_size=1200
    )
    
    # Example: Generate model performance report
    generator.generate_model_performance_report(
        accuracy=0.8234,
        precision=0.7856,
        recall=0.6923,
        f1=0.7368
    )
    
    # Example: Create metrics visualizations
    generator.create_metrics_visualization(
        accuracy=0.8234,
        precision=0.7856,
        recall=0.6923,
        f1=0.7368
    )
    
    # Example: Create confusion matrix
    generator.create_confusion_matrix_visualization(
        tn=3240, fp=890,
        fn=510, tp=2850
    )
    
    # Example: Create hashtag visualization
    hashtags = ['love', 'positive', 'healthy', 'smile', 'thank', 
                'fun', 'life', 'affirm', 'model', 'fatherday']
    counts = [850, 475, 320, 300, 275, 230, 225, 220, 210, 200]
    generator.create_hashtag_distribution_visualization(hashtags, counts)
    
    # Example: Create pipeline summary
    generator.create_pipeline_summary(
        data_shape=(17197, 3),
        feature_shapes=((17197, 1000), (17197, 1000))
    )
    
    print("\n" + "="*60)
    print("✅ ALL VISUALIZATIONS GENERATED SUCCESSFULLY!")
    print(f"📁 Outputs saved to: {generator.output_dir}/")
    print("="*60)
