
# 🌱 GHG Emissions Modeling Project

This project predicts supply chain greenhouse gas (GHG) emissions using U.S. industry and commodity data from 2010–2016. It uses regression-based machine learning models to estimate emission factors based on data quality indicators, source types, and emission characteristics.

---

## 📁 Project Structure

```

GHG\_Emissions\_Modeling/
├── data/               # Raw + combined data
├── models/             # Saved machine learning models (.pkl)
├── notebooks/          # Week 1 and Week 2 notebooks
│   ├── 01\_ghg\_modeling.ipynb
│   └── 02\_ghg\_week2.ipynb
├── src/                # Python scripts for preprocessing & modeling
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── .gitignore

```

---

## 🚀 Model Results

Both **Random Forest** and **Linear Regression** were trained and evaluated using:

- **RMSE** (Root Mean Squared Error)
- **R² Score** (Coefficient of determination)

Example output:
```

📊 Random Forest
RMSE: 0.027
R² Score: 0.91

📊 Linear Regression
RMSE: 0.054
R² Score: 0.75

```

---

## 🔧 How to Run

1. Clone or download the repository  
```

git clone [https://github.com/YOUR\_USERNAME/ghg-emissions-modeling.git](https://github.com/YOUR_USERNAME/ghg-emissions-modeling.git)

```

2. Install the required packages  
```

pip install -r requirements.txt

```

3. Open the notebook for Week 2 analysis  
```

jupyter notebook notebooks/02\_ghg\_week2.ipynb

```

4. (Optional) Load the trained model  
```

from joblib import load
model = load("models/random\_forest\_model.pkl")

```

---

## 📈 Tools & Technologies

- Python 3.12
- Jupyter Notebook
- Pandas, NumPy
- Scikit-learn
- Seaborn, Matplotlib
- joblib

---

## 🔮 Future Work

- Add hyperparameter tuning (e.g., GridSearchCV)
- Try more advanced models (e.g., XGBoost, LightGBM)
- Deploy as a Streamlit or Flask app

---

## 🙌 Acknowledgements

- U.S. Supply Chain Emission Factors Dataset  
- Guided and organized as part of a learning-based GHG modeling project
