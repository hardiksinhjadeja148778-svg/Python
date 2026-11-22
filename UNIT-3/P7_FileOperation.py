import shutil
import os

# Create a file to work with
f = open("file1.txt", "w")
f.write("Hello, this is a test file")
f.close()
print("Original file created")

# Make folders
os.makedirs("folder1", exist_ok=True)
os.makedirs("folder2", exist_ok=True)
print("Folders created")

# 1. Copy file
print("\n--- Copy ---")
shutil.copy("file1.txt", os.path.join("folder1", "file1_copy.txt"))
print("File copied to folder1")
print("Copy exists    :", os.path.exists("folder1/file1_copy.txt"))
print("Original exists:", os.path.exists("file1.txt"))

# 2. Copy with details (copy2)
shutil.copy2("file1.txt", os.path.join("folder1", "file1_copy2.txt"))
print("File copied using copy2()")
print("Files in folder1:", os.listdir("folder1"))

# 3. Move file
print("\n--- Move ---")
shutil.move("folder1/file1_copy.txt", "folder2/file1_moved.txt")
print("File moved to folder2")
print("Exists in folder1:", os.path.exists("folder1/file1_copy.txt"))
print("Exists in folder2:", os.path.exists("folder2/file1_moved.txt"))

# 4. Delete file
print("\n--- Delete ---")
os.remove("folder2/file1_moved.txt")
print("File deleted")
print("Exists in folder2:", os.path.exists("folder2/file1_moved.txt"))

# 5. Delete folders and original file
shutil.rmtree("folder1")
shutil.rmtree("folder2")
os.remove("file1.txt")
print("Folders and original file deleted")