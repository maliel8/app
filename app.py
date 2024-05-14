import streamlit as st
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
#from sklearn.metrics import accuracy_score
#from sklearn.model_selection import train_test_split
st.title('''BIENVENUE SUR PREDIT RESULTAT''')
st.write('''
   une application qui permet au etudiant de savoir s'il vont valider leur EU ou non
''')
    
col1, col2 = st.columns(2)
with col1:
    st.title('Donnees')
    nom = st.text_input('entrez votre nom')
    heure_etude = st.number_input("entrez votre nombre d'heures etude par jour",1.0,9.93,5.1)
    note_exam_passer = st.number_input('entrez votre note de cc',None,None,12)
    #avant de passer les donnees au model
    note_exam_passer = (note_exam_passer * 50) / 10
    
    donnees_user = {'heure_etude' : heure_etude,'note_exam_passer' : note_exam_passer} 
    donnees_entre = pd.DataFrame(donnees_user,index = [0])

with col2:
    st.title('Resultat')
    st.write('donnee de Mr/ Mme',nom)
    st.write(donnees_entre)

    #chargement du model 
    studs = pd.read_csv('data_me.csv')
    
    x_train_ = studs.drop(['resultat'], axis = 1)
    y_train_ = studs['resultat']
    ref = RandomForestClassifier()

    ref.fit(x_train_,y_train_)

    prediction = ref.predict(donnees_entre)

    ## prediction 
    if(prediction == 1):
        st.title('''UE VALIDER''')
        st.write('''si vous continue dans cette lancer ''')
    else:
        st.title('''UE NON VALIDER''')
        st.write(''' si vous continuer dans cette lancer l'echec vous attend ''')
        
