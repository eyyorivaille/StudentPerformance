"use client";

import { useState } from "react";
import Image from "next/image";

export default function Home() {
  const [formData, setFormData] = useState({
    Hours_Studied: 20,
    Attendance: 90,
    Parental_Involvement: "Medium",
    Access_to_Resources: "Medium",
    Extracurricular_Activities: "No",
    Sleep_Hours: 7,
    Previous_Scores: 75,
    Motivation_Level: "Medium",
    Internet_Access: "Yes",
    Tutoring_Sessions: 0,
    Family_Income: "Medium",
    Teacher_Quality: "Medium",
    School_Type: "Public",
    Peer_Influence: "Neutral",
    Physical_Activity: 3,
    Learning_Disabilities: "No",
    Parental_Education_Level: "High School",
    Distance_from_Home: "Near",
    Gender: "Male",
  });

  const [prediction, setPrediction] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: ["Hours_Studied", "Attendance", "Sleep_Hours", "Previous_Scores", "Tutoring_Sessions", "Physical_Activity"].includes(name)
        ? Number(value)
        : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Tahmin alınamadı.");
      }

      const data = await response.json();
      setPrediction(data.prediction_score);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 font-sans text-gray-900">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600 mb-4">
            Öğrenci Performans Tahmini
          </h1>
          <p className="text-lg text-gray-600">
            Yapay zeka ile öğrencinin gelecek başarı puanını hesaplayın.
          </p>
        </div>

        <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
          <div className="p-8">
            <form onSubmit={handleSubmit} className="space-y-8">
              {/* Bölüm 1: Akademik Veriler */}
              <div>
                <h3 className="text-xl font-semibold text-gray-800 mb-4 border-b pb-2">Akademik Durum</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <InputNumber label="Haftalık Çalışma Saati" name="Hours_Studied" value={formData.Hours_Studied} onChange={handleChange} min={0} max={168} />
                  <InputNumber label="Devamlılık (%)" name="Attendance" value={formData.Attendance} onChange={handleChange} min={0} max={100} />
                  <InputNumber label="Önceki Sınav Puanı" name="Previous_Scores" value={formData.Previous_Scores} onChange={handleChange} min={0} max={100} />
                  <InputNumber label="Özel Ders Sayısı (Aylık)" name="Tutoring_Sessions" value={formData.Tutoring_Sessions} onChange={handleChange} min={0} max={30} />
                </div>
              </div>

              {/* Bölüm 2: Kişisel Veriler */}
              <div>
                <h3 className="text-xl font-semibold text-gray-800 mb-4 border-b pb-2">Kişisel Bilgiler</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <Select label="Cinsiyet" name="Gender" value={formData.Gender} onChange={handleChange} options={["Male", "Female"]} />
                  <InputNumber label="Günlük Uyku Saati" name="Sleep_Hours" value={formData.Sleep_Hours} onChange={handleChange} min={0} max={24} />
                  <InputNumber label="Fiziksel Aktivite (Saat/Hafta)" name="Physical_Activity" value={formData.Physical_Activity} onChange={handleChange} min={0} max={50} />
                  <Select label="Motivasyon Seviyesi" name="Motivation_Level" value={formData.Motivation_Level} onChange={handleChange} options={["Low", "Medium", "High"]} />
                </div>
              </div>

              {/* Bölüm 3: Çevresel Faktörler */}
              <div>
                <h3 className="text-xl font-semibold text-gray-800 mb-4 border-b pb-2">Çevresel Faktörler</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                  <Select label="Ebeveyn Katılımı" name="Parental_Involvement" value={formData.Parental_Involvement} onChange={handleChange} options={["Low", "Medium", "High"]} />
                  <Select label="Kaynaklara Erişim" name="Access_to_Resources" value={formData.Access_to_Resources} onChange={handleChange} options={["Low", "Medium", "High"]} />
                  <Select label="İnternet Erişimi" name="Internet_Access" value={formData.Internet_Access} onChange={handleChange} options={["Yes", "No"]} />
                  <Select label="Aile Geliri" name="Family_Income" value={formData.Family_Income} onChange={handleChange} options={["Low", "Medium", "High"]} />
                  <Select label="Okul Türü" name="School_Type" value={formData.School_Type} onChange={handleChange} options={["Public", "Private"]} />
                  <Select label="Akran Etkisi" name="Peer_Influence" value={formData.Peer_Influence} onChange={handleChange} options={["Positive", "Neutral", "Negative"]} />
                  <Select label="Öğrenme Güçlüğü" name="Learning_Disabilities" value={formData.Learning_Disabilities} onChange={handleChange} options={["Yes", "No"]} />
                  <Select label="Ebeveyn Eğitim" name="Parental_Education_Level" value={formData.Parental_Education_Level} onChange={handleChange} options={["High School", "College", "Postgraduate"]} />
                  <Select label="Eve Uzaklık" name="Distance_from_Home" value={formData.Distance_from_Home} onChange={handleChange} options={["Near", "Moderate", "Far"]} />
                  <Select label="Öğretmen Kalitesi" name="Teacher_Quality" value={formData.Teacher_Quality} onChange={handleChange} options={["Low", "Medium", "High"]} />
                  <Select label="Okul Dışı Aktivite" name="Extracurricular_Activities" value={formData.Extracurricular_Activities} onChange={handleChange} options={["Yes", "No"]} />
                </div>
              </div>

              <div className="flex justify-center pt-6">
                <button
                  type="submit"
                  disabled={loading}
                  className="w-full md:w-1/2 flex justify-center py-4 px-6 border border-transparent rounded-xl shadow-sm text-lg font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed transform hover:scale-[1.02]"
                >
                  {loading ? (
                    <span className="flex items-center">
                      <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      Hesaplanıyor...
                    </span>
                  ) : (
                    "Tahmin Et"
                  )}
                </button>
              </div>
            </form>

            {/* Sonuç Gösterimi */}
            {prediction !== null && (
              <div className="mt-10 p-6 bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl border border-green-200 animate-in fade-in slide-in-from-bottom-4 duration-500">
                <h3 className="text-center text-xl font-medium text-green-800 mb-2">Tahmini Sınav Puanı</h3>
                <div className="text-center text-5xl font-extrabold text-green-600 mb-2">
                  {prediction.toFixed(1)}
                  <span className="text-base font-normal text-gray-500 ml-1">/ 100</span>
                </div>
                <p className="text-center text-gray-600">
                  Bu öğrenci, verilen koşullar altında yaklaşık olarak bu puanı alacaktır.
                </p>
              </div>
            )}

            {error && (
              <div className="mt-10 p-4 bg-red-50 border border-red-200 rounded-xl text-red-700 text-center">
                {error}
              </div>
            )}

          </div>
        </div>
      </div>
    </div>
  );
}

// Helper Components
function InputNumber({ label, name, value, onChange, min, max }: { label: string, name: string, value: number, onChange: any, min?: number, max?: number }) {
  return (
    <div className="flex flex-col">
      <label htmlFor={name} className="block text-sm font-medium text-gray-700 mb-1">{label}</label>
      <input
        type="number"
        name={name}
        id={name}
        value={value}
        onChange={onChange}
        min={min}
        max={max}
        className="block w-full rounded-lg border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-3 border bg-gray-50 transition-colors hover:bg-white"
        required
      />
    </div>
  );
}

function Select({ label, name, value, onChange, options }: { label: string, name: string, value: string, onChange: any, options: string[] }) {
  return (
    <div className="flex flex-col">
      <label htmlFor={name} className="block text-sm font-medium text-gray-700 mb-1">{label}</label>
      <select
        name={name}
        id={name}
        value={value}
        onChange={onChange}
        className="block w-full rounded-lg border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-3 border bg-gray-50 transition-colors hover:bg-white"
      >
        {options.map((opt) => (
          <option key={opt} value={opt}>{opt}</option>
        ))}
      </select>
    </div>
  );
}
