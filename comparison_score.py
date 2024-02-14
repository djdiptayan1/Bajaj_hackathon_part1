import requests
from difflib import SequenceMatcher
import time

# Dictionary to store cached content
content_cache = {}

def fetch_content_with_cache(url):
    # Check if content is present in the cache
    if url in content_cache:
        return content_cache[url]

    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            # Cache the fetched content
            content_cache[url] = content
            return content
        else:
            print(f"Failed to fetch content from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching content from {url}: {str(e)}")
        return None

def calculate_similarity(content1, content2):
    return SequenceMatcher(None, content1, content2).ratio()

def extract_keywords_from_link(link):
    # Split the link by '/' and take the last part
    last_part = link.split('/')[-1]
    # Extract keywords separated by '-'
    return last_part.split('-')

def find_most_similar_links(desired_link, other_links):
    desired_keywords = extract_keywords_from_link(desired_link)
    if not desired_keywords:
        print("No keywords found in the desired link.")
        return

    similarity_scores = {}
    desired_content = fetch_content_with_cache(desired_link)
    if desired_content is None:
        return

    for link in other_links:
        # Extract keywords from the current link
        link_keywords = extract_keywords_from_link(link)
        # Check if there is at least one matching keyword
        if any(keyword in link_keywords for keyword in desired_keywords):
            content = fetch_content_with_cache(link)
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

start = time.time()
find_most_similar_links(desired_link, other_links)
end = time.time()
print("Time taken: ", (end - start))
