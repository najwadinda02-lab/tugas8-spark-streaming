# Real-time Fraud Detection System 💳
**Tugas 8 - Pemrosesan Data Terdistribusi**

Sistem ini dirancang untuk mendeteksi transaksi mencurigakan (fraud) secara real-time menggunakan arsitektur **Apache Kafka** sebagai message broker dan **Apache Spark Streaming** sebagai engine pengolah datanya.

## 🚀 Arsitektur Sistem
Sistem bekerja dengan alur sebagai berikut:
1. **Producer**: Script Python mensimulasikan transaksi bank dan mengirim data dalam format JSON ke Kafka Topic.
2. **Broker**: Apache Kafka menampung aliran data transaksi secara antrean (queue).
3. **Stream Processing**: Spark Streaming membaca data dari Kafka, melakukan transformasi skema, dan mendeteksi kriteria fraud secara real-time.
4. **Output**: Hasil deteksi ditampilkan di konsol dan disimpan ke dalam folder output.

---

## 🛠️ Teknologi yang Digunakan
* **Apache Kafka**: Message Broker untuk pengiriman data stream.
* **Apache Spark 3.5.1**: Pemrosesan data terdistribusi.
* **Python**: Bahasa pemrograman utama (PySpark & Kafka-Python).
* **WSL2 (Ubuntu)**: Lingkungan pengembangan sistem.

---

## 📁 Struktur Folder
```text
tugas8_najwa_230104040082/
├── scripts/
│   ├── kafka_producer_bank.py       # Mengirim simulasi transaksi ke Kafka
│   └── spark_streaming_fraud_v2.py  # Logika deteksi fraud (Spark Streaming)
├── dashboard/
│   └── fraud_dashboard_v2.py        # Script visualisasi/dashboard (opsional)
└── README.md                        # Dokumentasi tugas
