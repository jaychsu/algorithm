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
        self.chunk_size = chunkSize
        self.chunk_num = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        if filename not in self.chunk_num:
            return
        i, content = 0, ''
        while i < self.chunk_num[filename]:
            content += self.readChunk(filename, i)
            i += 1
        return content

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        i, j, n = 0, 0, len(content)
        while j < n:
            self.writeChunk(filename, i, content[j : j + self.chunk_size])
            i += 1
            j += self.chunk_size
        self.chunk_num[filename] = i
