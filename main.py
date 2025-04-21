
import os

def main():
    notion_secret = os.getenv("NOTION_SECRET")
    boost_api_key = os.getenv("BOOST_API_KEY")
    alerts_email = os.getenv("ALERTS_EMAIL")

    print("Automation Runtime Started")
    print(f"Notion Secret: {notion_secret}")
    print(f"Boost API Key: {boost_api_key}")
    print(f"Alerts Email: {alerts_email}")

if __name__ == "__main__":
    main()
