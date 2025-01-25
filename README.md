# Music Recommendation System

## Overview

Spotify's recommendation system, powered by machine learning, predicts a user's likelihood of repeatedly listening to a song within a set timeframe. By analyzing user song histories and timestamps, it generates personalized song recommendations. The system uses a dataset where `1` indicates repeated plays within a month and `0` indicates songs that are not repeated. This model helps in improving user engagement by suggesting songs that are more likely to be replayed.

## Features

- **Machine Learning Model**: The system uses a trained machine learning model (Random Forest Classifier) to predict if a song will be repeated based on various audio features.
- **Personalized Recommendations**: Based on the user's song history and other features, the system generates personalized song recommendations.
- **User Interaction**: Users can input specific song features (like tempo, danceability, energy, etc.) to check if a song is likely to be repeated.

## Technologies Used

- **Django**: Web framework for building the web application.
- **Scikit-learn**: Python library used to train and deploy the machine learning model.
- **HTML/CSS**: Frontend technologies for building the user interface.
- **JavaScript**: For frontend interactivity.
- **Pickle**: Used for saving and loading the trained machine learning model.


