import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import streamlit as str

data = pd.read_csv('gapminder_with_codes.csv')

data_2007 = data[data['year'] == 2007]

str.set_page_config(page_title="Data 2007", page_icon=":sparkles:")

with str.container():
    str.header("Data Visualization for Life Expectancy , Population and GDP Per Capital for the year 2007")
    str.subheader('Data set used : ')
    str.write(data_2007)

fig, ax = plt.subplots()
str.markdown("---")
str.subheader('Violin Plots :')
# life expectancy
with str.container():
    str.write('### 1. Life Expectancy')
    str.write('##### 1.1 Life Expectancy in the Year 2007')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='lifeExp', scale="count")
    plt.title("Life Expectancy", {'fontsize': 20})
    plt.xlabel('lifeExp', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=14)
    str.pyplot(plt)

with str.container():
    str.write('##### 1.2 Life Expectancy in the Year 2007 across the Continents')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='lifeExp', y="continent", scale="count")
    plt.title("Life Expectancy", {'fontsize': 20})
    plt.xlabel('lifeExp', {'fontsize': 15})
    plt.ylabel('Continent', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=15)
    str.pyplot(plt)
str.markdown("---")
# population
with str.container():
    str.write('### 2. Population')
    str.write('##### 2.1 Population in the Year 2007')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='pop', scale="count",cut=0)
    plt.title("Population", {'fontsize': 20})
    plt.xlabel('pop', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=14)
    str.pyplot(plt)

with str.container():
    str.write('##### 1.2 Population in the Year 2007 across the Continents')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='pop', y="continent", scale="count",cut=0)
    plt.title("Population", {'fontsize': 20})
    plt.xlabel('population', {'fontsize': 15})
    plt.ylabel('Continent', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=15)
    str.pyplot(plt)

str.markdown("---")

#GDP Per Capital
with str.container():
    str.write('### 3. GDP Per Capital')
    str.write('##### 3.1 GDP Per Capital in the Year 2007')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='gdpPercap', scale="count")
    plt.title("GDP Per Capital", {'fontsize': 20})
    plt.xlabel('gdpPercap', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=14)
    str.pyplot(plt)

with str.container():
    str.write('##### 3.2 GDP Per Capital in the Year 2007 across the Continents')
    plt.figure(figsize=(10, 8))
    sn.violinplot(data=data_2007, x='gdpPercap', y="continent", scale="count")
    plt.title("GDP Per Capital", {'fontsize': 20})
    plt.xlabel('gdpPercap', {'fontsize': 15})
    plt.ylabel('Continent', {'fontsize': 15})
    plt.tick_params(axis='both', which='major', labelsize=15)
    str.pyplot(plt)
