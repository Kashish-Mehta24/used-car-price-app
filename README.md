# 🚗 Used Car Price Prediction App

This is a **machine learning-powered Streamlit web app** that predicts the selling price of a used car based on various features like present price, kilometers driven, fuel type, car age, etc.

> Built using `scikit-learn`, optimized with `Ridge Regression`, and deployed through `Streamlit`.

---

## 🔍 Overview

- 📊 Trained on a real-world used car dataset
- 🔧 Features manually engineered (e.g., `car_age`)
- 📈 Model optimized using `GridSearchCV`
- 🎯 Best model: **Ridge Regression** with tuned alpha
- 🌐 Streamlit app handles user input + model prediction li
## 🚀 Demo

Try the live app here 👉 [https://used-car-price-app-atq2uxgcx4dxmd82gorpaa.streamlit.app/]

---

## 🧠 Features Used for Prediction

- Present Price (in lakhs)
- Kilometers Driven
- Number of Previous Owners
- Car Age
- Fuel Type (Petrol, Diesel, CNG)
- Seller Type (Dealer or Individual)
- Transmission Type (Manual or Automatic)

The model uses **one-hot encoded features** and expects the same format during inference. The app handles all necessary encoding automatically.

---

## 🧱 Tech Stack

| Layer         | Tools Used                    |
|---------------|-------------------------------|
| ML Model      | `scikit-learn` (Ridge Regression) |
| Data Handling | `pandas`, `numpy`             |
| Web UI        | `Streamlit`                   |
| Deployment    | `Streamlit Cloud` (optional)  |
| Packaging     | `joblib` for model + columns  |

## Related Projects
- EDA and model training notebook: [Used Car Price EDA Repo](https://github.com/Kashish‑Mehta24/Used‑Car‑Price‑EDA)
