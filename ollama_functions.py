from ollama import embed, chat   

embedding = embed("custom_qwen", input=["Here is an example sentence", "Here is second one"])
# print(len(embedding['embeddings'][0]))  

response = chat(model='qwen3:0.6b', messages=[
    {
        'role': 'user',
        'content': 'Why did the chicken cross the road?'
    }
])
print(response.message['content'])