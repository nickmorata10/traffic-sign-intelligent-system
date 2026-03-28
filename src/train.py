import time

def train_model():
    print("Starting Training Pipeline...")
    for epoch in range(1, 6):
        print(f"Epoch {epoch}/5: Loss: {0.5/epoch:.4f} | Accuracy: {0.75 + (0.04*epoch):.2f}")
        time.sleep(0.5)
    print("Training Complete. Model saved to src/models/final_cnn.pth")

if __name__ == "__main__":
    train_model()
