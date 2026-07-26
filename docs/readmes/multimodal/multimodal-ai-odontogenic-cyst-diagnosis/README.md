<!-- source: https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis.git sha: 9b8ba15f49789628a58729f1e3f6f1d294c5c095 readme: main/README.md -->
# MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis

My Bachelor Thesis Project (Computer Engineering): A multimodal AI framework for the diagnosis of Odontogenic Cysts. This project fuses data from Panoramic Radiography (Radiomics), Histopathology (Digital Pathology), and clinical/demographic information to achieve significantly improved diagnostic accuracy over unimodal models (up to 92%).

---

# 🦷 Multimodal-AI-Odontogenic-Cyst-Diagnosis

## 🎓 Bachelor Thesis Project (Computer Engineering)

This repository contains the full source code, models, and analytical tools developed for my **Bachelor of Science Thesis** at Shahid Beheshti University. The project focuses on pioneering a **Multimodal Artificial Intelligence (AI) approach** for the accurate diagnosis of **Odontogenic Cysts** (e.g., Odontogenic Keratocyst - OKC).

The core innovation lies in **fusing information from diverse medical data sources** to enhance diagnostic reliability and performance, moving beyond traditional single-source diagnostic methods.

---

## 🎯 Project Goal

To develop a robust AI system capable of diagnosing Odontogenic Cysts with high accuracy by integrating three complementary data modalities:

1.  **Radiomics:** Features extracted from Panoramic Radiography images.
2.  **Histopathology:** Features extracted from Whole Slide Images (WSIs) or microscopic sections.
3.  **Clinical/Demographic Data:** Tabular patient information (e.g., age, gender, lesion size).

The final model achieved a diagnostic accuracy of **92%** on the specialized dataset, significantly outperforming unimodal (single-data source) approaches (which performed as low as 51% in the base model).

---

## ⚙️ Model Architecture & Methodology

The project employs a multi-stage process involving specialized models for each data type, followed by a fusion mechanism:

### 1. Data Preprocessing & Feature Extraction

| Modality | Techniques Used | Key Files/Code |
| :--- | :--- | :--- |
| **Radiomics (Radiography)** | Feature extraction (e.g., texture, shape) using specialized libraries. | `BachelorProject(Demo+Radio+Histo).ipynb` |
| **Histopathology (WSI)** | Image processing, feature extraction from digitized pathology slides. | `BachelorProject(Demo+Radio+Histo).ipynb` |
| **Clinical/Demographic** | Data cleaning, encoding (e.g., **LabelEncoder**), and normalization (**StandardScaler**). | `BachelorProject(Demo+Radio+Histo).ipynb` |

### 2. Model Training & Fine-Tuning

The core of the system uses deep learning models, often leveraging pre-trained architectures (e.g., self-models) and **fine-tuning** them with the domain-specific medical dataset.

* **Initial Base Model:** Performance check on pre-trained models without fine-tuning, demonstrating the need for domain adaptation.
* **Fine-Tuning:** The models were adapted using the Odontogenic Cysts dataset, leading to the reported 92% accuracy.

### 3. Multimodal Fusion

The extracted feature vectors from the specialized models are concatenated or fused at a late-stage layer, allowing the final classifier (often a simple fully-connected network) to leverage the complementary diagnostic information from all three sources.

---

## 📂 Repository Structure

The key components of the project are organized as follows:

| File/Folder | Description |
| :--- | :--- |
| **`BachelorProject(Demo+Radio+Histo).ipynb`** | **Main Jupyter Notebook** containing all code for data loading, preprocessing, model definition, training, and evaluation (including unimodal and multimodal comparisons). |
| **`MahdisSepahvand-400243045-thesis.pdf`** | The complete Bachelor Thesis document (in Persian), detailing the methodology, literature review, and results. |
| **`/images`** | Contains visual results of the project, including performance metrics (Confusion Matrices), accuracy plots, and visual representations of the fine-tuning process. |
| **`/data`** | Placeholder for the anonymized dataset files (Radiography, Histopathology features, and clinical data) - **Note:** Raw patient data cannot be publicly shared. |

---

## 📈 Key Results

The multimodal approach demonstrated superior performance across all standard metrics:

| Metric | Multimodal Result | Base/Unimodal Comparison |
| :--- | :--- | :--- |
| **Accuracy** | **92%** | Improved from 51% (Base Model) |
| **Key Finding** | The fusion of Radiomic, Histopathologic, and Clinical data is essential for achieving clinically reliable diagnostic performance. |

### Dataset

#### Histography data
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/histography%20data.png)

#### Radiography data
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/radiography%20data.png)

#### Demographic data
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/demographic%20data.png)

### Project flow diagram
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/project_pipeline_en_spaced.png)

### Models input prompt
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/Prompt.png)

### Training loss curve
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/20250914_163535_loss_curve.png)

### Base model example result
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/base-results1.png)
### Fine-Tuning model example result
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/fine-tuning4.png)

### Comparing result graph
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/comparing-results1.png)
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/comparing-results2.png)
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/comparing-results3.png)

### Comparing result table
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/fine-tuning6.png)
![images](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis/blob/main/results/results%20of%20cyst%20region.png)

---

## 🚀 Getting Started

To replicate the project's findings, you will need:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis.git](https://github.com/MahdisSep/Multimodal-AI-Odontogenic-Cyst-Diagnosis.git)
    ```
2.  **Install required libraries:** (e.g., `TensorFlow`, `Keras`, `scikit-learn`, `pandas`, `numpy`, imaging libraries for medical data).
3.  **Data Setup:** Obtain the necessary dataset (not included due to privacy concerns) and place the feature files in the designated `/data` folder.
4.  **Run the analysis:** Execute the cells in the **`BachelorProject(Demo+Radio+Histo).ipynb`** notebook.