from tensorflow.keras.preprocessing.image import ImageDataGenerator


class Dataset:

    DEFECT_TYPES_TRANSLATE = {"Crazing": "Мікротріщини", "Inclusion": "Включення", "Patches": "Забруднення",
                              "Pitted": "Рябизна", "Rolled": "Вкатана окалина", "Scratches": "Подряпини"}

    def __init__(self, path):
        train_data_generator = ImageDataGenerator(
            rescale=1.0 / 255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

        test_data_generator = ImageDataGenerator(rescale=1.0 / 255)

        self.__trainData = train_data_generator.flow_from_directory(path + 'train',
                                                                    target_size=(224, 224),
                                                                    class_mode='categorical')

        self.__validData = test_data_generator.flow_from_directory(path + 'valid',
                                                                   target_size=(224, 224),
                                                                   class_mode='categorical')

        self.__testData = test_data_generator.flow_from_directory(path + 'test',
                                                                  target_size=(224, 224),
                                                                  class_mode='categorical')

    def get_train_data(self):
        return self.__trainData

    def get_valid_data(self):
        return self.__validData

    def get_test_data(self):
        return self.__testData

    def get_num_of_classes(self):
        return len(self.__trainData.class_indices)

    def get_classes(self):
        return {value: key for key, value in self.__trainData.class_indices.items()}
