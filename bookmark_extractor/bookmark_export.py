from bs4 import BeautifulSoup

def extract_bookmarks(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    bookmarks = []
    # Find all <a> tags that represent bookmarks
    for a in soup.find_all('a'):
        title = a.text
        url = a.get('href')
        bookmarks.append((title, url))

    return bookmarks

if __name__ == "__main__":
    html_file_path = 'bookmarks.html'  
    bookmarks = extract_bookmarks(html_file_path)
    
    # Save to a text file with Title and URL
    with open('bookmarks_extracted.md', 'w', encoding='utf-8') as f_out:
        for title, url in bookmarks:
            f_out.write(f"{title} - {url}\n")

    print(f"Extracted {len(bookmarks)} bookmarks to bookmarks_extracted.md")
