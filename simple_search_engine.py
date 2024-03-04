import wolframalpha

question = input('Question: ')
app_id='AVE2P2-KE4JG6H24G'
client= wolframalpha.Client(app_id)
res=client.query(question)
answer=next(res.results).text
print(answer)