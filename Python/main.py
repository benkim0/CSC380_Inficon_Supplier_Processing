from vector_embedding_model import load_embedding_model
from Python.database_handler import load_form_data, load_confluence_data
from similarity_test import match_questions


def main():
    model = load_embedding_model()
    conf_df = load_confluence_data("confluence_data.json")
    form_df = load_form_data("form_data.json")
    results = match_questions(
        model = model,
        form_df = form_df,
        conf_df = conf_df,
        threshold=0.80
    )

    print("\nResults:\n")

    for r in results:
        print("Form Question:", r["form_question"])
        print("Confluence Question:", r["confluence_question"])
        print("Answer:", r["answer"])
        print("Field Type:", r["field_type"])
        print("Decision:", r["decision"])
        print("Similarity:", round(r["similarity_score"], 3))
        print()

if __name__ == "__main__":
    main()