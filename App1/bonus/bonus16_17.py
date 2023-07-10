import PySimpleGUI as Sg
import zip_creator

label1 = Sg.Text("Select file to compress:")
input_files = Sg.InputText(tooltip="Choose files")
select_file_button = Sg.FilesBrowse("Choose", key="files")

label2 = Sg.Text("Select destination folder:")
input_folders = Sg.InputText(tooltip="Choose folder")
select_folder_button = Sg.FolderBrowse("Choose", key="folder")

compress_button = Sg.Button("Compress")
output_label = Sg.Text("", key="output")

window = Sg.Window("File Zipper", layout=[[label1, input_files, select_file_button],
                                          [label2, input_folders, select_folder_button],
                                          [compress_button, output_label]])


while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    zip_creator.make_archive(filepaths, folder)

    window["output"].update(value="Compress done!")

window.close()
