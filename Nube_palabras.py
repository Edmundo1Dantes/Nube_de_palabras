import re
from collections import Counter
from docx import Document
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Cargar el contenido del documento Word
doc = Document("C:/Users/Santiago/Desktop/Tesis Maestria/Reuniones/Nube de palabras/Diálogos por Colombia_ Descentralización y desarrollo regional - 11_04_2025.docx")
text = '\n'.join([para.text for para in doc.paragraphs])  # Une todos los párrafos en un solo string. Extrae el texto de cada párrafo.

# Limpiar y separar palabras
text = re.sub(r'\s+', ' ', text).strip().lower() # Reemplaza múltiples espacios por uno solo. Elimina espacios al inicio/fin y pone todo en minúsculas.
words = re.findall(r'\b\w+\b', text) #Encuentra todas las palabras (letras y números).

# Crear y extender lista de stopwords (sin artículos y pronombres)
stop_words = set(STOPWORDS)
stop_words.update([
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
    'lo', 'le', 'les', 'se', 'nos', 'me', 'mi', 'mí', 'te', 'ti',
    'él', 'ella', 'ello', 'ellos', 'ellas', 'ese', 'esa', 'esos', 'esas',
    'esto', 'ese', 'aquí', 'ahí', 'allí', 'acá', 'allá', "de", "porque", "hay", "entonces", "para",
    "en", "si", "que", "con","pero","tienen", "ejemplo", "y", "por", "e", "o", 
    "como", "pues", "es", "todo", "más", "donde", "muy", "doctor", "eso", "del",
    "yo", "son", "qué", "ha", "del", "este", "al", "bueno", "tiene", "hacer", "también", "está", "su",
    "sobre", "estan", "ya", "otro", "están"
])
# Filtrar palabras
filtered_words = [word for word in words if word not in stop_words]
filtered_text = ' '.join(filtered_words)

# Generar nube de palabras
wordcloud = WordCloud(width=1600, height=800, background_color='white').generate(filtered_text)

# Mostrar nube
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()