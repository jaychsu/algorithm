"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
"""


class Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    This method will be invoked first, you should design your own algorithm
    to serialize a trie which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    '''
    For `<a<b<e<>>c<>d<f<>>>>`, the visual graph of the return data just like this:
        <
          a<
            b<
              e<>
            >
            c<>
            d<
              f<>
            >
          >
        >
    '''
    def serialize(self, root):
        if not root:
            return ''
        data = ''
        for key, node in root.children.items():
            data += key + self.serialize(node)
        return '<%s>' % data

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    def deserialize(self, data):
        if not data \
                or data[0] != '<' \
                or data[-1] != '>' \
                or len(data) < 1:
            return
        root = TrieNode()
        current = root
        queue = []
        for char in data:
            if char == '<':
                queue.append(current)
            elif char == '>':
                queue.pop()
            else:
                current = TrieNode()
                queue[-1].children[char] = current
        return root
