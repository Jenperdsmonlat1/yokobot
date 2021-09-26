import nltk
import string
import random
import numpy as np
import tensorflow as tf
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

nltk.download("punkt")
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()

words = []
classes = []
doc_x = []
doc_y = []

data = {"intents": [
    {"tag": "greeting",
     "patterns": ["Hello", "La forme?", "yo", "Salut", "ça roule?", "wesh", "bonjoir", "bonjour", "hola", "salem"],
     "responses": ["Salut à toi!", "Hello", "Comment vas tu?", "Salutations!", "Enchanté", "wesh ça va la mif et tout"],
     },
    {"tag": "age",
     "patterns": ["Quel âge as-tu?", "C'est quand ton anniversaire?", "Quand es-tu né?", "t'es née quand ?",
                  "t'es de quelle année ?"],
     "responses": ["J'ai 25 ans", "Je suis né en 1996", "Ma date d'anniversaire est le 3 juillet et je suis né en 1996",
                   "03/07/1996"]
     },
    {"tag": "date",
     "patterns": ["Que fais-tu ce week-end?",
                  "Tu veux qu'on fasse un truc ensemble?", "Quels sont tes plans pour cette semaine", "tu fais quoi ?"],
     "responses": ["Je suis libre toute la semaine", "Je n'ai rien de prévu", "Je ne suis pas occupé",
                   "Je ne fais rien"]
     },
    {"tag": "name",
     "patterns": ["Quel est ton prénom?", "Comment tu t'appelles?", "Qui es-tu?"],
     "responses": ["Mon prénom est Yoko", "Je suis Yoko", "Yoko"]
     },
    {"tag": "jokes",
     "patterns": ["Racontes-moi une blague", "raconte moi une blague", "raconte une blague", "dis une blague",
                  "dis-moi une balgue", "dis moi une blague"],
     "responses": [
         "Quelle mamie fait peur aux voleurs ? Mamie Traillette.",
         "J'ai une blague sur les magasins. Mais elle a pas supermarché",
         "Pourquoi est-ce c'est difficile de conduire dans le Nord ? Parce que les voitures arrêtent PAS DE CALER.",
         "Comment est-ce que la chouette sait que son mari fait la gueule ? Parce qu’HIBOUDE",
         "Pourquoi est-ce qu'on dit que les bretons sont tous frères et sœurs ? Parce qu’ils n’ont Quimper.",
         "Pourquoi est-ce qu'on met tous les crocos en prison ? Parce que les crocos dealent.",
         "Comment fait-on pour allumer un barbecue breton ? On utilise des breizh.",
         "Pourquoi dit-on que les poissons travaillent illégalement ? Parce qu’ils n’ont pas de FISH de paie.",
         "Quel est le bar préféré des espagnols ? Le Bar-celone",
         "Pourquoi est-ce que les mexicains mangent-ils aux toilettes ? Parce qu’ils aiment manger épicé",
         "Que faisaient les dinosaures quand ils n'arrivaient pas à se décider ? Des tirageosaures",
         "Qu'est-ce qu'un tennisman adore faire ? Rendre des services",
         "Pourquoi est-ce que les vêtements sont toujours fatigués quand ils sortent de la machine ? Parce qu’ils "
         "sont léssivés",
         "Pourquoi est-ce que les livres ont-ils toujours chaud ? Parce qu’ils ont une couverture",
         "Où est-ce que les super héros vont-ils faire leurs courses ? Au supermarché",
         "Que se passe-t-il quand 2 poissons s'énervent ? Le thon monte",
         " Quel fruit est assez fort pour couper des arbres ? Le ci-tron",
         "Quel est le jambon que tout le monde déteste ? Le sale ami",
         "Que fait un cendrier devant un ascenseur ? Il veut des cendres",
         " Que dit une imprimante dans l'eau ? J’ai papier",
         "Que dit une noisette quand elle tombe à l'eau ? je me noix",
         "Quel est l'aliment le plus hilarant ? Le riz",
         " Pourquoi est-ce que les moutons aiment le chewing-gum ? Parce que c’est bon pour la laine.",
         "Quel est le sport préféré des insectes ? Le criquet",
         "Quel est le café préféré des espagnols ? Le café Olé",
         "Que fait Platon quand ça le démange ? Il Socrate",
         "Pourquoi est ce que Hulk a un beau jardin ? Parce qu’il a la main verte"
     ]
     },
    {"tag": "insulte",
     "patterns": ["tg", "TG", "Tg", "ta gueule", "ferme ta gueule"],
     "responses": ["Ne viens pas me parler si c'est pour me dire ça."]
     },
    {"tag": "goodbye",
     "patterns": ["au revoir", "bye", "see ya", "adios", "cya"],
     "responses": ["C'était sympa de te parler", "à plus tard", "On se reparle très vite!"]
     }
]}

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)
        doc_x.append(pattern)
        doc_y.append(intent["tag"])

    if intent["tag"] not in classes:
        classes.append(intent["tag"])

words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in string.punctuation]

words = sorted(set(words))
classes = sorted(set(classes))

print(words)
print(classes)
print(doc_x)
print(doc_y)

training = []
out_empty = [0] * len(classes)

for idx, doc in enumerate(doc_x):
    bow = []
    text = lemmatizer.lemmatize(doc.lower())
    for word in words:
        bow.append(1) if word in text else bow.append(0)

    output_row = list(out_empty)
    output_row[classes.index(doc_y[idx])] = 1

    training.append([bow, output_row])

random.shuffle(training)
training = np.array(training, dtype=object)

train_X = np.array(list(training[:, 0]))
train_Y = np.array(list(training[:, 1]))

input_shape = (len(train_X[0]),)
output_shape = len(train_Y[0])
epochs = 200

model = Sequential([
    Dense(64, input_shape=input_shape, activation='relu'),
    Dropout(0.5),
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(output_shape, activation='softmax')
])

optimizer_adam = tf.keras.optimizers.Adam(learning_rate=0.01, decay=1e-6)
model.compile(
    loss='categorical_crossentropy',
    optimizer=optimizer_adam,
    metrics=["accuracy"]
)

print(model.summary())

hist = model.fit(train_X, train_Y,
                 epochs=epochs,
                 batch_size=64,
                 verbose=True
                 )

model.save("Modèle_chatbot.h5", hist)
print("Modèle sauvegardé")

train_loss, train_acc = model.evaluate(train_X, train_Y)
print(train_acc)
