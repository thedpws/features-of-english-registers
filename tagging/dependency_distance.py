import spacy
nlp = spacy.load('en_core_web_sm')
import statistics
import numpy as np


# Sets the dependency_distance attribute to each token
def __tag_dependency_distance(doc):
  # Adds attribute 'dependecy_distance' to Token
  if not spacy.tokens.Token.has_extension('dependency_distance'):
    spacy.tokens.Token.set_extension('dependency_distance', default=-1)


  for sentence_span in doc.sents:
    tokens = doc[sentence_span.start:sentence_span.end]
    words = list(map(lambda x: x.lower_, tokens))

    for token in tokens:
      for dependent in token.children:
        dependent._.dependency_distance = abs(words.index(token.lower_) - words.index(dependent.lower_))
      if token._.dependency_distance == -1:
        # Token is the head of the sentence
        token._.dependency_distance = 0

  if not spacy.tokens.Doc.has_extension('average_dependency_distance'):
    spacy.tokens.Doc.set_extension('average_dependency_distance', default=-1)

  doc._.average_dependency_distance = statistics.mean(map(lambda token: token._.dependency_distance, doc))


def __dependency_distance_demo():
  doc = nlp('My brain is small. I have 10 IQ. The bag that she bought yesterday was very expensive!')
  
  tag_dependency_distance(doc)

  for token in doc:
    print(token, token._.dependency_distance)
  print('average dependency distance', doc._.average_dependency_distance)