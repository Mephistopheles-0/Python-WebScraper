import requests
from bs4 import BeautifulSoup
import csv
import json

# Define the URL to scrape
url = "https://example.com"

# Send a GET request to the URL and parse the response using Beautiful Soup
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the elements on the page containing the data you want to scrape
data = []
for element in soup.find_all("div", class_="example-class"):
    # Extract the relevant information from each element and add it to the data list
    item = {
        "name": element.find("h2").text,
        "description": element.find("p").text,
        "price": element.find("span", class_="price").text
    }
    data.append(item)

# Save the data to a CSV file
with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "description", "price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

# Save the data to a JSON file
with open("data.json", "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False)
