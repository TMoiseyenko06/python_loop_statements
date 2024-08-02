import random

moods = ['happy','sad','energetic','calm','angry']
week = ['Monday','Tuesday','Wendsday','Thursday','Friday','Saturday','Sunday']

for day in week:
    mood = random.choice(moods)
    print(f"On {day} you were feeling {mood}.")

