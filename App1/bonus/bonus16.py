import PySimpleGUI as Sg

label1 = Sg.Text("Select file to compress:")
input_files = Sg.InputText(tooltip="Choose files")
select_file_button = Sg.FilesBrowse("Choose")

label2 = Sg.Text("Select destination folder:")
input_folders = Sg.InputText(tooltip="Choose folder")
select_folder_button = Sg.FolderBrowse("Choose")

compress_button = Sg.Button("Compress")

window = Sg.Window("File Zipper", layout=[[label1, input_files, select_file_button],
                                          [label2, input_folders, select_folder_button],
                                          [compress_button]])


window.read()
print("Hello from inside")
window.close()
