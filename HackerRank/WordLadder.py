from Graph import Graph, bfs1
from collections import deque
import os

def build_graph(wordFile):
	d = {}
	g = Graph()
	wfile = open(wordFile,'r')
	# create buckets of words that differ by one letter
	for line in wfile:
		word = line[:-1]
		for i in range(len(word)):
			bucket = word[:i] + '_' + word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]
	# add vertices and edges for words in the same bucket
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.add_edge(word1,word2)
	return g


if __name__ == "__main__":
	

	vocabulary_file = os.path.join(os.path.dirname(__file__), 'vocabulary.txt')
	vocabulary_file = str(vocabulary_file)
	word_graph = build_graph(vocabulary_file)





	for vertex,path in bfs1(word_graph,"FOOL"):
	
		if vertex=="SAGE":
			print ' -> '.join(path)

	








