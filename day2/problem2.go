package main

import (
	"os"
	"strings"
)

func main() {
    elf_moves := map[byte]string{'A': "rock", 'B': "paper", 'C': "scissors"}
    req_result := map[byte]string{'X': "lose", 'Y': "tie", 'Z': "win"}

    file, _ := os.ReadFile("input.txt")
    input := string(file)
    moves := strings.Split(input, "\n")

    my_score := 0
    for _, move := range moves {
        elf_move := elf_moves[move[0]]
        result := req_result[move[2]]
        if elf_move == "rock" {
            if result == "tie" {
                my_score += 4
            } else if result == "win" {
                my_score += 8
            } else {
                my_score += 3
            }
        } else if elf_move == "paper" {
            if result == "tie" {
                my_score += 5
            } else if result == "win" {
                my_score += 9
            } else {
                my_score += 1
            }
        } else {
            if result == "tie" {
                my_score += 6
            } else if result == "win" {
                my_score += 7
            } else {
                my_score += 2
            }
        }
    }
    println(my_score)
}