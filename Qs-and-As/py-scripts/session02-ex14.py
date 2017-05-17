import nltk

treebank = nltk.corpus.treebank

rules = []
counts = []

# listing rules
for id in treebank.fileids():
    t = treebank.parsed_sents(id)
    for tree in t:
        prod = nltk.tree.Tree.productions(tree)
        for rule in prod:
            s_rule = str(rule)
            if s_rule in rules : 
                counts[rules.index(s_rule)] += 1
            else :
                rules.append(s_rule)
                counts.append(1)
print("listing done")
print()

# compacting rules
compact_rules = dict()
for idx, rule in enumerate(rules):
    if counts[idx] > 1:
        left,right = rule.split(" -> ")
        if left in compact_rules:
            if not (right in compact_rules[left]):
                compact_rules[left].append(right)
        else:
            compact_rules[left] = [right]
print("compacting done")
print()

# rendering
for left, rights in compact_rules.items():
    s_rule = left + " -> "
    for right in rights:
        s_rule += right + " | "
    s_rule = s_rule[:-3]
    print (s_rule)
