import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def extract_archive(filepath, dest_dir):
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    make_archive(filepaths=["zip_creator.py"], dest_dir="dest")
    extract_archive(filepath=["dest\compressed.zip"], dest_dir="dest")
