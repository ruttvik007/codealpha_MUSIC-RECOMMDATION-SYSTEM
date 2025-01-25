from django.shortcuts import render
import os
import pickle
from django.conf import settings

# Load model
model_path = os.path.join(settings.BASE_DIR, 'music_app', 'model', 'music_recommendation_model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def home(request):
    # Render a simple home page with a link to the prediction page
    return render(request, 'music_app/home.html')

def predict(request):
    if request.method == 'POST':
        # Extract input features
        tempo = float(request.POST['tempo'])
        danceability = float(request.POST['danceability'])
        energy = float(request.POST['energy'])
        hour = int(request.POST['hour'])

        # Create input data for prediction
        input_data = [[tempo, danceability, energy, hour]]

        # Predict
        prediction = model.predict(input_data)
        prediction_text = "Song is repeated" if prediction[0] == 1 else "Song is not repeated"

        return render(request, 'music_app/result.html', {'prediction': prediction_text})
    return render(request, 'music_app/predict.html')
