import src.trie as tlc
import pytest

@pytest.fixture
def trie_with_words():
    trie = tlc.Trie()
    trie.insert("apple")
    trie.insert("app")
    return trie

@pytest.mark.parametrize('word, result',
                         [('apple', True),
                          ('aple', False),
                          ('appel', False),
                          ('app', True),
                          ('appp', False),
                         ])
def test_trie_search(word, result, trie_with_words):
    t = trie_with_words
    assert t.search(word) == result

@pytest.mark.parametrize('prefix, result',
                         [('apple', True),
                          ('aple', False),
                          ('appel', False),
                          ('app', True),
                          ('appp', False),
                          ])
def test_trie_startswith(prefix, result, trie_with_words):
    t = trie_with_words
    assert t.startsWith(prefix) == result
