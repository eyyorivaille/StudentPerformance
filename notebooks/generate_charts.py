import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Veri setini yükle
data_path = "data/StudentPerformanceFactors.csv"
if not os.path.exists("report_assets"):
    os.makedirs("report_assets")

df = pd.read_csv(data_path)

# Grafik Ayarları
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Heatmap (Korelasyon)
# Sadece sayısal sütunları alalım
numeric_df = df.select_dtypes(include=['number'])
corr = numeric_df.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr[['Exam_Score']].sort_values(by='Exam_Score', ascending=False), 
            annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Değişkenlerin Sınav Puanı ile Korelasyonu')
plt.tight_layout()
plt.savefig('report_assets/heatmap.png')
plt.close()

# 2. Regresyon Grafiği (Attendance vs Exam Score)
plt.figure(figsize=(10, 6))
sns.regplot(x='Attendance', y='Exam_Score', data=df, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
plt.title('Derse Devam ve Sınav Puanı İlişkisi (Regresyon)')
plt.xlabel('Devamlılık (%)')
plt.ylabel('Sınav Puanı')
plt.savefig('report_assets/regression_attendance.png')
plt.close()

# 3. Saçılım Grafiği (Hours Studied vs Exam Score)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Hours_Studied', y='Exam_Score', hue='Access_to_Resources', data=df, alpha=0.6)
plt.title('Çalışma Saati ve Sınav Puanı İlişkisi (Kaynak Erişimine Göre)')
plt.xlabel('Haftalık Çalışma Saati')
plt.ylabel('Sınav Puanı')
plt.savefig('report_assets/scatter_hours.png')
plt.close()

print("Grafikler 'report_assets' klasörüne kaydedildi.")
