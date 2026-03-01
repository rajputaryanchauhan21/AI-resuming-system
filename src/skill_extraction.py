import re

# =========================
# ROLE BASED SKILL DATABASE
# =========================

SKILL_DATABASE = {

    "Web Developer": {
        "html": ["html", "html5"],
        "css": ["css", "css3"],
        "javascript": ["javascript", "js", "java script", "java scripts"],
        "react": ["react", "reactjs", "react.js"],
        "angular": ["angular", "angularjs"],
        "vue": ["vue", "vuejs", "vue.js"],
        "node": ["node", "nodejs", "node.js"],
        "express": ["express", "expressjs"],
        "mongodb": ["mongodb", "mongo db"],
        "mysql": ["mysql"],
        "bootstrap": ["bootstrap"],
        "tailwind": ["tailwind", "tailwindcss"],
        "git": ["git", "github"],
        "api": ["rest api", "api", "apis"],
        "typescript": ["typescript", "ts"]
    },

    "Data Scientist": {
        "python": ["python"],
        "r": ["r programming", " r "],
        "sql": ["sql"],
        "excel": ["excel", "ms excel"],
        "pandas": ["pandas"],
        "numpy": ["numpy"],
        "matplotlib": ["matplotlib"],
        "seaborn": ["seaborn"],
        "scikit-learn": ["scikit", "sklearn", "scikit-learn"],
        "tensorflow": ["tensorflow"],
        "keras": ["keras"],
        "pytorch": ["pytorch"],
        "machine learning": ["machine learning", "ml"],
        "deep learning": ["deep learning", "dl"],
        "nlp": ["nlp", "natural language processing"],
        "power bi": ["power bi"],
        "tableau": ["tableau"],
        "statistics": ["statistics", "statistical analysis"]
    },

    "Software Developer": {
        "java": ["java"],
        "c++": ["c++", "cpp"],
        "c#": ["c#", "c sharp"],
        "python": ["python"],
        "sql": ["sql"],
        "spring": ["spring", "spring boot"],
        "hibernate": ["hibernate"],
        "docker": ["docker"],
        "kubernetes": ["kubernetes", "k8s"],
        "aws": ["aws", "amazon web services"],
        "azure": ["azure"],
        "git": ["git", "github"],
        "rest api": ["rest api", "api"]
    }
}

# =========================
# SKILL EXTRACTION FUNCTION
# =========================

def extract_skills(text, role=None):

    text = text.lower()
    found_skills = []

    # If role selected → use only that role skills
    if role in SKILL_DATABASE:
        skill_set = SKILL_DATABASE[role]
    else:
        # If Custom → combine all skills
        skill_set = {}
        for r in SKILL_DATABASE.values():
            skill_set.update(r)

    for skill, aliases in skill_set.items():
        for alias in aliases:
            if re.search(r'\b' + re.escape(alias) + r'\b', text):
                found_skills.append(skill)
                break

    return sorted(list(set(found_skills)))