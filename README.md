# Student Performance Prediction System 🎓

Bu proje, lise öğrencilerinin çeşitli akademik, kişisel ve çevresel faktörlere bakarak gelecek sınav puanlarını tahmin eden bir Yapay Zeka (AI) uygulamasıdır. Uçtan uca bir Makine Öğrenmesi projesi olarak tasarlanmıştır.

## 🚀 Proje Hakkında
Bu uygulama, öğrencilerin başarılarını etkileyen faktörleri (örneğin çalışma saati, aile katılımı, ders devamlılığı vb.) analiz eder ve eğitilmiş bir makine öğrenmesi modeli (Linear Regression) kullanarak tahmini bir sınav puanı üretir.

### Özellikler
*   **Veri Analizi (EDA):** Veri setinin detaylı analizi ve görselleştirilmesi.
*   **Makine Öğrenmesi:** Scikit-learn ile eğitilmiş ve optimize edilmiş regresyon modelleri.
*   **REST API:** FastAPI ile geliştirilmiş, modelin dış dünyayla konuşmasını sağlayan hızlı bir backend.
*   **Modern Arayüz:** Next.js ve Tailwind CSS ile tasarlanmış şık ve duyarlı (responsive) bir kullanıcı arayüzü.

## 🛠️ Teknolojiler
*   **Backend & ML:** Python, FastAPI, Scikit-learn, Pandas, Joblib
*   **Frontend:** TypeScript, Next.js, Tailwind CSS
*   **Veri Seti:** Student Performance Factors

## 📦 Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### 1. Ön Gereksinimler
*   Python 3.8 veya üzeri
*   Node.js 18 veya üzeri

### 2. Depoyu Klonlayın
```bash
git clone https://github.com/eyyorivaille/StudentPerformance.git
cd StudentPerformance
```

### 3. Backend (API) Kurulumu
```bash
# Sanal ortam oluşturma
python -m venv .venv

# Sanal ortamı aktif etme (Windows)
.venv\Scripts\activate

# Gereksinimleri yükleme
pip install -r backend/requirements.txt

# Modeli eğitme (Eğer models klasörü boşsa)
python notebooks/train_model.py

# Sunucuyu başlatma
uvicorn backend.main:app --reload
```
API şu adreste çalışacaktır: `http://127.0.0.1:8000`

### 4. Frontend (Arayüz) Kurulumu
Yeni bir terminal açın ve aşağıdaki komutları girin:
```bash
cd frontend

# Paketleri yükleme
npm install

# Uygulamayı başlatma
npm run dev
```
Uygulama şu adreste çalışacaktır: `http://localhost:3000`

## 📂 Proje Yapısı
```
StudentPerformance/
├── backend/            # FastAPI uygulaması (API)
├── frontend/           # Next.js uygulaması (Arayüz)
├── data/               # Ham veri seti
├── models/             # Eğitilmiş model dosyaları (.pkl)
├── notebooks/          # Veri analizi ve model eğitim kodları
├── Arastirma_Raporu.md # Detaylı proje araştırma raporu
└── README.md           # Proje dokümantasyonu
```

## 📊 Araştırma Raporu
Projenin arkasındaki bilimsel süreç, hipotez testleri ve model karşılaştırmaları hakkında detaylı bilgi için [Arastırma Raporu](Arastirma_Raporu.md) dosyasını inceleyebilirsiniz.

---
Geliştirici: [Arda Ardıç]
Lisans: MIT
