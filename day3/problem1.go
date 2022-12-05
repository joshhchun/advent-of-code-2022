package main

import (
	"os"
	"strings"
	"sync"
	"time"
)

func main() {
    data, _ := os.ReadFile("input.txt")
    rucksacks := strings.Split(string(data), "\n")
    common := make(chan rune, len(rucksacks))

    var wg sync.WaitGroup
    wg.Add(len(rucksacks))

    for _, rucksack := range rucksacks {
        go func(r string) {
            intersection(r[:len(r)/2], r[len(r)/2:], common)
            wg.Done()
        }(rucksack)
    }

		wg.Wait()
		close(common)

    total := 0
    for let := range common {
        total += computePriority(let)
    }

    println(total)
}

func intersection(a string, b string, common chan<- rune) {
    m1 := map[rune]struct{}{}
    for _, item := range a {
        m1[item] = struct{}{}
    }

    for _, item := range b {
        if _, exist := m1[item]; exist {
            common <- item
            return
        }
    }
}

func computePriority(item rune) int {
    if item >= 'a' && item <= 'z' {
        return int(item-'a') + 1
    }
    return int(item-'A') + 27
}