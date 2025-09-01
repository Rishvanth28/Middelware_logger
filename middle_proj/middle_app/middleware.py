import requests
from django.conf import settings

LOG_API_URL = "http://20.244.56.144/evaluation-service/logs"

STACKS = ["backend", "frontend"]
LEVELS = ["debug", "info","warn", "error","fatal"]
PACKAGE =["cache","controller","cron_job", "db", "domain", "handler", "repository","route",  "service"]
BOTH_PACKAGES = ["auth", "config","middleware","utils"]



def Log(stack: str, level: str, package: str, message: str):
    if stack not in STACKS:
        raise ValueError(f"Invalid stack: {stack}. Must be one of {STACKS}")
    if level not in LEVELS:
        raise ValueError(f"Invalid level: {level}. Must be one of {LEVELS}")
    if package not in PACKAGE and package not in BOTH_PACKAGES:
        raise ValueError(f"Invalid package: {package}. Must be one of {PACKAGE} or {BOTH_PACKAGES}")

    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }
    try:
        response = requests.post(LOG_API_URL, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send log: {e}")