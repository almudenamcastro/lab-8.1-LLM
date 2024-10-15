from huggingface_hub import InferenceClient

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("token1")

client = InferenceClient(api_key = api_key)


# ------------------------------------

def find_song(track_name, artist_name):
    # This promt will be sent to the model

    prompt = (f"Find similar songs to {track_name} by {artist_name}.")
    
    # To save the answers
    similar_tracks = ""

    # Use Phi-3.5-mini-instruct 
    for message in client.chat_completion(
        model="microsoft/Phi-3.5-mini-instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        stream=True,
    ):
        # Save songs
        similar_tracks += message.choices[0].delta.content
    
    return similar_tracks
    
def init_chatbot():
    print("Hi! I'm a chatbot that finds similar songs")
    track_name = input("Choose a song): ")
    artist_name = input("Who wrote that? ")
    
    print("\nFinding songs...\n")
    sim_songs = find_song(track_name, artist_name)
    print(sim_songs)
    return sim_songs

def continuar_chat(sim_songs):
    while True:
        answer = input("Would you like to find similar songs to sth else? (Y/N): ").lower()
        if answer[0] == "y":
            sim_songs = init_chatbot()
        elif answer[0] == "n":
            print("Hope you enjoyned the playlist!")
            break
        else:
            print("Please choose yes or no")

def song_finder():
    sim_songs = init_chatbot()
    continuar_chat(sim_songs)