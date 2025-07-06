# System Log Anomaly Detection Framework

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

A real-time log analysis toolkit to detect suspicious or anomalous events from system logs like `auth.log`.  
Built with Python using rich CLI displays, structured PDF reports, and modular architecture — inspired by real-world SOC workflows.

---

##  Features

- Log reader and regex-based parser
- Brute-force login + root user detection
- Colored CLI dashboard using `rich`
- PDF report generation using `fpdf`
- Unit test support
- Easy to extend with new detection rules

---

##  Project Structure

```
system-log-anomaly-framework/
├── main.py
├── collector/
│   └── log_reader.py
├── parser/
│   └── log_parser.py
├── detector/
│   └── rules_engine.py
├── reporter/
│   └── report_generator.py
├── display/
│   └── cli_display.py
├── tests/
│   └── test_parser.py
├── sample_logs/
│   └── auth.log
├── reports/
│   └── (PDF files)
├── requirements.txt
└── README.md
```

---

##  How to Run

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Place logs** in `sample_logs/auth.log`

3. **Run the project**:

```bash
python main.py
```

4. **Check output**:
   - CLI display (rich table)
   - PDF report in `/reports/`

---

##  Sample CLI Output

```
[+] Detected 2 anomaly event(s):

Timestamp            IP Address         Username     Reason
------------------------------------------------------------
2025-07-06 10:23:44  192.168.1.101      admin        Invalid username login attempt
2025-07-06 10:23:47  192.168.1.102      root         Failed login attempt for root user
```

---

##  Run Unit Tests

```bash
python -m unittest discover -s tests
```

---

##  Tech Stack

- Python 3.x
- `fpdf` – PDF reporting
- `rich` – CLI dashboards
- `unittest` – Testing framework
- Modular architecture inspired by security engineering tools

---

##  License

This project is licensed under the MIT License.
