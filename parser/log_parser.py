# parser/log_parser.py

import re
from datetime import datetime

# Pattern to extract overall log structure
LOG_PATTERN = re.compile(
    r'(?P<timestamp>\w{3}\s+\d+\s[\d:]+)\s+(?P<host>\S+)\s+(?P<service>\S+)\[(?P<pid>\d+)\]:\s(?P<message>.+)'
)

# Pattern to extract SSH failed login details
SSH_FAILED_PATTERN = re.compile(
    r'Failed password for (?P<user_type>invalid user\s)?(?P<username>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
)

def parse_log_line(line):
    """
    Parses a single log line into structured fields using regex.
    
    Args:
        line (str): A raw log line string

    Returns:
        dict: Structured log info or None if not matched
    """
    match = LOG_PATTERN.search(line)
    if not match:
        return None

    data = match.groupdict()
    message = data["message"]

    ssh_match = SSH_FAILED_PATTERN.search(message)
    if ssh_match:
        data.update({
            "event_type": "failed_login",
            "username": ssh_match.group("username"),
            "ip_address": ssh_match.group("ip"),
            "user_type": "invalid_user" if ssh_match.group("user_type") else "valid_user"
        })
    else:
        # Skip unrelated messages for now
        return None

    # Add parsed datetime and replace year with current
    try:
        parsed_time = datetime.strptime(data["timestamp"], "%b %d %H:%M:%S")
        current_year = datetime.now().year
        data["timestamp"] = parsed_time.replace(year=current_year)
    except:
        pass  # Keep raw if format fails

    return data
