import csv
import pandas as pd
from faker import Faker
import datetime
import random
from faker.providers import BaseProvider

semesters = ['Fall 2019', 'Fall 2020', 'Fall 2021', 'Fall 2022', 'Spring 2019', 'Spring 2020', 'Spring 2021', 'Spring 2022']
author_list = ['Stephen King', 'Dino Buzzati', 'Jeff VanderMeer', 'Leonora Carrington', 'William Sansom']
words = ['dog', 'cat', 'giraffe', 'elephant', 'amoeba', 'use', 'definition', 'HTML', 'css', 'python']

random_author = str(random.choice(author_list))
print(random_author)

fake = Faker()
Faker.seed(0)

sentences = []

for _ in range(5):
    random_author = str(random.choice(author_list))
    sentences.append(fake.sentence(nb_words=10))
    sentences.append(random_author)


print(sentences)
'''
#print(random.choice(extra_word_list))

def fake_data_generation(records):

    fake = Faker('en-US')
    
    entry = []

    for i in range(records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        semester = random.choice(semesters)
        random_author = random.choice(extra_word_list)     
        print(random_author)   
        text = []
        text.append(random_author)
        print(text)                       
        entry.append({'First Name': first_name, 'Last Name': last_name, 'Semester and Year': semester, 'Text of the Post': text})
    return(entry)

fake_df = pd.DataFrame(fake_data_generation(10))
#print(fake_df['Text of the Post'].head())

matches = fake_df[fake_df['Text of the Post'].isin(['Stephen King', 'Dino Buzzati', 'Jeff VanderMeer', 'Leonora Carrington', 'William Sansom'])]
print(matches)
'''

