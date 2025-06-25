package leetcode

// leetcode #229
func majorityElement(nums []int) []int {
	counters := make(map[int]int)
	res := make([]int, 0)

	for _, n := range nums {
		counters[n]++
		if len(counters) == 3 {
			for k := range counters {
				counters[k]--
				if counters[k] == 0 {
					delete(counters, k)
				}
			}
		}
	}
	for n := range counters {
		count := 0
		for _, num := range nums {
			if n == num {
				count++
			}
		}
		if count > len(nums)/3 {
			res = append(res, n)
		}
	}
	return res
}
