# NLP First-experience Lab

**Hands-on First Experience of Natural Language Processing**

Authors:
- [Li Peng-Hsuan 李朋軒](https://jacobvsdanniel.github.io) (jacobvsdanniel [at] gmail.com)
- Lai Hong-Sheng 賴鴻昇 (b08611048 [at] ntu.edu.tw)

## Overview

- Solve Natural Language Processing (NLP) tasks
- Apply Large Language Models (LLM) with prompting methods
- Intended for beginners
  - The source codes are short: be expected to understand them fully.
  - Be expected to develop your own program.
  - No GPU requirements or machine learning model engineering: we'll be using online services.

## Environment

- Operating system
  - OS-independent
- System apps
  - Python 3.9 (This is the development environment. Older versions may work.)
- Python packages
  - See *requirements.txt*

```bash
# move to your working directory
cd /path/to/your/working/directory

# Download this repository (If you don't have git, download and unzip the zip file instead.)
git clone https://github.com/hongsheng-lai/nlp_lab.git
cd nlp_lab

# To check python version
python --version

# Install with PyPI, or
pip install -r requirements.txt
# Install with Conda (If you have Anaconda installed)
conda install --file requirements.txt
```


## Lab 1

Prompting Large Language Models (LLM) to solve Natural Language Processing (NLP) tasks

### Lab 1.0. Preparation

#### Step 1. These are the relevant files:

- *lab1_nlp_tasks.py*
- *lab1_config.json*
- *corpora/news/*
- *corpora/prompt/*

#### Step 2. These are the core concepts:
- Tasks
  - Named Entity Recognition (NER)
  - Relation Extraction (REL)
  - Summarization (SUM)
- LLM prompting methods
  - Instruction prompting
  - In-context learning
- Languages
  - English (en)
  - Chinese (zh)

#### Step 3. [Create your OpenAI API Key](https://platform.openai.com/account/api-keys/)

It is a string that looks like "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx".
If you have already fill the google form, you should be able to see your orginiztion: "NTUI2AI".
We already fund the API for you, so you don't need to pay for it. But please don't abuse it.

> Note: Please remember to keep your API key. It only shows once. And do not share it with others.


If you want to try other methods:
- Plan B
  - You can skip Step 3 and 4
  - And try to use the free [website](https://chat.openai.com/) to get results for all the labs.
  - WARNING: A lot of manual labor ahead!
- Plan C
  - You can skip Step 3 and 4
  - And try to download and use a smaller LLM, eg. [this](https://huggingface.co/docs/transformers/main/model_doc/llama2) and [that](https://github.com/HqWu-HITCS/Awesome-Chinese-LLM), locally on your own GPU.
  - WARNING: Humongous engineering work ahead! And performance is not guaranteed!

#### Step 4. Check *lab1_config.json*

Modify it as you wish.

#### Step 5. Run *lab1_nlp_tasks.py*

For example, using linux command line, run
```bash
python lab1_nlp_tasks.py
```

#### Step 6. Check results in *lab1_output/*

For example, in *lab1_output/ner__instruction__en__Russo-Ukrainian_War.txt*:
```
Extract entities of persons, locations, organizations from the article.

Article:
The Russo-Ukrainian War is an ongoing international conflict...

####################################################################################################
# OUTPUT
####################################################################################################

1. Viktor Yanukovych (person)
...
```

The results may vary for each different runs.

### Lab 1.1. Solve existing tasks

#### Objectives

Solve all tasks (NER, REL, SUM) in both languanges (English, Chinese) with both prompting methods (instruction prompting, in-context learning).
> The English prompts is already there; you only need to get output results. And create your own Chinese prompts.
> If you have question about Chinese prompts, please contact TA.

#### Scoring
One task in one language: 5 point.

3 tasks in 2 languages: 30 point.

### Lab 1.2. Solve new tasks

#### Objectives

Solve tasks beyond NER, REL, SUM
- For at least 2 tasks, For inspiration:
  - [CKIP CoreNLP](https://ckip.iis.sinica.edu.tw/service/corenlp/)
  - [Stanford CoreNLP](https://corenlp.run/)
  - [Papers With Code - NLP](https://paperswithcode.com/area/natural-language-processing/)
  - [LDC Catalog](https://catalog.ldc.upenn.edu/)
- In at least 2 languages
  - One of them must be English
  - The other may be Chinese or another language
- You can use use other news materials, add them in corresponding folders, and don't need to provide them in your submission.

#### Scoring
One task in one language: 10 point.

2 tasks in 2 languages: 40 point.


## Lab 2

Using LLM train of thought to achieve complicated behavior

### Lab 2.0. Preparation

#### Step 1. These are the relevant files:

- *lab2_train_of_thought.py*
- *lab2_config.json*

#### Step 2. These are the core concepts:

- Parse LLM output to structured data
  - To use them programmatically beyond chatting with humans.
- Make LLM digest its own outputs
  - To get explanations, spot errors, edit results, do follow-up tasks, etc.

### Lab 2.1. A Druid's Journey

#### Objectives

Play the **修行的德魯伊(A Druid's Journey, 2023)** game
- Run *lab2_train_of_thought.py*
- Achieve the game objectives
- Check results in *lab2_output/* (you should see at least *summary_1.txt*)

#### Scoring
Finish the game: 20 point.

### Submission for Lab 1 + Lab 2.1

```
{student_id}_hw3    # In lowercase
├── lab1_output
|   ├── ner__in-context_learning__en__2023_Hawaii_wildfires.txt
|   ├── ner__in-context_learning__en__Russo-Ukrainian_War.txt
|   └── ...
├── lab1_prompt # You can copy from `corpora/prompt` 
|   ├── ner__in-context_learning__en.txt
|   ├── ner__in-context_learning__zh.txt
|   └── ...
└── lab2_output
    ├── state
    |   └── save_1.json
    ├── summary_1.txt
    └── ...

# Zip it and Summit to NTU COOL
-> {student_id}_hw3.zip
```

### Lab 2.2. Your own game
This lab takes a lot of time (at least 10 hours), so you can submit it before 11/21.
I believe you can learn a lot from this lab, so I highly recommend you to try it.
The TA will give you feedback on your game.
You can have bonus points depending on the quality of your game.

#### Objectives

Create your own game
- It may be a text adventure game or be in other forms of your wish.
- It must use multiple LLM tasks.
- It must require LLM to digest its own outputs.
- It must create an enjoyable review for each game run.
  
#### Scoring
10 point. (Bonus points may be given depending on the quality of your game.)

#### Submission
You can put in on Github or sumbit all the details directly in a zip file to TA.

- Your game
  - Program
  - Data
  - Manual (if needed)
- Runs of your game
  - The final game states and output files of at least one full run
- A report
  - Game description
  - Details on the LLM tasks applied
  - Your discovery

## LICENSE

Copyright © 2023 [Li Peng-Hsuan 李朋軒](https://jacobvsdanniel.github.io) Lai Hong-Sheng 賴鴻昇

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
