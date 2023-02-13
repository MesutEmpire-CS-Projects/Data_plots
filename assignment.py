import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import streamlit as st

data = pd.read_csv('gapminder_with_codes.csv')

data_2007 = data[data['year'] == 2007]

st.set_page_config(page_title="Data 2007", page_icon=":sparkles:")
with st.container():
    st.write(
        """
        ##### Name SAMUEL WAINAINA ODHIAMBO\n
        ##### Reg No: SCT211-0039/2021\n
        ##### Course: B.Sc COMPUTER SCIENCE\n
        ##### Unit Name: SCIENTIFIC COMPUTING\n
        ##### Unit Code: ICS2207\n
        """
    )
with st.container():
    st.header("Data Visualization for Life Expectancy , Population and GDP Per Capital for the Year 2007")
    st.subheader('Data set used : ')
    st.write(data_2007)

fig, ax = plt.subplots()
st.markdown("---")
st.subheader('Violin Plots :')
# life expectancy
with st.container():
    st.write('### 1. Life Expectancy')
    st.write('##### 1.1 Life Expectancy in the Year 2007')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='lifeExp', scale="count")
    plt.title("Life Expectancy", {'fontsize': 20})
    plt.xlabel('lifeExp', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=14)
    st.pyplot(plt)

with st.container():
    st.write('##### 1.2 Life Expectancy in the Year 2007 across the Continents')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='lifeExp', y="continent", scale="count")
    plt.title("Life Expectancy", {'fontsize': 20})
    plt.xlabel('lifeExp', {'fontsize': 15})
    plt.ylabel('Continent', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=15)
    st.pyplot(plt)
st.markdown("---")
# population
with st.container():
    st.write('### 2. Population')
    st.write('##### 2.1 Population in the Year 2007')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='pop', scale="count")
    plt.title("Population", {'fontsize': 20})
    plt.xlabel('pop', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=14)
    st.pyplot(plt)

with st.container():
    st.write('##### 1.2 Population in the Year 2007 across the Continents')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='pop', y="continent", scale="count")
    plt.title("Population", {'fontsize': 20})
    plt.xlabel('population', {'fontsize': 15})
    plt.ylabel('Continent', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=15)
    st.pyplot(plt)

st.markdown("---")

# GDP Per Capital
with st.container():
    st.write('### 3. GDP Per Capital')
    st.write('##### 3.1 GDP Per Capital in the Year 2007')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='gdpPercap', scale="count")
    plt.title("GDP Per Capital", {'fontsize': 20})
    plt.xlabel('gdpPercap', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=14)
    st.pyplot(plt)

with st.container():
    st.write('##### 3.2 GDP Per Capital in the Year 2007 across the Continents')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='gdpPercap', y="continent", scale="count")
    plt.title("GDP Per Capital", {'fontsize': 20})
    plt.xlabel('gdpPercap', {'fontsize': 15})
    plt.ylabel('Continent', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=15)
    st.pyplot(plt)
