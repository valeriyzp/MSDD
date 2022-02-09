import tensorflow as tf


class VGG13:

    @staticmethod
    def create_empty_model(num_of_classes):
        model = tf.keras.Sequential(name="vgg13")

        model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu', input_shape=(224, 224, 3), name="block1_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu', name="block1_conv2"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block1_pool"))

        model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3, padding='same', activation='relu', name="block2_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3, padding='same', activation='relu', name="block2_conv2"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block2_pool"))

        model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=3, padding='same', activation='relu', name="block3_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=3, padding='same', activation='relu', name="block3_conv2"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block3_pool"))

        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block4_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block4_conv2"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block4_pool"))

        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block5_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block5_conv2"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block5_pool"))

        model.add(tf.keras.layers.Flatten(name="flatten"))
        model.add(tf.keras.layers.Dense(units=4096, activation='relu', name="dense_fc1"))
        model.add(tf.keras.layers.Dense(units=4096, activation='relu', name="dense_fc2"))
        model.add(tf.keras.layers.Dense(units=num_of_classes, activation='softmax', name="dense_fc3_softmax"))

        return model
