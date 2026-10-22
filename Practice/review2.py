def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

print(celsius_to_fahrenheit(10))

def is_risk_day(temperature, rain_mm, shoot_cm):
    return temperature >= 10 and rain_mm >= 10 and shoot_cm >= 10

print(is_risk_day(12, 15, 11))
print(is_risk_day(12, 8, 11))

day = {"date": "2026-04-12", "temperature": 13, "rain_mm": 5, "shoot_cm": 12}

print(day["date"])
print(day["rain_mm"])
print(is_risk_day(day["temperature"], day["rain_mm"], day["shoot_cm"]))

days = [
    {"date": "2026-04-10", "temperature": 9.5, "rain_mm": 12, "shoot_cm": 8},
    {"date": "2026-04-11", "temperature": 11.0, "rain_mm": 15, "shoot_cm": 10},
    {"date": "2026-04-12", "temperature": 13.0, "rain_mm": 4, "shoot_cm": 11},
    {"date": "2026-04-13", "temperature": 12.5, "rain_mm": 18, "shoot_cm": 12},
]

count = 0
for day in days:
    if is_risk_day(day["temperature"], day["rain_mm"], day["shoot_cm"]):
        print(day["date"])
        count = count + 1
print(count)


