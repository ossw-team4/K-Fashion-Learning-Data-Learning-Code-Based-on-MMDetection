import zipfile
import os

# zip파일을 정해진 경로에 위치
# /data/clothes 생성
extension = ".zip"

zip_name=""
for item in os.listdir("data/clothes"):
    if item.endswith(extension):
        zip_name = item
        break


with zipfile.ZipFile("data/clothes/" + zip_name, 'r') as zip_ref:
    zip_ref.extractall("data")

path_first = os.getcwd() + "/data"
path_second = "data/clothes"
#os.mkdir(data)
os.chdir("./data")


for item in os.listdir(path_first):
     if item.endswith(extension):
        created_file = item[:-3]
        os.mkdir(created_file)
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        os.chdir("./" + created_file)
        zip_ref.extractall(created_file) # extract file to dir
        zip_ref.close() # close file
        os.chdir("../")


