# Proyecto redes neuronales

## Integrantes
### Isabela Mendoza, Miguen Angel Ortiz, luis Angel Nerio, Cesar Montoya

# Problema a resolver

## Definición del problema
El proyecto consiste en realizar un análisis de sentimiento sobre reseñas de productos o películas.  
El objetivo es que el modelo lea una reseña en texto y clasifique si la experiencia del usuario fue **positiva** o **negativa**.

---

# Datos

Se pueden utilizar los siguientes datasets:

- **Amazon Fine Food Reviews**  
  https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews

- **IMDB Dataset of 50K Movie Reviews**  
  https://www.kaggle.com/datasets/rehanliaqat17/imbd-dataset

Ambos datasets son adecuados para tareas de clasificación de texto porque:

- contienen una gran cantidad de ejemplos,
- permiten trabajar con datos en lenguaje natural,
- tienen etiquetas útiles para clasificación supervisada.

---

# Preprocesamiento del texto

Antes de entrenar cualquier modelo, el texto debe transformarse en una representación numérica.

## Según el tipo de modelo, se puede trabajar de dos formas:

### 1. Modelos clásicos o redes densas
En este caso, el texto se convierte manualmente en vectores mediante técnicas como:

- **TF-IDF**
- **Embeddings básicos** como Word2Vec o GloVe

Aquí sí es necesario aplicar un proceso de vectorización previo, porque estos modelos no entienden texto directamente.

### 2. Modelos preentrenados tipo Transformer
Si se usa un modelo como **BERT** o **DistilBERT**, no es necesario crear embeddings manualmente.

En este caso se debe usar el **tokenizer del mismo modelo preentrenado**, por ejemplo el de Hugging Face Transformers.  
El flujo correcto es:

- ingresar la reseña en texto bruto,
- aplicar el tokenizer correspondiente,
- convertir el texto en tokens e IDs numéricos,
- pasar esos tokens al modelo.

El propio modelo se encarga de generar sus embeddings internos y realizar la clasificación.

> Importante: no se deben usar tokenizers distintos al del modelo preentrenado, porque el modelo fue entrenado con una tokenización específica y espera esa misma representación de entrada.

---

# Arquitectura base

Se propone una **Red Neuronal Densa (MLP - Multilayer Perceptron)** como línea base.

## Características
- **Preprocesamiento**:
  - vectorización del texto con **TF-IDF** o embeddings básicos
- **Arquitectura**:
  - capas densas totalmente conectadas
- **Objetivo**:
  - servir como referencia de rendimiento para comparar con modelos más avanzados

---

# Arquitectura propuesta según la naturaleza de los datos

Dado que los datos son **secuenciales** (texto), se propone un modelo más adecuado para lenguaje natural.

## Modelo secuencial profundo

Se puede utilizar una red recurrente como:

- **LSTM (Long Short-Term Memory)**

### Ventajas
- capturan dependencias entre palabras,
- conservan contexto en secuencias largas,
- suelen obtener mejor desempeño que una red densa en tareas de NLP.

---

# Arquitectura con transfer learning

Se propone el uso de **modelos Transformer preentrenados**.

## Modelos sugeridos
- **BERT**
- **DistilBERT**

## Estrategia
- aplicar **fine-tuning** sobre el modelo preentrenado,
- usar la librería **Hugging Face Transformers**,
- utilizar el **tokenizer correspondiente al modelo elegido** para procesar las reseñas.

## Flujo de trabajo
1. Cargar el modelo preentrenado.
2. Cargar su tokenizer correspondiente.
3. Tokenizar las reseñas de texto.
4. Entrenar el modelo sobre el conjunto de datos etiquetado.
5. Evaluar el rendimiento en clasificación positiva/negativa.

### Ventajas
- aprovecha conocimiento previo del lenguaje,
- mejora significativamente el rendimiento,
- reduce el tiempo de entrenamiento frente a entrenar desde cero.

---

# Conclusión

Este proyecto puede abordarse en tres niveles:

1. **Modelo base**: MLP con TF-IDF.
2. **Modelo secuencial**: LSTM.
3. **Modelo avanzado**: Transformer preentrenado con tokenizer correspondiente.

Esto permite comparar distintos enfoques para análisis de sentimiento y evaluar cuál ofrece mejores resultados sobre las reseñas.

---

## Video Sustentación: [Vídeo](https://youtu.be/d-hh2da-Fv4?si=snvDZWiRyf5N3inn)

---
