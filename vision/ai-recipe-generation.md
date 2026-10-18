# AI-RECIPE-GENERATION
Recipe Generation from Food Image
– Developed a CNN-based image classification model achieving 94% accuracy across 100+ ingredients.
– Integrated LLM-based automation for recipe generation, reducing content creation time by 85%.
– Optimized inference using TensorFlow Lite for real-time processing under 2.5 seconds.
– Improved prediction precision by 35% using OpenCV-based preprocessing techniques

# Tech Stack
Deep Learning: TensorFlow, Keras
Computer Vision: OpenCV
Model Optimization: TensorFlow Lite
Natural Language Generation: LLM-based automation
Programming Language: Python

# Key Features
Food image classification with 94% accuracy
Supports 100+ ingredient categories
Automated recipe generation using LLMs
Real-time inference (< 2.5 seconds)
Optimized preprocessing for higher precision

## 🔄 Project Flow Structure: Recipe Generation from Food Image

### 📸 1. Image Input

User uploads or captures a **food image** using a camera or device.
➡️ This image becomes the input to the system.

---
### 🧹 2. Image Preprocessing (OpenCV)
The input image is cleaned and enhanced to improve prediction accuracy:

  * 🔍 Resize image
  * 🎚️ Normalize pixel values
  * 🧽 Noise removal
  * ✂️ Crop & enhance features
👉 Improves prediction precision by **35%**
---
### 🧠 3. Ingredient Detection (CNN Model)
  * 🧩 Preprocessed image is fed into a **CNN-based classification model**
  * 📊 Model predicts **100+ food ingredients**
  * 🎯 Achieves **94% accuracy**
---
### ⚡ 4. Model Optimization (TensorFlow Lite)
  * 🔄 Trained CNN model is converted to **TensorFlow Lite**
  * 📱 Enables fast inference on low-resource devices
  * ⏱️ Total prediction time **< 2.5 seconds**
---
### 📝 5. Ingredient Mapping
  * 🧾 Detected ingredients are structured into a readable format
  * 🔗 These ingredients act as input prompts for recipe generation
---
### 🤖 6. Recipe Generation (LLM Automation)
  * 🧠 Large Language Model generates:
  * 🥕 Ingredient list
  * 🍳 Step-by-step cooking instructions
  * ⏳ Reduces manual recipe creation time by **85%**
---
### 📤 7. Output Display
  * 📋 Generated recipe is displayed to the user
  * 🌐 Can be integrated into:
  * 📱 Mobile apps
  * 💻 Web applications
  * 🏠 Smart kitchen systems
---
## 🔁 End-to-End Flow Summary

📸 Image → 🧹 Preprocessing → 🧠 CNN Prediction → ⚡ TFLite Optimization → 📝 Ingredient Mapping → 🤖 Recipe Generation → 📤 Output

---

