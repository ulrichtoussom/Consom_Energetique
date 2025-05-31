import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_curve, auc
import pickle
import shap
import os
import sys
import base64

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(parent_dir, "Design"))

st.set_page_config(layout="wide", page_title="Visualisation Consommation Énergétique",page_icon="🔱")

from design_app import styleButton, description, card_design

styleButton()

@st.cache_data
def load_data(data):
    data = pd.read_csv(data)
    return data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="diabete_predictions.csv">Download CSV File</a>'
    return href

data = load_data("../Data/data_cleaned.csv")


st.sidebar.image("../images/images.jpeg",use_container_width=True)  
with st.sidebar :
    page= {
        '🏠 Home':'home',
        '📉 Statistique':'statistique',
        '📊 Visualisation':'visualisation',
        '💻📈 MachineLearnig':'machinelearnig'
    }
    	

    
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
        
    for page_name, page_key in page.items():
        if st.sidebar.button(page_name, use_container_width=True ,key=f'sidebar_btn_{page_key}'):
            st.session_state.page = page_key


if st.session_state.page == 'home': 
    
    st.write("<h1 style='text-align: center;'>📊 Analyse de la Consommation Énergétique</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
    
    left, middle, right = st.columns((2,6,2))
    with middle :
        st.image("../images/logo.jpg",use_container_width=True)
        st.subheader('Description')
        st.write(description(),unsafe_allow_html=True)  
        
elif st.session_state.page == 'visualisation':
    
    st.write('<h1 style="text-align: center;">📊 Visualisation de Consommation Électrique</h1>',unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center;"> </h2>',unsafe_allow_html=True)
    left , middle , right = st.columns((2,8,2))
    
    middle.subheader("Visualisation des Variables du dataset") 

    graphe_selected = middle.multiselect("selectionner les graphes a visualiser",[
        'Histogramme',
        'Boxplot',
        'Scatterplot',
        'Heatmap',
    ],'Histogramme')
    
    for graph in graphe_selected :
        #temperature (°C) humidite (%) vitesse_vent (km/h) nombre_personnes	consommation (kW)
        if graph == 'Histogramme':
            
            st.markdown('<h2 style="text-align: center;">Histogramme</h2>',unsafe_allow_html=True)
            st.markdown('<h2 style="text-align: center;"> </h2>',unsafe_allow_html=True)
            tab1 , tab2  = st.tabs([":clipboard: Detaillé", ":bar_chart: Groupés"])
            with tab1 :
                st.write('\n\n')
                col1,col2 = st.columns(2)
                with col1 :
                    fig = plt.figure(figsize=(5,5))
                    plt.hist(data["temperature (°C)"],bins=10,density=True)
                    plt.xlabel("temperature (°C)")
                    plt.ylabel("Frequences")
                    st.pyplot(fig)
                    
                    fig = plt.figure(figsize=(5,5))
                    plt.hist(data["consommation (kW)"],bins=10,density=True)
                    plt.xlabel("Consommation (kW)")
                    plt.ylabel("Frequences")
                    st.pyplot(fig)
                    
                    fig = plt.figure(figsize=(5,5))
                    plt.hist(data["nombre_personnes"],bins=10,density=True)
                    plt.xlabel("nombre_personnes")
                    plt.ylabel("Frequences")
                    st.pyplot(fig)
                    
                with col2:
                    st.write('\n\n')

                    fig = plt.figure(figsize=(5,5))
                    plt.hist(data["humidite (%)"],bins=10,density=True)
                    plt.xlabel("humidite (%)")
                    plt.ylabel("Frequences")
                    st.pyplot(fig)
                    
                    fig = plt.figure(figsize=(5,5))
                    plt.hist(data["vitesse_vent (km/h)"],bins=10,density=True)
                    plt.xlabel("vitesse_vent (km/h)")
                    plt.ylabel("Frequences")
                    st.pyplot(fig)
                    
            with tab2 :
                fig = plt.figure(figsize=(5,5))
                sns.histplot(data=data)
                st.pyplot(fig)
            
            
        elif graph == 'Boxplot':
            st.write('<h2 style="text-align: center;">Boxplot</h2>',unsafe_allow_html=True)
            st.markdown('<h2 style="text-align: center;"> </h2>',unsafe_allow_html=True)
            fig = plt.figure(figsize=(5,5))
            sns.boxplot(data=data)
            st.pyplot(fig)
            
            
        elif graph == 'Scatterplot':
            st.write('<h2 style="text-align: center;">Scatterplot</h2>',unsafe_allow_html=True)
            st.markdown('<h2 style="text-align: center;"> </h2>',unsafe_allow_html=True)
            
            col1,col2 = st.columns(2)
            choice1 = col1.selectbox("Chosir la valeur de la premiere variable",["temperature (°C)","humidite (%)","vitesse_vent (km/h)","consommation (kW)","nombre_personnes"])
            choice2 = col2.selectbox("Chosir la valeur de la Deuxieme variable",["humidite (%)","vitesse_vent (km/h)","consommation (kW)","temperature (°C)","nombre_personnes"])
            choice3 = col2.selectbox("Chosir la valeur de segmentation",["nombre_personnes","humidite (%)","vitesse_vent (km/h)","consommation (kW)","temperature (°C)"])
            
            if (choice1 == choice2):
                st.warning("Veuillez choisir deux variables differentes")
            else:
                if(choice3 == choice1 or choice3 == choice2):
                    choice3 = None
                    
                fig = plt.figure(figsize=(5,5))
                sns.scatterplot(data=data,x=choice1,y=choice2,hue=choice3)
                plt.xlabel(choice1)
                plt.ylabel(choice2)
                st.pyplot(fig)
            
        elif graph == 'Heatmap':
            st.write('<h2 style="text-align: center;">Heatmap</h2>',unsafe_allow_html=True)
            st.markdown('<h2 style="text-align: center;"> </h2>',unsafe_allow_html=True)
            
            fig = plt.figure(figsize=(5,5))
            sns.heatmap(data.corr(),annot=True)
            st.pyplot(fig)
            
        with st.expander(graph):
            st.write(f"Vous avez choisit le graph {graph}")
                      
elif st.session_state.page == 'statistique' : 

    st.write("<h1 style='text-align: center;'>📊 Analyse de la Consommation Énergétique</h1>", unsafe_allow_html=True)
    st.write('\n\n')
    st.subheader('Statistique descriptives du dataset')
    st.write('\n\n')
    st.write(data)
    
    if (st.checkbox("Afficher les statistiques descriptives")):
        st.write(data.describe())
        
    if (st.checkbox("Tableau  matrice de correlation")):
        st.write(data.corr())
    #visualiser la matrice de correlation
    
    if (st.checkbox("Matrice de correlation")):
        fig = plt.figure(figsize=(5,5))
        sns.heatmap(data.corr(),annot=True)
        st.pyplot(fig)

elif st.session_state.page == 'machinelearnig':
    st.write("<h1 style='text-align: center;'>📈 Machine Learnig</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
    st.subheader("Machine Learnig")
    
    tab1, tab2, tab3 = st.tabs([":clipboard: Data", ":bar_chart: visualisation", ":mask: :smile: Prediction"])
    model = pickle.load(open('../model_svm.pkl','rb'))
    newdata = data.drop(["consommation (kW)"],axis=1)
    predictions = model.predict(newdata)
    predict_data = pd.DataFrame(predictions,columns=["Prediction (kW)"])
    
    with tab1 :
        st.markdown("<h2 style='text-align: center;'> </h2>", unsafe_allow_html=True)
        st.write(data)
    with tab2 :
        
        visual1, visual2, visual3 = st.tabs(['📊 visualisation consommation (kW) reel', '📊 visualisation consommation (kW) predicte', 'Comparaison'])
       
        
        with visual1: 
            fig = plt.figure(figsize=(5,5))
            data["consommation (kW)"].plot(kind="kde",label="consommation (kW) Reel")
            plt.xlabel("consommation (kW)")
            plt.legend()
            plt.grid(True)
            st.pyplot(fig)
        with visual2 :
            fig=plt.figure(figsize=(5,5))
            predict_data["Prediction (kW)"].plot(kind="kde",label="consommation (kW) Predicte",color="red")
            plt.xlabel("Prediction (kW)")
            plt.legend()
            plt.grid(True)
            st.pyplot(fig)
        with visual3 :
            
            fig, ax = plt.subplots(figsize=(6, 5))
            # KDE de la consommation réelle
            data["consommation (kW)"].plot(kind="density", label="Consommation réelle (kW)", ax=ax)

            # KDE de la consommation prédite
            predict_data["Prediction (kW)"].plot(kind="density", label="Consommation prédite (kW)", ax=ax, color="red")

            # Mise en forme
            ax.set_xlabel("Consommation (kW)")
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)
    with tab3 :
        
        st.subheader('Effectuez une prediction')
        with st.form("my_form"):
            part1, part2 = st.columns((6,3))
            with part1 :
                col1,col2 = st.columns(2)
                with col1 :
                    temperature = st.number_input("temperature",min_value=0,max_value=100,value=2)
                    humidite = st.number_input("humidite",min_value=0,max_value=100,value=2)
                with col2 :
                    vitesse_vent = st.number_input("vitesse_vent",min_value=0,max_value=100)
                    nombre_personnes = st.number_input("nombre_personnes",min_value=0,max_value=100)
                
                submit_button = st.form_submit_button("Submit",use_container_width=True)
                
            if submit_button:
                st.session_state.temperature = temperature
                st.session_state.humidite = humidite
                st.session_state.vitesse_vent = vitesse_vent
                st.session_state.nombre_personnes = nombre_personnes

                with part2 :
                    col1, col2 = st.columns(2)
                    
                    with col1 :
                        card_design('Temperature (°C)',st.session_state.temperature)
                        card_design('Humidite (%)',st.session_state.humidite)
                        
                    with col2 :
                        card_design('Vitesse_vent (km/h)',st.session_state.vitesse_vent)
                        card_design('Nombre_personnes',st.session_state.nombre_personnes)
                        
                prediction = model.predict([[st.session_state.temperature, st.session_state.humidite, st.session_state.vitesse_vent, st.session_state.nombre_personnes]])
                part1.markdown(f"""
                                <p class="prediction-card" style ="font-size:24px" > Predict Consommation (kW) :{prediction[0]}</div>
                            """,unsafe_allow_html=True)
        
        st.subheader('Prediction')
        ndf =  pd.concat([data,predict_data,], axis=1)
        st.write(ndf)
        button =  st.button('Download csv')
        if button :
            st.markdown(filedownload(ndf),unsafe_allow_html=True)