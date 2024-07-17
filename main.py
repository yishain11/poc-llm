from transformers import pipeline
classifier = pipeline("sentiment-analysis")
res = classifier("i am wating for your answer")
print('res: ', res)
