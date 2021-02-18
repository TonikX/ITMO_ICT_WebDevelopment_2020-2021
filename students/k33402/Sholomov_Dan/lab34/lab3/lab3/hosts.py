from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(r"api", "lab3.urls", name="api"),
)
