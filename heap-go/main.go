package main

import (
	"container/heap"
	"fmt"
)

type ItemClicks struct {
	ItemName  string
	NumClicks int
}

type ItemsClicks []ItemClicks

func (ic ItemsClicks) Len() int { return len(ic) }

// Less implements heap.Interface.
func (ic ItemsClicks) Less(i int, j int) bool { return ic[i].NumClicks > ic[j].NumClicks }

// Swap implements heap.Interface.
func (ic ItemsClicks) Swap(i int, j int) { ic[i], ic[j] = ic[j], ic[i] }

// Pop implements heap.Interface.
func (ic *ItemsClicks) Pop() any {
	last := len(*ic) - 1
	minItem := (*ic)[last]
	*ic = (*ic)[0:last]
	return minItem
}

// Push implements heap.Interface.
func (ic *ItemsClicks) Push(x any) {
	*ic = append(*ic, x.(ItemClicks))
}

func main() {
	items := &ItemsClicks{
		{
			ItemName:  "belt",
			NumClicks: 4,
		},
		{
			ItemName:  "lamp",
			NumClicks: 12,
		},
		{
			ItemName:  "statue",
			NumClicks: 7,
		},
		{
			ItemName:  "table",
			NumClicks: 3,
		},
	}
	item := ItemClicks{
		ItemName:  "flower",
		NumClicks: 9,
	}
	heap.Init(items)

	heap.Push(items, item)
	for items.Len() > 0 {
		fmt.Println(heap.Pop(items))
	}
}
