class Activity:
    def __init__(self, filePath, fileOperation):
        self.filePath = filePath
        self.fileOperation = fileOperation

    def getFilePath(self):
        return self.filePath

    def getFileOperation(self):
        return self.fileOperation

    def __str__(self):
        operationString = self.getFileOperation()
        if operationString == "Extracted":
            operationString += " "
        return operationString + "\t|\t" + self.getFilePath()
