import ollama 

msg=[{"role":"user","content":"내이름이 뭐라고" }]


response_1=ollama.chat(
    model="gemma2:9b"
    ,
    messages=msg
)

print(response_1["message"])

msg.append({"role":"user","content":"내이름 당장 말해"})

response_2=ollama.chat(
    model="gemma2:9b",
    messages=msgp
)
print(response_2["message"])

print(msg)