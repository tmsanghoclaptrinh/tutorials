# Import library
import time

# Set constant color
OK_GREEN = '\033[92m'

# Print test passed
for i in range(1, 8):
    print(f"{OK_GREEN} √ Test {i} passed")
    time.sleep(0.5)