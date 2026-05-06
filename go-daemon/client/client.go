package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"

	"github.com/spf13/cobra"
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

func sendRequest(action string) {
	cmd := Command{Action: action}
	jsonData, _ := json.Marshal(cmd)

	resp, err := http.Post(fmt.Sprintf("http://localhost:8080/%s", action), "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()

	var response Response
	json.NewDecoder(resp.Body).Decode(&response)
	fmt.Printf("Response: %s - %s\n", response.Status, response.Message)
}

func handleLogin(username string, password string) {
	var cmd Command = Command{Username: username, Password: password}
	jsonData, _ := json.Marshal(cmd)

	resp, err := http.Post("http://localhost:8080/login", "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error when logging in: ", err)
		return
	}
	var response Response
	json.NewDecoder(resp.Body).Decode(&response)
	fmt.Printf("Response: %s - %s\n", response.Status, response.Message)
}

var rootCmd = &cobra.Command{
	Use:   "myclient",
	Short: "MyClient is a CLI for interacting with the MyDaemon service",
	Run: func(cmd *cobra.Command, args []string) {
		cmd.Help()
	},
}

var loginCmd = &cobra.Command{
	Use:   "login",
	Short: "Login to the MyDaemon service",
	Long: `Log in to the MyDaemon service with the provided username and password
	
Required positional arguments:
  username	Your username
  password 	Your password
	`,
	Args: cobra.ExactArgs(2),
	Run: func(cmd *cobra.Command, args []string) {
		var username string = args[0]
		var password string = args[1]
		handleLogin(username, password)
	},
}

var statusCmd = &cobra.Command{
	Use:   "status",
	Short: "Check the status of the MyDaemon service",
	Run: func(cmd *cobra.Command, args []string) {
		sendRequest("status")
	},
}

var logoutCmd = &cobra.Command{
	Use:   "logout",
	Short: "Logout from the MyDaemon service",
	Run: func(cmd *cobra.Command, args []string) {
		sendRequest("logout")
	},
}

func init() {
	rootCmd.AddCommand(loginCmd)
	rootCmd.AddCommand(statusCmd)
	rootCmd.AddCommand(logoutCmd)
}

func main() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
