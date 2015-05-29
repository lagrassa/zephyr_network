import networkx as nx
import matplotlib.pyplot as plt
z = nx.Graph()



def alpha_only(c):
    if str(c).isalpha() and c != ' ':
        return str(c)
    return ''

f = open('zephyrs.txt', 'r')
classes_to_subscribers = {}

for line in f:
    if '/' in line and ':' in line and '(' in line and ')' in line:
        classname_slash_index = line.index('/')
        classname = ''.join([alpha_only(line[c]) for c in range(classname_slash_index) ])
        if classname not in classes_to_subscribers:
            classes_to_subscribers[classname] = []
        #finds the name of the person writing to the class
        last_slash_index = line[::-1].index('/');
        writer = ''
        index = last_slash_index
        character = line[index]
        while character != ':' or index < len(line)-1:
            writer+=character
            index +=1
            try: 
                character = line[index]
            except IndexError:
                print "error", line, index
        writer = writer[:-2]
        if writer not in classes_to_subscribers[classname] and writer !='UNAU':
            classes_to_subscribers[classname].append(writer)
print classes_to_subscribers

classes_to_subscribers = name_to_friends

for friend in name_to_friends.keys():
    for other_friend in name_to_friends[friend]:
        z.add_edge(friend,other_friend)

nx.draw(z)
plt.show()
