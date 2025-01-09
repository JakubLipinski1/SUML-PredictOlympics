import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os


# Funkcje do zapisywania i wczytywania modeli
def save_models(models, scaler, filename="models_and_scaler.pkl"):
    with open(filename, "wb") as file:
        joblib.dump({"models": models, "scaler": scaler}, file)


def load_models(filename="./suml/models_and_scaler.pkl"):
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            return joblib.load(file)
    else:
        return None



df = pd.read_csv("../suml/przefiltrowane.csv")
df.dropna(inplace=True)

# Tworzenie kolumn binarnych dla każdego rodzaju medalu
df['Gold'] = df['Medal'].apply(lambda x: 1 if x == 'Gold' else 0)
df['Silver'] = df['Medal'].apply(lambda x: 1 if x == 'Silver' else 0)
df['Bronze'] = df['Medal'].apply(lambda x: 1 if x == 'Bronze' else 0)

# Konwersja zmiennych kategorycznych na zmienne binarne
features = pd.get_dummies(df[['Team', 'Sport', 'Event', 'Year', 'Season']], drop_first=True)
labels = df[['Gold', 'Silver', 'Bronze']]

# Sprawdzenie czy iostnieje zapisany model
data = load_models()
if data:
    models = data["models"]
    scaler = data["scaler"]
    print("Wczytano istniejące modele.")
else:
    print("Brak zapisanych modeli. Rozpoczynam trening...")

    # Skalowanie danych
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Trening modeli
    models = {}
    for medal_type in labels.columns:
        y = labels[medal_type]
        model = LogisticRegression(max_iter=2000, solver='saga')
        model.fit(features_scaled, y)
        models[medal_type] = model

    # Zapisz modele i skalera
    save_models(models, scaler)
    print("Modele zapisano.")


# Funkcja przewidująca top 3 kraje dla konkretnego wydarzenia
def predict_top_3_countries(models, scaler, event_name):
    # Filtrowanie danych dla wybranego wydarzenia
    event_data = df[df['Event'] == event_name]
    if event_data.empty:
        print("Nie znaleziono wydarzenia o nazwie:", event_name)
        return

    # Tworzenie cech dla eventu
    event_features = pd.get_dummies(event_data[['Team', 'Sport', 'Event', 'Year', 'Season']], drop_first=True)
    event_features = event_features.reindex(columns=features.columns, fill_value=0)
    event_features_scaled = scaler.transform(event_features)

    # Przewidywanie szans na medale
    for medal_type, model in models.items():
        probabilities = model.predict_proba(event_features_scaled)[:, 1]
        team_probabilities = dict(zip(event_data['Team'], probabilities))

        top_3_teams = sorted(team_probabilities.items(), key=lambda x: x[1], reverse=True)[:3]

        print(f"\nTop 3 kraje z największą szansą na zdobycie medalu {medal_type.lower()} w: {event_name}")
        for team, prob in top_3_teams:
            print(f"{team}: {prob:.2%}")


def predict_top_3_countries_API(event_name):
  # Filtrowanie danych dla wybranego wydarzenia
  event_data = df[df['Event'] == event_name]
  if event_data.empty:
    print("Nie znaleziono wydarzenia o nazwie:", event_name)
    return

  # Tworzenie cech dla eventu
  event_features = pd.get_dummies(event_data[['Team', 'Sport', 'Event', 'Year', 'Season']], drop_first=True)
  event_features = event_features.reindex(columns=features.columns, fill_value=0)
  event_features_scaled = scaler.transform(event_features)

  # Przewidywanie szans na medale
  for medal_type, model in models.items():
    probabilities = model.predict_proba(event_features_scaled)[:, 1]
    team_probabilities = dict(zip(event_data['Team'], probabilities))

    top_3_teams = sorted(team_probabilities.items(), key=lambda x: x[1], reverse=True)[:3]

    print(f"\nTop 3 kraje z największą szansą na zdobycie medalu {medal_type.lower()} w: {event_name}")
    for team, prob in top_3_teams:
      print(f"{team}: {prob:.2%}")


# # Pobieranie od użytkownika nazwy wydarzenia
# event_name = input("Podaj nazwę wydarzenia: ")
# predict_top_3_countries(models, scaler, event_name)

