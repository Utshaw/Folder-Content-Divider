import os, math

def getAnnotatedSubDirectory(folderName, folderNumber):
  """Add a suffix at the end of the folderName
    :param folderName: Folder which is to be annotated
    :type folderName: str
    :param folderNumber: Number which is to be added at the end of the folderName
    :type folderNumber: int
  """

  return folderName + "_" + str(folderNumber)




def createDirectoryWithSanityCheck(dirName):
    """Check if any directory named as dirName exists if no then dirName directory is created
    :param dirName: Directory which needs to be created
    :type dirName: str
    """

    if not os.path.exists(dirName):
        os.mkdir(dirName)



def getTotalNumberOfSubdirectories(totalNumberOfFiles, numberOfFilesPerSubDir):
    """Returns total number of sub-directories that will be created
    :param totalNumberOfFiles: Total number of files inside the Root directory
    :type totalNumberOfFiles: int
    :param numberOfFilesPerSubDir: Number of files that each sub-directory will contain
    :type numberOfFilesPerSubDir: int
    """

    decimalPart, integerPart = math.modf(totalNumberOfFiles / numberOfFilesPerSubDir)
    retValue = 0
    if decimalPart > 0:
        retValue += 1
    return int(retValue + integerPart) 




def divideFolderContents(rootFolderName, numberOfFilesPerSubDir=100):
  """Divide all files inside rootFolder into groups and each group is placed inside a sub-folder
    :param rootFolderName: The root folder under which the files to be divided are placed
    :type rootFolderName: str
    :param numberOfFilesPerSubDir: Number of files each sub directory will contain
    :type numberOfFilesPerSubDir: int
  """


  os.chdir(rootFolderName)
  filenames = next(os.walk(os.getcwd()))[2]
  totalNumberOfFiles = len(next(os.walk(os.getcwd()))[2])
  print()
  print('Folder content divider starting......')
  print('Current Directory: ' +   str(os.getcwd()))
  print('----------------------------------------------------------------------------------')
  print('Total number of files: '  +  str(totalNumberOfFiles))
  print('Number of sub-directories going to be created: ' + str(getTotalNumberOfSubdirectories(totalNumberOfFiles , numberOfFilesPerSubDir)))
  print('Number of files in each directory(except last one): ' + str(numberOfFilesPerSubDir))
  print('Number of files in the last sub-directory: ' + str(totalNumberOfFiles % numberOfFilesPerSubDir))
  print('----------------------------------------------------------------------------------')
  totalSubDirectories = math.floor(totalNumberOfFiles / numberOfFilesPerSubDir)
  subDirectories = []

  for i in range(0, totalSubDirectories):
    new_dir = getAnnotatedSubDirectory(rootFolderName, i + 1)

    createDirectoryWithSanityCheck(new_dir)

    subDirectories.append(new_dir)
    for j in range(0, numberOfFilesPerSubDir):
      currentIndex = i * numberOfFilesPerSubDir + j
      newLocation = os.path.join(new_dir, filenames[currentIndex])
      os.rename(filenames[currentIndex], newLocation)
      print(filenames[currentIndex] + ' is moving to ' + newLocation)
  
  new_dir = getAnnotatedSubDirectory(rootFolderName, totalSubDirectories + 1)
  createDirectoryWithSanityCheck(new_dir)
  subDirectories.append(new_dir)

  for k in range(0 ,  totalNumberOfFiles % numberOfFilesPerSubDir):
  
    currentIndex  =  totalSubDirectories * numberOfFilesPerSubDir + k
    newLocation = os.path.join(new_dir, filenames[currentIndex])
    os.rename(filenames[currentIndex], newLocation)
    print(filenames[currentIndex] + ' is moving to ' + newLocation)


  print()
  print('Result: ')

  for subDirectory in subDirectories:
      totalFilesInsideThisSubDirectory = len(next(os.walk(subDirectory))[2])
      print('Number of files inside ' + subDirectory + " = " + str(totalFilesInsideThisSubDirectory))
  if len(subDirectories) > 0 :
    print('All required sub directories are created!')
  else:
    print('No sub directory could be created!')

  print('Program exiting......')





if __name__ == '__main__':  
  divideFolderContents('dummy', 100)

