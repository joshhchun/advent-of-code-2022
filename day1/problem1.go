package main

import (
    "bufio"
    "os"
    "strconv"
)

func main() {
    s := bufio.NewScanner(os.Stdin)
    nums := make([]int, 0)
    var num_calories int
    for s.Scan() {
        if snack := s.Text(); snack != "" {
	    snack, _ := strconv.Atoi(snack)
	    num_calories += snack
        } else {
            nums = append(nums, num_calories)
            num_calories = 0
        }
    }

    max := 0
    for _, num := range nums {
        if num > max {
	    max = num
        }
    }
    println(max)
}
