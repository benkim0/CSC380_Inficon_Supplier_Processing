from vector_embedding_model import load_embedding_model
from Python.database_handler import load_form_data, load_confluence_data
from similarity_test import match_questions
from autofill_engine import autofill_form

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

    form_fields = form_df.to_dict(orient="records")

    autofilled_form = autofill_form(form_fields, results)

    print("\nAutofilled Form:\n")
    for f in autofilled_form:
        print(f"Question ID: {f['form_question_id']}")
        print(f"Question: {f['question_text']}")
        print(f"Value: {f.get('value')}")
        print(f"Status: {f['status']}")
        print("")

if __name__ == "__main__":
    main()