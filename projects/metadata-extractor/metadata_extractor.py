from pathlib import Path
import hashlib
import sys

def inspect(path):
    data = path.read_bytes()
    print(f"File: {path.name}")
    print(f"Size: {len(data)} bytes")
    print(f"SHA-256: {hashlib.sha256(data).hexdigest()}")
    print(f"Extension: {path.suffix or 'none'}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python metadata_extractor.py <file>")
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.is_file():
        print("File not found.")
        sys.exit(1)
    inspect(path)
