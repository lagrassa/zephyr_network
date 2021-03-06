import networkx as nx
import matplotlib.pyplot as plt
z = nx.Graph()



#def valid_character_only(c):
#    if (str(c).isalpha() and c != ' ' and not str(c).isdigit()) or c == "_":
#        return str(c)
#    return ''

#def get_writer(last_slash_index,line):
#    writer = ''
#    index = last_slash_index
#    try:
#        character = line[index]
#    except IndexError:
#        print line
#    while character != ':' and index < len(line)-1:  #checks for timestamp
#        writer+=valid_character_only(character)
#        index +=1
#        character = line[index]
#    return writer,index

def remove_zsig(line):
    left_parenthesis_index = line.index('(')
    right_parenthesis_index = line.index(')')
    line = line[:left_parenthesis_index]+line[right_parenthesis_index:]
    return line
def non_ascii_class(classname):
    ascii_name = ''
    for letter in classname:
        try:
            ascii_name+=letter.encode('ascii')
        except:
            continue

f = open('zephyrs.txt', 'r')
classes_to_subscribers = {}

for line in f:
    classname = unicode(line[5:19], errors='replace').strip()
    if classname not in classes_to_subscribers:
        classes_to_subscribers[classname] = []
    #finds the name of the person writing to the class
    writer = line[31:44].strip()
    if writer not in classes_to_subscribers[classname]:
        classes_to_subscribers[classname].append(writer)

name_to_friends = classes_to_subscribers 
for friend in name_to_friends.keys():
    for other_friend in name_to_friends[friend]:
        z.add_edge(friend,other_friend)

nx.draw(z)
plt.show()
f.close()
