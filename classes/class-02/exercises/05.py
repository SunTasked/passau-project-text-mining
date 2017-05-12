import nltk
from nltk.corpus import wordnet as wn

motorcar = wn.synset('car.n.01')
print("motorcar member_meronyms : " + str(motorcar.member_meronyms()))
print("motorcar part_meronyms : " + str(motorcar.part_meronyms()))
print("motorcar substance_meronyms : " + str(motorcar.substance_meronyms()))
print("motorcar member_holonyms : " + str(motorcar.member_holonyms()))
print("motorcar part_holonyms : " + str(motorcar.part_holonyms()))
print("motorcar substance_holonyms : " + str(motorcar.substance_holonyms()))
print()

tree = wn.synset('tree.n.01')
print("tree member_meronyms : " + str(tree.member_meronyms()))
print("tree part_meronyms : " + str(tree.part_meronyms()))
print("tree substance_meronyms : " + str(tree.substance_meronyms()))
print("tree member_holonyms : " + str(tree.member_holonyms()))
print("tree part_holonyms : " + str(tree.part_holonyms()))
print("tree substance_holonyms : " + str(tree.substance_holonyms()))