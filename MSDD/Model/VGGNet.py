from datetime import datetime
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import json
import os
import shutil

from Model.VGG11 import VGG11
from Model.VGG11_LRN import VGG11_LRN
from Model.VGG13 import VGG13
from Model.VGG16 import VGG16
from Model.VGG16_1 import VGG16_1
from Model.VGG19 import VGG19

from Data.Dataset import Dataset


class VGGNet:

    def __init__(self, name, path):
        self.name = name
        self.path = path

        self.modelPath = path + "model_weights.h5"
        self.dataPath = path + "data.json"

        self.model = None
        self.classes = {}
        self.fitHistory = {"loss": [], "accuracy": [], "val_loss": [], "val_accuracy": []}
        self.evaluateResults = {"loss": None, "accuracy": None}
        self.parametersCount = None

        self.lastChangeTime = datetime.now()

    def is_saved_fitted_model(self):
        if not os.path.exists(self.modelPath) or not os.path.exists(self.dataPath):
            return False
        else:
            return True

    def set_new_model(self, num_of_classes):
        self.clear_model_variables()
        self.model = VGGNet.get_empty_model_architecture_by_name(self.name, num_of_classes)

        self.lastChangeTime = datetime.now()

        if os.path.exists(self.path):
            shutil.rmtree(self.path)

    def set_new_model_and_compile(self, num_of_classes):
        self.set_new_model(num_of_classes)
        self.compile_model()

    def compile_model(self):
        self.model.compile(loss=tf.keras.losses.categorical_crossentropy,
                           optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                           metrics=['accuracy'])

        print(self.model.summary())
        self.parametersCount = self.model.count_params()

    def fit_model(self, dataset):
        self.classes = dataset.get_classes()

        early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_accuracy',
                                                          mode='auto',
                                                          min_delta=0,
                                                          verbose=1,
                                                          patience=3,
                                                          restore_best_weights=False)

        # Save model after each epoch
        #
        #
        # filepath = self.path + "model_" + datetime.now().strftime("%Y%d%m_%H%M%S%f") + "_epoch_" \
        #                                                                                "{epoch:04d}" \
        #                                                                                "_acc_" \
        #                                                                                "{val_accuracy:.4f}.h5"
        # model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=filepath,
        #                                                                save_weights_only=False,
        #                                                                monitor='val_accuracy',
        #                                                                mode='auto',
        #                                                                save_best_only=False,
        #                                                                verbose=1)

        class HistoryCallback(tf.keras.callbacks.Callback):
            def __init__(self, outer_class):
                super().__init__()
                self.outerClass = outer_class

            def on_epoch_end(self, epoch, logs=None):
                self.outerClass.fitHistory['loss'].append(logs['loss'])
                self.outerClass.fitHistory['accuracy'].append(logs['accuracy'])
                self.outerClass.fitHistory['val_loss'].append(logs['val_loss'])
                self.outerClass.fitHistory['val_accuracy'].append(logs['val_accuracy'])

                self.outerClass.evaluateResults = self.model.evaluate(dataset.get_test_data(), return_dict=True)

                self.outerClass.save_model(self.model)

                self.outerClass.lastChangeTime = datetime.now()

        # Stop fitting, but it works only after end of epoch
        #
        # class TerminateOnFlag(tf.keras.callbacks.EarlyStopping):
        #     def __init__(self, outer_class):
        #         super().__init__()
        #         self.outerClass = outer_class
        #
        #     def on_batch_end(self, batch, logs=None):
        #         if self.outerClass.stopTrainingImmediately is True:
        #             self.model.stop_training = True
        #             self.outerClass.stopTrainingImmediately = False

        callbacks = [early_stopping, HistoryCallback(self)]

        self.model.fit(dataset.get_train_data(),
                       batch_size=32,
                       epochs=20,
                       validation_data=dataset.get_valid_data(),
                       verbose=1,
                       shuffle=True,
                       callbacks=callbacks)

    def save_model(self, model=None):
        current_time = datetime.now().strftime("%Y%d%m_%H%M%S%f")
        temp_model_path = self.path + current_time + ".h5"
        temp_swap_model_path = self.path + current_time + "swap.h5"
        temp_data_path = self.path + current_time + ".json"
        temp_swap_data_path = self.path + current_time + "swap.json"

        if not os.path.exists(self.path):
            os.mkdir(self.path)

        if model is not None:
            model.save_weights(temp_model_path)
        else:
            self.model.save_weights(temp_model_path)

        data = {"classes": self.classes,
                "fitHistory": self.fitHistory,
                "evaluateResults": self.evaluateResults,
                "parametersCount": self.parametersCount}

        with open(temp_data_path, 'w') as outfile:
            json.dump(data, outfile, indent=4)

        if os.path.exists(self.modelPath):
            os.rename(self.modelPath, temp_swap_model_path)

        if os.path.exists(self.dataPath):
            os.rename(self.dataPath, temp_swap_data_path)

        os.rename(temp_model_path, self.modelPath)
        os.rename(temp_data_path, self.dataPath)

        if os.path.exists(temp_swap_model_path):
            os.remove(temp_swap_model_path)

        if os.path.exists(temp_swap_data_path):
            os.remove(temp_swap_data_path)

    def predict(self, img_path):
        test_image = image.load_img(img_path, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image.astype('float32') / 255

        result = self.classes[np.argmax(self.model.predict(test_image))]
        if result in Dataset.DEFECT_TYPES_TRANSLATE:
            return Dataset.DEFECT_TYPES_TRANSLATE[result]
        else:
            return result

    def load_model_info(self):
        self.lastChangeTime = datetime.now()
        with open(self.dataPath) as json_file:
            data = json.load(json_file)
            self.classes = {int(key): value for key, value in data["classes"].items()}
            self.fitHistory = data["fitHistory"]
            self.evaluateResults = data["evaluateResults"]
            self.parametersCount = data["parametersCount"]

    def load_model(self):
        self.load_model_info()

        self.model = VGGNet.get_empty_model_architecture_by_name(self.name, len(self.classes))
        self.compile_model()
        self.model.load_weights(self.modelPath)

    def clear_model_variable(self):
        self.model = None

    def clear_model_variables(self):
        self.clear_model_variable()

        self.classes = {}
        self.fitHistory = {"loss": [], "accuracy": [], "val_loss": [], "val_accuracy": []}
        self.evaluateResults = {"loss": None, "accuracy": None}
        self.parametersCount = None

    @staticmethod
    def get_empty_model_architecture_by_name(model_name, num_of_classes):
        if model_name == "VGG11":
            return VGG11.create_empty_model(num_of_classes)
        elif model_name == "VGG11_LRN":
            return VGG11_LRN.create_empty_model(num_of_classes)
        elif model_name == "VGG13":
            return VGG13.create_empty_model(num_of_classes)
        elif model_name == "VGG16":
            return VGG16.create_empty_model(num_of_classes)
        elif model_name == "VGG16_1":
            return VGG16_1.create_empty_model(num_of_classes)
        elif model_name == "VGG19":
            return VGG19.create_empty_model(num_of_classes)
        else:
            return None
