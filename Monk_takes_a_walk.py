'''
Monk went for a walk in a garden.There are many trees in the garden and each tree has an English alphabet on it.
While Monk was walking, he noticed that all trees with vowels on it are not in good state.
He decided to take care of them. So, he asked you to tell him the count of such trees in the garden.
Note : The following letters are vowels: 'A', 'E', 'I', 'O', 'U' ,'a','e','i','o' and 'u'.
'''
t=input()
for i in range(0,t):
    count=0
    string_input = raw_input()
    char_list=['A', 'E','I','O',"U",'a','e', 'i', 'o', 'u']
    for char in string_input:
        if char in char_list:
            count+=1
    print count
