import os
import time

def print_important_env_vars():
    important_vars = [
        "HOME",
        "USER",
        "SHELL",
        "PATH",
        "LANG",
        "PWD",
        "LOGNAME",
        "TERM",
        "HOSTNAME",
        "EDITOR"
    ]

    for var in important_vars:
        value = os.getenv(var, "<Not Set>")
        print(f"{var}={value}")

if __name__ == "__main__":
    print_important_env_vars()
    while True:
        time.sleep(60)