import os
try:
    import PyPDF2
except:
    os.system(f'cmd /c "pip install PyPDF2"')
    import PyPDF2
try:
    from openai import OpenAI
    import ast
except:
    os.system(f'cmd /c "pip install openai"')
    from openai import OpenAI
    import ast
try:
    from pyttsx3 import Engine
except:
    os.system(f'cmd /c "pip install pyttsx3"')
    from pyttsx3 import Engine
def Speak(text):
    engine = Engine()
    engine.say(text)
    engine.runAndWait()
    return
def gpt(txt):
    try:
        client = OpenAI()
        api_key="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"
        response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": f"{txt}"}
        ]
        )
        x=ast.literal_eval(response.choices[0].message.content)
        lst=list(x.keys())
        res=x[f'{lst[0]}']
        return res
    except Exception as e:
        return f"error code {e}"
def paragraph(listinp):
    if len(listinp)==1:
        return listinp[0]
    return f"{listinp[0]}'\n'{paragraph(listinp[1:])}"
def summary(paralist):
    para=paragraph(paralist)
    query=f'''summarise the following paragraph to less than 500 words :\n{para}'''
    result=gpt(query)
    return result
file = open('G:\Codes\general projects\PDF-Reader\sample.pdf', 'rb')
reader = PyPDF2.PdfReader(file)
l=int(len(reader.pages))
lis=[]
for i in range(l):
    page = reader.pages[i]
    lis.append(page.extract_text())
for i in range(len(lis)):
    lis[i]=lis[i].replace('\n',' ') 
print(summary(lis))
Speak(summary(lis))


# closing the pdf file object
file.close()
