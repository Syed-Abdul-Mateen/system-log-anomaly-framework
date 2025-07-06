# reporter/report_generator.py

import os
from fpdf import FPDF
from datetime import datetime

class AnomalyReportPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "System Log Anomaly Report", ln=True, align="C")
        self.set_font("Arial", "", 10)
        self.cell(0, 10, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def anomaly_table(self, anomalies):
        self.set_font("Arial", "B", 11)
        self.cell(40, 10, "Timestamp", border=1)
        self.cell(40, 10, "IP Address", border=1)
        self.cell(40, 10, "Username", border=1)
        self.cell(70, 10, "Reason", border=1)
        self.ln()

        self.set_font("Arial", "", 10)
        for item in anomalies:
            self.cell(40, 10, str(item.get("timestamp", "")).split('.')[0], border=1)
            self.cell(40, 10, item.get("ip", ""), border=1)
            self.cell(40, 10, item.get("username", "N/A"), border=1)
            self.cell(70, 10, item.get("reason", "N/A"), border=1)
            self.ln()

def generate_pdf_report(anomalies, output_dir="reports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"anomaly_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    output_path = os.path.join(output_dir, filename)

    pdf = AnomalyReportPDF()
    pdf.add_page()
    pdf.anomaly_table(anomalies)
    pdf.output(output_path)

    return output_path
