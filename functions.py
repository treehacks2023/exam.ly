from PyPDF2 import PdfMerger, PdfReader
import openai
import re


def merge_files(filenames:list, merged_filename:str):
  merger=PdfMerger()
  for filename in filenames:
    merger.append(filename)
  merger.write(merged_filename+'.pdf')
  merger.close()

def add_prompt(text_file:str):
  prompt_intro='Generate new questions based on the following questions, in the format of 1., 2. etc. Do not answer them:'
  final_query=prompt_intro+'\n'+text_file
  return final_query

def textify(filename:str):
  pdf_file = open(filename, 'rb')
  read_pdf = PdfReader(pdf_file)
  fulltext = ""
  for page in read_pdf.pages:
    part = page.extract_text()
    fulltext += part
  return fulltext


class QuestionGenerator:
    def __init__(self, model_engine, openai_api_key):
        self.model_engine = model_engine
        self.openai_api_key = openai_api_key

    def generate_questions(self, prompt, max_tokens, temperature, top_p, frequency_penalty, presence_penalty):
        """
        Generates questions based on the prompt provided.
        """
        openai.api_key = self.openai_api_key
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
        response = completion.choices[0].text
        return response

def add_newlines(text):
  # new_text = re.sub(r'(?<!^)(\d+\.)', r'\n\1', text)
  # return new_text
  matches = re.finditer(r'\d+\.\s', text)
  indices = [match.start() for match in matches]

  result = [text[i:j] for i, j in zip([0]+indices, indices+[None])][1:]
  final_list=[]
  for elem in result:
    final_list.append(re.sub(r'\d+\.\s', '', elem, count=1))

  return final_list