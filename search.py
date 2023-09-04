import os
import sys
import json
import csv
from slack_bolt import App
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the token
SLACK_TOKEN = os.getenv("SLACK_TOKEN")

# Initialize the app with your bot token
app = App(token=SLACK_TOKEN)

def search_messages(query, format="json"):
    all_messages = []
    
    next_cursor = None
    
    while True:
        params = {
            "query": query,
            "count": 100  # Fetch 100 messages at a time; adjust as needed
        }
        
        if next_cursor:
            params["cursor"] = next_cursor
            
        # Use the search_messages method
        response = app.client.search_messages(**params)
        
        # Append the results to the all_messages list
        all_messages.extend(response['messages']['matches'])

        next_cursor = response.get("response_metadata", {}).get("next_cursor")
        if not next_cursor:
            break

    # Save the results based on the specified format
    if format == "json":
        with open("messages.json", "w") as json_file:
            json.dump(all_messages, json_file, indent=4)
    elif format == "csv":
        with open("messages.csv", "w", newline='') as csvfile:
            fieldnames = ['username', 'text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for message in all_messages:
                writer.writerow({
                    'username': message['username'],
                    'text': message['text']
                })

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        format = sys.argv[2] if len(sys.argv) > 2 else "json"
        if format not in ["json", "csv"]:
            print("Invalid format. Please choose either 'json' or 'csv'.")
            sys.exit(1)
        search_messages(query, format)
    else:
        print("Please provide a query message as an argument.")
