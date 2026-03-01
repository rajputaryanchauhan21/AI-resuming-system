def calculate_match(resume_skills, jd_skills):

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched_skills = sorted(list(resume_set & jd_set))
    missing_skills = sorted(list(jd_set - resume_set))

    if len(jd_set) == 0:
        score = 0
    else:
        score = int((len(matched_skills) / len(jd_set)) * 100)

    return matched_skills, missing_skills, score