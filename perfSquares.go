package main

import (
	"fmt"
)

func perfSquares(num int) {
	var result []int
	count := 0
	for count < num {
		roots := 1
		for roots < count {
			if count/roots == roots && count%roots == 0 {
				result = append(result, count)
				break
			}
			roots++
		}
		count++
	}
	fmt.Println(result)
}

func main() {
	perfSquares(900)
}
