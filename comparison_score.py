import requests
from difflib import SequenceMatcher
import time

def fetch_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching content from {url}: {str(e)}")
        return None

def calculate_similarity(content1, content2):
    return SequenceMatcher(None, content1, content2).ratio()

def find_most_similar_links(desired_link, other_links):
    desired_content = fetch_content(desired_link)
    if desired_content is None:
        return

    similarity_scores = {}
    for link in other_links:
        content = fetch_content(link)
        if content is not None:
            similarity_scores[link] = calculate_similarity(desired_content, content)

    sorted_links = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    print("Links with the most similarity to the desired link:")
    for link, score in sorted_links:
        print(f"{link}: Similarity score = {score}")

# Example usage
desired_link = "https://www.bajajfinserv.in/personal-loan"
other_links = [
    "https://www.bajajfinserv.in/gold-loan",
]

start=time.time()
find_most_similar_links(desired_link, other_links)
end=time.time()
print("Time taken: ",(end-start))