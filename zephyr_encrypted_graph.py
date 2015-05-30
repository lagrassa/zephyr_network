import networkx as nx
import matplotlib.pyplot as plt
import string
import random
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
    right_parenthesis_index = line.index('(')
    left_parenthesis_index = line.index(')')
    line = line[:right_parenthesis_index]+line[left_parenthesis_index:]
    return line

encryption_dictionary = {}
def encrypt(classname):
    N = 8
    encryption_dictionary[classname] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

f = open('zephyrs.txt', 'r')
classes_to_subscribers = {}

for line in f:
    classname = line[5:19]
    if classname not in classes_to_subscribers:
        classes_to_subscribers[classname] = []
        encrypt(classname)
    #finds the name of the person writing to the class
    writer = line[31:44]
    if writer not in encryption_dictionary.keys():
        encrypt(writer)
    if writer not in classes_to_subscribers[classname]:
        classes_to_subscribers[classname].append(writer)

name_to_friends = classes_to_subscribers 
for friend in name_to_friends.keys():
    for other_friend in name_to_friends[friend]:
        z.add_edge(encryption_dictionary[friend],encryption_dictionary[other_friend])

nx.draw(z)
plt.show()
