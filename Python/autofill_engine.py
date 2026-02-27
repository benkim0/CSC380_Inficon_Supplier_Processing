def autofill_field(field, match):
    decision = match.get("decision")
    answer = match.get("answer")
    field_type = field.get("field_type", "text")
    options = field.get("options", [])

    if decision == "autofill":
        if field_type in ["text", "textarea"]:
            field["value"] = answer
        elif field_type == "checkbox":
            if answer in options:
                field["value"] = answer
            else:
                field["value"] = None
        elif field_type == "multi_checkbox":
            field["value"] = [a for a in answer if a in options] if answer else []
        elif field_type == "dropdown":
            if answer in options:
                field["value"] = answer
            else:
                field["value"] = None
        field["status"] = "autofilled"

    elif decision == "review suggested":
        field["value"] = answer
        field["status"] = "review suggested"

    else:
        field["value"] = None
        field["status"] = "needs manual review"

    return field



def autofill_form(form_fields, match_results, key="form_question_id"):
    match_map = {m[key]: m for m in match_results if key in m}

    for field in form_fields:
        field_key = field.get(key)
        if field_key in match_map:
            autofill_field(field, match_map[field_key])
        else:
            field["value"] = None
            field["status"] = "needs manual review"
    return form_fields