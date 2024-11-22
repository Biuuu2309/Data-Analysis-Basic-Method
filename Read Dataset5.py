import kagglehub
import csv

filepath = "Project/Data-Analysis-Basic-Method/Dataset5/Youtube_utf8.csv"
def docnd(file):
    try:
        with open(file, "rt", encoding="utf-8") as f:
            csv_read = csv.reader(f)
            csv_read.__next__()
            # print(list(csv_read))
            for row in csv_read:
                print(list(row))
    except FileNotFoundError:
        print("Khong tim thay tap tin")
    else:
        print("Da thuc hien hoan tat")
        
docnd(filepath)