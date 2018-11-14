package main

import "os"
import "fmt"

func main() {
	path := os.Getenv("PATH")
	fmt.Println(path)
}
