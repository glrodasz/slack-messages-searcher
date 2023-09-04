import os
from slack_bolt import App
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the token
SLACK_TOKEN = os.getenv("SLACK_TOKEN")

# Initialize the app with your bot token
app = App(token=SLACK_TOKEN)

def search_messages(query):
    # Your hardcoded search query
    query = "{query}"
    
    # Use the search_messages method
    response = app.client.search_messages(query=query)
    
    # Print the results
    for message in response['messages']['matches']:
        print(f"User: {message['username']}, Text: {message['text']}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        search_messages(query)
    else:
        print("Please provide a query message as an argument.")