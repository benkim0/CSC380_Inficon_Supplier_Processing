from vector_embedding_model import (
    load_embedding_model,
    embed_texts,
    compute_similarity,
    find_match
)

from database import (
    load_data,
    get_questions_list,
    get_row_index
)


if __name__ == "__main__":
    model = load_embedding_model()

    df = load_data("confluence_data.json")
    confluence_questions = get_questions_list(df)
    confluence_embeddings = embed_texts(model, confluence_questions)

    form_question = "What state is the company located in?"

    form_embedding = embed_texts(model, [form_question])[0]

    scores = compute_similarity(form_embedding, confluence_embeddings)
    best_idx, best_score = find_match(scores)
    matched_row = get_row_index(df, best_idx)

    print("Best match:", matched_row["question_text"])
    print("Answer:", matched_row["answer_text"])
    print("Score:", round(best_score, 3))