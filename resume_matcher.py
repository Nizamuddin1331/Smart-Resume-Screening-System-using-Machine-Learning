import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class ResumeScreener:
    def __init__(self):
        """Initialize the Resume Screener with NLP tools"""
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
        
        try:
            nltk.data.find('tokenizers/punkt_tab')
        except LookupError:
            nltk.download('punkt_tab', quiet=True)
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet', quiet=True)
        
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
        
        # Common skills and keywords (expanded for better matching)
        self.common_skills = {
            # Programming Languages
            'python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin', 'r',
            'typescript', 'go', 'rust', 'scala',
            
            # ML/AI/Data Science
            'machine learning', 'deep learning', 'nlp', 'natural language processing',
            'data science', 'ai', 'artificial intelligence', 'data analysis',
            'neural networks', 'computer vision', 'reinforcement learning',
            
            # ML Frameworks & Libraries
            'tensorflow', 'pytorch', 'keras', 'scikit-learn', 'sklearn', 'sci-kit learn',
            'pandas', 'numpy', 'scipy', 'matplotlib', 'seaborn', 'xgboost',
            'lightgbm', 'catboost', 'hugging face', 'transformers', 'bert',
            'spacy', 'nltk', 'opencv', 'pillow',
            
            # Databases
            'sql', 'mysql', 'postgresql', 'postgres', 'mongodb', 'nosql', 'database',
            'redis', 'cassandra', 'dynamodb', 'sqlite', 'oracle', 'mssql',
            'database management', 'data modeling',
            
            # Web Frameworks
            'flask', 'django', 'fastapi', 'react', 'angular', 'vue', 'vue.js',
            'node.js', 'nodejs', 'express', 'spring', 'asp.net',
            
            # Cloud & DevOps
            'aws', 'amazon web services', 'azure', 'gcp', 'google cloud', 'cloud',
            'docker', 'kubernetes', 'k8s', 'jenkins', 'terraform', 'ansible',
            'ec2', 's3', 'lambda', 'sagemaker',
            
            # Version Control & Methodologies
            'git', 'github', 'gitlab', 'bitbucket', 'agile', 'scrum', 'devops', 
            'ci/cd', 'continuous integration', 'continuous deployment',
            'test-driven development', 'tdd',
            
            # Frontend
            'html', 'html5', 'css', 'css3', 'bootstrap', 'tailwind', 'sass', 'less',
            'jquery', 'webpack', 'babel',
            
            # API & Architecture
            'api', 'rest', 'rest api', 'restful', 'graphql', 'microservices',
            'api development', 'web services',
            
            # Big Data & Processing
            'spark', 'hadoop', 'kafka', 'airflow', 'etl', 'data pipeline',
            'big data', 'pyspark',
            
            # Soft Skills
            'leadership', 'communication', 'teamwork', 'team collaboration',
            'problem solving', 'problem-solving', 'analytical', 'critical thinking',
            
            # Other Technical
            'linux', 'unix', 'bash', 'shell scripting', 'powershell',
            'jupyter', 'anaconda', 'virtual environment', 'testing',
            'unit testing', 'integration testing', 'debugging'
        }
    
    def preprocess_text(self, text):
        """
        Preprocess text using NLP techniques:
        - Convert to lowercase
        - Remove special characters
        - Tokenization
        - Stop-word removal
        - Lemmatization
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and digits (keep spaces)
        text = re.sub(r'[^a-zA-Z\s]', ' ', text)
        
        # Tokenization
        tokens = word_tokenize(text)
        
        # Remove stop words and lemmatize
        processed_tokens = [
            self.lemmatizer.lemmatize(token) 
            for token in tokens 
            if token not in self.stop_words and len(token) > 2
        ]
        
        return ' '.join(processed_tokens)
    
    def extract_skills(self, text):
        """Extract skills from text based on common skill keywords"""
        text_lower = text.lower()
        found_skills = []
        
        for skill in self.common_skills:
            # Use word boundaries to match whole words/phrases
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.append(skill)
        
        return found_skills
    
    def calculate_tfidf_similarity(self, resume_text, job_description):
        """Calculate TF-IDF based cosine similarity"""
        # Preprocess texts
        resume_processed = self.preprocess_text(resume_text)
        job_processed = self.preprocess_text(job_description)
        
        # Create TF-IDF vectors
        try:
            tfidf_matrix = self.vectorizer.fit_transform([job_processed, resume_processed])
            
            # Calculate cosine similarity
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            
            return similarity * 100  # Convert to percentage
        except Exception as e:
            print(f"Error calculating TF-IDF similarity: {e}")
            return 0.0
    
    def calculate_skill_match(self, resume_skills, job_skills):
        """Calculate skill match percentage"""
        if not job_skills:
            return 0.0
        
        matched_skills = set(resume_skills).intersection(set(job_skills))
        match_percentage = (len(matched_skills) / len(job_skills)) * 100
        
        return match_percentage
    
    def calculate_match(self, resume_text, job_description):
        """
        Calculate overall match score between resume and job description
        Returns detailed match information
        """
        # Extract skills from both texts
        resume_skills = self.extract_skills(resume_text)
        job_skills = self.extract_skills(job_description)
        
        # Calculate TF-IDF similarity
        tfidf_score = self.calculate_tfidf_similarity(resume_text, job_description)
        
        # Calculate skill match
        skill_match_score = self.calculate_skill_match(resume_skills, job_skills)
        
        # Calculate weighted overall score (50% TF-IDF, 50% skill match for better balance)
        overall_score = (tfidf_score * 0.5) + (skill_match_score * 0.5)
        
        # Find matched and missing skills
        matched_skills = list(set(resume_skills).intersection(set(job_skills)))
        missing_skills = list(set(job_skills) - set(resume_skills))
        
        # Generate recommendation
        if overall_score >= 70:
            recommendation = "Highly Recommended - Strong match"
        elif overall_score >= 55:
            recommendation = "Recommended - Good match"
        elif overall_score >= 35:
            recommendation = "Maybe - Moderate match"
        else:
            recommendation = "Not Recommended - Weak match"
        
        return {
            'match_score': overall_score,
            'tfidf_score': tfidf_score,
            'skill_match_score': skill_match_score,
            'matched_skills': matched_skills,
            'missing_skills': missing_skills,
            'total_resume_skills': len(resume_skills),
            'total_job_skills': len(job_skills),
            'recommendation': recommendation
        }
    
    def rank_resumes(self, resumes, job_description):
        """
        Rank multiple resumes against a job description
        Returns sorted list of results
        """
        results = []
        
        for resume_id, resume_text in resumes.items():
            match_data = self.calculate_match(resume_text, job_description)
            match_data['resume_id'] = resume_id
            results.append(match_data)
        
        # Sort by match score (descending)
        results.sort(key=lambda x: x['match_score'], reverse=True)
        
        return results