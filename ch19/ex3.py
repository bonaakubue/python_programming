# Navigating the trees

from bs4 import BeautifulSoup


# Parent
html = '''
<html>
<div id="part1">
<p>Paragraph 1</p>
<p>Paragraph 2</p>
</div>
<div id="part2">
<p>Paragraph 3</p>
<p>Paragraph 4</p>
<p>Paragraph 5</p>
</div>
</html>
'''

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')
# Find the first <p> element
p1 = soup.find_all('p')[0]

# Access the parent element
pe = p1.parent

print("Current element:", p1)
print("Parent element:", pe)

# Children
# Create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")
pe = soup.find('div', {'id': 'part1'})

# Iterate over the child elements
for child in pe.children:
    print(child)

# Sibling
# Find the first <p> element
p = soup.find('p')

# Get the next sibling element
next_sibling = p.next_sibling


