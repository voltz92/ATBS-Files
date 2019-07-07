import os

# os.mkdir('Python-made')
# os.mkdir('Spam')

os.chdir('D:\\AUST\\')

#print('The Current Directory is :: ' + os.getcwd())
for folderName, subFolders, files in os.walk(os.getcwd()):
    print('The current directory is :: '+ folderName)
    print('The folders inside it are :: '+  '\n>>'.join(subFolders))
    print('It contains the files :: ' + '\n>>'.join(files))
