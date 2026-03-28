def get_retriever(db):
    return db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "score_threshold": 0.6,
            "k": 3
        }
    )