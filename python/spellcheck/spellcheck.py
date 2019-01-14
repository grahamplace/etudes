import Levenshtein as lv

class Node:
    def __init__(self, c: str, prefix: str):
        self.c = c
        self.seen_str = prefix + c
        self.children = {}
        self.word_end_count = 0

    def add_word(self, word: str):
        first_char = word[0]
        if not first_char in self.children:
            self.children[first_char] = Node(first_char, self.seen_str)

        next_node = self.children[first_char]
        if len(word) == 1:
            next_node.word_end_count += 1
        else:
            next_node.add_word(word[1:])

    def lookup(self, word: str):
        # base case, word is one character
        if len(word) == 1:
            if word[0] not in self.children:
                return (False, self)
            elif self.children[word[0]].word_end_count > 0:
                return (True, self.children[word[0]])
            else: # match, but not a terminal word
                return (False, self)
        else:
            if word[0] not in self.children:
                return (False, self)
            else:
                return self.children[word[0]].lookup(word[1:])

    def suggest(self, word: str, options: set):
        if lv.distance(word, self.seen_str) > SENSITIVITY:
            return options

        if lv.distance(word, self.seen_str) <= SENSITIVITY and self.word_end_count > 0:
            options.add(self.seen_str)

        # handles base case: node w/o children
        for child in self.children.values():
            options.update(child.suggest(word, options))

        return options


class Trie:
    def __init__(self):
        self.root = Node('', '')

    def add_word(self, word: str):
        self.root.add_word(word)

    def lookup(self, word: str):
        return self.root.lookup(word)

    def get_all_suggestions(self, word: str):
        lookup_result = self.lookup(word)
        if lookup_result[0]:  # exact match case
            return [lookup_result[1].seen_str]
        else:  # edit distance limited search from closest word found during looking
            return lookup_result[1].suggest(word, set())

    def select_best_suggestion(self, word, suggestions: list):
        if len(suggestions) == 0:
            return word

        min_dist = SENSITIVITY + 1
        best_str = word
        dists = {sug: lv.distance(word, sug) for sug in suggestions}
        return sorted(sorted(dists, key=dists.get))[0]

    def suggest(self, word: str):
        options = self.get_all_suggestions(word)
        selection = self.select_best_suggestion(word, options)
        return selection


def load_corpus(filename: str):
    with open(CORPUS_FILE) as f:
        lines = list(f)

    for line in lines:
        line = line.replace('\n', '')
        CORPUS_DICT[line] = CORPUS_DICT.get(line, 0) + 1

    for word in CORPUS_DICT.keys():
        CORPUS_TRIE.add_word(word)


def run_tests():
    # Try adding a word and looking it up
    t = Trie()
    t.add_word('test')
    assert t.lookup('test')[0]

    # Words we haven't added shouldn't return true for lookup
    assert not t.lookup('tes')[0]
    assert not t.lookup('test1')[0]

    # Adding a new word shouldn't have side effects on previously added words
    t.add_word('testagain')
    assert t.lookup('test')[0]
    assert t.lookup('testagain')[0]

    # get_all_suggestions() should return just the word if it is in the corpus
    assert CORPUS_TRIE.get_all_suggestions('test') == ['test']

    # get_all_suggestions() should return many results for words not in the corpus
    assert len(CORPUS_TRIE.get_all_suggestions('testl')) > 1

    # get_all_suggestions() is biased towards prefix correctness, so get_all_suggestions('testl') should suggest 'test'
    assert 'test' in CORPUS_TRIE.get_all_suggestions('testl')

    # suggest() should return only one string
    assert CORPUS_TRIE.suggest('testl') == 'test', f"Expected 'test', got {CORPUS_TRIE.suggest('testl')}"

    # suggest() should return the word if no suggestion can be made
    bad_str = 'kdjhfgkhjsdgfjhkgsdf'
    assert CORPUS_TRIE.suggest(bad_str) == bad_str


if __name__ == '__main__':
    CORPUS_FILE = 'corpus.txt'
    CORPUS_DICT = {}
    CORPUS_TRIE = Trie()
    SENSITIVITY = 4  # limit suggestions to words within N edit distance

    load_corpus(CORPUS_FILE)
    run_tests()

    while True:
        word = input('Enter a word to search: ').lower()
        if len(word) < 1:
            continue
        elif word == 'quit()':
            print('Goodbye!')
            break
        print(f'Suggestion: {CORPUS_TRIE.suggest(word)}\n')
