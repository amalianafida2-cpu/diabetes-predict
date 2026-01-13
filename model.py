import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score

# ===============================
# LOAD DATA (WAJIB sep=";")
# ===============================
data = pd.read_csv("diabetes.csv", sep=";")

# ===============================
# PREPROCESSING
# ===============================
cols_zero = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

for col in cols_zero:
    data[col] = data[col].replace(0, np.nan)
    data[col] = data[col].fillna(data[col].median())

# ===============================
# FEATURE SELECTION
# ===============================
X = data[
    ["Glucose", "BMI", "Age", "Pregnancies", "DiabetesPedigreeFunction"]
]

y = data["Outcome"]

# ===============================
# SPLIT DATA
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ===============================
# TRAIN MODEL
# ===============================
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ===============================
# EVALUATION
# ===============================
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_prob)

# ===============================
# SAVE MODEL & METRICS
# ===============================
joblib.dump(model, "logistic_model.pkl")

metrics = {
    "accuracy": accuracy,
    "auc": auc
}

joblib.dump(metrics, "metrics.pkl")

print("Model berhasil disimpan")
print("Accuracy:", round(accuracy, 3))
print("AUC:", round(auc, 3))
