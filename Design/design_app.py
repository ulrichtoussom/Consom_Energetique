
import streamlit as st

    
def styleButton():
    
    st.markdown("""
<style>
/* Style pour tous les boutons dans la sidebar */
section[data-testid="stSidebar"] button {
    background-color: #28d7eb;
    color: white;
    font-size: 15px;
    border-radius: 8px;
    padding: 8px 18px;
    transition: 0.3s;
}
section[data-testid="stSidebar"] button:hover {
    background-color:  #16a085;
    transform: scale(1.05);
}

/* Style pour les boutons dans le contenu principal */
div.block-container button {
    background-color:#16a085;
    color: white;
    font-size: 16px;
    border-radius: 10px;
    padding: 10px 24px;
    transition: 0.3s;
}
div.block-container button:hover {
    background-color:#de6767;
    color: white;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)
   
    
def description():
    return """
    <p> 
        Bienvenue sur notre application interactive conçue pour vous aider à mieux comprendre et anticiper votre consommation électrique !\n
        Ce projet innovant utilise des modèles de Machine Learning pour prédire le taux de consommation électrique d'une habitation en se basant sur des facteurs environnementaux et démographiques clés.
    </p>
    <h3 style="font-weight: bold;">Comment sa fonctionne </h3>
    <p> 
         L'application prend en compte les données suivantes pour générer ses prédictions :
         <ul>
            <li><i style="font-weight: bold;">Température ambiante</i> : Les variations de température influencent directement le besoin en chauffage ou en climatisation.</li>
            <li><i style="font-weight: bold;">Humidité</i> : Le niveau d'humidité peut également impacter le confort thermique et, par conséquent, la consommation énergétique.</li>
            <li><i style="font-weight: bold;">Vitesse de vent</i> : Une vitesse de vent élevée peut augmenter la déperdition de chaleur ou le besoin en ventilation.</li>
            <li><i style="font-weight: bold;">Nombre d'occupants</i> : Le nombre d'occupants est un indicateur direct de l'activité domestique et de l'utilisation des appareils électriques.</li>
        </ul>
    </p>
    <h3 style="font-weight: bold;">Objectif du projet </h3>
    <p> 
    Notre objectif est de fournir un outil simple et intuitif qui permet aux utilisateurs de :
        <ul>
            <li>Estimer leur consommation future</li>
            <li>Identifier les facteurs principaux influençant leur consommation.</li>
            <li>Prendre des décisions éclairées pour optimiser leur utilisation de l'énergie et potentiellement réduire leurs factures.</li>
        </ul>
    </p>
    \n
    Développée avec Streamlit, cette application offre une interface conviviale et des visualisations claires pour \n une expérience utilisateur optimale. Explorez les différentes options et découvrez comment les variables environnementales et domestiques façonnent votre consommation d'électricité !
    
"""

def card_design(title, value):
    
    st.markdown(f"""
                <style>
                    .card {{
                        
                    min-height: 100px;
                    margin: 1em auto;
                    border-radius: 15px;
                    overflow-y: auto;
                    box-shadow: 0 6px 10px rgba(0, 0, 1, 0.1);
                    font-family: 'Arial', sans-serif;
                    background: #de6767;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    
                    transition: transform 0.2s ease-in-out;
                    }}
                    .card:hover {{
                    transform: scale(1.02);
                    }}
                    .prediction-card {{
                        border-radius: 5px;
                        text-align: center;
                        font-weight: bold;
                        color: red;
                        height: 80px;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        shadow: 0 6px 10px rgba(17, 153, 6, 0.1);
                        border: 1px solid green;
                    }}
                    .prediction-card:hover {{
                        transform: scale(1.02);
                        border: 3px solid green;
                    }}
                    .card-content {{
                    padding: 15px;
                    }}
                    .card-title {{
                    text-align: center; 
                    font-size: 1.1rem;
                    margin: 0 0 10px;
                    font-weight: bold;
                    }}
                    .card-description {{
                    font-size: 2rem;
                    font-weight: bold;
                    text-align: center;
                    color: #555;
                    }}
                </style>
                <div class="card">
                    <div class="card-content">
                        <p class="card-title">{title}</p>
                        <p class="card-description"> {value} </p>
                    </div>
                </div>
                
                """, unsafe_allow_html=True)
    