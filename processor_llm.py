from dotenv import load_dotenv
from groq import Groq
import os


load_dotenv()

groq = Groq(api_key=os.getenv("GROQ_API_KEY"))
def classify_with_llm(log_msg):
    prompt = f"Classify the log message as one of following categories: 1.Workflow error, 2. Deprecatian Warning, If you cannot figure out, return classified, only return label not preamble"

    chat_completion = groq.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        #model="deepseek-r1-distill-llama-70b",
    )
    return chat_completion.choices[0].message.content




if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))

