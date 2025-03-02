import os
from pathlib import Path
import csv
from connection import Connection

dataset_dir = "./../dataset"
output_csv = "./../dataset/captions.csv"

openai_connection = Connection()


def process_dataset(dataset, output_csv):
    data = []
    for root, _, files in os.walk(dataset):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', 'heic')):
                image_path = os.path.join(root, file)
                caption = openai_connection.generate(image_path)
                print(caption)
                data.append((file, caption))
    
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "caption"])
        writer.writerows(data)

process_dataset(dataset_dir, output_csv)
    