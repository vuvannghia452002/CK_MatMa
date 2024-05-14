import os
import re
import shutil



def copy_folders_and_nghia_files(root_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for root, dirs, files in os.walk(root_folder):
        # Create corresponding directories in the destination folder
        for dir in dirs:
            dest_dir_path = os.path.join(dest_folder, os.path.relpath(os.path.join(root, dir), root_folder))
            if not os.path.exists(dest_dir_path):
                os.makedirs(dest_dir_path)
        
        # Process each file
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, root_folder)
            dest_file_path = os.path.join(dest_folder, relative_path + '.nghia')
            dest_file_dir = os.path.dirname(dest_file_path)
            
            if not os.path.exists(dest_file_dir):
                os.makedirs(dest_file_dir)
            
            # Copy .nghia files of size 0KB
            if file.endswith('.nghia') and os.path.getsize(file_path) == 0:
                shutil.copy2(file_path, dest_file_path)
            else:
                # Create an empty file with .nghia extension
                open(dest_file_path, 'w').close()





root_folder = r"C:\Users\vvn20206205\Desktop\github\20232\CK_MatMa\contents\video\Udemy_Master_Modern_Security_and_Cryptography_by_Coding_in_Python\en"
print(f"🚀 Folder root: {os.path.abspath(root_folder)}")
dest_folder = os.path.basename(root_folder)
dest_folder = re.sub(r'[^a-zA-Z0-9]', '', dest_folder)+"_VVN_COPY"
dest_folder = os.path.join(os.path.dirname(root_folder), dest_folder)
if os.path.exists(dest_folder):
    shutil.rmtree(dest_folder)
print(f"🚀 Folder dest: {os.path.abspath(dest_folder)}")
copy_folders_and_nghia_files(root_folder, dest_folder)
print(f"🚀 {"Xong"}")