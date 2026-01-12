#!/bin/bash

# --- DFN_NONATO Portfolio Sync ---
echo "---------------------------------------"
echo "Starting Self-Learning Telemetry Sync..."
echo "---------------------------------------"

# 1. Run the Progress Logger
python3 log_progress.py

# 2. Run the Site Updater
python3 update_site.py

echo "---------------------------------------"
echo "SYNCING WITH GITHUB..."
echo "---------------------------------------"

# 3. Git Workflow
git add .

# Ask for a commit message
echo "Enter update summary (or press Enter for 'Daily Progress Update'):"
read commit_msg

if [ -z "$commit_msg" ]
then
      commit_msg="Daily Progress Update"
fi

git commit -m "$commit_msg"
git push origin main

echo "---------------------------------------"
echo "DEPLOYMENT COMPLETE."
echo "Your site will be live in ~60 seconds."
echo "---------------------------------------"