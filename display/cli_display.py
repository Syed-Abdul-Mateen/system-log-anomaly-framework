# display/cli_display.py

from rich.console import Console
from rich.table import Table
from rich import box

def display_anomalies_rich(anomalies):
    console = Console()
    
    if not anomalies:
        console.print("[bold green]No anomalies detected. System logs appear clean.[/bold green]")
        return

    table = Table(title="Anomaly Detection Report", box=box.SIMPLE_HEAVY)

    table.add_column("Timestamp", style="dim", width=22)
    table.add_column("IP Address", style="cyan", width=20)
    table.add_column("Username", style="magenta", width=16)
    table.add_column("Reason", style="bold yellow")

    for anomaly in anomalies:
        ts = str(anomaly.get("timestamp", "")).split('.')[0]
        ip = anomaly.get("ip", "N/A")
        user = anomaly.get("username", "N/A")
        reason = anomaly.get("reason", "")

        # Color coding based on severity
        reason_style = "bold red" if "root" in reason.lower() else "yellow"

        table.add_row(ts, ip, user, f"[{reason_style}]{reason}[/{reason_style}]")

    console.print(table)
