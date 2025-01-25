import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Train the music recommendation model'

    def handle(self, *args, **kwargs):
        # Define data path
        data_path = r'C:\Users\ruttvik padhara\Desktop\r1\data.csv'
        if not os.path.exists(data_path):
            self.stdout.write(self.style.ERROR('Data file not found!'))
            return

        # Load data
        data = pd.read_csv(data_path)

        # Preprocess
        data['hour'] = pd.to_datetime(data['timestamp'], format='%H:%M:%S').dt.hour
        data = data.drop(columns=['id', 'name', 'timestamp'])

        # Select features
        selected_features = ['tempo', 'danceability', 'energy', 'hour']
        X = data[selected_features]
        y = data['repeated_plays']

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Save model
        model_path = os.path.join('music_app', 'model', 'music_recommendation_model.pkl')
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        with open(model_path, 'wb') as file:
            pickle.dump(model, file)

        self.stdout.write(self.style.SUCCESS('Model trained and saved successfully!'))
