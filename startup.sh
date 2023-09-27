#!/bin/bash

# Start the web server (webserver.py)
python3 ./webserver.py &
# Start the packet capture (main.py)
python3 ./main.py &
# Schedule preprocess.py to run every 2 minutes using cron
(crontab -l ; echo "*/2 * * * * sudo /usr/bin/python3 /home/porao/NetworkMonitor/preprocess.py") | crontab -
# Schedule yara_analyzer.py to run every 2 minutes using cron
(crontab -l ; echo "*/2 * * * * sudo /usr/bin/python3 /home/porao/NetworkMonitor/yara_analyzer.py") | crontab -
# Keep the script running to maintain the web server and packet capture
while true; do
    sleep 1
done