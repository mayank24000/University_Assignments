printfn "\n===== STUDENT MANAGEMENT ASSIGNMENT ====="

type Gender =
    | Male
    | Female
    | Other

type Student = {
    Id: int
    Name: string
    Age: int
    Course: string
    Gender: Gender
}

let seedStudents = [
    { Id = 1; Name = "Mayank"; Age = 21; Course = "Cybersecurity"; Gender = Male }
    { Id = 2; Name = "Abhijeet"; Age = 31; Course = "Computer Science"; Gender = Female }
    { Id = 3; Name = "Tappu"; Age = 25; Course = "Information Technology"; Gender = Male }
]

// Higher-order functions: map and filter
let getAdultStudents students =
    students |> List.filter (fun s -> s.Age >= 18)

let getStudentNames students =
    students |> List.map (fun s -> s.Name)

let categorizeByCourse students =
    students |> List.groupBy (fun s -> s.Course)

let getStudentsByCourse course students =
    students |> List.filter (fun s -> s.Course = course)

// Pattern matching
let describeGender gender =
    match gender with
    | Male -> "Male"
    | Female -> "Female"
    | Other -> "Other"

let displayStudentDetails student =
    match student with
    | { Name = name; Age = age; Course = course; Gender = gender } ->
        printfn "Name: %s, Age: %d, Course: %s, Gender: %s" name age course (describeGender gender)

let gradeAge age =
    match age with
    | age when age < 18 -> "Minor"
    | age when age <= 25 -> "Young Adult"
    | _ -> "Adult"

printfn "\n--- Higher-Order Functions & Pattern Matching Demo ---"

let adultStudents = getAdultStudents seedStudents
printfn "\nAdult students (>=18):"
adultStudents |> List.iter displayStudentDetails

let names = getStudentNames seedStudents
printfn "\nStudent names: %A" names

let byCourse = categorizeByCourse seedStudents
printfn "\nStudents grouped by course:"
byCourse |> List.iter (fun (course, students) ->
    printfn "  %s: %A" course (students |> List.map (fun s -> s.Name)))

let csStudents = getStudentsByCourse "Computer Science" seedStudents
printfn "\nComputer Science students:"
csStudents |> List.iter displayStudentDetails

printfn "\nAge categories (pattern matching):"
seedStudents |> List.iter (fun s -> printfn "  %s -> %s" s.Name (gradeAge s.Age))

printfn "\n===== DONE ====="
