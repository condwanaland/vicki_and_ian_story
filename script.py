#!/usr/bin/env python3

import os
import yaml
import functions as F

I_EMAIL = os.environ.get("I_EMAIL")
V_EMAIL = os.environ.get("V_EMAIL")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PWORD = os.environ.get("SENDER_PWORD")

with open('next_question.yml') as file:
    try:
        next_q = yaml.safe_load(file)   
    except yaml.YAMLError as exc:
        print(exc)

with open('questions.yml') as file:
    try:
        questions = yaml.safe_load(file)   
    except yaml.YAMLError as exc:
        print(exc)

q_no = next_q["next_question"]

cur_question = questions["questions"][q_no]

v_message = F.init_email(SENDER_EMAIL, "condwanaland@gmail.com", q_no)

F.send_email(v_message, "condwanaland@gmail.com")



