#問1
shows=["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for show in shows:
    print(show)
    
#問2
for i in range(25,51):
    print(i)

#問3
shows=["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for index,show in enumerate(shows):
    print(index)
    print(show)

#問4
qs=["Type passward:",
    "Type another password:",
    "This is the last time till reset:"]

n=0
while True:
    print("Invalid Password")
    a=input(qs[n])
    if a == "q":
        break
    n=(n+1)%3

numbers=[11,32,33,15,1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer =="q":
        break
    try:
        answer =int(answer)
    except ValueError:
        print("Guess a number or type q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
        break
    else:
        print("You guessed incorrectly!")
    
#問5
list1=[8,19,148,4]
list2=[9,1,33,83]
times=[]
for i in list1:
    for j in list2:
        times.append(i*j)
print(times)
