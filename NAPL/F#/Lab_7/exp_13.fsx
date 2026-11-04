let task1 = async {
    printfn "Task 1 Started"
    do! Async.Sleep(3000)
    printfn "Task 1 Completed"
    return "Task 1 Result"
}

let task2 = async {
    printfn "Task 2 Started"
    do! Async.Sleep(2000)
    printfn "Task 2 Completed"
    return "Task 2 Result"
}

let task3 = async {
    printfn "Task 3 Started"
    do! Async.Sleep(1000)
    printfn "Task 3 Completed"
    return "Task 3 Result"
}

printfn "Starting all tasks..."

let results =
    [task1; task2; task3]
    |> Async.Parallel
    |> Async.RunSynchronously

printfn "\nAll tasks completed!"
printfn "Results:"

results |> Array.iter (printfn "%s")
