import requests
import hashlib
import os

URL = "https://careers.universityhealth.com/events"
HASH_FILE = "last_hash.txt"

def fetch_page():
    response = requests.get(URL)
    response.raise_for_status()
    return response.text

def get_hash(content):
    return hashlib.md5(content.encode("utf-8")).hexdigest()

def load_last_hash():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return f.read()
    return None

def save_current_hash(new_hash):
    with open(HASH_FILE, "w") as f:
        f.write(new_hash)

def main():
    content = fetch_page()
    current_hash = get_hash(content)
    last_hash = load_last_hash()

    if current_hash != last_hash:
        print("🔔 New update detected on the events page!")
        save_current_hash(current_hash)
    else:
        print("✅ No changes detected.")
        save_current_hash(current_hash)  # Update the file even if unchanged

if __name__ == "__main__":
    main()
