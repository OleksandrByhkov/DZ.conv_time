seconds = int(input())

day_seconds = 24 * 60 * 60

days, seconds = divmod(seconds, day_seconds)
hours, seconds = divmod(seconds, 3600)
minutes, seconds = divmod(seconds, 60)

if days == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"
hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

print(f"{days} {day_word}, {hours}:{minutes}:{seconds}")
