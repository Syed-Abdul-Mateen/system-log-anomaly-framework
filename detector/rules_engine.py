# detector/rules_engine.py

from collections import defaultdict
from datetime import timedelta

def detect_anomalies(log_entries, brute_force_threshold=5, time_window_minutes=5):
    """
    Applies basic detection rules to parsed log entries.

    Args:
        log_entries (list): List of parsed log dictionaries
        brute_force_threshold (int): Number of attempts before flagging brute force
        time_window_minutes (int): Time window to count attempts in

    Returns:
        list: List of detected anomaly events with reason
    """
    anomalies = []
    failed_attempts_by_ip = defaultdict(list)

    for entry in log_entries:
        if entry.get("event_type") == "failed_login":
            ip = entry.get("ip_address")
            time = entry.get("timestamp")
            user = entry.get("username")
            user_type = entry.get("user_type")

            # Save login attempt per IP
            failed_attempts_by_ip[ip].append(time)

            # Flag root user failures immediately
            if user.lower() == "root":
                anomalies.append({
                    "ip": ip,
                    "timestamp": time,
                    "username": user,
                    "reason": "Failed login attempt for root user"
                })

            # Flag invalid user attempts
            if user_type == "invalid_user":
                anomalies.append({
                    "ip": ip,
                    "timestamp": time,
                    "username": user,
                    "reason": "Invalid username login attempt"
                })

    # Brute-force check per IP
    for ip, times in failed_attempts_by_ip.items():
        times = sorted(times)
        for i in range(len(times)):
            count = 1
            for j in range(i+1, len(times)):
                if (times[j] - times[i]) <= timedelta(minutes=time_window_minutes):
                    count += 1
                else:
                    break
            if count >= brute_force_threshold:
                anomalies.append({
                    "ip": ip,
                    "timestamp": times[i],
                    "reason": f"{count} failed login attempts within {time_window_minutes} minutes"
                })
                break  # One alert per IP is enough for now

    return anomalies
