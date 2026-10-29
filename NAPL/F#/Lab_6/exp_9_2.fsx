
let isPrime n =
    if n < 2 then
        false
    else
        let rec check divisor =
            if divisor * divisor > n then
                true
            elif n % divisor = 0 then
                false
            else
                check (divisor + 1)
        check 2

let testNumbers = [2; 7; 10]

testNumbers
|> List.iter (fun n ->
    printfn "%d is prime: %b" n (isPrime n))

printfn "Enter an integer:"
let number = int (System.Console.ReadLine())

if isPrime number then
    printfn "%d is a prime number" number
else
    printfn "%d is not a prime number" number
