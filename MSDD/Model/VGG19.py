import tensorflow as tf


class VGG19:

    @staticmethod
    def create_empty_model(num_of_classes):
        conv_model = tf.keras.applications.vgg19.VGG19(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

        for layer in conv_model.layers:
            layer.trainable = False

        x = tf.keras.layers.Flatten(name="flatten")(conv_model.output)
        x = tf.keras.layers.Dense(4096, activation='relu', name="dense_fc1")(x)
        x = tf.keras.layers.Dense(4096, activation='relu', name="dense_fc2")(x)
        output = tf.keras.layers.Dense(num_of_classes, activation='softmax', name="dense_fc3_softmax")(x)

        model = tf.keras.models.Model(inputs=conv_model.input, outputs=output, name="vgg19")

        return model

    @staticmethod
    def create_empty_model_2(num_of_classes):
        model = tf.keras.Sequential(name="vgg19")

        model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu', input_shape=(224, 224, 3), name="block1_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu', name="block1_conv2"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block1_pool"))

        model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3, padding='same', activation='relu', name="block2_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3, padding='same', activation='relu', name="block2_conv2"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block2_pool"))

        model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=3, padding='same', activation='relu', name="block3_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=3, padding='same', activation='relu', name="block3_conv2"))
        model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=3, padding='same', activation='relu', name="block3_conv3"))
        model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=3, padding='same', activation='relu', name="block3_conv4"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block3_pool"))

        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block4_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block4_conv2"))
        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block4_conv3"))
        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block4_conv4"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block4_pool"))

        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block5_conv1"))
        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block5_conv2"))
        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block5_conv3"))
        model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=3, padding='same', activation='relu', name="block5_conv4"))
        model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='same', name="block5_pool"))

        model.add(tf.keras.layers.Flatten(name="flatten"))
        model.add(tf.keras.layers.Dense(units=4096, activation='relu', name="dense_fc1"))
        model.add(tf.keras.layers.Dense(units=4096, activation='relu', name="dense_fc2"))
        model.add(tf.keras.layers.Dense(units=num_of_classes, activation='softmax', name="dense_fc3_softmax"))

        # draw vgg19 structure plot
        # from tensorflow.keras.utils import plot_model
        # plot_model(model, to_file='D:\\vgg19_plot.png', show_shapes=True, show_layer_names=True)

        return model
