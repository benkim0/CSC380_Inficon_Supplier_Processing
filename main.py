from vector_embedding_model import (
    load_embedding_model,
    embed_texts,
    compute_similarity,
    find_match
)


if __name__ == "__main__":
    model = load_embedding_model()

    confluence_questions = [
        "What is the name of the Company",
        "What is the Company Address"
    ]

    form_question = "Where is the company located?"

    conf_embeddings = embed_texts(model, confluence_questions)
    form_embedding = embed_texts(model, [form_question])[0]

    scores = compute_similarity(form_embedding, conf_embeddings)
    best_idx, best_score = find_match(scores)

    print("Best match:", confluence_questions[best_idx])
    print("Score:", round(best_score, 3))