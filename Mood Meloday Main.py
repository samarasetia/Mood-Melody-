import pandas as pd
import random

#Load songs data
songs_df = pd.read_csv("SongEmotionScore.csv", header = None, names = ["SongID", "Title", "Artist", "score"])

#Questions for user engagement
print("Hi! Let's find a song for you today.")
name= input("What's your name? ").strip()
print(f"Nice to meet you, {name}!")
day = input ("How has your day been so far?").strip()
print(f"Thanks for sharing! Let's find a song that fits your mood.")

#Asking the user for their mood
print ("Available moods: happy, relax, calm, sad, pain")
mood= input ("What mood are you in? ").strip().lower()

#Open the mood file and make a list of the data once the user enters their mood
#if entered mood doesn't exist, show an error message
try:
    with open(f"{mood}.txt", "r", encoding="utf-8") as f:
        mood_tags = [line.strip().lower() for line in f if line.strip()]
except FileNotFoundError:
    print("Sorry, I cannot find songs for your current mood.")
    exit()

def matches_tags(text):
    text = text.lower()
    return any(tag in text for tag in mood_tags)

matched = songs_df[songs_df.apply(
    lambda row: matches_tags(row["Title"]) or matches_tags(row["Artist"]),
    axis = 1
)]

#engagement before recommendation
if not matched.empty:
    ready = input("Ready to get a song recommendation? (yes/no) ").strip() .lower()
    if ready != "yes":
        print ("No worries, come back later!")
        exit()

    song = matched.sample(1).iloc[0]

    print("\nYour mood-based recommended song:")
    print(f"Title: {song['Title']}")
    print(f"Artist: {song['Artist']}")

else:
    print("No songs found for your mood. Try another mood.")