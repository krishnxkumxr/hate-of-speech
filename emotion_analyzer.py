"""
Emotion Analyzer for Social Media Tweets
Detects multiple emotions: Happy, Sad, Angry, Fear, Neutral, Disgusted, Surprised
"""

import pandas as pd
import json
import os
from datetime import datetime
from collections import defaultdict

class EmotionAnalyzer:
    """Analyze and classify emotions in tweets"""
    
    def __init__(self, csv_file='test_tweets_anuFYb8.csv'):
        self.csv_file = csv_file
        self.tweets_df = None
        self.emotion_keywords = self._get_emotion_keywords()
        self.emotions = ['Happy', 'Sad', 'Angry', 'Fear', 'Neutral', 'Disgusted', 'Surprised']
        
    def _get_emotion_keywords(self):
        """Define keywords for each emotion"""
        return {
            'happy': {
                'keywords': ['love', 'happy', 'beautiful', 'wonderful', 'great', 'amazing', 'awesome', 
                           'excited', 'joyful', 'blessed', 'grateful', 'fantastic', 'excellent', 'fun',
                           'celebrate', 'smile', 'laugh', 'joy', 'proud', 'perfect', 'lucky', 'best',
                           'good', 'nice', 'positive', 'lovely', 'sweet', 'perfect', 'brilliant'],
                'weight': 1.0
            },
            'sad': {
                'keywords': ['sad', 'unhappy', 'depressed', 'miserable', 'lonely', 'broke', 'cry', 
                           'tears', 'heartbreak', 'pain', 'suffering', 'lost', 'alone', 'down',
                           'died', 'rip', 'devastated', 'disappointed', 'sorry', 'miss', 'hurt',
                           'ache', 'grieve', 'weep', 'despair', 'melancholy'],
                'weight': 1.0
            },
            'angry': {
                'keywords': ['hate', 'angry', 'furious', 'rage', 'mad', 'pissed', 'damn', 'hell',
                           'fuck', 'bastard', 'idiot', 'stupid', 'worst', 'terrible', 'awful',
                           'disgusting', 'infuriate', 'outrage', 'rant', 'frustrated', 'annoyed',
                           'irritated', 'aggressive', 'hostile', 'violent', 'destroy'],
                'weight': 1.2
            },
            'fear': {
                'keywords': ['fear', 'scared', 'afraid', 'terror', 'panic', 'anxiety', 'worried',
                           'nervous', 'frightened', 'dread', 'alarm', 'horror', 'danger', 'threat',
                           'risk', 'unsafe', 'vulnerable', 'helpless', 'desperate', 'desperate'],
                'weight': 1.0
            },
            'neutral': {
                'keywords': ['information', 'data', 'report', 'news', 'update', 'find', 'check',
                           'read', 'look', 'search', 'question', 'ask', 'wondering', 'explain',
                           'suggest', 'recommend', 'think', 'believe', 'seem', 'appear'],
                'weight': 0.8
            },
            'disgusted': {
                'keywords': ['disgusting', 'gross', 'nasty', 'vile', 'repulsive', 'revolting',
                           'yuck', 'ugh', 'disgusted', 'abhorrent', 'loathsome', 'sickening',
                           'acorn', 'foul', 'obscene', 'perverted', 'depraved', 'wretched'],
                'weight': 1.1
            },
            'surprised': {
                'keywords': ['surprised', 'shocked', 'amazed', 'wow', 'omg', 'incredible', 'unbelievable',
                           'astonished', 'astounded', 'stunned', 'unexpected', 'sudden', 'wow',
                           'finally', 'at', 'last', 'never', 'thought', 'couldn\'t', 'believe'],
                'weight': 0.9
            }
        }
    
    def load_tweets(self):
        """Load tweets from CSV file"""
        if not os.path.exists(self.csv_file):
            raise FileNotFoundError(f"CSV file not found: {self.csv_file}")
        
        self.tweets_df = pd.read_csv(self.csv_file)
        print(f"✅ Loaded {len(self.tweets_df)} tweets")
        return self.tweets_df
    
    def classify_emotion(self, text):
        """Classify single tweet into emotion category"""
        text_lower = text.lower()
        emotion_scores = defaultdict(float)
        
        # Score each emotion based on keyword matches
        for emotion, data in self.emotion_keywords.items():
            for keyword in data['keywords']:
                if keyword in text_lower:
                    emotion_scores[emotion] += data['weight']
        
        # Special handling for hate speech / anger
        hate_keywords = ['hate', 'racist', 'racist', 'discrimination', 'xenophob', 'homophob',
                        'sexist', 'misogyn', 'supremacist', 'fascist', 'bigot']
        for keyword in hate_keywords:
            if keyword in text_lower:
                emotion_scores['angry'] += 2.0
        
        # If no emotion detected, classify as neutral
        if not emotion_scores:
            return 'Neutral', 0.3
        
        # Get emotion with highest score
        top_emotion = max(emotion_scores, key=emotion_scores.get)
        confidence = min(0.95, emotion_scores[top_emotion] / 10.0)
        
        return top_emotion.capitalize(), confidence
    
    def analyze_all_tweets(self):
        """Analyze all tweets and return results"""
        if self.tweets_df is None:
            self.load_tweets()
        
        results = []
        emotion_counts = defaultdict(int)
        
        for idx, row in self.tweets_df.iterrows():
            tweet_id = row['id']
            tweet_text = str(row['tweet'])
            emotion, confidence = self.classify_emotion(tweet_text)
            
            emotion_counts[emotion] += 1
            results.append({
                'id': tweet_id,
                'text': tweet_text,
                'emotion': emotion,
                'confidence': round(confidence, 4)
            })
        
        print(f"\n📊 Emotion Analysis Results:")
        print("=" * 60)
        for emotion, count in sorted(emotion_counts.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / len(results)) * 100
            print(f"  {emotion:12} : {count:5} tweets ({percentage:5.1f}%)")
        
        return results, dict(emotion_counts)
    
    def get_top_tweets_by_emotion(self, results, emotion, top_n=5):
        """Get top N confident tweets for a specific emotion"""
        emotion_tweets = [r for r in results if r['emotion'] == emotion]
        emotion_tweets.sort(key=lambda x: x['confidence'], reverse=True)
        return emotion_tweets[:top_n]
    
    def generate_statistics(self, results, emotion_counts):
        """Generate statistics for dashboard"""
        total_tweets = len(results)
        
        stats = {
            'total_tweets': total_tweets,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'emotions': {},
            'top_tweets_by_emotion': {}
        }
        
        # Calculate percentages
        for emotion, count in emotion_counts.items():
            percentage = (count / total_tweets) * 100
            stats['emotions'][emotion] = {
                'count': count,
                'percentage': round(percentage, 2)
            }
            # Get top tweets for each emotion
            stats['top_tweets_by_emotion'][emotion] = self.get_top_tweets_by_emotion(results, emotion, 3)
        
        return stats
    
    def save_results_json(self, results, emotion_counts, output_file='tweets_emotion_analysis.json'):
        """Save emotion analysis results to JSON"""
        stats = self.generate_statistics(results, emotion_counts)
        
        output = {
            'statistics': stats,
            'all_tweets': results
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Results saved to {output_file}")
        return output_file
    
    def create_dashboard_data(self, results, emotion_counts):
        """Create formatted data for dashboard"""
        stats = self.generate_statistics(results, emotion_counts)
        
        dashboard_data = {
            'total_tweets': stats['total_tweets'],
            'timestamp': stats['timestamp'],
            'emotion_distribution': {
                emotion: {
                    'count': stats['emotions'][emotion]['count'],
                    'percentage': stats['emotions'][emotion]['percentage']
                }
                for emotion in sorted(stats['emotions'].keys(), 
                                    key=lambda x: stats['emotions'][x]['count'], 
                                    reverse=True)
            },
            'sample_tweets': {}
        }
        
        # Add sample tweets for each emotion
        for emotion in self.emotions:
            tweets = [r for r in results if r['emotion'] == emotion]
            tweets.sort(key=lambda x: x['confidence'], reverse=True)
            dashboard_data['sample_tweets'][emotion] = tweets[:5]
        
        return dashboard_data

def main():
    """Main execution"""
    print("\n" + "="*70)
    print("🎯 EMOTION ANALYZER - TWEET CLASSIFICATION")
    print("="*70 + "\n")
    
    # Initialize analyzer
    analyzer = EmotionAnalyzer('test_tweets_anuFYb8.csv')
    
    # Load and analyze tweets
    print("📂 Loading tweets from CSV...")
    analyzer.load_tweets()
    
    print("\n🔍 Classifying emotions...")
    results, emotion_counts = analyzer.analyze_all_tweets()
    
    # Save results
    print("\n💾 Saving results...")
    analyzer.save_results_json(results, emotion_counts)
    
    # Generate dashboard data
    dashboard_data = analyzer.create_dashboard_data(results, emotion_counts)
    
    # Save dashboard data
    with open('dashboard_emotion_data.json', 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
    print("✅ Dashboard data saved to dashboard_emotion_data.json")
    
    print("\n" + "="*70)
    print("✨ EMOTION ANALYSIS COMPLETE!")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
