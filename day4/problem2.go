package main

import (
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    file, _ := os.ReadFile("input.txt")
    lines := string(file)
    count := 0

    for _, line := range strings.Split(lines, "\n") {
        x := strings.Split(line, ",")
        x0 := strings.Split(x[0], "-")
        x1 := strings.Split(x[1], "-")

        var pair [2][2]int
        pair[0][0], _ = strconv.Atoi(x0[0])
        pair[0][1], _ = strconv.Atoi(x0[1])
        pair[1][0], _ = strconv.Atoi(x1[0])
        pair[1][1], _ = strconv.Atoi(x1[1])

        if pair[0][0] > pair[1][0] {
            pair[0], pair[1] = pair[1], pair[0]
        }
        if pair[0][1] >= pair[1][0] {
            count++
        }
    }

    fmt.Println(count)
}