with open('filtered_words.txt','r') as f:
    text=f.read()
word=text.split('\n')
judge=True
while(1):
    k=input('enter to test:')
    for i in word:
        if(k==i):
            judge=False
    if(judge==False):
        print('Not OK')
    else:
        print('OK')
    judge=True

