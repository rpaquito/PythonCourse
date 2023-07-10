import PySimpleGUI as Sg
import zip_creator

label1 = Sg.Text("Select file to extract:")
input_files = Sg.InputText(tooltip="Choose files")
select_file_button = Sg.FileBrowse("Choose", key="file")

label2 = Sg.Text("Select destination folder:")
input_folders = Sg.InputText(tooltip="Choose folder")
select_folder_button = Sg.FolderBrowse("Choose", key="folder")

extract_button = Sg.Button("Extract")
output_label = Sg.Text("", key="output")

window = Sg.Window("Archive Extractor", layout=[[label1, input_files, select_file_button],
                                          [label2, input_folders, select_folder_button],
                                          [extract_button, output_label]])


while True:
    event, values = window.read()
    print(event, values)
    archivepath = values['file']
    dest_dir = values['folder']
    zip_creator.extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extract complete")

window.close()