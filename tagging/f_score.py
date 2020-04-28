import spacy

def __tag_fscore(doc):
  if not spacy.tokens.Doc.has_extension('f_score'):
    spacy.tokens.Doc.set_extension('f_score', default=-1)
  f_score = (sum(map(lambda t: t.pos_ in ['NOUN', 'ADJ', 'ADP', 'DET'], doc)) - sum(map(lambda t: t.pos_ in ['PRON','VERB','ADV','INTJ'], doc)) + 100)/2
  setattr(doc._, 'f_score', f_score)
  return doc