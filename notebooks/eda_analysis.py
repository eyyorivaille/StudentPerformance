import pandas as pd
import os

# Veri setini yükle
data_path = "data/StudentPerformanceFactors.csv"
if not os.path.exists(data_path):
    print(f"Hata: {data_path} bulunamadı.")
    exit()

df = pd.read_csv(data_path)

import sys

# Çıktıyı dosyaya yönlendir
with open("notebooks/eda_results.txt", "w", encoding="utf-8") as f:
    sys.stdout = f
    
    print("--- Veri Seti Genel Bilgileri ---")
    print(f"Satır Sayısı: {df.shape[0]}")
    print(f"Sütun Sayısı: {df.shape[1]}")
    print("\\n--- İlk 5 Satır ---")
    print(df.head())

    print("\\n--- Veri Tipleri ve Eksik Değerler ---")
    df.info() # info() methodu buffer argümanı almaz, bu yüzden sys.stdout yönlendirmesi çalışmayabilir.
    # info() için özel işlem:
    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    print(buffer.getvalue())

    print("\\n--- Eksik Değerlerin Sayısı ---")
    print(df.isnull().sum())

    print("\\n--- İstatistiksel Özet (Sayısal) ---")
    print(df.describe())

    print("\\n--- Kategorik Değerlerin Dağılımı ---")
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        print(f"\\nSütun: {col}")
        print(df[col].value_counts())

    print("\\n--- Korelasyon Analizi (Exam_Score ile) ---")
    numeric_df = df.select_dtypes(include=['number'])
    correlation = numeric_df.corr()['Exam_Score'].sort_values(ascending=False)
    print(correlation)
    
    # Standart çıktıyı geri yükle
    sys.stdout = sys.__stdout__
print("EDA analizi tamamlandı ve notebooks/eda_results.txt dosyasına kaydedildi.")
