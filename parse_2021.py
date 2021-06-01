import json

file_name = "data/2021.json"

if __name__ == "__main__":
    with open(file_name, "r") as f:
        data = json.loads(f.read())
    events = [e["Event"] for e in data["venues"] if len(e["Event"]) > 0]
    print(events[0])