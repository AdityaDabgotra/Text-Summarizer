# 🧠 Text Summarizer

An end‑to‑end **Text Summarization** project built with a clean, modular ML workflow and served using **FastAPI**. This project follows an industry‑style pipeline structure, making it easy to understand, extend, and deploy.

---

## 📌 Project Overview

This project takes raw text as input and generates a concise summary using a trained NLP model. It is designed with:

* Clear separation of concerns
* Reusable components
* Config‑driven architecture
* API + frontend integration

Whether you're learning **MLOps**, **NLP pipelines**, or **FastAPI deployment**, this project is a solid reference.

---

## 🗂️ Workflow (Step‑by‑Step)

> ⚠️ **Follow this exact order when modifying or extending the project**

1. **Update `config.yaml`**
   Define paths, artifacts, and global configurations.

2. **Update `params.yaml`**
   Set model‑specific parameters and hyperparameters.

3. **Update Entity**
   Define data classes for structured configuration handling.

4. **Update Configuration Manager** (`src/config`)
   Reads configs and creates structured configuration objects.

5. **Update Components**
   Core logic for data ingestion, transformation, training, and evaluation.

6. **Update Pipeline**
   Orchestrates component execution step‑by‑step.

7. **Update `main.py`**
   Runs the complete training pipeline.

8. **Update `app.py`**
   Exposes the trained model via a FastAPI endpoint.

---

## 🚀 How to Run the Project

### 🔹 STEP 01: Clone the Repository

```bash
git clone https://github.com/AdityaDabgotra/Text-Summarizer
cd Text-Summarizer
```

---

### 🔹 STEP 02: Create a Conda Environment

```bash
conda create -n summary python=3.10 -y
```

```bash
conda activate summary
```

---

### 🔹 STEP 03: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 STEP 04: Train the Model

This will execute the full ML pipeline (data ingestion → training → evaluation).

```bash
python main.py
```

✔️ Model artifacts will be saved automatically based on `config.yaml`.

---

### 🔹 STEP 05: Run the FastAPI Server

```bash
python app.py
```

* API will start on:
  👉 `http://localhost:8080`

---

### 🔹 STEP 06: Open the Frontend

* Open the provided **HTML file** in your browser
* Enter text and send a request to the API
* Get the summarized output instantly ✨

---

## 🧪 API Usage (Quick Reference)

**Endpoint:**

```
POST /predict
```

**Request Body (JSON):**

```json
{
  "text": "Your long input text here"
}
```

**Response:**

```json
{
  "summary": "Generated summary text"
}
```

---

## 🛠️ Tech Stack

* **Python 3.10**
* **FastAPI** – API layer
* **Transformers / NLP Model**
* **PyYAML** – Configuration management
* **Conda** – Environment management

---

## 🌟 Key Highlights

* Config‑driven ML pipeline
* Clean folder structure
* Easy to extend or retrain
* Beginner‑friendly + production‑ready concepts

---

## 👤 Author

**Aditya Dabgotra**
GitHub: [https://github.com/AdityaDabgotra](https://github.com/AdityaDabgotra)

---

⭐ If you found this project helpful, consider giving it a star!
