import pandas as pd

from processor_regex import classify_log # regex
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm

def classify(logs):
    labels = []
    for source, log_msg in logs:
        label = my_classifier(source, log_msg)
        labels.append(label)
    return labels

def my_classifier(source, log_msg):
    if source == "LegacyCRM":
        label = classify_with_llm(log_msg)
    else:
        label = classify_log(log_msg) # with regex
        if not label:
            label = classify_with_bert(log_msg)
    return label


def classify_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        assert "source" in df.columns and "log_message" in df.columns
        df["target_label"] = classify(zip(df["source"], df["log_message"]))
        df.to_csv("resources/output.csv", index=False)
    except Exception as e:
        print(f"[Error] Processing failed: {e}")

if __name__ == "__main__":
    classify_csv("resources/test.csv")
    '''
    logs = [
         ("ModernCRM", "IP 192.168.133.114 blocked due to potential attack"),
         ("BillingSystem", "User User12345 logged in."),
         ("AnalyticsEngine", "File data_6957.csv uploaded successfully by user User265."),
         ("AnalyticsEngine", "Backup completed successfully."),
         ("ModernHR", "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1 RCODE  200 len: 1583 time: 0.1878400"),
         ("ModernHR", "Admin access escalation detected for user 9429"),
         ("LegacyCRM", "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."),
         ("LegacyCRM", "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module."),
         ("LegacyCRM", "The 'BulkEmailSender' feature is no longer supported. Use 'EmailCampaignManager' for improved functionality."),
         ("LegacyCRM", " The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"),
         ("Othmane", "Heellooo bro, hey doing.")
     ]
    labels = classify(logs)

    for log, label in zip(logs, labels):
        print(log[0], "->", label)
    '''