import csv
import os

def format_csv(input_file, output_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"{input_file} does not exist")
    
    with open(input_file, "r") as inp, open(output_file, "w", newline="") as out:
        reader = csv.reader(inp)
        writer = csv.writer(out)
        writer.writerow(["label", "other", "value"])
        for row in reader:
            writer.writerow([item.strip() for item in row])

if __name__ == "__main__":
    format_csv("../data/master.csv", "../data/formatted.csv")