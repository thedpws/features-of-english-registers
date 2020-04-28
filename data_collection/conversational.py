import convokit

corpus = convokit.Corpus(filename=convokit.download('movie-corpus'))

def get_conversation_utterances(N=10):

    # get N conversations
    conversation_ids = corpus.get_conversation_ids()[:N]
    conversations = map(corpus.get_conversation, conversation_ids)

    utterances = []
    for convo in conversations:
        utterance_text = []
        for u in convo.get_utterance_ids():
            utterance_text.append(convo.get_utterance(u).text)

        utterance = ' '.join(utterance_text)
        utterances.append(utterance)

    return utterances