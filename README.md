# EcoSplit: Automated Waste Segregation

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Used-orange?style=flat-square&logo=tensorflow)
![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-success?style=flat-square&logo=opencv)
![CNN](https://img.shields.io/badge/CNN-Model-green?style=flat-square)

**EcoSplit** is an AI-powered automated waste segregation system that classifies waste into categories such as **organic** and **inorganic** using image processing and machine learning. Currently, the system works with static images, and real-time camera-based waste detection is planned as a future enhancement. EcoSplit aims to support sustainable waste management in smart cities through intelligent automation.

---

## 🚀 Features

- Waste classification using a trained machine learning model
- Categorizes waste into:
  - Organic
  - Inorganic
- Built using TensorFlow and OpenCV
- Simple and modular design for easy upgrades

---

## 🧠 Model Training

Model training is performed using a Convolutional Neural Network (CNN) in TensorFlow/Keras.

- File: `ecosplit_model_traning.ipynb`

---

## 🔮 Future Enhancements

- Integrate real-time camera feed for live waste detection
- Add support for recyclable waste category
- Deploy on embedded systems (e.g., Raspberry Pi)
- Connect to hardware components for physical sorting

---

## 📊 Dataset Structure

```
dataset/
│
├── train/
│ ├── organic/
│ │ ├── img1.jpg
│ │ └── ...
│ └── organic/
│   │ ├── img1.jpg
│   │ └── ...
│
└── test/
  ├── organic/
  │ ├── img1.jpg
  │ └── ...
  └── organic/
    │ ├── img1.jpg
    │ └── ...
```

---

## 📁 Project Structure

```
├── main.py                     # Image classification script
├── ecosplit_model_traning.ipynb # Jupyter notebook for model training
├── waste_model.h5              # Trained model (after running notebook)
├── dataset/                    # Training dataset
```

---
📄 License

MIT License © 2025 Aman Chand
---
## Author

Created by Aman Chand.





