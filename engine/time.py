import csv
import glob

def append_to_master():
    all_files = glob.glob("data/generated_*.csv")
    with open("data/master.csv", "a", newline="") as f:
        writer = csv.writer(f)
        for file in all_files:
            with open(file, "r") as rf:
                next(rf)  # skip header
                for row in csv.reader(rf):
                    writer.writerow(row)

if __name__ == "__main__":
    append_to_master()