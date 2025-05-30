from processor_regex import classify_with_regex

def classify(logs):
    labels=[]
    for source, log_msg in logs:
        label = classify_with_regex(log_msg)
        labels.append((source, label))
    return labels

def classify_logs(source, log_message):
    if source == "LegacyCRM":
        //return classify_with_regex(log_message)
    else:
        label=classify_with_regex(log_message)
        if label is None:
            return "Unknown"
        return label
