# 🧠 Employee Salary Prediction

This is a machine learning web application built using **Streamlit** that predicts an employee's salary based on various personal, educational, and professional attributes. It leverages the **XGBoost Regressor** model trained on the **Stack Overflow Developer Survey** dataset.

---

## 🚀 Live Demo

👉 [Streamlit Cloud App](https://employeesalaryprediction.streamlit.app/)

---

## 📁 Project Structure

```
employee_salaryprediction/
│
├── main.py                  # Streamlit frontend for input and prediction
├── preprocess.py            # Handles user input preprocessing to match training data
├── test.ipynb               # Notebook used to clean & preprocess raw survey data
├── model_files/
│   ├── salary_model.pkl             # Trained ML model
│   ├── country_encoder.pkl          # LabelEncoder for country field
│   └── features_list.pkl            # All features used for training
├── requirements.txt         # Required Python packages
└── README.md                # Project documentation (this file)
```

> **Explanation:**
> - `test.ipynb`: Used for preparing and transforming the raw dataset.
> - `preprocess.py`: Used by `main.py` to process user form data and send it to the model.
> - If you want the original dataset, download it from:  
>   👉 [https://survey.stackoverflow.co](https://survey.stackoverflow.co)

---

## 📦 Features

- Accepts user input on:
  - Job Role
  - Education Level
  - Age Group
  - Years of Experience
  - Employment Type
  - Work Style (Remote/In-Person)
  - Technologies Used: Languages, Databases, Cloud, Web Frameworks, Tools, etc.
- Encodes categorical and multivalued fields using label encoding and multi-label binarization.
- Outputs predicted salary with clean formatting using Streamlit components.

---

## 📊 Model Info

- **Model Used:** XGBoost Regressor
- **Performance:**
  RMSE (Root Mean Squared Error): 35,311.64
  MAE (Mean Absolute Error): 24,512.40
  R² Score: 0.5924
- **Total Features:** 269 (after one-hot + multi-hot encoding)

---

## 📚 Dataset

- Source: [Stack Overflow Developer Survey](https://survey.stackoverflow.co/)
- Download and extract the dataset to preprocess it using `test.ipynb`.
- Cleaned data is used to train the model and extract feature columns.

---

## 🔧 Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Harshavardhan-Raju/Employee_salaryprediction.git
   cd Employee_salaryprediction
   ```

2. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**
   ```bash
   streamlit run main.py
   ```

---

## 📌 Deployment Tips (Streamlit Cloud)

- Include all `pkl` files (model, encoder, features) in the repo.
- Ensure **relative paths** are used while loading `.pkl` files (e.g., `model_files/salary_model.pkl`).
- Commit everything to GitHub before deploying to [Streamlit Cloud](https://streamlit.io/cloud).
- In Streamlit Cloud dashboard:
  - Set the file to run as `main.py`
  - Add `requirements.txt` if not detected automatically

---

## 🎨 Final Output Display Options

- Use `st.success()` for green box output
- Alternatively, for better styling:
  ```python
  st.markdown(f"### 💰 Predicted Salary: `${output[0]:,.2f}`")
  ```
  This shows dollar symbol and formats with commas nicely.

---

## 📞 Contact

Made with ❤️ by **Harshavardhan Raju**  
📧 Email: [luckymuppala314@gmail.com]  
🔗 GitHub(https://github.com/Harshavardhan-Raju)

If you find this project helpful, please ⭐ the repo!
