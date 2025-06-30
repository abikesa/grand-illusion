import csv
import glob
import os

def append_to_master():
    all_files = glob.glob("../data/generated_*.csv")
    master_file = "../data/master.csv"
    
    if not os.path.exists(master_file):
        with open(master_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "scale", "value"])
    
    with open(master_file, "a", newline="") as f:
        writer = csv.writer(f)
        for file in all_files:
            with open(file, "r") as rf:
                reader = csv.reader(rf)
                for row in reader:
                    writer.writerow(row)

if __name__ == "__main__":
    append_to_master()