# Basic imports
from flask import Flask
import json

# CLTK Corpora
from cltk.corpus.utils.importer import CorpusImporter

corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_models_cltk')
corpus_importer.import_corpus('latin_pos_lemmata_cltk')
corpus_importer.import_corpus('latin_lexica_perseus')
corpus_importer.import_corpus('latin_treebank_index_thomisticus')
corpus_importer.import_corpus('latin_treebank_perseus')

# CLTK Stemmer
from cltk.stem.latin.stem import Stemmer

# CLTK Decliner
from cltk.stem.latin.declension import CollatinusDecliner

# CLTK Lemmatizer
from cltk.stem.lemma import LemmaReplacer

# CLTK POSTagger
from cltk.tag.pos import POSTag





app = Flask(__name__)
# ROUTE: TAG
@app.route("/tag/<form>")
def tag(form):
    tagger = POSTag("latin")
    list = tagger.tag_crf(form)
    return json.dumps(list)
# ROUTE: STEM
@app.route("/stem/<form>")
def stem(form):
    stemmer = Stemmer()
    string = stemmer.stem(form)
    return json.dumps(string)
# ROUTE DECLINE
@app.route("/decline/<form>")
def decline(form):
    decliner = CollatinusDecliner()
    list = decliner.decline(form)
    return json.dumps(list)
# ROUTE LEMMATIZE
@app.route("/lemmatize/<form>")
def lemmatize(form):
    lemmatizer = LemmaReplacer('latin')
    list = lemmatizer.lemmatize(form)
    return json.dumps(list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
