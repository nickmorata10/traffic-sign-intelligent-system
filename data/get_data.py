import os

def prepare_data_dirs():
    print("--- Initializing Data Structure ---")
    folders = ['data/train', 'data/val', 'data/test']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        # Create a dummy file to simulate data presence
        with open(os.path.join(folder, 'placeholder.txt'), 'w') as f:
            f.write('GTSRB data placeholder')
    print("Data directories ready.")

if __name__ == "__main__":
    prepare_data_dirs()
