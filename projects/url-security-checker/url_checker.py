from urllib.parse import urlparse
import ipaddress
import sys

def inspect_url(value):
    parsed = urlparse(value if "://" in value else "https://" + value)
    host = parsed.hostname

    if not host:
        print("Invalid URL.")
        return

    print(f"Scheme: {parsed.scheme}")
    print(f"Host: {host}")
    print(f"Port: {parsed.port or '(default)'}")

    try:
        ipaddress.ip_address(host)
        print("Host type: IP address")
    except ValueError:
        print("Host type: domain name")

    if parsed.scheme != "https":
        print("Warning: URL does not use HTTPS.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python url_checker.py <url>")
        sys.exit(1)
    inspect_url(sys.argv[1])
