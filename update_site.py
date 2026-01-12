import os
import re

def sync_log_to_html():
    html_file = "index.html"
    log_file = "LEARNING_LOG.md"

    if not os.path.exists(log_file):
        print("Log file not found. Run log_progress.py first.")
        return

    # 1. Get the latest entry from the Markdown table
    with open(log_file, "r") as f:
        lines = f.readlines()
        # The last line should be the latest entry
        latest_line = lines[-1].strip()
        
    # Split by pipe and clean up
    parts = [p.strip() for p in latest_line.split('|')]
    if len(parts) < 5: return
    
    date = parts[1]
    module = parts[2]
    summary = parts[4]
    
    status_text = f"LATEST_MASTERY: {date} // {module} // {summary}"

    # 2. Update the index.html using Regex
    with open(html_file, "r") as f:
        content = f.read()

    # This regex finds the span inside the latest-mastery div and replaces its content
    pattern = r'(<div id="latest-mastery"[^>]*>\s*<span[^>]*>).*?(</span>\s*</div>)'
    replacement = rf'\1{status_text}\2'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(html_file, "w") as f:
        f.write(new_content)
    
    print(f"Successfully synced: {module}")

if __name__ == "__main__":
    sync_log_to_html()