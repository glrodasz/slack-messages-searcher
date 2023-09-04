import os
import sys
import csv
from slack_bolt import App
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the token
SLACK_TOKEN = os.getenv("SLACK_TOKEN")

# Initialize the app with your bot token
app = App(token=SLACK_TOKEN)


def search_messages(query):
    # Open a CSV file for writing
    with open("messages.csv", "w", newline='') as csvfile:
        fieldnames = ['username', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

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

            # Write the results to the CSV file
            for message in response['messages']['matches']:
                writer.writerow({
                    'username': message['username'],
                    'text': message['text']
                })

            next_cursor = response.get(
                "response_metadata", {}).get("next_cursor")
            if not next_cursor:
                break


if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        search_messages(query)
    else:
        print("Please provide a query message as an argument.")
