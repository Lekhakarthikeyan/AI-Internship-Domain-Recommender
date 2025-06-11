from flask import Flask, render_template, request

app = Flask(__name__)

internship_domains = {
    "Data Science": ["data", "machine learning", "statistics", "python", "analysis", "ai"],
    "Web Development": ["html", "css", "javascript", "frontend", "backend", "react", "django", "flask"],
    "Mobile Development": ["android", "ios", "flutter", "swift", "kotlin", "react native"],
    "Cybersecurity": ["security", "network", "cryptography", "ethical hacking", "penetration testing"],
    "Marketing": ["seo", "content", "digital marketing", "social media", "branding"],
    "Finance": ["accounting", "financial analysis", "investment", "excel", "risk management"],
    "Design": ["ui", "ux", "graphic design", "photoshop", "illustrator", "adobe"],
}

def recommend_domains(interests, experience):
    interests = interests.lower().split(',')
    experience = experience.lower().split(',')
    score_map = {domain: 0 for domain in internship_domains}

    for domain, keywords in internship_domains.items():
        for keyword in keywords:
            if keyword.strip() in [i.strip() for i in interests] or keyword.strip() in [e.strip() for e in experience]:
                score_map[domain] += 1

    sorted_domains = sorted(score_map.items(), key=lambda x: x[1], reverse=True)
    recommendations = [d for d, score in sorted_domains if score > 0]

    return recommendations if recommendations else ["General Internship Opportunities"]

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = None
    name = ""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        interests = request.form.get('interests', '')
        experience = request.form.get('experience', '')

        recommendations = recommend_domains(interests, experience)

    return render_template('index.html', recommendations=recommendations, name=name)

if __name__ == '__main__':
    app.run(debug=True)
