import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")
""" В этих строках мы импортируем библиотеки streamlit и pandas, назначая им, 
соответственно, псевдонимы st и pd. Мы, кроме того, импортируем пакет datasets из 
библиотеки scikit-learn (sklearn). Мы воспользуемся этим пакетом ниже, в команде 
iris = datasets.load_iris(), для загрузки интересующего нас набора данных. И наконец, 
тут мы импортируем функцию RandomForestClassifier() из пакета sklearn.ensemble."""

#В этой строке мы описываем заголовок боковой панели, используя функцию о том, что мы 
#хотим поместить заголовок в боковую панель.
st.sidebar.header('User Input Parameters')

""" Здесь мы объявляем функцию user_input_features(), которая берёт данные, введённые пользователем 
(то есть — четыре характеристики цветка, которые вводятся с использованием ползунков), и возвращает 
результат в виде датафрейма. Последний аргумент задаёт значение, выставляемое на ползунке по умолчанию,
 при загрузке страницы. Здесь это — 5.4"""

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

#Здесь датафрейм, сформированный функцией user_input_features(), которую мы только что обсудили, 
#записывается в переменную df.

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

#Загрузка набора данных Iris из пакета sklearn.datasets и запись его в переменную iris.
iris = datasets.load_iris()

#Создание переменной Х, содержащей сведения о 4 характеристиках цветка, которые имеются в
X = iris.data

#Создание переменной Y, которая содержит сведения о виде цветка. Эти сведения хранятся в iris.target.
Y = iris.target

#Здесь мы, пользуясь функцией RandomForestClassifier(), назначаем классификатор, основанный на 
#алгоритме «случайный лес», переменной clf.
clf = RandomForestClassifier()

#Суть происходящего заключается в том, что модель будет обучена определению вида цветка (Y) 
#на основе его характеристик (X).

clf.fit(X, Y)

#Получение сведений о виде цветка с помощью обученной модели.
prediction = clf.predict(df)

#Получение сведений о прогностической вероятности.
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)