# Text mining Q&A 2

**Question 1 :** Identify the subordination in the following sentence: When Mary moved to the United States, she was five years old.

**Answer:** when Mary moved to the United States

-----------------------

**Question 2 :** Identify the subordination in the following sentence: Because the class was so noisy today, we didn’t get to have any free time.

**Answer:** Because the class was so noisy today

-----------------------

**Question 3 :** Identify the subordination in the following sentence:I haven't gotten any allowance since my father lost his job.

**Answer:** since my father lost his job

-----------------------

**Question 4 :** Classify the mood of the verb in the sentence: Sally is drinking coffee.

**Answer:** indicative

-----------------------

**Question 5 :** Classify the mood of the verb in the sentence: `Sally drank coffee.'

**Answer:** indicative

-----------------------

**Question 6 :** Classify the mood of the verb in the sentence: `That programming language was cool. I wish it were still in use.'

**Answer:** subjunctive

-----------------------

**Question 7 :** Identify the aspect of the verb in the sentence: `Klaus was lecturing about information theory.'

**Answer:** progressive

-----------------------

**Question 8 :** Identify the aspect of the verb in the sentence: `She has visited her old school.'

**Answer:** perfect

-----------------------

**Question 9 :**

Can the grammar in grammar1 be used to describe sentences that are more than 20 words in length?

grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)

**Answer:** 

Yes. Consider the following expansion using grammar1:

S
NP VP
Det N PP VP
Det N P NP VP
Det N P Det N PP VP
And so on...

Basically you go from `NP -> Det N PP` to `PP -> P NP` and back.


-----------------------

**Question 10 :** 

Consider the sequence of words: `Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo'. This is a grammatically correct sentence, as explained at {http://en.wikipedia.org/wiki/Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo}. Consider the tree diagram presented on this Wikipedia page, and write down a suitable grammar. Normalize case to lowercase, to simulate the problem that a listener has when hearing this sentence. Can you find other parses for this sentence? How does the number of parse trees grow as the sentence gets longer? (More examples of these sentences can be found at \utrl{http://en.wikipedia.org/wiki/List_of_homophonous_phrases}).

**Answer:**

S -> NP VP
NP -> NP RC | PN N
RC -> NP V
VP -> V NP
PN -> buffalo
N -> buffalo
V -> buffalo

For this particular case, we can find another parse:

                (S
                    (NP
                        (PN buffalo)
                        (N buffalo)
                    )
                    (VP
                        (V buffalo)
                        (NP
                            (NP
                                (PN buffalo)
                                (N buffalo)
                            )
                            (RC
                                (NP
                                    (PN buffalo)
                                    (N buffalo)
                                )
                                (V buffalo)
                            )
                        )
                    )
                )

-----------------------

**Question 11 :** Write code in Python using nltk to produce two trees, one for each reading of the phrase `old men and women'.

**Answer:** 

                import nltk

                def a():
                    """
                    Write code to produce two trees, one for each reading of the phrase old men and women
                    """
                    first_reading = """
                    (NP
                        (JJ old)
                        (NP
                            (NNS men)
                            (CC and)
                            (NNS women)
                        )
                    )
                    """
                    second_reading = """
                    (NP
                        (NP
                            (JJ old)
                            (NNS men)
                        )
                        (CC and)
                        (NNS women)
                    )
                    """
                    t = nltk.tree.Tree.fromstring(first_reading)
                    t.draw()
                    t = nltk.tree.Tree.fromstring(second_reading)
                    t.draw()

-----------------------

**Question 12 :** 

Encode the tree represented using labeled bracketing and use nltk.Tree() to check that it is well-formed. Now use draw() to display the tree.

**Answer:**

                import nltk

                test = """
                (S
                    (NP I)
                    (VP
                        (VP
                            (V shot)
                            (NP
                                (Det an)
                                (N elephant)
                            )
                        )
                        (PP
                            (P in)
                            (NP
                                (Det my)
                                (N pajamas)
                            )
                        )
                    )
                )
                """

                t = nltk.tree.Tree.fromstring(test)
                t.draw()

-----------------------

**Question 13 :** As in the previous exercise, draw a tree for The woman saw a man last Thursday.

**Answer:** 

                def c():
                    """
                    As in (a) above, draw a tree for The woman saw a man last Thursday.
                    """
                    tree_str = """
                    (S
                        (NP
                            (DT The)
                            (NN woman)
                        )
                        (VP
                            (VBD saw)
                            (NP
                                (DT a)
                                (NN man)
                            )
                            (ADVP
                                (JJ last)
                                (NNP Thursday)
                            )
                        )
                    )
                    """
                    t = nltk.tree.Tree.fromstring(tree_str)
                    t.draw()

-----------------------

**Question 14 :**
Process each tree of the Treebank corpus sample nltk.corpus.treebank and extract the productions with the help of Tree.productions(). Discard the productions that occur only once. Productions with the same left hand side, and similar right hand sides can be collapsed, resulting in an equivalent but more compact set of rules.

**Answer:** 
            #Process each tree of the Treebank corpus sample nltk.corpus.treebank and extract the productions with the help of Tree.productions(). Discard the productions that occur only once.
            #Productions with the same left hand side, and similar right hand sides can be collapsed, resulting in an equivalent but more compact set of rules. 
            #Write code to output a compact grammar.
            from nltk.corpus import treebank

            treebank.ensure_loaded()

            trees = treebank.parsed_sents()

            #Index by the production and count each occurrence
            productions = {}
            for tree in trees:
                tree_productions = tree.productions()
                for prod in tree_productions:
                    if prod not in productions:
                        productions[prod] = 1
                    else:
                        productions[prod] += 1

            #Exclude productions with only one occurrence
            to_exclude = [] #Can't change dict while looping through it
            for prod in productions:
                if productions[prod] == 1:
                    to_exclude.append(prod)
            for prod in to_exclude: #Now exclude them
                productions.pop(prod)

            print 'CFG size: {} productions'.format(len(productions))