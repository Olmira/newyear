import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title('Ceci est ma page du projet')

st.write("la voilà")

df= pd.read_csv('data.csv', sep=',')
#df
pt = pd.read_csv('pivot.csv', sep=',', index_col = 0)
#pt

def town_info(town_name, country_name):
    try:
        timezone = df[((df['Name']== town_name)|(df['ASCII Name']== town_name))&(df['Country name EN']== country_name)]['Timezone'].values[0]
        population = pt[pt['Timezone']==timezone]['Population']
        return population.values[0]
    except:
        return "Combien"

town_name = st.text_input("Rntrer le nom de votre ville:")
country_name = st.text_input("Rntrer le nom de votre pays (en anglais):")
#print(town_info("Nice", "France"))
st.write(town_info(town_name, country_name),"de personnes vont fêter avec vous")
