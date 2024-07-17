from transformers import pipeline

pipe = pipeline("text-generation", model="tiiuae/falcon-180B")
res = pipe("please generate a hard python question with 3 wrong answers and 1 correct one, with explenations for each")
print('res: ', res)
