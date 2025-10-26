#!/bin/bash
# start_all.sh

# Run Python server in background
echo "Starting Python server..."
python3 server.py &

PYTHON_PID=$!

# Give Python server a few seconds to start
sleep 1

# Run frontend
echo "Starting frontend..."
cd website || exit
npm run dev

# Optionally, wait for Python server if frontend exits
wait $PYTHON_PID
