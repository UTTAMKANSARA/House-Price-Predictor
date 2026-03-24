# 🏠 Bangalore House Price Predictor

A machine learning web application that predicts residential property prices across Bangalore using a Ridge Regression model. Built with Python, Flask, and a custom dark-themed frontend.

---

## 🔗 Live Demo

👉 [bangalore-house-predictor.onrender.com](https://bangalore-house-predictor.onrender.com)
---

## 📸 Preview
<img width="960" height="600" alt="image" src="https://github.com/user-attachments/assets/62d35e3f-141f-4a5a-95c4-0ce66b985963" />

---

## ✨ Features

- Predicts house prices for 200+ locations across Bangalore
- Instant price display in both numeric and word format (e.g. ₹ 85 Lakh)
- Full input validation — catches empty fields, invalid numbers, and logical errors
- Clean, modern dark UI with responsive design
- Flask REST backend with Ridge Regression model

---

## 🧠 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, Bootstrap 4, Vanilla JS |
| Backend | Python, Flask |
| ML Model | Scikit-learn (Ridge Regression) |
| Data | Bangalore House Price Dataset |
| Deployment | Render |

---

## 📁 Project Structure

```
bangalore-house-predictor/
│
├── app.py                    # Flask backend + prediction logic
├── cleaned_data.csv          # Preprocessed dataset
├── RidgeModeluttam.pkl       # Trained Ridge Regression model
├── requirements.txt          # Python dependencies
├── Procfile                  # For deployment
├── render.yaml               # Render deployment config
│
└── templates/
    └── index.html            # Frontend UI
```

---

## 🚀 How to Run This Project Locally

Follow these steps exactly to get the project running on your machine.

### Step 1 — Prerequisites

Make sure you have these installed:
- **Python 3.8 or above** → [Download here](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** → [Download here](https://git-scm.com/)
To check if they are installed, open your terminal and run:
```bash
python --version
pip --version
git --version
```

### Step 2 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/bangalore-house-predictor.git
```
Then navigate into the project folder:
```bash
cd bangalore-house-predictor
```

### Step 3 — Create a Virtual Environment (Recommended)

A virtual environment keeps dependencies isolated from your system Python.
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```
You should see `(venv)` appear in your terminal — that means it's active.
---

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```
This will install Flask, scikit-learn, pandas, numpy, and gunicorn.

### Step 5 — Run the App

```bash
python app.py
```
You should see output like:
```
* Running on http://127.0.0.1:5001
* Debug mode: on
```

### Step 6 — Open in Browser

Open your browser and go to:
http://127.0.0.1:5001
The app is now running locally! 🎉

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
---

## 👨‍💻 Author
Made with ❤️ for Bangalore real estate enthusiasts.
If this project helped you, give it a ⭐ on GitHub!
