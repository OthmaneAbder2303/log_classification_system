from processor_regex import classify_log
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm

def classify(logs):
    labels = []
    for source, log_msg in logs:
        label = Myclassify(source, log_msg)
        labels.append(label)
    return labels;

def Myclassify(source, log_msg):
    if source == "LegacyCRM":
        classify_with_llm(log_msg)
        return None
    else :
        label = classify_log(log_msg)
        if label is None:
            classify_with_bert(log_msg)
        return label


if __name__ == "__main__":
    logs = [
        "User User1 logged in.",
        "Backup started at 12:00.",
        "Backup completed successfully.",
        "System updated to version 1.0.",
        "File file1 uploaded successfully by user user1.",
        "Disk cleanup completed successfully.",
        "System reboot initiated by user user1.",
        "Account with ID 1234 created by user user1.",
        "Heellooo bro, hey doing."
    ]

    for log in logs:
        print(classify_log(log))