import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# 1. Veri Yükleme
print("Veri yükleniyor...")
data_path = "data/StudentPerformanceFactors.csv"
if not os.path.exists(data_path):
    print("Veri dosyası bulunamadı!")
    exit()

df = pd.read_csv(data_path)

# 2. Ön İşleme (Preprocessing) Hazırlığı
print("Veri ön işleme hazırlanıyor...")

# Hedef ve Özelliklerin Ayrılması
X = df.drop("Exam_Score", axis=1)
y = df["Exam_Score"]

# Kategorik ve Sayısal Sütunların Belirlenmesi
categorical_cols = X.select_dtypes(include=['object']).columns
numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns

# Pipeline Oluşturma
# Sayısal veriler için: Standartlaştırma (StandardScaler)
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# Kategorik veriler için: Eksikleri doldurma (En sık değer) ve One-Hot Encoding
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# İkisini birleştirme (ColumnTransformer)
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

from sklearn.ensemble import RandomForestRegressor

# 3. Model Pipeline Oluşturma
# İki farklı pipeline oluşturuyoruz: Biri Linear Regression, biri Random Forest için.
lr_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('regressor', LinearRegression())])

rf_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))])

# 4. Eğitim ve Test Setine Ayırma
print("Veri eğitim ve test setlerine ayrılıyor...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Modelleri Eğitme
print("Linear Regression eğitiliyor...")
lr_pipeline.fit(X_train, y_train)

print("Random Forest eğitiliyor...")
rf_pipeline.fit(X_train, y_train)

# 6. Değerlendirme ve Karşılaştırma
print("Modeller değerlendiriliyor...")
y_pred_lr = lr_pipeline.predict(X_test)
y_pred_rf = rf_pipeline.predict(X_test)

mae_lr = mean_absolute_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print(f"\n--- Karşılaştırma Sonuçları ---")
print(f"Linear Regression -> MAE: {mae_lr:.2f}, R2: {r2_lr:.2f}")
print(f"Random Forest     -> MAE: {mae_rf:.2f}, R2: {r2_rf:.2f}")

with open("models/training_results.txt", "w", encoding="utf-8") as f:
    f.write(f"Linear Regression -> MAE: {mae_lr:.2f}, R2: {r2_lr:.2f}\n")
    f.write(f"Random Forest     -> MAE: {mae_rf:.2f}, R2: {r2_rf:.2f}\n")

# 7. En İyi Modeli Kaydetme
if r2_rf > r2_lr:
    best_model = rf_pipeline
    best_model_name = "Random Forest"
else:
    best_model = lr_pipeline
    best_model_name = "Linear Regression"

print(f"\nEn başarılı model seçildi: {best_model_name}")


# Modeli Kaydetme
print("Model kaydediliyor...")
if not os.path.exists("models"):
    os.makedirs("models")

joblib.dump(best_model, "models/student_performance_model.pkl")
print(f"En iyi model ({best_model_name}) 'models/student_performance_model.pkl' olarak kaydedildi.")
