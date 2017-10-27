'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        BaseGFSClient.__init__(self)
        self.chunkSize = chunkSize
        self.chunkNum = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        if filename not in self.chunkNum:
            return
        content = ''
        for i in range(self.chunkNum[filename]):
            content += BaseGFSClient.readChunk(self, filename, i)
        return content

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        i, j, length = 0, 0, len(content)
        while j < length:
            BaseGFSClient.writeChunk(self, filename, i, content[j : j + self.chunkSize])
            i += 1
            j += self.chunkSize
        self.chunkNum[filename] = i
