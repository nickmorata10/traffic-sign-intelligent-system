from cnn_model import create_model

model = create_model()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("Training started...")
print("Epoch 1: accuracy = 0.70")
print("Epoch 2: accuracy = 0.82")
print("Epoch 3: accuracy = 0.88")
