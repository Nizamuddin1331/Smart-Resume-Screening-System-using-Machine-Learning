# Quick Start Guide - Smart Resume Screening System

## Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
# Start the Flask server
python app.py
```

The application will start on `http://127.0.0.1:5000`

### Step 3: Use the System

1. **Open your browser** and go to `http://127.0.0.1:5000`

2. **Enter Job Description**:
   - Paste the complete job description including:
     - Job title and responsibilities
     - Required skills and qualifications
     - Preferred qualifications
     - Experience requirements

3. **Upload Resumes**:
   - Click the upload area or drag and drop files
   - Supported formats: PDF, DOCX, TXT
   - You can upload multiple files at once
   - Maximum file size: 16MB per file

4. **View Results**:
   - Click "Screen Resumes" button
   - Wait for ML processing (usually takes 1-2 seconds per resume)
   - View ranked results with:
     - Match scores (0-100%)
     - Hiring recommendations
     - Matched skills
     - Missing skills

## Testing the System

### Option 1: Use Sample Files
We've provided sample resumes and job description in the `sample_resumes/` folder:

1. Copy the job description from `sample_job_description.txt`
2. Upload one or more resume files:
   - `resume_john_doe.txt` (Expected: High match ~75%+)
   - `resume_jane_smith.txt` (Expected: Low match ~40%)
   - `resume_alex_johnson.txt` (Expected: Very high match ~85%+)

### Option 2: Run Test Script
```bash
python test_screener.py
```

This will demonstrate the ML matching algorithm with sample data.

## Understanding the Results

### Match Score Interpretation
- **75-100%**: Highly Recommended (Strong match)
- **60-74%**: Recommended (Good match)
- **40-59%**: Maybe (Moderate match)
- **0-39%**: Not Recommended (Weak match)

### Score Components
- **TF-IDF Score** (60% weight): Measures overall content similarity
- **Skill Match Score** (40% weight): Percentage of required skills found

### Matched Skills
Shows specific skills/technologies found in both the resume and job description.

### Missing Skills
Shows required skills from the job description that weren't found in the resume.

## Tips for Best Results

### For Job Descriptions:
- Be specific about required skills and technologies
- Include both technical and soft skills
- Mention frameworks, tools, and methodologies
- Add experience level requirements

### For Resumes:
- Use clear, standard section headings (Skills, Experience, etc.)
- List technical skills explicitly
- Include project descriptions with technologies used
- Use industry-standard terminology

## Common Use Cases

### 1. Initial Screening
Upload all applicant resumes to quickly identify top candidates.

### 2. Skill Gap Analysis
Check which required skills candidates are missing.

### 3. Bulk Processing
Screen 10-50 resumes simultaneously for efficiency.

### 4. Comparative Analysis
Compare multiple candidates side-by-side based on match scores.

## Troubleshooting

**Problem**: No results showing
**Solution**: Check that job description and files are uploaded correctly

**Problem**: Low match scores for good candidates
**Solution**: Ensure resume includes relevant keywords and skills from job description

**Problem**: File upload fails
**Solution**: Verify file format (PDF, DOCX, TXT) and size (<16MB)

**Problem**: NLTK errors
**Solution**: The required NLTK data downloads automatically on first run

## Technical Architecture

```
User Upload → Text Extraction → NLP Preprocessing → 
→ TF-IDF Vectorization → Similarity Calculation → 
→ Skill Matching → Score Ranking → Results Display
```

## Next Steps

1. **Customize Skills**: Edit `resume_matcher.py` to add industry-specific skills
2. **Adjust Weights**: Modify scoring formula based on your preferences
3. **Add Features**: Extend with experience extraction, location filtering, etc.

## Support

For issues or questions:
1. Check the README.md for detailed documentation
2. Review the code comments in `resume_matcher.py`
3. Run `test_screener.py` to verify setup

---

Happy Screening! 🎯
