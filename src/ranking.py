def rank_resumes(results):

    # Sort by score (highest first)
    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    # Add rank field
    for idx, r in enumerate(ranked, start=1):
        r["rank"] = idx

    return ranked