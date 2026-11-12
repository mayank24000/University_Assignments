
package myutils

import "strings"

// Reverse reverses a given string
func Reverse(str string) string {
	runes := []rune(str)

	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	return string(runes)
}

// CountVowels counts vowels in a string
func CountVowels(str string) int {
	count := 0
	str = strings.ToLower(str)

	for _, ch := range str {
		if strings.ContainsRune("aeiou", ch) {
			count++
		}
	}

	return count
}

// Factorial calculates the factorial of a number
func Factorial(n int) int {
	if n < 0 {
		return -1
	}

	result := 1
	for i := 2; i <= n; i++ {
		result *= i
	}

	return result
}

// Power calculates base raised to exponent
func Power(base, exponent int) int {
	result := 1

	for i := 0; i < exponent; i++ {
		result *= base
	}

	return result
}
