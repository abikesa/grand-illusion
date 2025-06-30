import csv
import random
from datetime import datetime

def generate_data(n=10, level="hour"):
    now = datetime.now().isoformat()
    return [[now, level, random.randint(0, 100)] for _ in range(n)]

def write_csv(data, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)  # No header written

if __name__ == "__main__":
    levels = ["hour", "day", "week", "month", "year"]
    for level in levels:
        data = generate_data(10, level)
        write_csv(data, f"../data/generated_{level}.csv")