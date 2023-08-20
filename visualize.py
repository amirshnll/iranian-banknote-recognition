import visualkeras

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPool2D, Dropout
from tensorflow.keras.models import Sequential


from sklearn.model_selection import train_test_split

model = Sequential()
model.add(
    Conv2D(
        kernel_size=(3, 3),
        filters=32,
        activation="tanh",
        input_shape=(
            300,
            200,
            3,
        ),
    )
)
model.add(Conv2D(filters=30, kernel_size=(3, 3), activation="tanh"))
model.add(MaxPool2D(2, 2))
model.add(Conv2D(filters=30, kernel_size=(3, 3), activation="tanh"))
model.add(MaxPool2D(2, 2))
model.add(Conv2D(filters=30, kernel_size=(3, 3), activation="tanh"))

model.add(Flatten())

model.add(Dense(20, activation="relu"))
model.add(Dense(15, activation="relu"))
model.add(Dense(6, activation="softmax"))

model.save("")

visualkeras.layered_view(
    model, legend=True, draw_volume=False, show_dimantion=True, to_file="output.png"
).show()
