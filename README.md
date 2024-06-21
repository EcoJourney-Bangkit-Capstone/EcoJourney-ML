# Ecojourney Object Detection and Image Classification

Machine Learning pada Eco Journey dirancang untuk mendukung platform Ecojourney, yang mencakup fitur deteksi objek jenis sampah tertentu, dan melakukan klasifikasi berdasarkan gambar sampah.

## Fitur

1. **Trash Object Detection**

   - Melakukan object detection pada kamera secara real-time.
   - Melakukan lokalisasi bounding box pada objek sampah yang dikenali.
   - Melakukan klassifikasi sampah berdasarkan hasil bounding box.
   - Memberikan informasi terkait nilai probability dari hasil klasifikasi.

2. **Trash Image Classification**
   - Melakukan klasifikasi sampah berdasarkan gambar yang diunggah atau hasil foto kamera.
   - Memberikan informasi terkait hasil klassifikasi sampah.

## Teknologi yang Digunakan

- Python
- TensorFlow
- TensorFlow Lite

## Struktur Proyek

```bash
.
├── README.md
├── TFLite-Trash-Detection-with-TFLite-Model-Maker
│   ├── TFLite_Model_Maker.ipynb
│   ├── create_csv.py
│   ├── data
│   │   ├── test
│   │   │   ├── **.jpg
│   │   │   ├── **.xml
│   │   ├── test_labels.csv
│   │   ├── train
│   │   │   ├── **.jpg
│   │   │   ├── **.xml
│   │   └── train_labels.csv
│   ├── eda.ipynb
│   ├── model.tflite
│   ├── model_edgetpu.log
│   ├── model_edgetpu.tflite
│   ├── process_data.py
│   └── requirements.txt
└── img_classification
    ├── Image_Classification.ipynb
    ├── labels.txt
    ├── metadata.py
    ├── model.tflite
    ├── model_with_metadata.tflite
    └── requirements.txt
```

# Konfigurasi

## Object Detection Setup
1. Clone the Machine Learning Repository
   ```bash
   git clone https://github.com/EcoJourney-Bangkit-Capstone/EcoJourney-ML.git
   ```
2. Change the directory to /TFLite-Trash-Detection-with-TFLite-Model-Maker/
   ```bash
   cd TFLite-Trash-Detection-with-TFLite-Model-Maker/
   ```
3. Download object detection dataset from [Drive](https://drive.google.com/drive/folders/153YmYgm2rV4s0FJ5HKiO-UQ5wUCtS_C5?usp=sharing)
   
4. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```
5. Run the notebook
6. Done

## Image Classification Setup
1. Clone the Machine Learning Repository
    ```bash
    git clone https://github.com/EcoJourney-Bangkit-Capstone/EcoJourney-ML.git
    ```
2. Change the directory to /Waste-Image-Classification/
    ```bash
    cd Waste-Image-Classification/
    ```
3. Download image classification dataset from [Drive](https://drive.google.com/drive/folders/153YmYgm2rV4s0FJ5HKiO-UQ5wUCtS_C5?usp=sharing)
4. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```
5. Run the notebook
6. Done