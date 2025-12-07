from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# 1. Uygulama Başlatma
app = FastAPI(
    title="Student Performance Prediction API",
    description="Öğrenci performansını tahmin eden makine öğrenmesi modeli için API.",
    version="1.0.0"
)

# CORS Ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend adresi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Modeli Yükleme
# Dosya yolunu dinamik olarak buluyoruz (bu dosyanın olduğu yerin bir üst klasöründeki models klasörü)
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "models", "student_performance_model.pkl")

if not os.path.exists(model_path):
    raise RuntimeError(f"Model dosyası bulunamadı: {model_path}. Lütfen önce modeli eğitin.")

try:
    model = joblib.load(model_path)
    print("Model başarıyla yüklendi.")
except Exception as e:
    raise RuntimeError(f"Model yüklenirken hata oluştu: {e}")

# 3. Veri Modeli (Pydantic)
# Kullanıcıdan gelecek verinin şemasını tanımlıyoruz.
# EDA aşamasındaki sütun isimleri ve tipleriyle birebir aynı olmalı.
class StudentData(BaseModel):
    Hours_Studied: int
    Attendance: int
    Parental_Involvement: str
    Access_to_Resources: str
    Extracurricular_Activities: str
    Sleep_Hours: int
    Previous_Scores: int
    Motivation_Level: str
    Internet_Access: str
    Tutoring_Sessions: int
    Family_Income: str
    Teacher_Quality: str
    School_Type: str
    Peer_Influence: str
    Physical_Activity: int
    Learning_Disabilities: str
    Parental_Education_Level: str
    Distance_from_Home: str
    Gender: str

# 4. Endpoints
@app.get("/")
def read_root():
    return {"message": "API Hazır. /predict endpoint'ini kullanarak tahmin yapabilirsiniz."}

@app.post("/predict")
def predict_performance(data: StudentData):
    try:
        # Gelen veriyi (dict) DataFrame'e çevir
        # Tek bir satır olduğu için index=[0] veriyoruz.
        data_dict = data.dict()
        df = pd.DataFrame([data_dict])
        
        # Modeli kullanarak tahmin yap
        # Pipeline içindeki ön işleme adımları (encoding/scaling) otomatik çalışacak.
        prediction = model.predict(df)
        
        # Sonucu döndür (Numpy array olduğu için float'a çeviriyoruz)
        return {
            "prediction_score": float(prediction[0])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Tahmin sırasında hata oluştu: {str(e)}")
