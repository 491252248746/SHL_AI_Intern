def recommend_courses(catalog, query):
    query = query.lower()
    results = []

    for item in catalog:
        name = item.get("name", "").lower()
        desc = item.get("description", "").lower()

        if query in name or query in desc:
            results.append(item)
        
    return results
