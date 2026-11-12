package main
import "fmt"

func main(){
	var num1 int = 2
	var num2 int = 9
	var float1 float32 = 4.9
	var float2 float32 = 9.6
	fmt.Println("Add", num1+num2)
	fmt.Println("Subtract", num2-num1)
	fmt.Println("Multiply", num1*num2)
	fmt.Println("Add Flaot: ", float1+float2)
	fmt.Println("Subtract Flaot: ", float1-float2)
	fmt.Println("Multiply Flaot: ", float1*float2)
}