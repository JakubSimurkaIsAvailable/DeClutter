import shutil
import os
import getpass

user = getpass.getuser()
path = fr'C:\Users\{user}\Desktop'
imagefolder = os.path.join(path, 'images')
excelfolder = os.path.join(path, 'excels')
pdffolder = os.path.join(path, 'pdfs')
exefolder = os.path.join(path, 'exes')
txtfolder = os.path.join(path, 'txts')


def inicialize_folders():
    
    if not os.path.exists(imagefolder):
        os.makedirs(imagefolder)
    if not os.path.exists(excelfolder):
        os.makedirs(excelfolder)
    if not os.path.exists(pdffolder):
        os.makedirs(pdffolder)
    if not os.path.exists(exefolder):
        os.makedirs(exefolder)
    if not os.path.exists(txtfolder):
        os.makedirs(txtfolder)

def flush_exes():
    for file in os.listdir(exefolder):
        full_path = os.path.join(exefolder, file)
        if os.path.isfile(full_path) and file.endswith('.exe'):
            try:
                os.remove(full_path)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Failed to delete {file}: {e}")
    
#move files from source folder to the destination folder
def move_file(src):
    for file in os.listdir(src):
        if file.endswith(('.jpg', '.png', '.jpeg', '.gif', '.webp')):
            shutil.move(os.path.join(src, file), os.path.join(imagefolder, file))
        if file.endswith(('.csv', '.xlsx')):
            shutil.move(os.path.join(src, file), os.path.join(excelfolder, file))
        if file.endswith(('.pdf', '.docx')):
            shutil.move(os.path.join(src, file), os.path.join(pdffolder, file))
        if file.endswith(('.exe')):
            shutil.move(os.path.join(src, file), os.path.join(exefolder, file))
        if file.endswith(('.txt')):
            shutil.move(os.path.join(src, file), os.path.join(txtfolder, file))

inicialize_folders()            
move_file(fr'C:\Users\{user}\Downloads')
move_file(fr'C:\Users\{user}\Desktop')
response = ""

print("Do you wish to flush the folder containing .exe files [y/n]?")
response = input().strip().lower()

if response == 'y':
    print("Flushing exes folder...")
    flush_exes()
if response == 'n':
    print("Next time :D")