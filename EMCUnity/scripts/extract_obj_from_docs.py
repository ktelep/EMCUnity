from BeautifulSoup import BeautifulSoup
import glob

object_files = glob.glob("*.html")

for file in object_files:
    soup = BeautifulSoup(open(file))

    obj_properties = []

    attr_table = soup.table
    if attr_table:
        for row in attr_table.findAll('tr'):
            prop = row.td.text
            if prop == 'Attribute':
                continue 
            obj_properties.append(prop)

    obj_name = file[:-5]
    line1 = "Unity%s = namedtuple_defaults('Unity%s', [" % (obj_name, obj_name)
    print line1
    for i in obj_properties:
        print " " * len(line1) + "'%s'," % i
    print " " * len(line1) + "])\n\n"
    

        

