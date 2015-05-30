import networkx as nx
import matplotlib.pyplot as plt
z = nx.Graph()



def alpha_only(c):
    if str(c).isalpha() and c != ' ' and not str(c).isdigit():
        return str(c)
    return ''

def get_writer(last_slash_index,line):
    writer = ''
    index = last_slash_index
    try:
        character = line[index]
    except IndexError:
        print line
    while character != ':' and index < len(line)-1:  #checks for timestamp
        writer+=alpha_only(character)
        index +=1
        character = line[index]
    return writer,index

def remove_zsig(line):
    right_parenthesis_index = line.index('(')
    left_parenthesis_index = line.index(')')
    line = line[:right_parenthesis_index]+line[left_parenthesis_index:]
    return line


f = open('zephyrs.txt', 'r')
classes_to_subscribers = {}

for line in f:
    if line.count('/')>=2 and ':' in line and '(' in line and ')' in line:
        #detects weird zsig cases
        if line.count('/')>2:
            line = remove_zsig(line)
        classname_slash_index = line.index('/')
        classname = ''.join([alpha_only(line[c]) for c in range(classname_slash_index) ])
        if classname not in classes_to_subscribers:
            classes_to_subscribers[classname] = []
        #finds the name of the person writing to the class
        last_slash_index = line.rfind('/');
        writer, endindex = get_writer(last_slash_index,line) 

        if writer == "UNAUTH":
            writer, endindex = get_writer(endindex+1,line)
        if writer not in classes_to_subscribers[classname] and writer !='UNAU':
            classes_to_subscribers[classname].append(writer)

name_to_friends = classes_to_subscribers 
print name_to_friends
for friend in name_to_friends.keys():
    for other_friend in name_to_friends[friend]:
        z.add_edge(friend,other_friend)

nx.draw(z)
plt.show()
