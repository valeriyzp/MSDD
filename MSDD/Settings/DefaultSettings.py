import os
from pathlib import Path


class DefaultSettings:

    PROJECT_PATH = str(Path(__file__).parent.parent)

    DATASET_PATH = PROJECT_PATH + os.sep + "dataset" + os.sep + "Data" + os.sep

    MODELS_PATH = PROJECT_PATH + os.sep + "models" + os.sep

    VGG11_PATH = MODELS_PATH + "VGG11" + os.sep
    VGG11_LRN_PATH = MODELS_PATH + "VGG11_LRN" + os.sep
    VGG13_PATH = MODELS_PATH + "VGG13" + os.sep
    VGG16_PATH = MODELS_PATH + "VGG16" + os.sep
    VGG16_1_PATH = MODELS_PATH + "VGG16_1" + os.sep
    VGG19_PATH = MODELS_PATH + "VGG19" + os.sep

    RESOURCES_PATH = PROJECT_PATH + os.sep + "resources" + os.sep

    ABOUT_PROGRAM = '<h3><strong>Програмне забезпечення для виявлення дефектів на металевих поверхнях</strong></h3><p />' \
                    '<p>Написано на Python з TensorFlow, Keras та PyQt</p><p />' \
                    '<p>Розробник - Козлов В.В.</p>' \
                    '<p>Керівник - Олійник А.О.</p><p />' \
                    '<p>Кафедра програмних засобів - Факультет комп\'ютерних наук і технологій</p>' \
                    '<p>2021 - Національний університет "Запорізька політехніка"</p>'
