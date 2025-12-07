import requests
import json

url = "http://127.0.0.1:8000/predict"

# Örnek bir öğrenci verisi (Veri setinden rastgele bir satıra benzer)
student_data = {
    "Hours_Studied": 20,
    "Attendance": 80,
    "Parental_Involvement": "Medium",
    "Access_to_Resources": "High",
    "Extracurricular_Activities": "Yes",
    "Sleep_Hours": 7,
    "Previous_Scores": 75,
    "Motivation_Level": "Medium",
    "Internet_Access": "Yes",
    "Tutoring_Sessions": 1,
    "Family_Income": "Medium",
    "Teacher_Quality": "High",
    "School_Type": "Public",
    "Peer_Influence": "Positive",
    "Physical_Activity": 3,
    "Learning_Disabilities": "No",
    "Parental_Education_Level": "College",
    "Distance_from_Home": "Near",
    "Gender": "Male"
}

try:
    print(f"İstek gönderiliyor: {url}")
    response = requests.post(url, json=student_data)
    
    if response.status_code == 200:
        print("Başarılı!")
        print("Tahmin Sonucu:", response.json())
    else:
        print("Hata:", response.status_code)
        print(response.text)
except Exception as e:
    print("Bağlantı hatası:", e)
