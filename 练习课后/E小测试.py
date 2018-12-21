import os
import glob

# 输出根目录下的所有文件及文件夹
# 1
# path = os.listdir('.')
path = os.listdir(os.getcwd())
print(path)
# 2
path2 = os.listdir("D:/E")
print(path2)


# 删除子目录
# os.rmdir('lol')


# folders location
path = r'D:\E\wegame\lol'
def delfile(path):
    #   read all the files under the folder
    fileNames = glob.glob(path + r'\*')

    for fileName in fileNames:
        try:
            #           delete file
            os.remove(fileName)
        except:
            try:
                #               delete empty folders
                os.rmdir(fileName)
            except:
                #               Not empty, delete files under folders
                delfile(fileName)
                #               now, folders are empty, delete it
                os.rmdir(fileName)
delfile(path)


# def del_files(path):
#   for root , dirs, files in os.walk(path):
#     for name in files:
#       if name.endswith(".CR2"):
#         os.remove(os.path.join(root, name))
#         print ("Delete File: " + os.path.join(root, name))
# # test
# if __name__ == "__main__":
#   path = '/Users/yjatt/Downloads/1104/'
#   del_files(path)
