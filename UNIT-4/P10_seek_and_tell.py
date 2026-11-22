
# create a file first
with open("pointer.txt", "w") as f:
    f.write("Hello Python Programming")
f = open("pointer.txt", "r")
print("Initial position   :", f.tell())          # 0
print("Read 5 characters  :", f.read(5))         # Hello
print("Position after read:", f.tell())          # 5
f.seek(6)                                        # move to 6th byte
print("\nAfter seek(6)      :", f.tell())
print("Read 6 characters  :", f.read(6))         # Python
f.seek(0)                                        # back to beginning
print("\nAfter seek(0)      :", f.tell())
print("Read whole file    :", f.read())
print("Position at end    :", f.tell())          # 24
f.seek(0)
print("\nRead again after seek(0):", f.readline())
f.close()
# seek with whence value (binary mode needed for 1 and 2)
print("\n--- seek(offset, whence) in binary mode ---")
with open("pointer.txt", "rb") as b:
    b.seek(-11, 2)                               # 11 bytes before end
    print("seek(-11, 2) ->", b.tell(), b.read())
    b.seek(0)
    b.seek(6, 1)                                 # 6 bytes from current
    print("seek(6, 1)   ->", b.tell(), b.read(6))
# modify file content at a position using r+
print("\n--- Overwriting using seek ---")
with open("pointer.txt", "r+") as f:
    f.seek(6)
    f.write("JAVA  ")
    f.seek(0)
    print("New content:", f.read())