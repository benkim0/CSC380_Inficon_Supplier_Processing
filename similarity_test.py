from locale import normalize

import numpy as np
from sentence_transformers.util import normalize_embeddings
from sklearn.metrics.pairwise import cosine_similarity

def match_questions(
        model,
        form_df,
        conf_df,
        threshold=0.75
):

    conf_embeddings = model.encode(
        conf_df["question_text"].tolist(),
        normalize_embeddings=True
    )

    form_embeddings = model.encode(
        form_df["question_text"].tolist(),
        normalize_embeddings=True
    )

    similarity_matrix = cosine_similarity(
        form_embeddings,
        conf_embeddings
    )

    results = []

    for i, row in form_df.iterrows():

        scores = similarity_matrix[i]
        best_idx = int(np.argmax(scores))
        best_score = float(scores[best_idx])
        matched_row = conf_df.iloc[best_idx]

        if best_score >= .80:
            decision = "autofill"
            answer = matched_row["answer_text"]
        elif  0.70 < best_score < 0.80:
            decision = "review suggested"
            answer = matched_row["answer_text"]
        else:
            decision = "needs manual review"
            answer = None

        field_type = row.get("field_type", "text")

        results.append({
            "form_question": row["question_text"],
            "confluence_question": matched_row["question_text"],
            "field_type": field_type,
            "answer": answer,
            "decision": decision,
            "similarity_score": best_score
        })

    return results

