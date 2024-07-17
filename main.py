# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="TheBloke/WizardLM-7B-uncensored-GPTQ")
res = pipe("gemerate a python question with 3 wrong answer and 1 correct one, with explanations for each")
print('res: ', res)