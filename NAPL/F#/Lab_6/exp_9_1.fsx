
printfn "Enter marks for Subject 1:"
let m1 = int (System.Console.ReadLine())

printfn "Enter marks for Subject 2:"
let m2 = int (System.Console.ReadLine())

printfn "Enter marks for Subject 3:"
let m3 = int (System.Console.ReadLine())

printfn "Enter marks for Subject 4:"
let m4 = int (System.Console.ReadLine())

let percentage = float (m1 + m2 + m3 + m4) / 4.0

let division =
    match percentage with
    | p when p >= 60.0 -> "First Division"
    | p when p >= 50.0 -> "Second Division"
    | p when p >= 40.0 -> "Third Division"
    | _ -> "Fail"

printfn "Percentage: %.2f%%" percentage
printfn "Division: %s" division
