# Pharmaceutical Image Classification (CNN, ResNet50, EfficientNet-B0)

This project focuses on building an image-based classifier that can identify 10 different drugs and vitamin products using deep learning.  
The goal was to compare a custom CNN model against two transfer-learning architectures (ResNet50 and EfficientNet-B0) to understand which approach works best for real-world medicine identification.

---

## Project Introduction
I wanted to explore how deep learning models, especially CNNs and transfer learning, can help recognize pharmaceutical products from images.  
The idea was to build a system that can support healthcare, pharmacy automation, and e-commerce by reducing manual identification errors and improving product verification.

This project compares:
- A **Custom CNN built from scratch**
- **ResNet50** (fine-tuned)
- **EfficientNet-B0** (fine-tuned, best performer)

---

## Dataset Used
- **Source:** Kaggle – “Drugs and Vitamins” dataset  
- **Images:** ~10,000 colored product images  
- **Classes:** 10 types of drugs/vitamins  
- **Structure:** ~1,000 images per class → clean & balanced dataset  
- **Preprocessing:**
  - All images resized to **224×224**
  - Normalized using computed dataset mean & standard deviation  
  - Dataset split: **85% train / 15% validation**

---

## Methodology & Implementation

### Tools & Frameworks
- **PyTorch + TorchVision** for model building and training  
- GPU acceleration for faster training  
- Standard image augmentation and normalization using TorchVision transforms  

### Training Setup
- Optimizer: **Adam**  
- Loss: **CrossEntropyLoss**  
- Epochs: **Up to 8**, with early stopping  
- Metrics monitored: **Accuracy**, **F1-score**, **Confusion Matrix**  

---

## Models Used

### 🔹 Custom CNN (Baseline)
A CNN built manually with:
- 4 convolution layers + ReLU  
- Batch Normalization  
- MaxPooling  
- Dropout  
- Fully connected classifier (10 classes)

Serves as a solid baseline trained completely from scratch.

---

### 🔹 ResNet50 (Fine-Tuned)
- Pre-trained on ImageNet  
- Final FC layer replaced with a 10-class output  
- Fine-tuning improves accuracy and convergence speed  
- Learns generic deep visual features extremely well  

---

### 🔹 EfficientNet-B0 (Fine-Tuned, Best Model)
- Modern CNN architecture with compound scaling  
- Efficient & high-accuracy model  
- Final layer modified for 10 classes  
- Consistently outperforms ResNet50 and the custom CNN  
- Achieved near-perfect validation results

---

##  Project Structure

```
Pharmaceutical Image Classification/
│
├── pharmafinal.ipynb          # Main training notebook
├── pharma_ui.py               # GUI application for drug viewer
├── pharmaceutical_dataset/    # Dataset folder (not included)
│   └── Drug Vision/
│       └── Data Combined/
│           ├── Alaxan/
│           ├── Bactidol/
│           ├── Bioflu/
│           ├── Biogesic/
│           ├── DayZinc/
│           ├── Decolgen/
│           ├── Fish Oil/
│           ├── Kremil S/
│           ├── Medicol/
│           └── Neozep/
│
├── .gitignore
├── README.md
└── requirements.txt
```
---

## Results & Performance Summary

### 📊 Validation Performance
| Model               | Accuracy | F1-Score |
|--------------------|----------|----------|
| Custom CNN         | ~90–94%  | ~0.90–0.95 |
| ResNet50           | ~98%     | ~0.98 |
| EfficientNet-B0    | ~99–99.5%| ~0.995 |

---

### Key Observations
- **EfficientNet-B0 performed the best**, with near-perfect results  
- Transfer learning models trained **faster and more accurately** than the custom CNN  
- Confusion matrix shows **very few misclassifications** across all 10 classes  
- Dataset is clean & balanced → helped models learn effectively  

---

## Workflow

1. Load and inspect Kaggle dataset  
2. Apply preprocessing (resize, normalization)  
3. Build training & validation dataloaders  
4. Train Custom CNN  
5. Fine-tune ResNet50 and EfficientNet-B0  
6. Compare accuracy, F1-score, and confusion matrices  
7. Analyze per-class predictions  
8. Identify best model (EfficientNet-B0)

---

## What I Did
- Prepared the image dataset with transforms and normalization  
- Built a full custom CNN architecture  
- Fine-tuned pre-trained ResNet50 and EfficientNet-B0  
- Used accuracy and F1-score to compare models  
- Generated confusion matrices for deeper insights  
- Evaluated how transfer learning improves convergence and performance  
- Documented differences in speed, performance, and reliability  

---

## GUI Demo (Concept)
A future GUI can:
- Let users upload or capture an image  
- Automatically preprocess and classify it  
- Show prediction, confidence, and top-3 alternatives  
- Integrate into pharmacy / warehouse workflows  

---


## What I Learned
- Transfer learning dramatically speeds up training and improves results  
- EfficientNet-B0 is extremely powerful for image classification with fewer parameters  
- Custom CNNs work well, but pre-trained architectures dominate in real tasks  
- Balanced datasets allow more stable and fair evaluation  
- Confusion matrices are essential for detecting per-class weaknesses  
- Normalization and consistent preprocessing are key for CNN performance  

---

## Future Improvements
- Apply stronger augmentation (brightness, color jitter, rotations, random crops)  
- Add more classes or include generic vs. branded variants  
- Fine-tune deeper layers for even higher accuracy  
- Build a deployment-ready GUI or web app for upload-and-predict  
- Add real-world testing with varied lighting, angles, and backgrounds  
- Explore transformer-based image models (ViT, Swin Transformer)

---

## Conclusion
This project shows how deep learning, especially transfer learning, can achieve highly reliable image classification for pharmaceutical products.  
With EfficientNet-B0 reaching ~99.5% accuracy, the model is strong enough for practical deployment in pharmacy automation, inventory systems, and healthcare support tools.

---
