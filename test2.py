from bs4 import BeautifulSoup
import textwrap

def pager(note, max_width):
    # Parse the HTML string using BeautifulSoup
    soup = BeautifulSoup(note, 'html.parser')

    # Find all the HTML tags in the parsed soup
    tags = soup.find_all()

    # Initialize an empty list to store the chunks
    chunks = []

    for tag in tags:
        # Convert the tag back to a string representation
        tag_string = str(tag)

        # Split the tag string into smaller chunks based on the max width
        tag_chunks = textwrap.wrap(tag_string, width=max_width)

        # Append the tag chunks to the list of chunks
        chunks.extend(tag_chunks)

    return chunks

# Example usage
html_string = "<p>Lorem ipsum <strong>dolor sit amet</strong>, consectetur adipiscing elit.</p>"
max_width = 20

# Split the HTML string into smaller chunks
chunks = pager(html_string, max_width)

# Print each chunk separately
for chunk in chunks:
    print(chunk)
