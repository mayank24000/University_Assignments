
open System
open System.Text.RegularExpressions

let reverseString (text: string) =
    text |> Seq.rev |> Seq.toArray |> String

let isPalindrome (text: string) =
    let cleaned = text.ToLower().Replace(" ", "")
    cleaned = reverseString cleaned

let transformString (text: string) =
    if text.Length > 0 && text |> Seq.forall Char.IsLetter then
        text.ToUpper()
    elif text.Length > 0 && text |> Seq.forall Char.IsDigit then
        text + text
    else
        text

let isValidEmail (email: string) =
    Regex.IsMatch(email, @"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

let palindromeTests = ["madam"; "hello"; "level"]

printfn "Palindrome Tests:"
palindromeTests
|> List.iter (fun text ->
    printfn "%s -> Reversed: %s, Palindrome: %b"
        text (reverseString text) (isPalindrome text))

let transformTests = ["hello"; "123"; "hello123"]

printfn "\nString Transformation Tests:"
transformTests
|> List.iter (fun text ->
    printfn "%s -> %s" text (transformString text))

let emailTests = ["user@example.com"; "invalid-email"; "student@gmail.com"]

printfn "\nEmail Validation Tests:"
emailTests
|> List.iter (fun email ->
    printfn "%s -> Valid: %b" email (isValidEmail email))
