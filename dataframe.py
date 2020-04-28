import spacy
import pandas as pd

pd.set_option('display.max_columns', None) # show all columns

def create_dataframe(genre, docs):
  docs = list(docs)
  # Add genre attribute to document
  if not spacy.tokens.Doc.has_extension('genre'):
    spacy.tokens.Doc.set_extension('genre', default='UNCLASSIFIED')

  for doc in docs:
    doc._.genre = genre
  
  df = pd.DataFrame(

      data=map(lambda doc: [
        str(doc),
        doc._.genre,
        doc._.average_dependency_distance,
        doc._.adverb_freq,
        doc._.modal_semimodal_freq,
        doc._.perfect_aspect_freq,
        doc._.progressive_aspect_freq,
        doc._.personal_pronoun_freq,
        doc._.f_score
      ], docs),
      
      columns=[
        'text',
        'genre',
        'average_dependency_distance',
        'adverb_frequency',
        'modal_semimodal_frequency',
        'perfect_aspect_frequency',
        'progressive_aspect_frequency',
        'personal_pronoun_frequency',
        'f_score'
      ],
  )

  return df

def __df_demo():
  doc = nlp('I met the neighbor\'s dog. It looks more like a rat.')
  tag_features(doc)
  print(to_dataframe('MYGENRE', [doc]))