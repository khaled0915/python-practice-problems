from bs4 import BeautifulSoup

html_content = """
<html>
<head><title>My Sample Blog</title></head>
<body>
    <h1>Welcome to My Blog</h1>
    <h2>Introduction to Python</h2>
    <p>Python is a versatile programming language...</p>
    <h2>Web Development with Flask</h2>
    <p>Flask is a lightweight web framework...</p>
    <h2>Data Analysis with Pandas</h2>
    <p>Pandas makes data manipulation easy...</p>
</body>
</html>
"""

def scrape_h2_titles_from_html(html):
  
    soup = BeautifulSoup(html, 'html.parser')
    titles = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
    return titles


titles = scrape_h2_titles_from_html(html_content)

print("Blog Titles Found:")
for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")
