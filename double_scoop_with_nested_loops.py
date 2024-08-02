import random

moods = ['happy','sad','energetic','calm','angry']
week = ['Monday','Tuesday','Wendsday','Thursday','Friday','Saturday','Sunday']
times_of_day = ['Morning','Afternoon','Evening']

for day in week:
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood}")
