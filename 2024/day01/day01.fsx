open System.IO

let list1: string list = File.ReadAllText(".//list-1.txt").Split '\n' |> Seq.toList
let list2: string list = File.ReadAllText(".//list-2.txt").Split '\n' |> Seq.toList

let sorted1: int list = list1 |> List.map int |> List.sort
let sorted2: int list = list2 |> List.map int |> List.sort

let sumOfdifference (a: int list) (b: int list) =
    let mutable sum: int = 0
    for num1, num2 in List.zip a b do
        let difference: int = abs (num1 - num2)
        sum <- sum + difference
    sum

let howMany pred = Seq.filter pred >> Seq.length

let similarity (a: int list) (b: int list) =
    let mutable score: list<int> = list.Empty
    for num1 in a do
        let count: int = b |> howMany (fun n -> n = num1)
        score <- [num1 * count] |> List.append score
    Seq.sum score

printfn "The total distance between lists is: %i" (sumOfdifference sorted1 sorted2)
printfn "The similarity score between lists is: %i" (similarity sorted1 sorted2)

