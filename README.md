# 💼 Employee Salary Prediction App

This is a machine learning-based web application that predicts an employee's salary using demographic and professional attributes. Built using **Streamlit** for the frontend and **XGBoost** for the prediction model, this app serves as a demonstration of end-to-end ML deployment.

---

## 🚀 Live App

👉 **[Launch the App](https://employeesalaryprediction.streamlit.app/)**  

---

## 📊 Features

- Input form to collect:
  - Age group
  - Education level
  - Job title
  - Work experience
  - Remote work type
  - Employment status
  - Tech stack (Languages, Databases, Tools, Platforms, etc.)
- Real-time salary prediction using trained model
- Input preprocessing using label encoding and multi-hot encoding
- Clean UI built with Streamlit

---

## 🧠 ML Model Details

- **Algorithm**: XGBoost Regressor
- **Preprocessing**:
  - Label Encoding (Age, Education, Country)
  - MultiLabelBinarizer for multi-select categorical fields
  - Dummy variable creation for job titles
  - All encoders and feature alignment preserved from training
- **Target**: Salary (USD)
- **Model Storage**:
  - `salary_model.pkl`
  - `country_encoder.pkl`
  - `features.pkl` (to ensure feature alignment at inference time)

---

## 🛠 Tech Stack

- Python 3.10+
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Pickle for model/encoder storage

---

## 📁 Directory Structure

```
project_employee/
│
├── main.py                  # Streamlit frontend
├── preprocess.py            # Preprocessing logic
├── requirements.txt         # Python dependencies
├── model_files/             # Saved models and encoders
│   ├── salary_model.pkl
│   ├── country_encoder.pkl
│   └── features.pkl
```

---

## 🔧 Installation Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Harshavardhan-Raju/Employee_salaryprediction.git
   cd Employee_salaryprediction
   ```

2. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run main.py
   ```

---

## 🌐 Deployment (Streamlit Cloud)

If deploying on **Streamlit Cloud**, make sure to:

- Upload all `.pkl` files inside a `model_files/` directory.
- Ensure correct **relative paths** are used when loading pickled models.
- Add `requirements.txt` to specify dependencies.

---

## 👨‍💻 Author

**Harshavardhan Raju**  
🎓 B.Tech Student | 💡 AI/ML Enthusiast  
🔗 [GitHub](https://github.com/Harshavardhan-Raju)

---
