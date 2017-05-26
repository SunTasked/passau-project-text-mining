# Text mining Q&A 2

**Question 1 :** Write out the equation for trigram probability estimation.

**Answer:** $P(w_i | w_{i-1}, w_{i-2}) = \frac{c(w_{i-2},c(w_{i-1},w_{i})}{c(w_{i-2},w_{i-1})}$

-----------------------

**Question 2 :** 
We are given the following corpus:

<s> I am Sam </s>
<s> Sam I am </s>
<s> I am Sam </s>
<s> I do not like green eggs and Sam </s>

Using a bigram language model with add-one smoothing, what is P(am | I)? Include <s> and </s> in your counts just like any other token.

**Answer:** 
4/15
Explanation:

The add-1 smoothing bigram language model is given by:

$P_{Add-1}(w_i | w_{i-1}) = \frac{c(w_{i-1},w_{i}) + 1}{c(w_{i-1}) + V}$

Calculating the unigrams and bigrams for the example corpus, we have:

$P_{Add-1}(am | I) = \frac{c(I, am) + 1}{c(I) + V}$

where V is the number of distinct words (vocabulary of the corpus):

$P_{Add-1}(am | I) = \frac{3 + 1}{4 + 11}$

$P_{Add-1}(am | I) = \frac{4}{15}$

-----------------------

**Question 3 :**
We are given the following corpus:

<s> I am Sam </s>
<s> Sam I am </s>
<s> I am Sam </s>
<s> I do not like green eggs and Sam </s>

If we use linear interpolation smoothing between a maximum-likelihood bigram model and a maximum-likelihood unigram model with lambda_1=1/2 and lambda_2 = 1/2, what is P(Sam|am)? Include <s> and </s> in your counts just like any other token.

**Answer:**

1/2 * 4/25 + 1/2 * 2/3
Explanation:

The linear interpolation smoothing for a bigram is given by:

$P(w_n | w_{n-1}) = \lambda_1 P(w_n | w_{n-1}) + \lambda_2 P(w_n)$

Calculating the model for $P(Sam | am)$:

$P(Sam | am) = \frac{1}{2} \times P(Sam | am) + \frac{1}{2} \times P(Sam)$

$P(Sam | am) = \frac{1}{2} \times \frac{2}{3} + \frac{1}{2} \times \frac{4}{25}$


-----------------------

**Question 4 :** 

Suppose we train a trigram language model with add-one smoothing on a given corpus. The corpus contains V word types. What is P(w_3|w_1, w_2), where w_3 is a word which follows the bigram (w_1, w_2)? We use the notation c(w_1, w_2, w_3) to denote the number of times that trigram (w_1, w_2, w_3) occurs in the corpus, and so on for bigrams and unigrams.

**Answer:** 

$\frac{c(w_1, w_2, w_3) + 1}{c(w_1, w_2) + V}$
Explanation:

The add-one smoothing model for the trigram considers only the vocabulary size for the unigrams given that the bigram prefix $(w_1, w_2)$ is fixed.

$P_{Add-1}(w_3 | w_1, w_2) = \frac{c(w_1, w_2, w_3) + 1}{c(w_1, w_2) + V}$


-----------------------

**Question 5 :**

Consider the following corpus:

S Sam Sam works E

Use the {Kneser-Ney smoothing technique (recursive formula) to calculate the following probabilities:

1. P_{KN} (Sam | <s>)
2. P_{KN} (works | <s>)
3. P_{KN} (</s> | <s>)

tip: start the process by calculating the P_{KN}(w_i) where w_i is a unigram.

**Answer:**

http://bit.ly/1Z7UqZ1

-----------------------

**Question 6 :**

Write a Python program that calculates the P_{continuation}(w) of a word w for a given corpus.

**Answer:** 

                #corpus is supposed to be a list of words

                def get_continuation_prob(word, corpus):
                    # get a set of all the different preceeding words contained within the corpus
                    set_of_all_preceedings = set(corpus[:-1])

                    # get a set of the word preceeding words
                    preceeding_words=set()
                    for i in range(1,len(corpus)):
                        if word == corpus[i]:
                            preceeding_words.add(corpus[i-1])
                    
                    # compute continuation probability
                    continutation_prob = len(preceeding_words) / len(set_of_all_preceedings) 

                    return continutation_prob
