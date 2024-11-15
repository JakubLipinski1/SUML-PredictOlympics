import pandas as pd

df = pd.read_csv("przefiltrowane.csv")

unique_sports = df['Sport'].dropna().unique()
unique_events = df['Event'].dropna().unique()

with open("sports.txt", "w") as sports_file:
    for sport in unique_sports:
        sports_file.write(sport + "\n")

with open("events.txt", "w") as events_file:
    for event in unique_events:
        events_file.write(event + "\n")

print("Eksport zakończony.")
