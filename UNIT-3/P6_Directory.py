import os
import sys

# ---------- Directory operations ----------
print("--- Directory Operations ---")

if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
print("Directory created")

print("Current Directory:", os.getcwd())
print("Contents         :", os.listdir("."))

os.rename("test_folder", "renamed_folder")
print("Directory renamed")

print("Exists      :", os.path.exists("renamed_folder"))
print("Is directory:", os.path.isdir("renamed_folder"))

# ---------- File operations ----------
print("\n--- File Operations ---")

file_path = os.path.join("renamed_folder", "sample.txt")

f = open(file_path, "w")
f.write("Hello Python")
f.close()
print("File created and written")

f = open(file_path, "r")
print("File content:", f.read())
f.close()

print("Is file     :", os.path.isfile(file_path))
print("File size   :", os.path.getsize(file_path), "bytes")
print("Files in folder:", os.listdir("renamed_folder"))

os.remove(file_path)
print("File removed")

os.rmdir("renamed_folder")
print("Directory removed")

# ---------- sys module ----------
print("\n--- sys Module ---")
print("Python version :", sys.version)
print("Platform       :", sys.platform)
print("Command line arguments:", sys.argv)

print("\nProgram ended")
sys.exit()