from bs4 import BeautifulSoup

def extract_bookmarks(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    bookmarks = []
    for a in soup.find_all('a'):
        title = a.text
        url = a.get('href')
        bookmarks.append((title, url))

    return bookmarks

if __name__ == "__main__":
    html_file_path = input("Enter the bookmarks HTML file name: ")
    output_file_path = input("Enter the output Markdown (.md) file name: ")

    bookmarks = extract_bookmarks(html_file_path)
    
    with open(output_file_path, 'w', encoding='utf-8') as f_out:
        for title, url in bookmarks:
            f_out.write(f"- [{title}]({url})\n")

    print(f"Extracted {len(bookmarks)} bookmarks to {output_file_path}")
