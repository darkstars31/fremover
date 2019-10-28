
import glob
from pathlib import Path

filesCount = 0
replacements = 0
lineCount = 0

def readFileLines(file):
    try:
        fileRead = open (file, 'r') 
        lines = fileRead.readlines()
        fileRead.close()
        return lines
    except:
        return


def detectSpecificStringInFile(file):
    removeFileFlag = False;
    lines = readFileLines(file);
    try:
        for line in lines:
            if line.find("fit(") != -1 or line.find("fdescribe(") != -1:
                removeFileFlag = True
    except:
        return removeFileFlag
    return removeFileFlag

def removeFs(line):
    global lineCount
    global replacements
    lineCount += 1
    if line.find("fit(") != -1:      
        line = line.replace("fit(","it(",1)    
        replacements += 1   
    elif line.find("fdescribe(") != -1:         
        line = line.replace("fdescribe(","describe(",1)
        replacements += 1 
    return line

def getTestFiles():
    files = []
    fileNamesToSearchFor = ["*test*.js","*.spec.ts","**/*test*.js","**/*.spec.ts"]
    for filesSearch in fileNamesToSearchFor:
        for filename in glob.glob(filesSearch,recursive=True):
            if filename.find("node_modules") == -1: 
                files.append(filename)   
    return files

def interactWithFile(file):
    
        lines = readFileLines(file)

        fileWrite = open(file, 'w')
        lineNumber = 0
        for line in lines:
            tempLine = line
            lineNumber += 1
            line = removeFs(line)
            if len(line) != len(tempLine): print("Removed from "+ file +" at line "+ str(lineNumber) + ": "+ line)
            fileWrite.write(line)
        fileWrite.close()


print("*** Tony's F Remover - version .1 ***")
print("*** No more wasted time and builds because you forgot to remove that f in your tests. ***")
files = getTestFiles()
# for file in files:
#     if detectSpecificStringInFile(file) == False:
#         files.remove(file)
print(str(len(files)) +" Files Located")
for file in files:
    interactWithFile(file)

print("Lines Checked: "+ str(lineCount) )
print("Lines Replaced: "+ str(replacements))
