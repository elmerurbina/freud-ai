import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder
from db import connect_to_database, fetch_data_from_information_table



max_feautures = 250


nltk.download("punkt")
nltk.download("stopwords")

#Conexion con la base de datos, que contiene el dataset
conn = connect_to_database()

if conn is None:
    exit(1)

#Acceder a la informacion almacenada en la tabla "information" en la base de datos

table_data = fetch_data_from_information_table(conn)

texts = [row[0] for row in table_data]
labels = [row[0] for row in table_data]


#Preprocesamiento del texto
def preprocess_text(text):
    words = word_tokenize(text)

    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stopwords.words("english")]

    return ' '.join(words)

preprocessed_texts = [preprocess_text(text) for text in texts]

text_array = np.array(preprocessed_texts)


#Vectorizacion del texto
tfidf_vectorizer = TfidfVectorizer(max_features=max_feautures)
X = tfidf_vectorizer.fit_transform(preprocessed_texts)


#Divide los datos en bloques de train (entrenamiento) y testing (prube)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

#Definicion del modelo con TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(max_feautures,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

label_encoder = LabelEncoder ()

#Encoder utilizado para la transformacion de datos
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.fit_transform(y_test)

#Entrenamiento del modelo
model.fit(X_train, y_train_encoded, epochs=10, batch_size=32, validation_data=(X_test, y_test_encoded))


#Vamos a probar el modelo
loss, accuracy =model.evaluate(X_test, y_test)
print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")

#El Bot se implementara en dos idiomas -English-Spanish- de momento estamos implementando el Ingles
#para probar el funcionamiento del modelo y la conexion a la base de datos,
#debido a que la informacion que contiene el dataset esta Ingles

new_text = ["I am stressed today"]
preprocessed_new_text = [preprocess_text(text) for text in new_text]
tfidf_vectors = tfidf_vectorizer.transform(preprocessed_new_text)
predictions = model.predict(tfidf_vectors)

#Cierra la conexion a la base de datos
conn.close()





