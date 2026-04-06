def analyze_resume(text):
    skills = ["python", "java", "sql", "html", "css", "javascript"]
    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    score = len(found_skills) * 10

    print("\n📊 Resume Analysis Report")
    print("---------------------------")
    print("✅ Skills Found:", found_skills)
    print("📈 Score:", score, "/ 100")

    if score < 30:
        print("⚠️ Add more technical skills")
    elif score < 60:
        print("👍 Good, but can improve")
    else:
        print("🔥 Strong resume!")


# 👇 THIS MUST BE THERE
resume_text = input("Paste your resume text here:\n")

analyze_resume(resume_text)