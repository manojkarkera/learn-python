import os
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
def generate_log_entry(correlation_id, status, description, retry=False):
   
    if retry:        
        return f'Index: "loyalty" ns="user" app-name="data-update-Api" corrleation-id="{correlation_id}" http-status={status} description="{description}"\n', status
    else:
        return f'Index: "loyalty" ns="user" app-name="data-update-Api" corrleation-id="{correlation_id}" http-status={status} description="{description}"\n', status

# Generating 100 log entries with retry logic
log_entries = []
for i in range(50):
    correlation_id = generate_guid()
    status, description = random.choice(statuses)
    entry, status = generate_log_entry(correlation_id, status, description)
    log_entries.append(entry)
   
    retries = 0
    while status != 200 and retries < 1:  # Retry up to 2 times if status is not 200
        entry, status = generate_log_entry(correlation_id,status, description, retry=True)
        log_entries.append(entry)
        retries += 1

# Define log file path
log_file_path = 'D:/Projects/python-project/docs/logs/temp_log.txt'

# Create directory if it doesn't exist
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# Writing log entries to a file
with open(log_file_path, 'w') as log_file:
    log_file.writelines(log_entries)
