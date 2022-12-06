package main

import (
    "fmt"
    "os"
)

func main() {
    file, _ := os.ReadFile("input.txt")
    line := string(file)

    for i := 14; i < len(line); i++ {
        if len(unique(line[i-14:i])) == 14 {
            fmt.Println(i)
            return
        }
    }
}

func unique(s string) map[rune]struct{} {
    chars := map[rune]struct{}{}
    for _, c := range s {
        chars[c] = struct{}{}
    }
    return chars
}