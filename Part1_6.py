#問1
author="Camus"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])
#問2
what=input("あなたは何を書きましたか？:")
who=input("あなたは誰に送りましたか？:")

r="私は、昨日{}を書いて、{}に送った！".format(what,who)
print(r)

#問3
print("aldous Huxley was born in 1894".capitalize())

#問4
r="いつ,どこで,誰が".split(",")
print(r)

#問5
word=["The","fox","jumped","over","the","fence","."]
word=" ".join(word)
word=word[0:-2]+"."
print(word)

#問6
word="A screaming comes across the sky"
word=word.replace("s","$")
print(word)

#問7
print("Hemingway".index("m"))

#問8
print("He said 'This pen is mine' without lough.")

#問9
print("Three"+"Three"+"Three")
print("Three"*3)

#問10
test="四月の晴れた寒い日で、時計がどれも十三時を売っていた"
print(test[:10])
print(test[11:])

