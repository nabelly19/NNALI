import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers, callbacks, initializers

epochs = 150 
batch_size = 64 
patience = 10 
learning_rate = 0.001
model_path = "models/mendes/Bom.keras" 
exists = os.path.exists(model_path)

model = (
    models.load_model(model_path)
    if exists
    else models.Sequential([
        layers.Resizing(120, 90),
        layers.Rescaling(1.0/255),
        layers.Conv2D(64, (3, 3),
            activation = 'relu',
            kernel_initializer = initializers.RandomNormal()
        ),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3),
            activation = 'relu',
            kernel_initializer = initializers.RandomNormal()
        ),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(256, (3, 3),
            activation = 'relu',
            kernel_initializer = initializers.RandomNormal()
        ),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(512,
            activation = 'relu',
            kernel_initializer = initializers.RandomNormal()
        ),
        layers.Dropout(0.5),
        layers.Dense(256,
            activation = 'relu',
            kernel_initializer = initializers.RandomNormal()
        ),
        layers.Dense(62,
            activation = 'softmax',
            kernel_initializer = initializers.RandomNormal()
        )
        ])
)

if not exists:
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    data_directory = "All"

    train_data = tf.keras.preprocessing.image_dataset_from_directory(
        data_directory,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(120, 90),  
        batch_size=batch_size
    )

    validation_data = tf.keras.preprocessing.image_dataset_from_directory(
        data_directory,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(120, 90),
        batch_size=batch_size
    )

    model.fit(
        train_data,
        epochs=epochs,
        validation_data=validation_data,
        callbacks=[
            callbacks.EarlyStopping(monitor="val_loss", patience=patience, verbose=1),
            callbacks.ModelCheckpoint(
                filepath=model_path,
                save_weights_only=False,
                monitor="val_loss",
                mode="min",
                save_best_only=True
            )
        ]
    )
