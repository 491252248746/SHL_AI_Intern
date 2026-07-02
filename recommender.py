def search_assessments(catalog, query):
    query = query.lower()
    results = []

    for item in catalog:
        score = 0

        if query in item.get("name", "").lower():
            score += 5

        if query in item.get("description", "").lower():
            score += 3

        for level in item.get("job_levels", []):
            if query in level.lower():
                score += 2

        for key in item.get("keys", []):
            if query in key.lower():
                score += 2

        if score > 0:
            item["score"] = score
            results.append(item)

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:5]