module AOC23D1 where
import Data.Char

intFilterer :: [String] -> Int
intFilterer [] = 0
intFilterer (x:xs) = number + intFilterer xs
    where
        onlyInts = findInts x
        number = firstAndLast onlyInts

firstAndLast :: [Char] -> Int
firstAndLast s = read (first : last : "")
    where 
        first = head s
        last = head $ reverse s 

findInts :: [Char] -> [Char]
findInts [] = []
findInts (x:xs) = if isDigit x
    then x : findInts xs
    else findInts xs

main :: IO()
main = do
    content <- readFile "input.txt"
    putStrLn $ show $ intFilterer $ lines content