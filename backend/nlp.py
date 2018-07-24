from rake_nltk import Rake
from docx import Document
from nltk.tokenize import RegexpTokenizer
r = Rake()

def extract_keywords(file):
    print("Extracting keywords...")
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
    print("Top ranked keywords: "+str(top_ranked[:10]))
    return top_ranked[:10]
