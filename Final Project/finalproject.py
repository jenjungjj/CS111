#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:09:02 2020

@author: jennyjung
"""
import math

def clean_text(txt):
    """ helper function that returns a list containing the words 
        in parameter txt after it has been "cleaned"
    """
    clean = txt.lower().split()
    for i in range(len(clean)): 
        if clean[i][-1] in """.,?"'!""":
            clean[i] = clean[i].replace(clean[i][-1],'')
    return clean

def sample_file_write(filename):
    """ A function that demonstrates how to write a 
        Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}
    f = open(filename, 'w')
    f.write(str(d))
    f.close()
    
def sample_file_read(filename):
    """ A function that demonstrates how to read 
        a Python dictionary from a file.
    """
    f = open(filename, 'r')
    d_str = f.read()
    f.close()
    
    d = dict(eval(d_str))
    
    print("Inside the newly-read dictionary, d, we have:")
    print(d)
    
def stem(s):
    """ returns the stem of the given parameter s
    """
    stem = ''
    if s[-3: ] == 'ies':
        stem += s[0:-3]
        stem += 'y'
    elif s[-2: ] == 'es' or s[-2: ] == 'er' or s[-2: ] == 'ed':
        stem += s[0:-2]
    elif s[-1] == 'y':
        stem += s[0:-1]
        stem += 'i'
    elif s[-3: ] == 'ing' or s[-3: ] == 'ers':
        stem += s[0:-3]
    elif s[-4: ] == 'tion' or s[-4: ] == 'sion':
        stem += s[0:-4]
    elif s[0:1] == 'un' or s[0:1] == 'im' or s[0:-1] == 're' or s[0:-1] == 'em':
        stem += s[2:]
    elif s[0:2] == 'mis' or s[0:2] == 'dis' or s[0:2] == 'pre':
        stem += s[3: ]
    elif s[-1] == 's':
        stem += s[0:-1]
    else:
        stem += s
    return stem

def compare_dictionaries(d1, d2):
    """ returns the log similarity score of the input dictionaries d1 and d2
    """
    score = 0
    total = sum(d1.values())
    key_listd1 = list(d1)
    key_listd2 = list(d2)
    for i in range(len(key_listd2)):
        if key_listd2[i] in key_listd1:
            each_score = d1.get(key_listd2[i]) / total
            score += d2.get(key_listd2[i]) * math.log(each_score)
        else:
            each_score = 0.5 / total
            score += d2.get(key_listd2[i]) * math.log(each_score)
    return score
        

class TextModel:
    def __init__(self, model_name):
        """ constructor that initializes the name, words, and word_lengths
            words is a dictionary that records the number of times each word appears in text
            word_lengths is a dictionary that records the number of times each word length appears
            takes in the param model_name which is a string 
            stems records the frequency of number of times each stem appears
            sentence_lengths records the number of times each sentence length appears
            first_letter records the number of times first letter of each words appears. 
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        
        self.stems = {}
        self.sentence_lengths = {}
        self.first_letter = {}
        
    def __repr__(self):
       """ Returns a string that represents the TextModel object
       """
       s = 'text model name: ' + self.name + '\n'
       s += '  number of words: ' + str(len(self.words)) + '\n'
       s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
       s += '  number of stems: ' + str(len(self.stems)) + '\n'
       s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
       s += '  number of first letters: ' + str(len(self.first_letter)) +'\n'
       return s
   
    def add_string(self, s):
        """ Analyzes the string txt and adds its pieces
            to all of the dictionaries in this text model.
        """
        word_list = clean_text(s)
        sent_list = s.split(""".,?"'!""")
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
                
            if len(w) <= 3:
                if w not in self.stems:
                    self.stems[w] = 1
                else:
                    self.stems[w] += 1
            else:
                if stem(w) not in self.stems:
                    self.stems[stem(w)] = 1
                else:
                    self.stems[stem(w)] += 1
            if w[0] not in self.first_letter:
                self.first_letter[w[0]] = 1
            else:
                self.first_letter[w[0]] += 1
        for w in sent_list:
            if len(w.split()) not in self.sentence_lengths:
                self.sentence_lengths[len(w.split())] = 1
            else:
                self.sentence_lengths[len(w.split())] += 1
            
    def add_file(self, filename):
        """ adds all of the text in file identified by the filename
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        
        text = self.add_string(text)
        
    def save_model(self):
        """ saves TextModel object by writing its feature dictionaries to files
        """
        f = open(self.name + '_words', 'w')
        f.write(str(self.words))
        f.close() 
        
        file = open(self.name + '_word_lengths', 'w')
        file.write(str(self.word_lengths))
        file.close()
        
        f2 = open(self.name + '_stems', 'w')
        f2.write(str(self.stems))
        f2.close()
        
        f3 = open(self.name + '_sentence_lengths', 'w')
        f3.write(str(self.sentence_lengths))
        f3.close()
        
        f4 = open(self.name + '_first_letter', 'w')
        f4.write(str(self.first_letter))
        f4.close()
        
    def read_model(self):
        """ reads the stored dictionaries and assigns them to attributes
            of the called TextModel
        """
        f = open(self.name + '_words', 'r')
        d_str = f.read()
        f.close()
        self.words = dict(eval(d_str))
        
        file = open(self.name + '_word_lengths', 'r')
        d = file.read()
        file.close()
        self.word_lengths = dict(eval(d))
        
        f2 = open(self.name + '_stems', 'r')
        d2 = f2.read()
        f2.close()
        self.stems = dict(eval(d2))
        
        f3 = open(self.name + '_sentence_lengths', 'r')
        d3 = f3.read()
        f3.close()
        self.sentence_lengths = dict(eval(d3))
        
        f4 = open(self.name + '_first_letter', 'r')
        d4 = f4.read()
        f4.close()
        self.first_letter = dict(eval(d4))
        
        
    def similarity_scores(self, other):
        """ returns a list of log similarity scores computed between self and other.
        """
        word_score = compare_dictionaries(other.words, self.words)
        word_length_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sent_length_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        first_letter_score = compare_dictionaries(other.first_letter, self.first_letter)
        log_sim_scores = [word_score, word_length_score, stems_score, sent_length_score, 
                                                                  first_letter_score]
        return log_sim_scores
    
    def classify(self, source1, source2):
        """ compares TextModel self to the two other TextModels (source1 and source2)
            and determines which of the two is the more likely source of the called TextModel
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print("scores for ", source1.name, ": ", scores1)
        print("scores for ", source2.name, ": ", scores2)
        
        num_higher1 = 0
        num_higher2 = 0
        for i in range(len(scores1)):
            if abs(scores1[i]) > abs(scores2[i]):
                num_higher1 += 1
            else:
                num_higher2 += 1
        if num_higher1 > num_higher2:
            print(self.name, " is more likely to have come from ", source1.name)
        else:
            print(self.name, " is more likely to have come from ", source2.name)
            
            
def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    
def run_tests():
    """ returns the result of the tests after comparing 
        which sources the TextModel seems to be more likely.
    """
    source1 = TextModel('studio ghibli')
    source1.add_file('studio_ghibli.txt')

    source2 = TextModel('disney')
    source2.add_file('disney.txt')

    new1 = TextModel('an101')
    new1.add_file('an101_paper.txt')
    new1.classify(source1, source2)
        
    new2 = TextModel('frozen')
    new2.add_file('frozen.txt')
    new2.classify(source1, source2)
        
        
        
        

        

        
        
        



        
       
       