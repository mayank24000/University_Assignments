
package main

import (
	"fmt"
	"math"
	"strings"
)

func SafeDivide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, fmt.Errorf("cannot divide by zero")
	}
	return a / b, nil
}

func SafeSqrt(n float64) (float64, error) {
	if n < 0 {
		return 0, fmt.Errorf("cannot calculate square root of a negative number")
	}
	return math.Sqrt(n), nil
}

func ValidateInput(input string) (string, error) {
	if strings.TrimSpace(input) == "" {
		return "", fmt.Errorf("input cannot be empty")
	}
	return input, nil
}

func main() {
	result, err := SafeDivide(10, 2)
	fmt.Println(result, err)

	root, err := SafeSqrt(25)
	fmt.Println(root, err)

	input, err := ValidateInput("Hello Go")
	fmt.Println(input, err)
}
