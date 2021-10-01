import xml.etree.ElementTree as ET
import re

tree = ET.parse('./movies.xml')

root = tree.getroot()

for movie in root.iter('movie'):
    print(movie.attrib)
    
for description in root.iter('description'):
    print(description.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for form in root.findall("./genre/decade/movie/format"):
    # Search for the commas in the format text
    match = re.search(',',form.text)
    if match:
        form.set('multiple','Yes')
    else:
        form.set('multiple','No')

action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, 'decade')
new_dec.attrib["years"] = '2000s'

xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)

# Write out the tree to the file again
tree.write("movies.xml")