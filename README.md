# Mask Detector con YOLOv4

Actualización del proyecto usando como detector de Rostros con Mascarilla usando YOLOv4. Las configuraciones realizadas están basadas en el repositorio original de Darknet-YOLOv4.

En caso de tener alguna duda:

✉️ jjorge.rc93@gmail.com

## Objetivo 🚀

Este proyecto contiene la configuración de YOLOv4 para detectar en una imagen o un video que personas están usando mascarilla, con el fin de prevenir la expansión del COVID-19.

<center><p> 
    <img src="https://user-images.githubusercontent.com/7152507/94376136-3d881400-00de-11eb-8194-fc8539c3fd49.png" alt="Resultado">
    Detección de mascarillas con YOLOv4
</p></center>

## Procedimiento 🛠️

1. El proceso para poder generar un modelo con un dataset propio de mascarillas, se encuentra descrito paso a paso en el notebook <a href="https://github.com/jjrodcast/MaskDetector-YoloV4/blob/master/notebooks/PY1_Configuraci%C3%B3n_YOLOv4_Objetos_Personalizados.ipynb">PY1_Configuración_YOLOv4_Objetos_Personalizados.ipynb</a> (este paso se puede omitir si se desea usar los pesos ya entrenados que se encuentra en ruta <a href="https://drive.google.com/file/d/1k2g6YOf55I7e0TAIX7iNl-xGD11d1CfC/view">yolo-obj_final.weights</a>)

2. Luego de tener los pesos de la red YOLOv4 para el detector de mascarillas, se debe pasar estos pasos a Tensorflow o Tensorflow-Lite, por lo cual todos los pasos para realizar esta tarea están en el notebook <a href="https://github.com/jjrodcast/MaskDetector-YoloV4/blob/master/notebooks/PY1_Conversi%C3%B3n_YOLOv4_to_Tensorflow.ipynb">PY1_Conversión_YOLOv4_to_Tensorflow.ipynb</a>

## Pre-Requisitos 📋

* Los notebooks que se presentan en esta versión usando YOLOv4 fueron duseñados para ser ejecutados en Google Colab usando GPU, por lo cual si se desea ejecutar localmente se recomienda tener una máquina con GPU.

* A diferencia del notebook de la rama master de este repositorio no se usa *Multi-Task Cascaded Convolutional Neural Network*

## Archivos del Repositorio 🛠️

📌 **ARCHIVOS GENERALES:**

* Todos los modelos archivos se encuentran en: <a href="https://drive.google.com/drive/folders/1gQMWHOCsb4zuPYI9lvJp-62KyTaGXCbt">Archivos YOLOv4</a>

📌 **UTILITARIOS:**

* **utils/predict.py** : Este utilitario contiene la clase `Predictor` que se utiliza para realizar las predicciones en las imágenes.

* **utils/model_utils** : Este utilitario contiene una función para poder dibujar los cuadros delimitadores de las personas que no tienen mascarilla, tienen mascarilla o se han puesto mal la mascarilla.

📌 **ARCHIVO PRINCIPAL:**

* **_MaskDetector_YOLOv4.ipynb_** : Notebook con las pruebas end-to-end para generar sobre imágenes las predicciones de si una persona está usando o no una mascarilla. (No está optimizado para ser usado en video)

📌 **ARCHIVOS MULTIMEDIA:**

Básicamente puedes cargar imágenes o videos propios, pero por defecto puedes utilizar las imágenes presentes en la carpeta **"multimedia/"**.

## Proceso de Ejecución ⚙️ 

* Validar que el Tipo de Entorno de Ejecución está en **GPU** en todos los Notebooks
* Ejecutar el Notebook `PY1_Configuración_YOLOv4_Objetos_Personalizados.ipynb` (puede que demore dependiendo de el tamaño de las imágenes y la configuración)
* Ejecutar el Notebook `PY1_Conversión_YOLOv4_to_Tensorflow.ipynb`
* Ejecutar el Notebook `MaskDetector_YOLOv4.ipynb`
* Fin 😃

## Archivos Adicionales 📁

* **notebooks/PY1_Configuración_YOLOv4_Objetos_Personalizados.ipynb** : Notebook para generar el modelo entrenado desde cero con YOLOv4 para predecir si un rostro en una imagen tiene una mascarilla o no. Tener en cuenta que este Notebook puede ser usado de manera independiente si sólo se quiere generar un modelo YOLOv4 sin se exportado a Tensorflow.

* **notebooks/PY1_Conversión_YOLOv4_to_Tensorflow.ipynb** : Notebook que permite convertir el modelo generado de YOLOv4 del notebook _PY1_Configuración_YOLOv4_Objetos_Personalizados.ipynb_ hacia Tensorflow 2.x. Este notebook requiere únicamente el archivo de pesos para poder ser ejecutado por lo cual se debe ejecutar el primer notebook (para su simplicidad ya se provee dichos pesos para que pueda ser ejecutado independientemente, estos pesos se mencionaron en el punto `1` del apartado `Procedimiento`)

## Documentación de apoyo 📚

RoboFlow - Transformar imágenes para ser entrenadas:
https://roboflow.com/

Darknet-YOLOv4 - Configuración de YOLOv4 para detección de objetos: https://github.com/pjreddie/darknet

## Autor ✒️

* **Jorge Rodríguez Castillo** - [Linkedin](https://www.linkedin.com/in/jorge-rodr%C3%ADguez-castillo/) - [Github](https://github.com/jjrodcast)

## Licencia 📄

Este proyecto está bajo la Licencia **GNU General Public License v3.0** - mira el archivo [LICENSE.md](LICENSE.md) para más detalles.

