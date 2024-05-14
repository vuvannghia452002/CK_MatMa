import os

def xoa_thu_muc_trong(root_folder):
    for root, dirs, files in os.walk(root_folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"🚀 Đã xóa thư mục trống: {dir_path}")

# Xóa thư mục con trống
root_folder = "../../../"
print(f"🚀 Folder root: {os.path.abspath(root_folder)}")
xoa_thu_muc_trong(root_folder)
