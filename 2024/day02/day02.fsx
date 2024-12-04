let inputs = System.IO.File.ReadLines("input.txt")
let mutable part1count = 0
let mutable part2count = 0


for line in inputs do
    let report = line.Split(" ") |> Array.map int

    let is_safe report =
        let diff = report |> Array.skip 1 |> Array.mapi (fun index value -> value - report[index])
        let increasing = diff |> Seq.forall (fun num -> num < 0)
        let decreasing = diff |> Seq.forall (fun num -> num > 0)

        if increasing || decreasing then
            let abso = diff |> Array.map abs
            if abso |> Array.exists (fun num -> num > 3) then
                false
            else
                true
        else
            false

    if is_safe report then 
        part1count <- part1count + 1
        part2count <- part2count + 1
    else
        let mutable new_report = report
        let rec recurse i =
            if not(i = report.Length) then
                let new_report = report |> Array.removeAt i
                if is_safe new_report then
                    part2count <- part2count + 1
                else
                    recurse (i + 1)
        
        recurse 0

printfn "The number of safe levels in part 1: %i" part1count
printfn "The number of safe levels in part 2: %i" part2count