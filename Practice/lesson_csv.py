import csv

with open("Practice/weather.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        temperature = float(row["temperature"])
        rain = float(row["rain_mm"])
        print(row["date"], temperature >= 10 and  rain >= 10)

        




