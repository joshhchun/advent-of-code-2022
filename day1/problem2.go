package main

import (
    "bufio"
    "os"
    "sort"
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

    sort.Ints(nums)
    total := nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3]
    println(total)
}

