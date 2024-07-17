import pathlib
import textwrap
import google.generativeai as genai
import os
from IPython.display import display
from IPython.display import Markdown

genimi_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=genimi_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("What is the meaning of life?")

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

to_markdown(response.text)