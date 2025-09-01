import requests
from django.conf import settings

LOG_API_URL = "http://20.244.56.144/evaluation-service/logs"

STACKS = ["backend", "frontend"]
LEVELS = ["debug", "info","warn", "error","fatal"]
PACKAGE =["cache","controller","cron_job", "db", "domain", "handler", "repository","route",  "service"]
BOTH_PACKAGES = ["auth", "config","middleware","utils"]


