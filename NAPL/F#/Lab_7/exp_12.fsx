let list1 = [1; 2; 3; 4; 5]
let list2 = [2; 4; 6; 8; 10]

let result1 = List.map (fun x -> x * x) list1
let result2 = List.map (fun x -> x * x) list2

printfn "List.map - Square"
printfn "%A" result1
printfn "%A" result2

let result3 = List.filter (fun x -> x % 2 = 0) list1
let result4 = List.filter (fun x -> x % 2 = 0) list2

printfn "\nList.filter - Even Numbers"
printfn "%A" result3
printfn "%A" result4

let result5 = List.fold (fun a b -> a + b) 0 list1
let result6 = List.fold (fun a b -> a + b) 0 list2

printfn "\nList.fold - Sum"
printfn "%d" result5
printfn "%d" result6
