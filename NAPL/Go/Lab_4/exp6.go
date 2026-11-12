package main

import (
	"fmt"
	"sync"
	"time"
)

// Function to calculate squares
func calculateSquares(ch chan string, wg *sync.WaitGroup) {
	defer wg.Done()

	fmt.Println("[Goroutine 1] Started: Calculating Squares")
	time.Sleep(2 * time.Second)

	result := 5 * 5

	ch <- fmt.Sprintf("Square of 5 = %d", result)

	fmt.Println("[Goroutine 1] Completed")
}

// Function to calculate cubes
func calculateCubes(ch chan string, wg *sync.WaitGroup) {
	defer wg.Done()

	fmt.Println("[Goroutine 2] Started: Calculating Cubes")
	time.Sleep(1 * time.Second)

	result := 3 * 3 * 3

	ch <- fmt.Sprintf("Cube of 3 = %d", result)

	fmt.Println("[Goroutine 2] Completed")
}

// Function to calculate Fibonacci numbers
func calculateFibonacci(ch chan string, wg *sync.WaitGroup) {
	defer wg.Done()

	fmt.Println("[Goroutine 3] Started: Calculating Fibonacci")

	a, b := 0, 1
	fibonacci := []int{a, b}

	for i := 2; i < 8; i++ {
		a, b = b, a+b
		fibonacci = append(fibonacci, b)
	}

	ch <- fmt.Sprintf("Fibonacci Series = %v", fibonacci)

	fmt.Println("[Goroutine 3] Completed")
}

func main() {
	fmt.Println("===== GOROUTINES AND CHANNELS DEMONSTRATION =====")

	// Create channel
	ch := make(chan string, 3)

	// Create WaitGroup
	var wg sync.WaitGroup
	wg.Add(3)

	fmt.Println("\nLaunching three goroutines...")

	// Launch goroutines concurrently
	go calculateSquares(ch, &wg)
	go calculateCubes(ch, &wg)
	go calculateFibonacci(ch, &wg)

	// Wait for all goroutines to finish
	wg.Wait()

	// Close channel after completion
	close(ch)

	// Collect and print results
	fmt.Println("\n===== RESULTS RECEIVED IN MAIN =====")

	for result := range ch {
		fmt.Println(result)
	}

	fmt.Println("\n===== ALL TASKS COMPLETED SUCCESSFULLY =====")
}
