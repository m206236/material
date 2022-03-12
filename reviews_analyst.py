data = []
count = 0
with open ("reviews.txt", "r") as f :
    for line in f:
        count +=1
        data.append (line)
        if count % 1000 == 0:
           print (len (data))
print('total number of data are ', len(data))
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print ("average length of reviews are ", sum_len / len (data))

new = []
for d in data:
	if len(d) < 100 :
		new.append (d)
print ("have", len (new), "reviews length less than 100")
print (new[0])

good = []
for d in data:
	if "good" in d:
		good.append(d)
print("there have", len(good),"include good word")
print(good[0])