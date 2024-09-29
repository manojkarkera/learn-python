import uuid
import random

# Function to generate a random GUID
def generate_guid():
    return str(uuid.uuid4()).upper()

# Possible HTTP statuses and descriptions
statuses = [
    (200, "OK"),
    (400, "Bad Request"),
    (401, "Unauthorized"),
    (403, "Forbidden"),
    (404, "Not Found"),
    (500, "Internal Server Error"),
    (502, "Bad Gateway"),
    (503, "Service Unavailable"),
    (504, "Gateway Timeout")
]

# Function to generate a single log entry
def generate_log_entry(index, retry=False):
    status, description = random.choice(statuses) if not retry else (500, "Timeout")
    return f'Index: "loyalty" ns="user" app-name="data-update-Api" corrleation-id="{generate_guid()}" http-status={status} description="{description}"\n'

# Generating 100 log entries with retry logic
log_entries = []
for i in range(100):
    entry = generate_log_entry(i)
    log_entries.append(entry)
    if "http-status=500" in entry:  # Simulating retry for 500 status
        for _ in range(2):  # Retry up to 2 times
            retry_entry = generate_log_entry(i, retry=True)
            log_entries.append(retry_entry)
            if "http-status=200" in retry_entry:
                break

# Writing log entries to a file
log_file_path = 'D:/Projects/python-project/docs/logs/temp_log.txt'
with open(log_file_path, 'w') as log_file:
    log_file.writelines(log_entries)

log_file_path
