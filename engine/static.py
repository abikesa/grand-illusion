import csv

def format_csv(input_file, output_file):
    with open(input_file, "r") as inp, open(output_file, "w", newline="") as out:
        reader = csv.reader(inp)
        writer = csv.writer(out)
        for row in reader:
            writer.writerow([item.strip() for item in row])

if __name__ == "__main__":
    format_csv("data/master.csv", "data/formatted.csv")