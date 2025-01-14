# SUML-PredictOlympics

## Opis projektu

**SUML-PredictOlympics** to aplikacja wykorzystująca uczenie maszynowe do przewidywania szans na zdobycie medali przez kraje na nadchodzących Igrzyskach Olimpijskich. Projekt bazuje na historycznych danych z igrzysk olimpijskich i umożliwia analizę oraz prognozowanie wyników, wspierając sportowców i organizatorów w przygotowaniach do wydarzenia.

### Główne funkcje
- Analiza danych historycznych uczestników igrzysk olimpijskich.
- Przewidywanie prawdopodobieństwa zdobycia medali (złoto, srebro, brąz).
- Sortowanie krajów według ich szans na sukces.

### Technologie
#### Backend:
- **Python** (framework: Flask)
- **Biblioteki:** pandas, numpy, scikit-learn, joblib, scipy, pyodbc, os

#### Frontend:
- **Angular**

#### Hosting:
- Platforma Render do publikacji API

## Instalacja i uruchomienie

### Wymagania systemowe
- System operacyjny: Windows 7-11
- Wolne miejsce na dysku: 700 MB
- Python w wersji 3.9 lub nowszej

### Instalacja
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/JakubLipinski1/SUML-PredictOlympics.git
   cd SUML-PredictOlympics
   ```
2. Zainstaluj wymagane biblioteki:
   ```bash
   pip install -r requirements.txt
   ```

### Uruchamianie aplikacji lokalnie
1. Uruchom backend (Flask):
   ```bash
   python app.py
   ```
2. Frontend uruchom przy użyciu Angular CLI:
   ```bash
   ng serve
   ```
3. Otwórz aplikację w przeglądarce pod adresem:
   ```
   http://localhost:4200
   ```

### Uruchamianie w środowisku produkcyjnym
- Aplikacja została wdrożona na platformie Render i jest dostępna online. Aby uzyskać dostęp, odwiedź stronę [PredictOlympics](https://github.com/JakubLipinski1/SUML-PredictOlympics).

## Struktura API
Aplikacja udostępnia następujące punkty końcowe:

- `/sports` – Zwraca listę dostępnych dyscyplin sportowych.
- `/sport/events` – Zwraca podkategorie dla wybranej dyscypliny.
- `/predict` – Zwraca listę trzech krajów z największym prawdopodobieństwem zdobycia medalu.

## Opis danych
W projekcie wykorzystano dane historyczne igrzysk olimpijskich (1896-2016). Dane te zawierają informacje o:
- Sportowcach (imię, nazwisko, wiek, wzrost, waga, płeć).
- Krajach uczestniczących.
- Dyscyplinach sportowych.
- Medale (złoto, srebro, brąz).

### Link do danych:
[Dane na Kaggle](https://www.kaggle.com/datasets/mysarahmadbhat/120-years-of-olympic-history)

## Główne funkcjonalności aplikacji
- **Trenowanie modeli:**
  Modele regresji logistycznej są trenowane i zapisywane w pliku `models_and_scaler.pkl`.
- **Przewidywanie wyników:**
  Na podstawie wprowadzonego zbioru danych aplikacja oblicza szanse na zdobycie medalu przez kraje.

## Autorzy
- **Jakub Lipiński (S24915)**
- **Wiktor Bućkowski (S24604)**
- **Bartosz Iwańczyk (S24897)**
