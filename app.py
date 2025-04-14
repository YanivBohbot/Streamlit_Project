import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("model/spotify_hit_predictor.pkl")

# App title
st.set_page_config(page_title="Spotify Hit Predictor", page_icon="🎵")
st.title("🎵 Spotify Hit Predictor")
st.write("Enter your song features to see if it might be a **Spotify hit!**")

# Main song features
bpm = st.slider("BPM (Tempo)", 60, 200, 120)
dance = st.slider("Danceability (%)", 0, 100, 70)
valence = st.slider("Valence (Positivity) (%)", 0, 100, 60)
energy = st.slider("Energy (%)", 0, 100, 80)
acoustic = st.slider("Acousticness (%)", 0, 100, 10)
instrum = st.slider("Instrumentalness (%)", 0, 100, 0)
live = st.slider("Liveness (%)", 0, 100, 10)
speech = st.slider("Speechiness (%)", 0, 100, 5)

# Playlist/chart features
playlists = st.number_input("Appears in Spotify Playlists", min_value=0, value=150)
charts = st.number_input("Appears in Spotify Charts", min_value=0, value=50)

# New user inputs to cover required model columns
mode = st.selectbox("Mode", [0, 1], index=1)
key = st.slider("Musical Key", 0, 11, 5)
artist_count = st.number_input("Number of Artists", min_value=1, value=1)

in_apple_charts = st.selectbox("In Apple Charts?", [0, 1], index=0)
in_apple_playlists = st.selectbox("In Apple Playlists?", [0, 1], index=0)
in_deezer_charts = st.selectbox("In Deezer Charts?", [0, 1], index=0)
in_deezer_playlists = st.selectbox("In Deezer Playlists?", [0, 1], index=0)
in_shazam_charts = st.selectbox("In Shazam Charts?", [0, 1], index=0)

released_year = st.number_input(
    "Release Year", min_value=2000, max_value=2025, value=2023
)
released_month = st.slider("Release Month", 1, 12, 6)
released_day = st.slider("Release Day", 1, 31, 15)

# Derived features
log_streams = np.log1p(1000000)  # You can adjust this to your dataset logic
streams_per_playlist = 1000000 / (playlists + 1)
streams_per_chart = 1000000 / (charts + 1)
playlist_per_chart = playlists / (charts + 1)

# Construct DataFrame for prediction
input_df = pd.DataFrame(
    [
        {
            "bpm": bpm,
            "danceability_%": dance,
            "valence_%": valence,
            "energy_%": energy,
            "acousticness_%": acoustic,
            "instrumentalness_%": instrum,
            "liveness_%": live,
            "speechiness_%": speech,
            "in_spotify_playlists": playlists,
            "in_spotify_charts": charts,
            "streams_per_playlist": streams_per_playlist,
            "streams_per_chart": streams_per_chart,
            "playlist_per_chart": playlist_per_chart,
            "log_streams": log_streams,
            "mode": mode,
            "key": key,
            "artist_count": artist_count,
            "in_apple_charts": in_apple_charts,
            "in_apple_playlists": in_apple_playlists,
            "in_deezer_charts": in_deezer_charts,
            "in_deezer_playlists": in_deezer_playlists,
            "in_shazam_charts": in_shazam_charts,
            "released_year": released_year,
            "released_month": released_month,
            "released_day": released_day,
        }
    ]
)

# Predict
if st.button("Predict 🎯"):
    prediction = model.predict(input_df)[0]
    confidence = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.success(f"🎵 This song is likely a **HIT**! (Confidence: {confidence:.1%})")
    else:
        st.error(
            f"🚫 This song is **not likely** to be a hit. (Confidence: {confidence:.1%})"
        )
