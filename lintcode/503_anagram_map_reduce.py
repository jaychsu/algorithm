class Anagram:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        for word in line.split():
            yield ''.join(sorted(word.lower())), word

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        yield key, values
