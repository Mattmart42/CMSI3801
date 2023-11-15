package main

import (
	"fmt"
)

func main() {
	fib := fibonacci()
	for x := 0; x < 10; x++ {
		fmt.Println(fib())
	}
}

func fibonacci() func() int {
	a, b := 0, 1
	return func() int {
		result := a
		a, b = b, a+b
		return result
	}
}
