import os
import hashlib

paths = os.listdir('C:\\Users\\Sebastiaan\\Desktop\\testpath')

# print(paths)

initial_list = ["test", ]

hash_list = []

for x in paths:
    print(x)
    with open(x, 'rb') as file_to_check:
        # read contents of the file
        data = file_to_check.read()
        # pipe contents of the file through
        md5_returned = hashlib.md5(data).hexdigest()
        initial_list.append(md5_returned)
        print(md5_returned)

print(initial_list)

for x in paths:
    print(x)
    with open(x, 'rb') as file_to_check:
        # read contents of the file
        data = file_to_check.read()
        # pipe contents of the file through
        md5_returned = hashlib.md5(data).hexdigest()
        hash_list.append(md5_returned)
        print(md5_returned)

print(hash_list)



if initial_list[0] == hash_list[0]:
    print('All good')
else:
    print('Something is wrong')

# https://stackoverflow.com/questions/16874598/how-to-calculate-the-md5-checksum-of-a-file-in-python
# https://docs.python.org/3.3/library/hashlib.html

# hash = hashlib.md5(b"Nobody inspects the spammish repetition").hexdigest()
# print(hash)

# Open,close, read file and calculate MD5 on its contents
# with open("file1.txt", 'rb') as file_to_check:
#     # read contents of the file
#     data = file_to_check.read()
#     # pipe contents of the file through
#     md5_returned = hashlib.md5(data).hexdigest()
#     print(md5_returned)

