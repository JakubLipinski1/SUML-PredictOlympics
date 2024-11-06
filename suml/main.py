import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.impute import SimpleImputer

# Załóżmy, że dane są w pliku CSV
df = pd.read_csv(r'przefiltrowane.csv')

df = df.drop(columns=['ID'])
df = df.drop(columns=['Name'])


# Zamiana wartości `Medal` na wartości numeryczne (np. 0 - brak medalu, 1 - medal)

df['Medal'] = df['Medal'].fillna('No Medal')

label_encoder = LabelEncoder()
df['Medal'] = label_encoder.fit_transform(df['Medal'])

# Podział na cechy (X) i zmienną docelową (y)
X = df.drop(['Medal', 'Team', 'NOC', 'Games', 'City', 'Event'], axis=1)
y = df['Medal']

# Dalsza konwersja danych kategorycznych
X = pd.get_dummies(X, drop_first=True)

imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Definiujemy algorytmy do przetestowania
models = {
    'Logistic Regression': LogisticRegression(max_iter=2000),
    'Decision Tree': DecisionTreeClassifier(),
    'K-Nearest Neighbors': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB(),
    'Support Vector Classifier': SVC()
}

# Zbadajmy dokładność każdego algorytmu
results = {}
for model_name, model in models.items():
    # Trening
    model.fit(X_train, y_train)
    # Predykcja
    y_pred = model.predict(X_test)
    # Dokładność
    accuracy = accuracy_score(y_test, y_pred)
    results[model_name] = accuracy

# Wyświetlenie wyników
best_model = max(results, key=results.get)
print("Najlepszy algorytm to:", best_model, "z dokładnością:", results[best_model])

