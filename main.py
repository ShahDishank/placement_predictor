import streamlit as st
import numpy as np
import pickle

st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'mailto:shahdishank24@gmail.com',
        'Report a bug': "mailto:shahdishank24@gmail.com",
        'About': "**Predict you Placement**"
    }
)

st.title("Placement Predictor")
st.write("")

def load_model(data):
	clf_model = pickle.load(open("clf_model.pkl", 'rb'))
	clf_pred = clf_model.predict(data)

	if clf_pred == 1:
		data = np.append(data, clf_pred[0]).reshape(1,-1)
		reg_model = pickle.load(open("reg_model.pkl", 'rb'))
		reg_pred = reg_model.predict(data)
		st.subheader(f":green[You will be placed with {reg_pred[0]} salary! 🎉]")
	else:
		st.subheader(":red[You will not get placed! 🥲]")

with st.container(border=True):
	gender = st.selectbox("Gender", ("Male", "Female"))
	if gender == "Male":
		gender = 1
	else:
		gender = 0
	st.write("")

	c1, c2 = st.columns(2)
	ssc_b = c1.selectbox("SSC Board", ("Central", "Others"))
	if ssc_b == "Central":
		ssc_b = 0
	else:
		ssc_b = 1
	c1.write("")

	ssc_p = c2.number_input("SSC Percentage")
	c2.write("")

	hsc_b = c1.selectbox("HSC Board", ("Central", "Others"))
	if hsc_b == "Central":
		hsc_b = 0
	else:
		hsc_b = 1
	c1.write("")

	hsc_p = c2.number_input("HSC Percentage")
	c2.write("")

	hsc_s = c1.selectbox("HSC Stream", ("Science", "Commerce", "Arts"))
	if hsc_s == "Science":
		hsc_s = 2
	elif hsc_s == "Commerce":
		hsc_s = 1
	else:
		hsc_s = 0
	c1.write("")

	degree_p = c2.number_input("Degree Percentage")
	c2.write("")

	degree_t = c1.selectbox("Degree Type", ("Science & Technology", "Commerce & Management", "Others"))
	if degree_t == "Science & Technology":
		degree_t = 2
	elif degree_t == "Commerce & Management":
		degree_t = 0
	else:
		degree_t = 1
	c1.write("")

	workex = c2.selectbox("Work Experience", ("No", "Yes"))
	if workex == "No":
		workex = 0
	else:
		workex = 1
	c2.write("")

	etest_p = st.number_input("Employability test percentage (out of 100)")
	st.write("")

	specialisation = 0

	mba_p = 0

	submitted = st.button("Submit")
	if submitted:
		data = np.array([[gender, ssc_p, ssc_b, hsc_p, hsc_b, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p]])
		load_model(data)