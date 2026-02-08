"""
Test script to demonstrate the Resume Screening System functionality
"""

from resume_matcher import ResumeScreener

# Sample job description
job_description = """
Senior Python Developer

We are looking for an experienced Python developer to join our data science team.

Requirements:
- 5+ years of experience in Python development
- Strong knowledge of machine learning and deep learning
- Experience with NLP and text processing
- Proficiency in scikit-learn, TensorFlow, or PyTorch
- Experience with Flask or Django web frameworks
- Knowledge of SQL and database management
- Familiarity with cloud platforms (AWS, Azure, or GCP)
- Strong problem-solving and communication skills
- Experience with Git and Agile methodologies

Nice to have:
- Experience with Docker and Kubernetes
- Knowledge of React or Angular
- Previous experience in building AI-powered applications
"""

# Sample resumes
resume1 = """
John Doe
Senior Software Engineer

EXPERIENCE:
6 years of professional experience in Python development and machine learning.
Built multiple NLP applications for text classification and sentiment analysis.

SKILLS:
- Programming: Python, Java, JavaScript
- ML/AI: TensorFlow, PyTorch, scikit-learn, NLTK
- Web: Flask, Django, REST API
- Database: PostgreSQL, MySQL, MongoDB
- Cloud: AWS (EC2, S3, Lambda)
- Tools: Git, Docker, CI/CD
- Soft Skills: Leadership, Team collaboration, Problem solving

PROJECTS:
- Developed a chatbot using deep learning and NLP
- Created a recommendation system using collaborative filtering
- Built data pipelines for machine learning model deployment
"""

resume2 = """
Jane Smith
Full Stack Developer

EXPERIENCE:
3 years as a Full Stack Developer

SKILLS:
- Frontend: React, Angular, HTML, CSS, JavaScript
- Backend: Node.js, Express, Python
- Database: MySQL, MongoDB
- Tools: Git, GitHub
- Basic knowledge of machine learning

PROJECTS:
- Built e-commerce platforms
- Developed responsive web applications
- Created REST APIs
"""

resume3 = """
Alex Johnson
Data Scientist

EXPERIENCE:
7 years in data science and machine learning

SKILLS:
- Python, R, SQL
- Machine Learning: scikit-learn, XGBoost, Random Forests
- Deep Learning: TensorFlow, Keras, PyTorch
- NLP: NLTK, spaCy, transformers
- Data Visualization: Matplotlib, Seaborn, Plotly
- Big Data: Spark, Hadoop
- Cloud: AWS, Google Cloud Platform
- Databases: PostgreSQL, MongoDB
- Version Control: Git
- Methodologies: Agile, Scrum

PROJECTS:
- Built NLP models for customer feedback analysis
- Developed predictive models for business forecasting
- Created automated ML pipelines using Flask and Docker
"""

def main():
    print("=" * 80)
    print("SMART RESUME SCREENING SYSTEM - TEST DEMO")
    print("=" * 80)
    print("\n")
    
    # Initialize the screener
    print("Initializing Resume Screener with NLP and ML capabilities...")
    screener = ResumeScreener()
    print("✓ Screener initialized\n")
    
    # Create resume dictionary
    resumes = {
        "Resume_1_John_Doe.pdf": resume1,
        "Resume_2_Jane_Smith.pdf": resume2,
        "Resume_3_Alex_Johnson.pdf": resume3
    }
    
    print("Job Description:")
    print("-" * 80)
    print(job_description)
    print("\n")
    
    # Screen resumes
    print("Screening resumes using TF-IDF and cosine similarity...")
    print("=" * 80)
    print("\n")
    
    results = screener.rank_resumes(resumes, job_description)
    
    # Display results
    for i, result in enumerate(results, 1):
        print(f"RANK #{i}: {result['resume_id']}")
        print("-" * 80)
        print(f"Overall Match Score: {result['match_score']:.2f}%")
        print(f"TF-IDF Score: {result['tfidf_score']:.2f}%")
        print(f"Skill Match Score: {result['skill_match_score']:.2f}%")
        print(f"Recommendation: {result['recommendation']}")
        print(f"\nMatched Skills ({len(result['matched_skills'])}): {', '.join(result['matched_skills']) if result['matched_skills'] else 'None'}")
        print(f"\nMissing Skills ({len(result['missing_skills'])}): {', '.join(result['missing_skills']) if result['missing_skills'] else 'None'}")
        print("\n" + "=" * 80 + "\n")
    
    # Summary
    print("\nSUMMARY:")
    print("-" * 80)
    print(f"Total Resumes Screened: {len(results)}")
    print(f"\nTop Candidate: {results[0]['resume_id']}")
    print(f"Top Match Score: {results[0]['match_score']:.2f}%")
    print(f"\nRecommended for Interview:")
    
    recommended = [r for r in results if r['match_score'] >= 55]
    if recommended:
        for r in recommended:
            print(f"  • {r['resume_id']} ({r['match_score']:.2f}%)")
    else:
        print("  None meet the 55% threshold")
    
    print("\n" + "=" * 80)
    print("Test completed successfully!")
    print("=" * 80)

if __name__ == "__main__":
    main()