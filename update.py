from datetime import datetime

with open("data.txt", "w") as f:
    f.write(f"Last updated: {datetime.utcnow().isoformat()} UTC\n")
