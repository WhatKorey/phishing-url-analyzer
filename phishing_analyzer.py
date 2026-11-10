from urllib.parse import urlsplit

def analyze_url(url):
    try:
        parts = urlsplit(url.strip())
    except ValueError:
        return "That URL looks malformed. Please enter a valid URL."
    if parts.scheme in ("http", "https") and not parts.hostname:
        return "Enter a URL with a hostname, like https://example.com."
    if parts.scheme in ("http", "https") and "@" in parts.netloc:
        return f"Flag: the @ can hide the distination. Hostname: {parts.hostname}"
    if url.strip().lower().startswith("http://"):
        return "Flag: this URL uses unencrypted HTTP."

    if url.startswith("https://"):
        return "No HTTP flag. This check alone can't tell if a URL is safe."

    return "Enter a URL that starts with http:// or https://."
    

if __name__ == "__main__":
    url = input("Enter a URL: ")
    print(analyze_url(url)) 