# main.py

from collector.log_reader import read_log_file
from parser.log_parser import parse_log_line
from detector.rules_engine import detect_anomalies
from reporter.report_generator import generate_pdf_report
from display.cli_display import display_anomalies_rich

def main():
    print("=== System Log Anomaly Detection Framework ===\n")
    
    log_path = "sample_logs/auth.log"  # Change if using a different log source
    
    try:
        raw_logs = read_log_file(log_path)
        print(f"[+] Loaded {len(raw_logs)} log lines.\n")
    except FileNotFoundError as e:
        print(f"[!] Error: {e}")
        return

    parsed_entries = []

    for line in raw_logs:
        parsed = parse_log_line(line)
        if parsed:
            parsed_entries.append(parsed)

    print(f"[+] Parsed {len(parsed_entries)} structured log entries:\n")

    for entry in parsed_entries:
        print(entry)

    if not parsed_entries:
        print("[-] No valid entries were parsed. Check log format or patterns.")
        return

    # Run anomaly detection
    anomalies = detect_anomalies(parsed_entries)

    # Rich CLI output
    print(f"\n[+] Detected {len(anomalies)} anomaly event(s):\n")
    display_anomalies_rich(anomalies)

    # Generate PDF report
    if anomalies:
        report_path = generate_pdf_report(anomalies)
        print(f"\n[+] PDF report generated at: {report_path}")
    else:
        print("\n[-] No anomalies to report.")

if __name__ == "__main__":
    main()
