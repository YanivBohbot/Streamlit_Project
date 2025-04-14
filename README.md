# 🎵 Spotify Hit Predictor

A simple and interactive web app built with **Streamlit** that predicts whether a song is likely to be a **Spotify hit** based on its audio features.

---

## 📊 Overview

This project uses a **logistic regression model** trained on a Spotify dataset to classify songs as a potential hit (`1`) or not (`0`). The model considers features such as BPM, danceability, energy, and more to make the prediction.

---

## 🚀 Features

- 🔧 **Machine Learning**: Logistic Regression pipeline with preprocessing and feature scaling.
- 🎛️ **User Input Interface**: Sliders to input song attributes like tempo, valence, energy, etc.
- 📈 **Prediction Result**: Instantly shows if the song is a "hit".
- 🌐 **Web Deployment**: Built with Streamlit for easy sharing and deployment.

---

## 🧠 Model Details

- **Algorithm**: Logistic Regression
- **Libraries**: `scikit-learn`, `pandas`, `numpy`, `joblib`
- **Preprocessing**: Feature scaling, pipeline integration
- **Target**: `Hit` (Binary classification: 0 = Not a hit, 1 = Hit)

---

## 🛠 How to Run the App Locally

1. **Clone the repo**
    ```bash
    git clone https://github.com/your-username/spotify-hit-predictor.git
    cd spotify-hit-predictor
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app**
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure

