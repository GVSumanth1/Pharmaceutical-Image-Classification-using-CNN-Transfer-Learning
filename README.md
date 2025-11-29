# Pharmaceutical Image Classification using CNN & Transfer Learning

A deep learning project for classifying pharmaceutical drugs using Convolutional Neural Networks (CNN) and Transfer Learning techniques with PyTorch.

## 🎯 Project Overview

This project implements and compares multiple deep learning architectures for classifying 10 different pharmaceutical drugs from images:
- **Alaxan** - Analgesic
- **Bactidol** - Antiseptic
- **Bioflu** - Cold medicine
- **Biogesic** - Pain reliever
- **DayZinc** - Vitamin supplement
- **Decolgen** - Decongestant
- **Fish Oil** - Omega-3 supplement
- **Kremil S** - Antacid
- **Medicol** - Anti-inflammatory
- **Neozep** - Cold remedy

## 🏗️ Architecture

### Models Implemented
1. **Custom CNN** - Custom-built 4-layer convolutional neural network
2. **EfficientNetB0** - Transfer learning with pre-trained weights
3. **ResNet50** - Transfer learning with pre-trained weights

### Key Features
- Data augmentation with random horizontal flips
- Batch normalization for stable training
- Early stopping to prevent overfitting
- Hyperparameter tuning for optimization
- Comprehensive evaluation metrics (Precision, Recall, F1-Score)

## 📁 Project Structure

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

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- CUDA-compatible GPU (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/GVSumanth1/Pharmaceutical-Image-Classification-using-CNN-Transfer-Learning.git
cd Pharmaceutical-Image-Classification-using-CNN-Transfer-Learning
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Download the dataset and place it in the `pharmaceutical_dataset/` folder.

### Usage

#### Training Models (Jupyter Notebook)

1. Open `pharmafinal.ipynb` in Jupyter Notebook or VS Code
2. Update the `data_path` variable to point to your dataset location
3. Run all cells sequentially to:
   - Load and visualize the dataset
   - Compute normalization statistics
   - Train multiple models (CustomCNN, EfficientNetB0, ResNet50)
   - Compare model performance
   - Generate evaluation metrics and visualizations

#### GUI Application

1. Update file paths in `pharma_ui.py`:
   - `DATASET_DIR` - Path to your dataset
   - `CSV_FILE` - Path for saving drug information

2. Run the application:
```bash
python pharma_ui.py
```

3. Features:
   - Search for drugs by name
   - View random drug images
   - Add drug information (dosage, ingredients, side effects)
   - Save data to CSV
   - View and manage saved records

## 📊 Results

The models are evaluated using:
- **Accuracy** - Overall classification accuracy
- **Precision** - Positive predictive value
- **Recall** - Sensitivity/True positive rate
- **F1-Score** - Harmonic mean of precision and recall
- **Confusion Matrix** - Per-class performance visualization

## 🛠️ Technologies Used

- **PyTorch** - Deep learning framework
- **torchvision** - Pre-trained models and transforms
- **PIL/Pillow** - Image processing
- **scikit-learn** - Evaluation metrics
- **matplotlib/seaborn** - Visualization
- **pandas** - Data management
- **tkinter** - GUI development

## 📈 Model Training Details

- **Image Size**: 224x224 pixels
- **Batch Size**: 32
- **Train/Val Split**: 80/20
- **Optimizer**: Adam
- **Learning Rate**: 1e-3 (with tuning)
- **Early Stopping**: Patience of 3 epochs
- **Epochs**: Up to 15 (with early stopping)

## 🎨 GUI Features

- Modern, user-friendly interface with hover effects
- Drug search functionality
- Random drug viewer
- Form-based data entry with tooltips
- CSV database for drug information
- Tabbed interface for search and saved data views

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is part of an academic assignment for Advanced Programming coursework.

## 👥 Authors

- GV Sumanth - [GitHub Profile](https://github.com/GVSumanth1)

## 🙏 Acknowledgments

- Dataset: Pharmaceutical Drug Vision Dataset
- Pre-trained models: ImageNet weights from torchvision
- Course: Masters in Advanced Programming

---

**Note**: The dataset is not included in this repository due to size constraints. Please contact the repository owner for dataset access.
