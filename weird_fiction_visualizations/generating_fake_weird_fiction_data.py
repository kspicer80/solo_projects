import csv
import pandas as pd
pd.options.display.max_colwidth = 300
from faker import Faker
import datetime
import random 
from random import randint

semesters = ['Fall 2019', 'Fall 2020', 'Fall 2021', 'Fall 2022', 'Spring 2019', 'Spring 2020', 'Spring 2021', 'Spring 2022']
author_list = ['Stephen King', 'Dino Buzzati', 'Jeff VanderMeer', 'Leonora Carrington', 'William Sansom']

def fake_canvas_data_generation(num_of_records):
    fake = Faker('en-US')
    dataframe = []
    for i in range(num_of_records):
        sentences = []
        replies = []
        course_id = 9999999
        topic_id = 1111111
        topic_title = 'Week 0: Introductions (Section Z)'
        entry_id = fake.unique.first_name() + fake.unique.last_name()
        semester = random.choice(semesters)
        sentences.append(fake.sentence(10))
        sentences.append(random.choice(author_list))
        entry_message = ' '.join(sentences)
        entry_word_count = randint(100, 999)
        reply_id = fake.first_name() + fake.last_name()
        replies.append(fake.sentence(5))
        replies.append(random.choice(author_list))
        reply_message = ' '.join(replies)
        reply_word_count = randint(100, 999)

        dataframe.append({
            'course_id': course_id, 
            'topic_id': topic_id, 
            'topic_title': topic_title, 
            'entry_id': entry_id,
            'Semester and Year': semester, 
            'entry_message': entry_message,
            'entry_word_count': entry_word_count,
            'reply_id': reply_id, 
            'reply_message': reply_message,
            'reply_word_count': reply_word_count})
    return(dataframe)

fake_df = pd.DataFrame(fake_canvas_data_generation(100))
fake_df.to_csv('fake_dataset_csv.csv', index=False)



