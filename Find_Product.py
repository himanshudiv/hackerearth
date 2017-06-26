n=input()
a=map(int, raw_input().split())
ans=1
for i in a:
    ans= (ans*i)%(10**9 + 7)
print ans
