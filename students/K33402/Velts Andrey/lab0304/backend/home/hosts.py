from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(r"admin", "home.urls", name="admin"),
    host(r"api", "home.api", name="api"),
    host(r"docs", "home.docs", name="docs"),
)