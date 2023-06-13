import unittest
import os
import sys

# set the MONGO_URL to use a test database
os.environ["TEST_ENVIRONMENT_FLAG"] = "true"

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Create a TestSuite and discover test cases
test_suite = unittest.defaultTestLoader.discover(
    start_dir=current_dir, pattern="*test*.py"
)

# Create a TextTestRunner and run the tests
test_runner = unittest.TextTestRunner(verbosity=5)
test_runner.run(test_suite)
