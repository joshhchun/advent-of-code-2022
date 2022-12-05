package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseInput() ([]string, []string){
	file, _ := os.ReadFile("input.txt")
	parts := strings.Split(string(file), "\n\n")
	one, two := parts[0], parts[1]

	stacks := strings.Split(one, "\n")
	instr := strings.Split(two, "\n")
	return stacks, instr

}

func main() {
	stacks, instr := parseInput()
	numStacks, _ := strconv.Atoi(string(stacks[len(stacks)-1][len(stacks[len(stacks)-1])-2]))
	cargo := make([][]string, numStacks)


	for i := len(stacks) - 1; i >= 0; i-- {
		for j, item := range stacks[i] {
			if item >= 'A' && item <= 'Z' {
				cargo[(j-1)/4] = append(cargo[(j-1)/4], string(item))
			}
		}
	}

	for _, line := range instr {
		parts := strings.Split(line, " ")
		numMove, _ := strconv.Atoi(parts[1])
		fromC, _ := strconv.Atoi(parts[3])
		toC, _ := strconv.Atoi(parts[5])
		for i := 0; i < numMove; i++ {
			cargo[toC-1] = append(cargo[toC-1], cargo[fromC-1][len(cargo[fromC-1])-1])
			cargo[fromC-1] = cargo[fromC-1][:len(cargo[fromC-1])-1]
		}
	}
	
	var result string
	for _, stack := range cargo {
		result += stack[len(stack)-1]
	}
	fmt.Println(result)
}