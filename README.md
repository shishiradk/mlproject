# 🧠 End-to-End Machine Learning Project

This is a complete **end-to-end machine learning pipeline** built with Python. It includes everything from data ingestion to model training and a simple web interface for predictions using Flask.

---

## 🚀 Project Goals

- Build a robust, modular ML pipeline from scratch  
- Practice real-world MLOps techniques like logging, exception handling, and config management  
- Provide a web interface for model inference using Flask  

---

## 🏗️ Project Architecture

```
mlproject/
│
├── artifacts/                # Stores output from each pipeline stage  
├── config/                   # Configuration files (e.g. config.yaml)  
├── components/               # Custom Python modules (data ingestion, transformation, training)  
├── constants/                # Constant values used across the pipeline  
├── exception/                # Custom exception class  
├── logger/                   # Custom logging module  
├── pipeline/                 # Training and prediction pipeline scripts  
├── utils/                    # Utility functions  
├── main.py                   # Entry point to trigger pipeline  
├── application.py            # Flask app for web-based predictions  
├── requirements.txt          # Project dependencies  
└── README.md                 # Project overview  
```

---

## ✅ Current Features

- [x] Clean and modular project structure  
- [x] Configuration management using YAML  
- [x] End-to-end logging and custom exception handling  
- [x] Reusable pipeline components  
- [x] Version-controlled data & artifacts  
- [x] Simple Flask web app for predictions  

---

## 📦 Installation

```bash
# 1. Clone the repo  
git clone https://github.com/shishiradk/mlproject.git  
cd mlproject  

# 2. Create a virtual environment (optional but recommended)  
python -m venv venv  
venv\Scripts\activate  # On Windows

# 3. Install dependencies  
pip install -r requirements.txt  
```

---

## 🧪 Run the Pipeline

```bash
python main.py
```

This triggers the end-to-end ML pipeline including:  
- Data ingestion  
- Data transformation  
- Model training  

---

## 🌐 Run the Web App

To start the Flask web interface for predictions:

```bash
python application.py
```

Then open your browser and go to `http://localhost:5000` to use the web interface.

---

## 📊 Tech Stack

- **Language**: Python  
- **Frameworks**: Flask  
- **MLOps Tools**: YAML, Logging, Exception Handling  

---

## 📈 Learning Outcomes

- Building production-grade ML pipelines  
- Writing modular and maintainable Python code  
- Creating a web interface for ML model inference  
- Project versioning and collaboration on GitHub  

---

## 🤝 Contribution

This is a personal learning project, but you're welcome to explore or fork it.  
Feel free to open issues or discussions if you have ideas or feedback!

---

## 📬 Contact

Built by [Shishir Adhikari](https://www.linkedin.com/in/shishiradhikari444/)  
Connect with me for collaboration or questions!

---

## ⭐️ Show Your Support

If you found this project useful, please consider giving it a ⭐️ on GitHub.  
It motivates and helps others discover this