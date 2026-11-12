
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Person structure
type Person struct {
	Name   string
	Age    int
	Job    string
	Salary float64
}

func (p *Person) ReadData(reader *bufio.Reader) {
	fmt.Print("Enter Name: ")
	p.Name, _ = reader.ReadString('\n')
	p.Name = strings.TrimSpace(p.Name)

	fmt.Print("Enter Age: ")
	ageInput, _ := reader.ReadString('\n')
	p.Age, _ = strconv.Atoi(strings.TrimSpace(ageInput))

	fmt.Print("Enter Job: ")
	p.Job, _ = reader.ReadString('\n')
	p.Job = strings.TrimSpace(p.Job)

	fmt.Print("Enter Salary: ")
	salaryInput, _ := reader.ReadString('\n')
	p.Salary, _ = strconv.ParseFloat(strings.TrimSpace(salaryInput), 64)
}


func (p Person) PrintData() {
	fmt.Println("\n----- Person Details -----")
	fmt.Println("Name   :", p.Name)
	fmt.Println("Age    :", p.Age)
	fmt.Println("Job    :", p.Job)
	fmt.Printf("Salary : Rs. %.2f\n", p.Salary)
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	var person1, person2 Person

	fmt.Println("Enter details for Person 1:")
	person1.ReadData(reader)
	person1.PrintData()

	fmt.Println("\nEnter details for Person 2:")
	person2.ReadData(reader)
	person2.PrintData()

	fmt.Println("\n===== PROGRAM EXECUTED SUCCESSFULLY =====")
}
