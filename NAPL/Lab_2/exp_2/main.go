
package main

import (
	"fmt"
	"exp2/myutils"
)

func main() {
	fmt.Println("===== CUSTOM GO PACKAGE DEMONSTRATION =====")

	// 1. String Reverse
	text := "Cybersecurity"
	fmt.Println("\nOriginal String:", text)
	fmt.Println("Reversed String:", myutils.Reverse(text))

	// 2. Count Vowels
	fmt.Println("\nString:", text)
	fmt.Println("Number of Vowels:", myutils.CountVowels(text))

	// 3. Factorial
	num := 5
	fmt.Println("\nNumber:", num)
	fmt.Println("Factorial:", myutils.Factorial(num))

	// 4. Power
	base := 2
	exponent := 4
	fmt.Printf("\n%d raised to %d = %d\n",
		base, exponent, myutils.Power(base, exponent))

	fmt.Println("\n===== PROGRAM EXECUTED SUCCESSFULLY =====")
}
