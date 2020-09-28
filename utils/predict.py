import cv2
import numpy as np
import tensorflow as tf
from tensorflow.python.saved_model import tag_constants
from PIL import Image
from utils.model_utils import draw_bbox

class Predictor:
    # Modificado de: https://github.com/hunglc007/tensorflow-yolov4-tflite/blob/master/detect.py
    def __init__(self, model_path, classes, confidence):
        self.model_path = model_path
        self.classes = classes
        self.box_colors = [(255,128,0),(0,255,0),(255,0,0)]
        self.confidence = confidence
        self.model = self.__load_model()

    def __load_model(self):
        return tf.saved_model.load(self.model_path, tags=[tag_constants.SERVING])

    def predict(self, img_path, img_size):
        """
        Función que permite realizar las predicciones

        Parameters
        ----------
        img_path : Ruta de la imagen a predecir.
        img_size : Tupla de la dimensión de la imagen.
        """
        # Read oiginal image
        original_image = cv2.imread(img_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

        # Resize & Scale image
        image_scaled = cv2.resize(original_image, img_size)
        image_scaled = image_scaled / 255.
        
        # Expand first dimension
        images = np.expand_dims(image_scaled, axis=0).astype(np.float32)

        # We are not using tflite, so there is no condition
        inference = self.model.signatures['serving_default']
        image_batch = tf.constant(images)
        prediction_bboxes = inference(image_batch)

        # Obtenemos los boxes y confidences
        boxes = None
        confidences = None
        for key, value in prediction_bboxes.items():
            boxes = value[:,:,0:4]
            confidences = value[:,:,4:]

        # Non-maximum supression
        boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
            boxes = tf.reshape(boxes, (tf.shape(boxes)[0], -1, 1, 4)),
            scores = tf.reshape(confidences,(tf.shape(confidences)[0], -1, tf.shape(confidences)[-1])),
            max_output_size_per_class=50,
            max_total_size=50,
            iou_threshold=0.45,
            score_threshold=self.confidence) #score_threshold=0.25

        # Obtenemos las predicciones
        predictions = [boxes.numpy(), scores.numpy(), classes.numpy(), valid_detections.numpy()]

        # Generamos la imagen con los bounding boxes
        image = draw_bbox(original_image, predictions, self.classes, self.box_colors)
        image = Image.fromarray(image.astype(np.uint8))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
        
        return image

    def predict_frame(self, image, img_size):
        """
        Función que permite realizar las predicciones

        Parameters
        ----------
        img_path : Ruta de la imagen a predecir.
        img_size : Tupla de la dimensión de la imagen.
        """
        # Copy original image
        original_image = image.copy()

        # Resize & Scale image
        image_scaled = cv2.resize(original_image, img_size)
        image_scaled = image_scaled / 255.
        
        # Expand first dimension
        images = np.expand_dims(image_scaled, axis=0).astype(np.float32)

        # We are not using tflite, so there is no condition
        inference = self.model.signatures['serving_default']
        image_batch = tf.constant(images)
        prediction_bboxes = inference(image_batch)

        # Obtenemos los boxes y confidences
        boxes = None
        confidences = None
        for key, value in prediction_bboxes.items():
            boxes = value[:,:,0:4]
            confidences = value[:,:,4:]

        # Non-maximum supression
        boxes, scores, classes, valid_detections = tf.image.combined_non_max_suppression(
            boxes = tf.reshape(boxes, (tf.shape(boxes)[0], -1, 1, 4)),
            scores = tf.reshape(confidences,(tf.shape(confidences)[0], -1, tf.shape(confidences)[-1])),
            max_output_size_per_class=50,
            max_total_size=50,
            iou_threshold=0.45,
            score_threshold=self.confidence) #score_threshold=0.25

        # Obtenemos las predicciones
        predictions = [boxes.numpy(), scores.numpy(), classes.numpy(), valid_detections.numpy()]

        # Generamos la imagen con los bounding boxes
        image = draw_bbox(original_image, predictions, self.classes, self.box_colors)
        image = Image.fromarray(image.astype(np.uint8))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
        
        return image