import re

def classify_with_regex(log_message):
    regex_patterns = {
        r"User [User\d]+ logged (in|out).*" : "User Action",
        r"Backup (started|ended) at .*" : "System Notification",
        r"Backup completed successfully.*" : "System Notification",
        r"System updated to version .*" : "System Notification",
        r"FILE .* uploaded successfully by user .*" : "System Notification",
        r"DISK cleanup completed successfully.*" : "System Notification",
        r"System reboot initiated by user .*" : "System Notification",
        r"ACCOUNT with ID .* created by .*" : "User Action"
    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label

    return None

if __name__ == "__main__":
    print(classify_with_regex("User 123 logged in successfully."))
    print(classify_with_regex("Backup started at 12:00 AM."))
    print(classify_with_regex("Backup completed successfully."))
    print(classify_with_regex("SYSTEM UPDATED TO VERSION 1.2.3"))
    print(classify_with_regex("FILE 123456789 uploaded successfully by user 123456789"))
    print(classify_with_regex("DISK cleanup completed successfully."))
    print(classify_with_regex("SYSTEM REBOOT INITIATED BY USER 123456789"))
    print(classify_with_regex("ACCOUNT with ID 123456789 created by user 123456789"))