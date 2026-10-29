
package main

import "testing"

func TestSafeDivideValidInput(t *testing.T) {
	result, err := SafeDivide(10, 2)

	if err != nil {
		t.Fatal(err)
	}

	if result != 5 {
		t.Errorf("expected 5, got %v", result)
	}
}

func TestSafeDivideByZero(t *testing.T) {
	_, err := SafeDivide(10, 0)

	if err == nil {
		t.Fatal("expected division by zero error")
	}
}

func TestSafeSqrtValidInput(t *testing.T) {
	result, err := SafeSqrt(25)

	if err != nil {
		t.Fatal(err)
	}

	if result != 5 {
		t.Errorf("expected 5, got %v", result)
	}
}

func TestSafeSqrtNegativeInput(t *testing.T) {
	_, err := SafeSqrt(-4)

	if err == nil {
		t.Fatal("expected negative square root error")
	}
}

func TestValidateInputValidInput(t *testing.T) {
	result, err := ValidateInput("Hello Go")

	if err != nil {
		t.Fatal(err)
	}

	if result != "Hello Go" {
		t.Errorf("expected Hello Go, got %v", result)
	}
}

func TestValidateInputEmpty(t *testing.T) {
	_, err := ValidateInput(" ")

	if err == nil {
		t.Fatal("expected empty input error")
	}
}
