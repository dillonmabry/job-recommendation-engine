from rake_nltk import Rake
from docx import Document
from nltk.tokenize import RegexpTokenizer
from logger import Logger
r = Rake()

class NLP(object):

    def __init__(self):
        self.logger = Logger(self.__class__.__name__).get()

    def extract_keywords(self, file):
        try:
            self.logger.info('Processing file for keyword extraction')
            # process Word doc
            doc = Document(file)
            text_list = [para.text for para in doc.paragraphs]
            text = ' '.join(text_list)

            # tokenization
            tokenizer = RegexpTokenizer(r'\w+')
            filtered_text = tokenizer.tokenize(text)
            text = ' '.join(filtered_text)

            # process full text and extract key words
            keywords = r.extract_keywords_from_text(text)
            ranked = r.get_ranked_phrases_with_scores()
            # [(score, list of words)]
            ranked = [item[1] for item in ranked]
            # str -> [words]
            top_ranked = ranked[0].split()
            self.logger.info('Successfully processed file for keywords')
            return top_ranked[:10]

        except Exception as e:
            self.logger.exception(str(e))
