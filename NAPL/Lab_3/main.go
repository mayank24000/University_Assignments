package main
import "fmt"

func modval(x *int){
	*x = 25
}

type Student struct{
	Name string
	Marks float32
	Age int
}

 func main(){
// 1
	x:= 15
	y:= &x
	*y =20
	fmt.Println("Address", y)
	fmt.Println("Access Val: ",x)
// 2
	var n int =24
	fmt.Println("Before: ",n)
	modval(&n)
	fmt.Println("After: ",n)
// 3
	s := new(Student)
	fmt.Println("Values before modifying: ", *s)
	s.Name = "Mayank"
	s.Marks = 85.5
	s.Age = 20
	fmt.Println("After modifying",*s)
}


