import hashlib
from pathlib import Path
import sys

def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_integrity.py <file>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.is_file():
        print("File not found.")
        sys.exit(1)

    print(f"SHA-256: {sha256_file(path)}")
