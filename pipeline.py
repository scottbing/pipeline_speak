# -*- coding: iso-8859-15 -*-
import os, sys
from transformers import pipeline
from query import askQuestion, getAnswer

def main():

    # get the volcano corpus
    with open('volcanic.corpus', encoding="utf8") as file:
        context = file.read().replace('\n', '')

    # endless loop - keep soliticitng for questions
    while(True):
        # say greeting
        question = askQuestion()

        # Generating an answer to the question in context
        qa = pipeline("question-answering")
        answer = qa(question=question, context=context)

        getAnswer(answer)


if __name__ == "__main__":
    main()
