import csv

from pygments.lexers import resource

from processor_regex import classify_with_regex
from processor_llm import classify_with_llm
from processor_bert import classify_with_bert
import pandas as pd



def classify(logs):
    labels=[]
    for source, log_msg in logs:
        label = classify_with_regex(log_msg)
        labels.append((source, label))
    return labels

def classify_logs(source, log_message):
    if source == "LegacyCRM":
        label=classify_with_llm(log_message)
    else:
        label=classify_with_regex(log_message)
        if label is None:
            label=classify_with_bert(log_message)
    return label


def classify_csv(input_file):
    df=pd.read_csv(input_file)
    df["target_label"]=classify(list(zip(df["source"], df["log_message"])))
    output_file="resource/output.csv"
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    classify_csv("resource/test.csv")

