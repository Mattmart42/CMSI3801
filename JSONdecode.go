package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

func main() {
	apiURL := "http://universities.hipolabs.com/search?name=Loyola+Marymount+University"

	response, err := http.Get(apiURL)
	if err != nil {
		fmt.Printf("Error making GET request: %v\n", err)
		return
	}
	defer response.Body.Close()

	var universities []struct {
		State     string   `json:"state-province"`
		Country   string   `json:"country"`
		Domains   []string `json:"domains"`
		WebPages  []string `json:"web_pages"`
		AlphaCode string   `json:"alpha_two_code"`
		Name      string   `json:"name"`
	}

	err = json.NewDecoder(response.Body).Decode(&universities)
	if err != nil {
		fmt.Printf("Error decoding JSON: %v\n", err)
		return
	}

	for _, university := range universities {
		fmt.Printf("Name: %s\nCountry: %s\nState: %s\nDomains: %v\nWeb Pages: %v\nAlpha Code: %s\n\n",
			university.Name, university.Country, university.State, university.Domains, university.WebPages, university.AlphaCode)
	}
}