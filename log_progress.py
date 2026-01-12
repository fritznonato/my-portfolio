import datetime
import os

def update_learning_log():
    log_file = "LEARNING_LOG.md"
    
    # Get user input for today's progress
    print("--- DFN_NONATO: Self-Learning Telemetry ---")
    topic = input("Enter the topic mastered (e.g., ASP.NET Core, AI Foundations): ")
    hours = input("Time spent (hours): ")
    summary = input("Short summary of what you built/learned: ")
    
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    
    # Create the log entry
    new_entry = f"| {date_str} | {topic} | {hours} hrs | {summary} |\n"
    
    # Check if file exists to add header
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("# 📚 Self-Learning Deployment Log\n\n")
            f.write("| Date | Module | Duration | Achievement Summary |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
            
    with open(log_file, "a") as f:
        f.write(new_entry)
        
    print(f"\n[SUCCESS] Log updated for {date_str}. Keep building.")

if __name__ == "__main__":
    update_learning_log()