package leetcode

type childMap map[rune]*trieNode

type trieNode struct {
	children childMap
	isEnd    bool
}

type Trie struct {
	root *trieNode
}

func newTrieNode() *trieNode {
	return &trieNode{
		children: make(childMap),
		isEnd:    false,
	}
}
func Constructor() Trie {
	return Trie{
		root: &trieNode{
			children: make(childMap),
			isEnd:    false,
		},
	}
}

func (t *Trie) Insert(word string) {
	n := t.root

	for _, r := range []rune(word) {
		if _, ok := n.children[r]; !ok {
			n.children[r] = newTrieNode()
		}
		n = n.children[r]
	}
	n.isEnd = true
}

func (t *Trie) Search(word string) bool {
	n := t.root

	for _, r := range []rune(word) {
		if _, ok := n.children[r]; !ok {
			return false
		}
		n = n.children[r]
	}
	return n.isEnd == true
}

func (t *Trie) StartsWith(prefix string) bool {
	n := t.root

	for _, r := range []rune(prefix) {
		if _, ok := n.children[r]; !ok {
			return false
		}
		n = n.children[r]
	}
	return true
}
