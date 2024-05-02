import os
import csv
import shutil




def create_folders():
    folders = ['images', 'annotations']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)


def copy_files(csv_file, image_folder, annotation_folder):
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            image_name = row['Test Images']
            annotation_name = row['Test Annotations']

            if image_name:
                source_image = os.path.join(image_folder, image_name)
                if os.path.exists(source_image):
                    shutil.copy(source_image, 'images')
                    print(source_image)


            if annotation_name:
                source_annotation = os.path.join(
                    annotation_folder, annotation_name)
                if not os.path.exists(source_annotation):
                    shutil.copy(source_annotation, 'annotations')
                    print(source_annotation)


if __name__ == "__main__":
    source_root_folder = r'dataset'  # Using raw string literal
    csv_folder = r'section2-group8'  # Using raw string literal
    csv_file = os.path.join(csv_folder, 'test.csv')
    image_folder = os.path.join(source_root_folder, 'global_images')
    source_root_folder1 = os.path.join(source_root_folder, 'test')
    annotation_folder =  os.path.join(source_root_folder1, 'annotations')

    # create_folders()
    copy_files(csv_file, image_folder, annotation_folder)
    print("Files copied successfully.")