import re

# Define regex patterns for each log category
log_patterns = {
    r"User User\d+ logged (in|out).": "User Action",
    r"Backup (started|ended) at .*": "System Notification",
    r"Backup completed successfully.": "System Notification",
    r"System updated to version .*": "System Notification",
    r"File .* uploaded successfully by user .*": "System Notification",
    r"Disk cleanup completed successfully.": "System Notification",
    r"System reboot initiated by user .*": "System Notification",
    r"Account with ID .* created by .*": "User Action"
}

def classify_log(message):
    for pattern, category in log_patterns.items():
        if re.search(pattern, message):
            return category
    return None

if __name__ == "__main__":
    print(classify_log("User User1 logged in."))
    print(classify_log("Backup started at 12:00."))
    print(classify_log("Backup completed successfully."))
    print(classify_log("System updated to version 1.0."))
    print(classify_log("File file1 uploaded successfully by user user1."))
    print(classify_log("Disk cleanup completed successfully."))
    print(classify_log("System reboot initiated by user user1."))
    print(classify_log("Account with ID 1234 created by user user1."))
    print(classify_log("Heellooo bro, hey doing."))