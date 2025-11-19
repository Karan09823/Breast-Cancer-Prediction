# Breast Cancer Prediction  - https://breast-cancer-prediction-r5c6ywv2fnirjijto6jnjj.streamlit.app/

# 🚀 How to Add and Run a Streamlit App

This guide walks you through creating a virtual environment, installing dependencies, running your Streamlit application locally, and finally deploying it on Streamlit Community Cloud.

---

## 🧪 1. Create a Virtual Environment

Creating a virtual environment ensures all required Python libraries are installed in an isolated workspace.

```bash
python -m venv virtualEnvironmentName
```

---

## ▶️ 2. Activate the Virtual Environment

Use the following command:

```bash
virtualEnvironmentName/Scripts/activate
```

Once activated, your terminal will show the virtual environment name at the beginning.

---

## 📦 3. Install Required Libraries

Install essential packages like Streamlit, NumPy, and others:

```bash
pip install streamlit numpy
# Install any other libraries your project needs
```

---

## 🏃‍♂️ 4. Run the Streamlit App

Run your app using:

```bash
streamlit run filename.py
```

Your Streamlit application will open automatically in your browser.

---

## 🛑 5. Stop the App

To stop the running Streamlit server:

```
Ctrl + C
```

---

## 🔚 6. Deactivate Virtual Environment

When you're done, exit the environment using:

```bash
deactivate
```

---

## 📄 7. Generate requirements.txt

Freeze the installed packages:

```bash
pip freeze
```

Then save them to a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

---

## ☁️ 8. Prepare Files for Deployment

Upload the following files to your GitHub repository:

* `YourModel.sav`
* `PredictiveSystem.py`
* `requirements.txt`
* Your Streamlit app file(s)

---

## 🚀 9. Deploy on Streamlit Community Cloud

1. Visit the Streamlit website.
2. Click **Create app**.
3. Provide your GitHub repository link.
4. Fill in the project details.
5. Click **Deploy**.

Your application will go live within seconds! 🎉

---

## ✅ You're All Set!

You have successfully:

* Set up and run a Streamlit environment
* Generated and uploaded all necessary files
* Deployed your application online

Enjoy sharing your interactive app with the world! 🌐
