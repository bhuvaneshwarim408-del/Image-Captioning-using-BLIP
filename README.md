# codsoft_task3
# Image Captioning using BLIP

## 📌 Project Overview

This project is an **Image Captioning System** developed using Python and a pretrained **BLIP (Bootstrapping Language-Image Pre-training)** model from Hugging Face.

The system takes an image as input and uses Artificial Intelligence to generate a natural-language caption describing the contents of the image.

This project was developed as part of my **CodSoft Artificial Intelligence Internship – Task 3**.

## 🎯 Objective

The objective of this project is to build an AI-based image captioning system that can understand the contents of an image and automatically generate a meaningful textual description.

## ✨ Features

* Generates captions automatically from images
* Uses a pretrained BLIP image captioning model
* Supports JPG and other common image formats supported by PIL
* Uses Hugging Face Transformers
* Converts images into the required format automatically
* Generates natural-language descriptions
* Simple command-line interface
* Easy to run with a local image

## 🧠 How It Works

The project uses the pretrained **Salesforce BLIP image captioning model**.

The process works as follows:

1. The user provides an image.
2. The image is opened using the PIL library.
3. The BLIP processor preprocesses the image.
4. The pretrained BLIP model analyzes the image.
5. The model generates text describing the image.
6. The generated tokens are decoded into a readable caption.
7. The caption is displayed in the terminal.

### Workflow

```text
Input Image
     ↓
PIL Image Processing
     ↓
BLIP Processor
     ↓
Pretrained BLIP Model
     ↓
Caption Generation
     ↓
Generated Text Caption
```

## 🛠️ Technologies Used

* Python 3
* Hugging Face Transformers
* Salesforce BLIP
* PyTorch
* PIL (Pillow)

## 📦 Requirements

Install the required Python libraries before running the project:

```bash
pip install transformers torch pillow
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installed version using:

```bash
python --version
```

### Step 2: Install Required Libraries

Open Command Prompt or Terminal and run:

```bash
pip install transformers torch pillow
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/bhuvaneshwarim408-del/codsoft_task3.git
```

### Step 4: Open the Project Folder

```bash
cd codsoft_task3
```

### Step 5: Make Sure the Image is Available

The repository contains a sample image named:

```text
sample.jpg
```

The Python program uses this image as the default input.

### Step 6: Run the Program

```bash
python imagecaptioning.py
```

The pretrained BLIP model will be downloaded automatically the first time the program is executed.

## 🖼️ Input Image

The project includes a sample image:

**sample.jpg**

The program processes this image and generates a caption based on its visual content.

## 💬 Example Output

```text
Generating caption for: sample.jpg

Generated Caption: [AI-generated description of the image]
```

The exact caption may vary depending on the contents of the image and the model's prediction.

## 📷 Demo

The project takes an image as input and generates a natural-language caption using the pretrained BLIP model.

The included `sample.jpg` can be used to test the project.

## 📚 What I Learned

Through this project, I learned:

* Basics of Image Captioning
* How pretrained AI models can be used for computer vision tasks
* How to use Hugging Face Transformers
* How the BLIP model generates captions
* Image preprocessing using PIL
* How to work with pretrained models
* How to generate text from visual information
* How to organize and document an AI project on GitHub

## 👩‍💻 Author

**Bhuvaneshwari M**

Computer Science and Engineering Student

## 🏆 Internship

**CodSoft Artificial Intelligence Internship**

**Task 3 – Image Captioning**
