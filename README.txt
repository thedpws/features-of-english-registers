README

The files in this directory are all original work by Aeyzechiah Vasquez and Reese Porter, aside from the auto-generated Jupyter Notebook file main.ipynb.
The directory structure and its files are described below.

(project folder)
│   main.ipynb     - the main Jupyter Notebook. Contains all the model-training, evaluating, and visualizing.
│   dataframe.py   - contains code to transform a list of spacy.Doc into a pandas.Dataframe
│   README.txt     - README.txt
│   
+───data_collection         - three data-collecting modules, one for each register in question
│       academic.py         - query academic data from arXiv.org.
│       conversational.py   - query Cornell's movie corpus for conversations
│       news.py             - query the Reuter corpus for news articles
│       
\───tagging
        dependency_distance.py   - tags list of spacy.Doc.Token with their dependency distance
        f_score.py               - tags spacy.Doc with their f (formality) score
        tagger.py                - houses a complete composite tag function and its smaller tagging functions
        
