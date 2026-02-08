# Smart Resume Screening System using Machine Learning

An intelligent resume screening application that uses Machine Learning and Natural Language Processing (NLP) to automatically match resumes with job descriptions, helping recruiters efficiently identify the best candidates.

## 🎯 Features

- **Machine Learning-Based Matching**: Uses TF-IDF vectorization and cosine similarity to match resumes with job descriptions
- **NLP Text Processing**: Implements tokenization, stop-word removal, and lemmatization
- **Skill Extraction**: Automatically identifies technical and soft skills from resumes
- **Multiple File Format Support**: Accepts PDF, DOCX, and TXT files
- **Visual Results Dashboard**: Beautiful, interactive interface showing match scores and skill analysis
- **Batch Processing**: Screen multiple resumes simultaneously
- **Ranking System**: Automatically ranks candidates based on match score

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Flask**: Web framework for the application interface
- **Scikit-learn**: Machine learning library for TF-IDF and cosine similarity
- **NLTK**: Natural Language Processing toolkit
- **PyPDF2**: PDF text extraction
- **python-docx**: DOCX file processing
- **NumPy**: Numerical computations

## 📋 Requirements

See `requirements.txt` for all dependencies:
- Flask
- PyPDF2
- python-docx
- scikit-learn
- nltk
- numpy
- werkzeug

## 🚀 Installation

1. **Clone or download the project**

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Download NLTK data** (will be done automatically on first run):
The application will automatically download required NLTK data (punkt, stopwords, wordnet) on first execution.

## 📁 Project Structure

```
resume-screening-system/
│
├── app.py                  # Main Flask application
├── resume_matcher.py       # ML and NLP processing module
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
│
├── templates/
│   └── index.html         # Web interface
│
└── uploads/               # Temporary storage for uploaded files (auto-created)
```

## 💻 Usage

1. **Start the Flask server**:
```bash
python app.py
```

2. **Open your browser** and navigate to:
```
http://127.0.0.1:5000
```

3. **Use the application**:
   - Enter the job description in the text area
   - Upload one or multiple resume files (PDF, DOCX, or TXT)
   - Click "Screen Resumes"
   - View the ranked results with match scores and skill analysis

## 🔬 How It Works

### 1. Text Preprocessing
- Converts text to lowercase
- Removes special characters and numbers
- Tokenizes text into words
- Removes common stop words
- Applies lemmatization to reduce words to base form

### 2. Feature Extraction
- **TF-IDF Vectorization**: Converts text into numerical vectors based on term frequency and inverse document frequency
- **Skill Extraction**: Identifies technical skills, programming languages, frameworks, and soft skills

### 3. Matching Algorithm
- Calculates cosine similarity between job description and resume TF-IDF vectors
- Computes skill match percentage
- Combines scores with weighted formula: `Overall Score = (TF-IDF Score × 0.6) + (Skill Match × 0.4)`

### 4. Ranking & Recommendation
- **Highly Recommended** (≥75%): Strong match with job requirements
- **Recommended** (60-74%): Good match with most requirements
- **Maybe** (40-59%): Moderate match, some gaps
- **Not Recommended** (<40%): Weak match

## 📊 Output Information

For each resume, the system provides:
- **Match Score**: Overall percentage match (0-100%)
- **Recommendation**: Hiring recommendation based on score
- **Matched Skills**: Skills found in both resume and job description
- **Missing Skills**: Required skills not found in resume
- **Ranking**: Resumes sorted from highest to lowest match

## 🎨 Web Interface Features

- Modern, responsive design
- Drag-and-drop file upload
- Real-time file validation
- Loading animations during processing
- Color-coded match scores (green/yellow/red)
- Detailed skill breakdown for each candidate
- Mobile-friendly interface

## 🔧 Customization

### Adding More Skills
Edit the `common_skills` set in `resume_matcher.py`:
```python
self.common_skills = {
    'python', 'java', 'your_skill_here',
    # Add more skills...
}
```

### Adjusting Match Weights
Modify the scoring formula in the `calculate_match` method:
```python
overall_score = (tfidf_score * 0.6) + (skill_match_score * 0.4)
```

### Changing Recommendation Thresholds
Update threshold values in the `calculate_match` method:
```python
if overall_score >= 75:  # Change this value
    recommendation = "Highly Recommended"
```

## 🧪 Example Use Cases

1. **HR Departments**: Screen hundreds of applications quickly
2. **Recruitment Agencies**: Match candidates to multiple job openings
3. **Job Portals**: Automated candidate ranking system
4. **Hiring Managers**: Initial resume filtering before manual review

## 📈 Performance

- Processes average resume (1-2 pages) in < 1 second
- Handles batch processing of 10-50 resumes efficiently
- Accurate skill extraction with 100+ predefined skills
- TF-IDF similarity provides context-aware matching

## 🔒 Security & Privacy

- Files are temporarily stored only during processing
- Automatic cleanup after screening
- No permanent data storage
- All processing happens server-side

## 🐛 Troubleshooting

**Issue**: NLTK data not found
**Solution**: The app automatically downloads required data. If it fails, manually run:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

**Issue**: PDF text extraction fails
**Solution**: Ensure PDF is not image-based. For scanned PDFs, OCR preprocessing is required.

**Issue**: File upload fails
**Solution**: Check file size is under 16MB and format is PDF, DOCX, or TXT.

## 🚀 Future Enhancements

- [ ] Deep learning models (BERT, transformers) for better semantic matching
- [ ] Experience level extraction and matching
- [ ] Education qualification matching
- [ ] Location-based filtering
- [ ] Salary expectation analysis
- [ ] Integration with ATS systems
- [ ] Email notification for top candidates
- [ ] Resume parsing for structured data extraction
- [ ] Multi-language support
- [ ] PDF report generation

## 📝 License

This project is open source and available for educational and commercial use.

## 👨‍💻 Author

Developed as a demonstration of Machine Learning and NLP applications in HR technology.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Contact

For questions or support, please open an issue in the repository.

---

**Note**: This system is designed to assist recruiters in the initial screening process. Final hiring decisions should always involve human judgment and comprehensive evaluation.
