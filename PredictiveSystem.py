import numpy as np
import pickle
import streamlit as st


# Model Loaded
model = pickle.load(open('Breast_cancer_model.sav','rb'))


st.title("🩺Breast Cancer Prediction System")
st.write("Enter Patient Details ")

# Form
Clump_Thickness = st.number_input("Clump Thickness",min_value=0,max_value=10,value=8)
Uniformity_of_CellSize=st.number_input("Uniformity of Cell Size",min_value=0,max_value=10,value=10)
Uniformity_of_CellShape=st.number_input("Uniformity of Cell Shape",min_value=0,max_value=10,value=10)
Marginal_Adhesion=st.number_input("Marginal Adhesion",min_value=0,max_value=10,value=8)
Single_Epithelial_CellSize=st.number_input("Single Epithelial Cell Size",min_value=0,max_value=10,value=7)
Bare_Nuclei=st.number_input("Bare Nuclei",min_value=0,max_value=10,value=10)

Bland_Chromatin=st.number_input("Bland Chromatin",min_value=0,max_value=10,value=9)

Normal_Nuclei=st.number_input("Normal Nuclei",min_value=0,max_value=10,value=7)
Mitoses=st.number_input("Mitoses",min_value=0,max_value=10,value=1)

# collect form data into array
input_data=np.array([
    [
        Clump_Thickness,
        Uniformity_of_CellSize,
        Uniformity_of_CellShape,
        Marginal_Adhesion,
        Single_Epithelial_CellSize,
        Bare_Nuclei,
        Bland_Chromatin,
        Normal_Nuclei,
        Mitoses
    ]
    ])

# execute prediction

if st.button("Predict"):
    prediction=model.predict(input_data)

    if prediction[0]==0:
        st.success("✅ Patient comes under class-2(Benign), indicates **No Cancer**")
    else:
        st.error("⚠️ Patient comes under class-4(Malignant),indicates patient has **⚠️ Cancer**")

    