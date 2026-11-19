# Test file for authorized CodeRabbit security research (test account A, org Doppio7).
# Intentionally insecure patterns so the Secure scanner has something to flag.
import os, pickle, subprocess

def run_user_command(user_input):
    subprocess.call(user_input, shell=True)

def load_user_data(blob):
    return pickle.loads(blob)

ADMIN_PASSWORD = "test-only-not-a-real-secret"
