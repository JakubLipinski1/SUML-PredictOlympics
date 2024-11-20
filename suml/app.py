from flask import Flask, jsonify, request
from flask_cors import CORS
import pyodbc
import sys
import os

import Predict


app = Flask(__name__)
CORS(app)

@app.route('/elementy', methods=['GET'])
def get_element():
        return jsonify({'nazwa': 'elementTestowy', 'opis': 'taki o to element'})


def get_sports_list(file_path):
  """Wczytuje listę dyscyplin sportowych z pliku."""
  try:
    with open(file_path, 'r') as file:
      sports = [line.strip() for line in file.readlines()]
    return sports
  except FileNotFoundError:
    return []


@app.route('/sports', methods=['GET'])
def get_sports():
  """Endpoint zwracający listę dyscyplin sportowych."""
  sports_file = '../suml/sports.txt'  # Ścieżka do pliku
  sports = get_sports_list(sports_file)
  if sports:
    return jsonify(sports), 200
  else:
    return jsonify({'error': 'File not found or empty'}), 404

def get_sports_event(file_path):
  """Wczytuje listę dyscyplin sportowych z pliku."""
  try:
    with open(file_path, 'r') as file:
      sports = [line.strip() for line in file.readlines()]
    return sports
  except FileNotFoundError:
    return []


@app.route('/sport/events', methods=['GET'])
def get_sport_events():
  """Endpoint zwracający listę dyscyplin sportowych."""
  sports_file = '../suml/events.txt'  # Ścieżka do pliku
  sports = get_sports_list(sports_file)
  if sports:
    return jsonify(sports), 200
  else:
    return jsonify({'error': 'File not found or empty'}), 404



@app.route('/predict', methods=['GET'])
def predict_top_3_countries_api():
    # Pobranie nazwy wydarzenia z parametrów zapytania
    # event_name = request.get_json().get('event_name')
    event_name = request.args.get('event_name')
    if not event_name:
        return jsonify({'error': 'Nie podano nazwy wydarzenia. Prześlij JSON z parametrem "event_name".'}), 400

    # Filtrowanie danych dla wybranego wydarzenia
    event_data = Predict.df[Predict.df['Event'] == event_name]
    if event_data.empty:
        return jsonify({'error': f"Nie znaleziono wydarzenia o nazwie: {event_name}"}), 404

    # Tworzenie cech dla eventu
    event_features = Predict.pd.get_dummies(event_data[['Team', 'Sport', 'Event', 'Year', 'Season']], drop_first=True)
    event_features = event_features.reindex(columns=Predict.features.columns, fill_value=0)
    event_features_scaled = Predict.scaler.transform(event_features)

    # Przewidywanie szans na medale
    results = []
    for medal_type, model in Predict.models.items():
        probabilities = model.predict_proba(event_features_scaled)[:, 1]
        team_probabilities = dict(zip(event_data['Team'], probabilities))

        # Top 3 drużyny
        top_3_teams = sorted(team_probabilities.items(), key=lambda x: x[1], reverse=True)[:3]

        # Tworzenie wyniku w formie JSON
        results.append({
            'medal_type': medal_type.lower(),
            'event_name': event_name,
            'top_teams': [
                {'team': team, 'probability': f"{prob:.2%}"} for team, prob in top_3_teams
            ]
        })

    # Zwracanie wyniku w formacie JSON
    return jsonify(results), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
