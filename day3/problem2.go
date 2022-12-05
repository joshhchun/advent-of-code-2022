package main

import (
	"os"
	"strings"
)

func main() {
    data, _ := os.ReadFile("input.txt")
    rucksacks := strings.Split(string(data), "\n")
    amount := len(rucksacks)
    groups := make(chan []string, amount)
    common := make([]rune, 0)

    go findGroups(rucksacks, groups)
    for group := range groups {
    	inter := intersection(group)
        common = append(common, inter)
    }

    total := 0
    for _, let := range common {
        total += computePriority(let) 
    }
    println(total)
}

func findGroups(rucksacks []string, groups chan<- []string) {
    for i := 0; i < len(rucksacks) - 1; i += 3 {
        groups <- rucksacks[i:i+3]
    }
    close(groups)
}

func intersection(group []string) rune {
    m1 := map[rune]struct{}{}
    m2 := map[rune]struct{}{}
		for _, item := range group[0] {
			m1[item] = struct{}{}
		}

		for _, item := range group[1] {
			if _, exist := m1[item]; exist {
				m2[item] = struct{}{}
			}
		}

		for _, item := range group[2] {
			if _, exist := m2[item]; exist {
				return item
			}
		}
    return -1
}

func computePriority(item rune) int {
    if item >= 'a' && item <= 'z' {
	return int(item-'a') + 1
    }
    return int(item-'A') + 27
}

