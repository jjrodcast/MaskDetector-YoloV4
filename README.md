# Mask Detector con YOLOv4

Actualización del proyecto usando como detector de Rostros con Mascarilla usando YOLOv4. Las configuraciones realizadas están basadas en el repositorio original de Darknet-YOLOv4.

## Objetivo 🚀

Este proyecto contiene la configuración de YOLOv4 para detectar en una imagen o un video que personas están usando mascarilla, con el fin de prevenir la expansión del COVID-19.

<p align="center"> 
    <img src="https://user-images.githubusercontent.com/7152507/94376136-3d881400-00de-11eb-8194-fc8539c3fd49.png" alt="Resultado">
    Detección de mascarillas con YOLOv4
</p>

## Procedimiento 🛠️

1. El proceso para poder generar un modelo con un dataset propio de mascarillas, se encuentra descrito paso a paso en el notebook <a href="https://github.com/jjrodcast/MaskDetector-YoloV4/blob/master/notebooks/PY1_Configuraci%C3%B3n_YOLOv4_Objetos_Personalizados.ipynb">PY1_Configuración_YOLOv4_Objetos_Personalizados.ipynb</a> (este paso se puede omitir si se desea usar los pesos ya entrenados que se encuentra en ruta <a href="https://drive.google.com/file/d/1k2g6YOf55I7e0TAIX7iNl-xGD11d1CfC/view">yolo-obj_final.weights</a>)

2. Luego de tener los pesos de la red YOLOv4 para el detector de mascarillas, se debe pasar estos pasos a Tensorflow o Tensorflow-Lite, por lo cual todos los pasos para realizar esta tarea están en el notebook <a href="https://github.com/jjrodcast/MaskDetector-YoloV4/blob/master/notebooks/PY1_Conversi%C3%B3n_YOLOv4_to_Tensorflow.ipynb">PY1_Conversión_YOLOv4_to_Tensorflow.ipynb</a>

## Pre-Requisitos 📋

* Los notebooks que se presentan en esta versión usando YOLOv4 fueron duseñados para ser ejecutados en Google Colab usando GPU, por lo cual si se desea ejecutar localmente se recomienda tener una máquina con GPU.

* A diferencia del notebook de la rama master de este repositorio no se usa *Multi-Task Cascaded Convolutional Neural Network*

## Archivos del Repositorio 🛠️

📌 **Archivos Generales:**

* Todos los modelos archivos se encuentran en: <a href="https://drive.google.com/drive/folders/1gQMWHOCsb4zuPYI9lvJp-62KyTaGXCbt">Archivos YOLOv4</a>

📌 **UTILITARIOS:**

* En construcción ...

📌 **ARCHIVO PRINCIPAL:**

* **_MaskDetector_YOLOv4.ipynb_** : Notebook con las pruebas end-to-end para generar sobre imágenes las predicciones de si una persona está usando o no una mascarilla. (No está optimizado para ser usado en video)

📌 **ARCHIVOS MULTIMEDIA:**

Básicamente puedes cargar imágenes o videos propios, pero por defecto puedes utilizar las imágenes presentes en la carpeta **"multimedia/"**.

## Proceso de Ejecución ⚙️ 

* Levantar el notebook principal en Colab
* Cargar los archivos necesarios al notebook
* Validar que el Tipo de Entorno de Ejecución está en **GPU**
* Ejecutar todo el notebook

## Archivos Adicionales 📁

* **notebooks/CNN_Zero_ProyectoFinal.ipynb** : Notebook para generar el modelo entrenado desde cero con Keras para predecir si un rostro en una imagen tiene una mascarilla o no.

* **notebooks/VC_MaskDetector_Transfer Learning.ipynb** : Notebook con Transfer Learning del modelo pre-entrenado de ResNet18 con Pytorch para predecir si un rostro en una imagen tiene una mascarilla o no.

* **dataset/** : Este folder contiene los datasets utilizados para entrenar y validar los modelos clasificadores del uso de la mascarilla. _Repositorio Fuente:_ facial_mask_classifier (https://bit.ly/3beau7v)

## Documentación de apoyo 📚

RoboFlow - Transformar imágenes para ser entrenadas:
https://roboflow.com/

Darknet-YOLOv4 - Configuración de YOLOv4 para detección de objetos: https://github.com/pjreddie/darknet

## Autor ✒️

* **Jorge Rodríguez Castillo** - [Linkedin](https://www.linkedin.com/in/jorge-rodr%C3%ADguez-castillo/) - [Github](https://github.com/jjrodcast)

## Licencia 📄

Este proyecto está bajo la Licencia **GNU General Public License v3.0** - mira el archivo [LICENSE.md](LICENSE.md) para más detalles.

