nyc_weather={}
with open("nyc_weather.csv","r") as f:
    next(f)
    for line in f:
        date, temp = line.strip().split(",")
        nyc_weather[date] = int(temp)
    print(nyc_weather)

print(type(nyc_weather))

def avg_temp(arr,n):
    values_t = list(arr.values())[:n]
    if len(values_t) == 0:
        return 0
    return round(sum(values_t) / len(values_t),2)

day_max = max(nyc_weather, key=nyc_weather.get)
max_temp = nyc_weather[day_max]

print(f"The temperature the first week of January was: {avg_temp(nyc_weather,7)}")
print(f"The day {day_max}, has the maximum temp: {max_temp}")

print(nyc_weather["Jan 9"])
print(nyc_weather["Jan 4"])

