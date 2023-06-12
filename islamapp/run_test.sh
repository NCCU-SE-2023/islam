#!/bin/bash
cd ./tests
python3 runner.py

# Get the exit code of the previous command
exit_code=$?

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No color

# Print a line separator
printf -- '-%.0s' {1..70}
echo

# Check the exit code and print appropriate status
if [ $exit_code -eq 0 ]; then
    echo -e "${GREEN}TESTS ALL PASS ${NC} \xE2\x9C\xA8"  # Sad face emoji
    exit 0  # Success status code
else
    echo -e "${RED}Tests failed${NC} \xE2\x98\xB9"  # Sad face emoji
    exit 1  # Failure status code
fi
