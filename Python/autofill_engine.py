from re import match


def autofill_field(field, match):
    field_type = field.get("field_type", "text")
    decision = match.get("decision")
    answer = match.get("answer")

    if decision == "autofill":
        if field_type == "text":
            field["value"] = answer

        elif field_type == "checkbox":
            if answer in field.get("options", []):
                field["value"] = answer
            else:
                field["value"] = None
                field["status"] = "manual"

        elif field_type == "multi_checkbox":
            valid_answers = [a for a in answer if a in field.get("options", [])]
            field["value"] = valid_answers

        elif field_type == "dropdown":
            if answer in field.get("options", []):
                field["value"] = answer
            else:
                field["value"] = None
                field["status"] = "manual"

        if "status" not in field:
            field["status"] = "autofilled"

    elif decision == "review suggested":
        field["value"] = answer
        field["status"] = "review suggested"

    else:
        field["value"] = None
        field["status"] = "needs manual review"

    return field


def autofill_form(form_fields, match_results):
    match_map = {m["form_question"]: m for m in match_results}

    for field in form_fields:
        qid = field["form_question_id"]
        if qid in match_map:
            field = autofill_field(field, match_map[qid])
        else:
            field["status"] = "needs manual review"

    return form_fields