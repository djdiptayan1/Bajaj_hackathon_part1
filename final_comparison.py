import json
from difflib import SequenceMatcher

def calculate_similarity(keywords1, keywords2):
    # Convert keywords to sets for efficient comparison
    set1 = set(keywords1)
    set2 = set(keywords2)
    # Calculate Jaccard similarity
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

def extract_keywords_from_link(link):
    # Split the link by '/' and take the last part
    last_part = link.split('/')[-1]
    # Extract keywords separated by '-'
    return last_part.split('-')

def read_links_from_json(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            # Debug print
            return data 
    except FileNotFoundError:
        print(f"File '{json_file}' not found.")
        return []

    
def find_most_similar_links(desired_link, other_links):
    if not desired_link:
        print("No title found in the desired link.")
        return []

    desired_keywords = extract_keywords_from_link(desired_link)
    similarity_scores = {}
    for link in other_links:
        if link is not None:
            other_keywords = extract_keywords_from_link(link)
            similarity_scores[link] = calculate_similarity(desired_keywords, other_keywords)

    sorted_links = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    print("Top 5 links with the most similarity to the desired link based on titles:")
    top_5_links = []
    for link, score in sorted_links[:5]:
        print(f"{link}: Similarity score = {score}")
        top_5_links.append(link)
    return top_5_links

# Example usage
desired_link = "https://bajajfinserv.in/loans/personal-loan/marriage-loan.html"
json_file = "filtered_links101.json"  # Replace with the path to your JSON file containing the links

other_links = read_links_from_json(json_file)

top_5_similar_links = find_most_similar_links(desired_link, other_links)
print("Top 5 similar links:")
for link in top_5_similar_links:
    print(link)
