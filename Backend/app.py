from flask import Flask, jsonify, request
from flask_cors import CORS
import pyodbc
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../suml')))

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
    return jsonify({'sports': sports}), 200
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
    return jsonify({'events': sports}), 200
  else:
    return jsonify({'error': 'File not found or empty'}), 404


@app.route('/olympic/predict', methods=['GET'])
def get_predict():
  """Endpoint zwracający listę dyscyplin sportowych."""
  sports_file = '../suml/events.txt'  # Ścieżka do pliku
  sports = get_sports_list(sports_file)
  if sports:
    return jsonify({'events': sports}), 200
  else:
    return jsonify({'error': 'File not found or empty'}), 404


@app.route('/predict', methods=['GET'])
def predict_top_3_countries_api():
    # Pobranie nazwy wydarzenia z parametrów zapytania
    event_name = request.get_json().get('event_name')
    if not event_name:
        return jsonify({'error': 'Nie podano nazwy wydarzenia. Użyj parametru ?event_name=<nazwa_wydarzenia>'}), 400

    # Filtrowanie danych dla wybranego wydarzenia
    event_data = Predict.df[Predict.df['Event'] == event_name]
    if event_data.empty:
        return jsonify({'error': f"Nie znaleziono wydarzenia o nazwie: {event_name}"}), 404

    # Tworzenie cech dla eventu
    event_features = pd.get_dummies(event_data[['Team', 'Sport', 'Event', 'Year', 'Season']], drop_first=True)
    event_features = event_features.reindex(columns=features.columns, fill_value=0)
    event_features_scaled = scaler.transform(event_features)

    # Przewidywanie szans na medale
    results = []
    for medal_type, model in models.items():
        probabilities = model.predict_proba(event_features_scaled)[:, 1]
        team_probabilities = dict(zip(event_data['Team'], probabilities))

        # Top 3 drużyny
        top_3_teams = sorted(team_probabilities.items(), key=lambda x: x[1], reverse=True)[:3]

        # Tworzenie wyniku dla danego medalu
        result = f"Top 3 kraje z największą szansą na zdobycie medalu {medal_type.lower()} w: {event_name}\n"
        for team, prob in top_3_teams:
            result += f"{team}: {prob:.2%}\n"
        results.append(result)

    # Łączenie wyników w jeden string
    return jsonify({'results': '\n'.join(results)}), 200


if __name__ == '__main__':
    app.run(debug=True)
