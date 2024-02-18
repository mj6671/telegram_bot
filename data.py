def bot(arr:str):
    arr.lower()
    user_input = arr.split(" ")
    lower_input=[x.lower() for x in user_input]
    print(lower_input)

    sample_input = {
        "maths": "12/3/4",
        "sci": "1/1/2"
    }

    result = []
    ans=[]
    for i in lower_input:
        if i in sample_input:
            result.append(i)
    print(result)
    for j in range(len(result)):
        ans.append(sample_input[result[j]])
        ans.append(result[j])
        
    return "".join(ans)    
             
'''return f"{''.join(result[j])}: {sample_input[result[j]]}"'''
