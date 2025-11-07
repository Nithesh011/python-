def top_n_words(text:str,N:int):
    d={}
    clean="".join(i for i in text if i.isalpha() or i.isspace())
    spliting=clean.split()
    for i in spliting:
        d[i]=d.get(i,0)+1 
    sorting=sorted(d.items(), key = lambda x: x[1],reverse=True)
    return sorting[:N]
    
text = """
Data engineers design, build, and maintain data pipelines.
They ensure that data is reliable, accessible, and efficient.
Data
"""

N=3
print(top_n_words(text,N))

--------------------------------------------------OR------------------------------------------------------------------------------------------------
import re
N=3
d={}
text = """
Data engineers design, build, and maintain data pipelines.
They ensure that data is reliable, accessible, and efficient.
Data pipelines help companies make better decisions.
"""
text=re.sub(r'[^a-zA-Z\s]','',text).lower()
splits=text.split()

for i in splits:
    d[i]=d.get(i,0)+1 
sorting = sorted(d.items(),key=lambda x: x[1],reverse=True)
print(sorting[:N])
