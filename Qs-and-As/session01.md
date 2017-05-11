# Text mining Q&A 1

**Question 1 :** Define what is a phrasal node.

**Answer:** Phrasal nodes are non-terminal symbols in a phrase structure grammar which aggregate words which form a cohesive meaning unit.

-----------------------

**Question 2 :** In your own words how would you describe the difference between dependency and constituent (tree) structures?

**Answer:** Both structures are syntactic representation forms. Phrase structure represent structural categories while dependency structure focus on bilexical head-dependent relations (every node in the structure represents a word).

-----------------------

**Question 3 :** Find the tagging error in the following sentence, correcting the POS tag: "How/WRB do/MD I/PRP get/VB to/TO Bulgaria/NN"

**Answer:** Bulgaria/NNP

-----------------------

**Question 4 :** Find the tagging error in the following sentence, correcting the POS tag: "Do/VBP you/PRP have/VB any/DT vacancies/NN"

**Answer:** vacancies/NNS

-----------------------

**Question 5 :** Find the tagging error in the following sentence, correcting the POS tag: "This/DT room/NN is/VBZ too/JJ noisy/JJ"

**Answer:** too/RT

-----------------------

**Question 6 :** Find the tagging error in the following sentence, correcting the POS tag: "Can/VB you/PRP give/VB me/PRP another/DT room/NN"

**Answer:** Can/MD

-----------------------

**Question 8 :** Use the Penn Treebank tagset to tag each word in the following sentence from Damon Runyon's short stories.  "He is a tall, skinny guy with a long, sad, mean-looking kisser, and a mournful voice."

**Answer:** He/PRP is/VBZ a/DT tall/JJ ,/, skinny/JJ guy/NN with/IN a/DT long/JJ ,/, sad/JJ ,/, mean-looking/JJ kisser/NN ,/, and/CC a/DT mournful/JJ voice/NN ./.

-----------------------

**Question 9 :** For the following exercises use the labeled bracket notation (example here (http://ironcreek.net/phpsyntaxtree/?PHPSESSID=aaefahsok2dibs33dmp4spqip6) to manually annotate the syntactic trees. Use the Penn Treebank tagset. Draw the syntactic tree for the following sentence: "departing from Newark"

**Answer:** [VP [VB departing] [PP [IN from] [NP [NNP Newark]]]]

-----------------------

**Question 10 :** Draw the syntactic tree (C-Structure) for the following sentence: "all non-stop flights"

**Answer:** [NP [DT all] [JJ non-stop] [NNS flights]]

-----------------------

**Question 11 :** Draw the syntactic tree (C-Structure) for the following sentence: "Here in Baltimore"

**Answer:** [ADVP [RB here] [PP [IN in] [NP [NNP Baltimore]]]]

-----------------------

**Question 12 :** Draw the syntactic tree (C-Structure) for the following sentence: "Does American airlines have a flight between five a.m. and six a.m.?"

**Answer:** [S [VBP Does] [NP [JJ American] [NNS airlines]] [VP [VB have] [NP [NP [DT a] [NN flight]] [PP [IN between] [NP [NP [CD five] [NN a.m.]] [CC and] [NP [CD six] [NN a.m.]]]]]] [. ?]]
**My Answer:** [S [VP [VBZ Does] [NP [NN American Airlines] ] [VB have] ] [NP [NP [DT a] [NN flight] ] [PP [IN between] [NP [NP [CD five] [FW a.m.] ] [CC and] [NP [CD six] [FW a.m.]]]]]]

-----------------------

**Question 13 :** Draw the syntactic tree (C-Structure) for the following sentence: "Please repeat that."

**Answer:** [S [VP [RB Please] [VB repeat] [NP [DT that]]]]

-----------------------

**Question 14 :** Draw the syntactic tree (C-Structure) for the following sentence: "What is the fare from Atlanta to Denver?"

**Answer:** [S [WHNP [WP What]] [VP [VBZ is] [NP [DT the] [NP [NN fare] [PP [IN from] [NNP Atlanta]] [PP [TO to] [NP [NNP Denver]] ] ]]] ]

-----------------------

**Question 15 :**
Draw the dependency structure for the following sentence:

GE acquired the assets of Enron.

Use the Stanford parser notation \footnote{\url{http://nlp.stanford.edu/software/dependencies\_manual.pdf}}. Example:

``GXS is a provider of technology solutions.''

nsubj(provider-4, GXS-1)
cop(provider-4, is-2)
det(provider-4, a-3)
root(ROOT-0, provider-4)
prep(provider-4, of-5)
nn(solutions-7, technology-6)
pobj(of-5, solutions-7)

**Answer:** 
nsubj(acquired-2, GE-1)
root(ROOT-0, acquired-2)
det(assets-4, the-3)
dobj(acquired-2, assets-4)
case(Enron-6, of-5)
nmod(assets-4, Enron-6)

-----------------------

**Question 16 :** List three legitimate subcategorization frames for the verb ``tell''.

**Answer:** 
Here are four – there are more.
[] She told!
[NP] She told him.
[NP NP] She told him lies.
[NP PP] She told him in secret.

-----------------------

**Question 17 :** 
List three legitimate subcategorization frames for the following verbs: 
Also classify them as transitive, intransitive and ditransitive.

**Answer:** 
_ intransitive sleep
NP transitive assassinate
NP NP ditransitive toss

-----------------------

**Question 18 :** 
A sentence can have multiple auxiliary verbs, but they must occur in a particular order:

modal < perfect < progressive < passive

Here are some examples of multiple auxiliaries. Classify them according to their type:

a. could have been a contender 

b. will be married 

c. have been feasting 

d. might have been prevented

**Answer:** 
modal perfect : could have been a contender
modal passive : will be married
perfect progressive : have been feasting
modal perfect passive : might have been prevented
Auxiliaries : are often treated just like verbs such as want, seem,

-----------------------

**Question 19 :** 
Grammar 1 (G1) illustrates a simple CF PSG for a small fragment of English.

\begin{orgtext}
Grammar 1

Rules 										
a. S --> NP VP. 					
b. VP --> V. 							
c. VP --> V NP. 					
d. VP --> V PP.  					
e. VP --> V NP NP.  			
f. NP --> Nname.  				
g. NP --> Det N.  				
h. PP --> P NP.  					

Lexicon

Sam : Nname. 
plays : V.
Kim : Nname. 
chases : V.
Felix : Nname. 
sings : V.
Tweety : Nname. 
the : Det.
cat : N. 
miaows : V.
bird : N. 
a : Det.
park : N. 
in : P.
ball : N. 
with : P.

\end{orgtext}

Write 2 sentences this grammar generates.

**Answer:** 
These are some possible sentences:

Sam plays with Felix.
Kim sings in a park.

-----------------------

**Question 20 :** Is the previous grammar in the Chomsky normal form? Justify.

**Answer:** No. The derivation rule \textit{VP --> V NP NP} is not binary