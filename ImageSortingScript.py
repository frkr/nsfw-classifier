import os
import shutil
from PIL import Image

from nudenet import NudeClassifier

# Initialize the classifier (downloads the model the first time)
classifier = NudeClassifier()

def is_pornographic(image_path):
    # Classify the image
    results = classifier.classify(image_path)
    # print("Results var:", results)
    if results[image_path]['unsafe'] > 0.5:
        print(image_path)
        return True
    return False


def sort_images(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    if is_pornographic(file_name):
                        shutil.move(file_path, os.path.join(destination_folder, file_name))
            except Exception:
                continue

source_directory = "/Users/frkr/fleet/vgarage"
destination_directory = "/Users/frkr/fleet/porn"
sort_images(source_directory, destination_directory)

