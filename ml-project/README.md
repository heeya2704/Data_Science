# 🎵 Spotify Song Popularity Predictor

An end-to-end Machine Learning pipeline to predict track popularity scores on Spotify based on acoustic features, metadata, and artist popularity metrics.

---

## 📌 Project Summary

The **Spotify Song Popularity Predictor** leverages audio characteristics (such as danceability, energy, loudness, valence, tempo, and acousticness) alongside artist metadata to estimate the popularity rating (0 to 100) of a track on Spotify. The objective is to assist independent artists and record labels in optimizing track features before distribution to maximize listener engagement and playlist placement.

### Key Objectives
- Analyze acoustic feature correlations with overall popularity.
- Feature engineering of temporal and genre-level aggregations.
- Train and evaluate regression models (Random Forest, LightGBM, XGBoost).
- Deploy an inference pipeline for real-time popularity scoring.

---

## 📊 Dataset Information

- **Dataset Source:** [Kaggle Spotify Tracks Dataset Placeholder](https://www.kaggle.com/datasets/spotify-tracks-dataset) / [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- **Data Range:** ~114,000 Spotify tracks across 125 distinct genres.
- **Features Included:** `danceability`, `energy`, `key`, `loudness`, `mode`, `speechiness`, `acousticness`, `instrumentalness`, `liveness`, `valence`, `tempo`, `duration_ms`, `track_genre`, `popularity`.

---

## ⚙️ Setup & Installation Instructions

### Prerequisites
- **Python Version:** Python `3.9+` or `3.10+`
- **Environment Management:** `venv` or `conda`

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/spotify-song-popularity-predictor.git
   cd spotify-song-popularity-predictor
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Required Python Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

   *Core dependencies:*
   - `pandas >= 2.0.0`
   - `numpy >= 1.24.0`
   - `scikit-learn >= 1.3.0`
   - `lightgbm >= 4.0.0`
   - `matplotlib >= 3.7.0`
   - `seaborn >= 0.12.0`
   - `joblib >= 1.3.0`

4. **Running the Pipeline:**
   ```bash
   # Run data preprocessing and model training
   python src/train.py
   ```

---

## 📈 Results & Visuals

### Model Evaluation Summary

| Model | RMSE | MAE | R² Score |
| :--- | :---: | :---: | :---: |
| Baseline Linear Regression | 14.82 | 11.20 | 0.412 |
| Random Forest Regressor | 9.45 | 6.85 | 0.748 |
| **LightGBM Regressor (Best)** | **8.12** | **5.90** | **0.814** |

### Feature Importance & Popularity Distribution

```
Feature Importance (LightGBM Top 5)
-----------------------------------------------------------
1. Artist Popularity Avg   ██████████████████████ 38%
2. Loudness (dB)           ████████████ 22%
3. Danceability            █████████ 16%
4. Valence (Positivity)    ██████ 11%
5. Acousticness            ████ 8%
-----------------------------------------------------------
```

![Model Feature Importance Visualization](https://via.placeholder.com/800x400.png?text=Spotify+Popularity+Model+Feature+Importance+%26+Residual+Plots)

---

## 📂 Directory Structure

```
ml-project/
├── data/              # Raw & processed data placeholders
├── src/               # Python source modules (data loader, train, predict)
├── notebooks/         # Jupyter notebooks for EDA and experiment tracking
├── models/            # Serialized trained model binaries (.pkl, .joblib)
├── saved_artifacts/   # Preprocessing scalers, encoders, and evaluation metrics
└── README.md          # Project documentation
```
