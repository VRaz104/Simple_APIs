import os
from datetime import datetime
report_dir = "reports"
def create_report_directory():
    try:
        os.makedirs(report_dir, exist_ok=True)
    except Exception as e:
        print(f"ERROR: Failed to create report directory '{report_dir}'.")
        print(f"Details: {e}")
        return False
    return True
def build_report_content(today):
    return f"""
DAILY REPORT
Date: {today}
Time: {datetime.now().strftime('%H:%M:%S')}

TASKS COMPLETED:
- eat
- sleep
- code
- exercise

NOTES:
- today was a productive day!
"""
def write_report_file(filepath, content):
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"ERROR: Failed to write report file '{filepath}'.")
        print(f"Details: {e}")
        return False
def write_log(filename):
    try:
        with open("daily_report.log", "a", encoding="utf-8") as log:
            log.write(f"{datetime.now()} - Report created: {filename}\n")
        return True
    except Exception as e:
        print("ERROR: Failed to write to log file.")
        print(f"Details: {e}")
        return False
def main():
    if not create_report_directory():
        return
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}_report.txt"
    filepath = os.path.join(report_dir, filename)
    content = build_report_content(today)
    if not write_report_file(filepath, content):
        return
    write_log(filename)
    print(f"Daily report generated successfully: {filepath}")
if __name__ == "__main__":
    main()