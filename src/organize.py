import os
import shutil

folder = "Downloads"

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)

    if not os.path.isfile(file_path):
        continue

    _, extension = os.path.splitext(file)

    if extension in [".png", ".jpg", ".jpeg", ".gif"]:
        category = "Images"
    elif extension in [".pdf", ".docx", ".txt"]:
        category = "Documents"
    elif extension in [".mp3", ".wav"]:
        category = "Music"
    elif extension in [".mp4", ".mkv", ".avi"]:
        category = "Videos"
    elif extension in [".py", ".js", ".html", ".css"]:
        category = "Code"
    else:
        category = "Others"

    destination = os.path.join(folder, category)

    os.makedirs(destination, exist_ok=True)

    shutil.move(file_path, os.path.join(destination, file))

    print(f"Moved: {file} -> {category}")