# 🎭 Sarcasm Detection using Support Vector Machine (SVM)

A Machine Learning project that detects whether a news headline is **Sarcastic** or **Not Sarcastic** using the **Support Vector Machine (SVM)** algorithm.

The project also includes a modern web application built with **React.js** for the frontend and **FastAPI** for the backend, allowing users to enter headlines and receive real-time sarcasm predictions.

---

# 📌 Project Overview

Sarcasm detection is a Natural Language Processing (NLP) classification problem. This project uses the **Sarcasm Headlines Dataset** to train an SVM classifier capable of predicting whether a headline is sarcastic.

The application provides an easy-to-use web interface where users can input any headline and instantly receive a prediction.

---

# 🚀 Features

- Detects sarcastic and non-sarcastic headlines
- Machine Learning model trained using Support Vector Machine (SVM)
- Text preprocessing using TF-IDF Vectorization
- FastAPI backend for serving predictions
- React.js frontend with a responsive user interface
- REST API integration
- Pickle (.pkl) model for deployment
- Easy to run locally

---

# 🛠 Technologies Used

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Support Vector Machine (SVM)
- TF-IDF Vectorizer
- Pickle

## Frontend

- React.js
- HTML5
- CSS3
- JavaScript
- Axios

## Backend

- FastAPI
- Uvicorn

---

# 📂 Project Structure

```
Sarcasm-Detection/
│
├── Backend/
│   ├── app.py
│   ├── sarcasm_svm_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── requirements.txt
│
├── Frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── Dataset/
│   └── sarcasm.json
│
├── README.md
└── LICENSE
```

---

# 📊 Dataset

Dataset contains news headlines with two classes:

- **0 → Not Sarcastic**
- **1 → Sarcastic**

Example:

| Headline | Label |
|----------|-------|
| This CEO Will Send Your Kids To School | 0 |
| Giant Altoid Heading Toward Earth | 1 |

---

# ⚙ Machine Learning Pipeline

1. Load Dataset
2. Data Cleaning
3. Feature Extraction using TF-IDF
4. Train-Test Split
5. Train Support Vector Machine (SVM)
6. Evaluate Model
7. Save Model using Pickle
8. Deploy using FastAPI
9. Connect React Frontend

---

# 🌐 Web Application

## Frontend

- Users enter a news headline.
- Request is sent to FastAPI.
- Prediction is displayed instantly.

## Backend

FastAPI loads:

- sarcasm_svm_model.pkl
- tfidf_vectorizer.pkl

The backend converts the input text into TF-IDF features and predicts whether the headline is sarcastic.

---

# ▶ How to Run

## Clone Repository

```bash
git clone https://github.com/your-username/Sarcasm-Detection.git
```

---

## Install Backend

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app:app --reload
```

---

## Install Frontend

```bash
npm install
npm run dev
```

---

# 📈 Model

Algorithm:

- Support Vector Machine (SVM)

Feature Extraction:

- TF-IDF Vectorizer

Output:

- Sarcastic
- Not Sarcastic

---

# 📷 Application Workflow

```
User Input
      │
      ▼
React Frontend
      │
      ▼
FastAPI Backend
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
SVM Model (.pkl)
      │
      ▼
Prediction
```

---

# 📌 Future Improvements

- Deep Learning (LSTM)
- BERT Transformer Model
- Hugging Face Deployment
- Docker Support
- Cloud Deployment
- Multi-language Sarcasm Detection

---

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

--------------------


# 👨‍💻 Author

**SofiaKamal**

Machine Learning | Python | React | FastAPI

---

# ⭐ Support

If you found this project helpful, don't forget to ⭐ star this repository.


This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
