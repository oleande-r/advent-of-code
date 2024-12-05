// regex: mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)
let inputs = System.IO.File.ReadLines("matches.txt")

let sumOfmulti instructions =
    let mutable products = List.empty
    let mutable flag = true
    
    for line: string in instructions do
        if line.Contains "do()" then
            flag <- true
        elif line.Contains "don't()" then
            flag <- false 
        else
            if flag then
                let instruct: string array = line.Split([|'('; ',';')'|])
                products <- List.append products [int instruct[1] * int instruct[2]]
            else
                ()
    
    products |> List.sum

printfn "%i" (sumOfmulti inputs)