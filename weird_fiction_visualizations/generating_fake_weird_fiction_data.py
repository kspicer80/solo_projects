import csv
import pandas as pd
pd.options.display.max_colwidth = 300
from faker import Faker
import datetime
import random
from pathlib import Path

semesters = ['Fall 2019', 'Fall 2020', 'Fall 2021', 'Fall 2022', 'Spring 2019', 'Spring 2020', 'Spring 2021', 'Spring 2022']
author_list = ['Stephen King', 'Dino Buzzati', 'Jeff VanderMeer', 'Leonora Carrington', 'William Sansom']

def fake_data_generation(num_of_records):
    fake = Faker('en-US')
    dataframe = []
    for i in range(num_of_records):
        sentences = []
        first_name = fake.first_name()
        last_name = fake.last_name()
        semester = random.choice(semesters)
        sentences.append(fake.sentence(10))
        sentences.append(random.choice(author_list))
        joined_sentence = ' '.join(sentences)
        dataframe.append({'First Name': first_name, 'Last Name': last_name, 'Semester and Year': semester, 'Text of the Post': joined_sentence})
    return(dataframe)

fake_df = pd.DataFrame(fake_data_generation(100))
fake_df.to_csv('fake_dataset_csv.csv', index=False)



