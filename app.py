import numpy as np
import pandas as pd
import spacy


from flask import Flask
from flask_restful import Resource, Api, reqparse


TITLE_PROP = 0.8
DESCRIPTION_PROP = 0.2

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('query', type=str)

nlp = spacy.load("en_core_web_md")
data = pd.read_excel("static/data.xlsx", index_col=0)
title_docs = [nlp(str(doc)) for doc in data['title']]
description_docs = [nlp(str(doc)) for doc in data['description']]


def get_suggestion(query):
    query = nlp(query)

    title_similarities = [query.similarity(doc) for doc in title_docs]
    description_similarities = [query.similarity(doc) for doc in description_docs]
    combined_similarities = list(enumerate(TITLE_PROP * np.array(title_similarities) +
                                           DESCRIPTION_PROP * np.array(description_similarities)))
    combined_similarities.sort(reverse=True, key=lambda x: x[1])

    most_similar = [{'title': data['title'].iloc[i], 'similarity': sim} for i, sim in combined_similarities[:10]]
    return most_similar


class QuerySuggestion(Resource):
    def post(self):
        args = parser.parse_args()
        suggestion = get_suggestion(args['query'])
        return suggestion, 201


api.add_resource(QuerySuggestion, '/query')


if __name__ == '__main__':
    app.run(debug=True)
