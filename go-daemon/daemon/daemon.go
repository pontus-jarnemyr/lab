package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type Command struct {
	Action   string `json:"action"`
	Username string `json:"username,omitempty"`
	Password string `json:"password,omitempty"`
}

type Response struct {
	Status  string `json:"status"`
	Message string `json:"message"`
}

func loginHandler(w http.ResponseWriter, r *http.Request) {
	var cmd Command
	err := json.NewDecoder(r.Body).Decode(&cmd)
	if err != nil {
		log.Printf("Error decoding JSON: %v", err)
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}

	log.Printf("Received login request with username: %s and password: %s", cmd.Username, cmd.Password)

	// Validate the username and password
	if cmd.Username == "hannes" && cmd.Password == "thorsell" {
		response := Response{Status: "success", Message: "Logged in successfully"}
		json.NewEncoder(w).Encode(response)
	} else {
		response := Response{Status: "failure", Message: "Invalid username or password"}
		json.NewEncoder(w).Encode(response)
	}
}

func statusHandler(w http.ResponseWriter, r *http.Request) {
	response := Response{Status: "success", Message: "Daemon is running"}
	json.NewEncoder(w).Encode(response)
}

func logoutHandler(w http.ResponseWriter, r *http.Request) {
	response := Response{Status: "success", Message: "Logged out successfully"}
	json.NewEncoder(w).Encode(response)
}

func main() {
	http.HandleFunc("/login", loginHandler)
	http.HandleFunc("/status", statusHandler)
	http.HandleFunc("/logout", logoutHandler)

	log.Println("Starting daemon on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
