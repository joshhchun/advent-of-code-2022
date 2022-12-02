package main

import (
	"os"
	"strings"
)

func main() {
    elf_moves := map[byte]string{'A': "rock", 'B': "paper", 'C': "scissors"}
    my_moves := map[byte]string{'X': "rock", 'Y': "paper", 'Z': "scissors"}
    move_weight := map[string]int{"rock": 1, "paper": 2, "scissors": 3}

    file, _ := os.ReadFile("input.txt")
    input := string(file)
    moves := strings.Split(input, "\n")

    my_score := 0
    for _, move := range moves {
        elf_move := elf_moves[move[0]]
        my_move := my_moves[move[2]]
        my_score += move_weight[my_move]
        if my_move == elf_move {
            my_score += 3
        } else if my_move == "rock" && elf_move == "scissors" {
            my_score += 6
        } else if my_move == "paper" && elf_move == "rock" {
            my_score += 6
        } else if my_move == "scissors" && elf_move == "paper" {
            my_score += 6
        }
    }
    println(my_score)
}