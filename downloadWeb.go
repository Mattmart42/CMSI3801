package main

import (
    "fmt"
    "net/http"
    "os"
    "io"
)

func download(url string) {
    resp, err:= http.Get(url)
    defer resp.Body.Close()
    
    if err != nil {
        fmt.Println(err)
    }
    
    bodyBytes, err := io.ReadAll(resp.Body)

    if err != nil {
        fmt.Println(err)
    }
    
    bodyString := string(bodyBytes)
    fmt.Println(bodyString)
}

func main() {
    url := os.Args[1]
    download(url)
}