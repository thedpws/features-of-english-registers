import spacy
nlp = spacy.load('en_core_web_sm')
import statistics
import numpy as np

from tagging.dependency_distance import __tag_dependency_distance
from tagging.f_score import __tag_fscore

# A Generic tagger
def __tag(feature_name, characteristic_fn, domain, doc):
  '''A generic tagging function that handles boilerplate.

  Arguments:
  feature_name      : str                     -- the attribute name to give the document
  characteristic_fn : spacy.Doc.Token -> bool -- the function that determines a token's membership in the metric
  domain            : [spacy.Doc.Token]       -- the set of tokens to calculate the metric from
  doc               : spacy.Doc               -- the document to tag
  '''
  if not spacy.tokens.Doc.has_extension(feature_name):
    spacy.tokens.Doc.set_extension(feature_name, default=-1)
  try:
    feature_metric = statistics.mean(map(characteristic_fn, domain))
  except statistics.StatisticsError:
    feature_metric = 0
  setattr(doc._, feature_name, feature_metric)
  return doc


def __tag_modal_semimodal_freq(doc):
  return __tag(
      feature_name        = 'modal_semimodal_freq',
      characteristic_fn   = lambda token: token.tag_ == 'MD',
      domain              = [token for token in doc if token.pos_ == 'VERB'],
      doc                 = doc
  )


def __tag_progressive_aspect_freq(doc):
  return __tag(
      feature_name        = 'progressive_aspect_freq',
      characteristic_fn   = lambda token: token.tag_ == 'VBG',
      domain              = [token for token in doc if token.pos_=='VERB'],
      doc                 = doc
  )


def __tag_perfect_aspect_freq(doc):
  return __tag(
      feature_name        = 'perfect_aspect_freq',
      characteristic_fn   = lambda token: token.tag_ in ['VB', 'VBD', 'VBP', 'VBZ'],
      domain              = [token for token in doc if token.pos_=='VERB'],
      doc                 = doc
  )


# Does not do possessive pronouns "PRP$" (my, your, his)
def __tag_personal_pronoun_freq(doc):
  return __tag(
      feature_name        = 'personal_pronoun_freq',
      characteristic_fn   = lambda token: token.tag_ == 'PRP',
      domain              = [token for token in doc],
      doc                 = doc
  )


def __tag_adverb_freq(doc):
  return __tag(
      feature_name        = 'adverb_freq',
      characteristic_fn   = lambda token: token.pos_ == 'ADV',
      domain              = [token for token in doc],
      doc                 = doc
  )


def tag(sample):
  doc = nlp(sample)
  __tag_adverb_freq(doc)
  __tag_personal_pronoun_freq(doc)
  __tag_perfect_aspect_freq(doc)
  __tag_progressive_aspect_freq(doc)
  __tag_modal_semimodal_freq(doc)
  __tag_dependency_distance(doc)
  __tag_fscore(doc)
  return doc