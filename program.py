import statistics

print("Sinav notlari puanlayici")
print("Bittiginde isim soruldugunda, cevap olarak 'exit' yazin")
ders_adi = input("Course name: ")
ders_adi = ders_adi.replace(" ","-")
yil = input("Year: ")
term = input("Term: (fall or spring): ")
sinav_turu = input("Type of the exam: ")
filename = f"{yil}-{term}-{ders_adi}-{sinav_turu}"

def main():
	global filename
	soru_sayisi = int(input("soru sayisi: > "))
	mydict = {}
	while(True):
		isim = input("isim > ")
		if isim == "exit":
			break
		puanlar = []
		for i in range(soru_sayisi):
			ans = int(input(f"q{i+1}: "))
			puanlar.append(ans)
		toplam = sum(puanlar)
		mydict[isim] = toplam
	analyze(mydict)
	writeToFile(mydict, filename)
	print("Written to file alphabetically sorted...")

def get_max_grade(param):
	name = max(param, key=param.get)
	score = param[name]
	#print(f"Maximum grade: {name} with a score of {param[name]}")
	return (name, score)

def get_min_grade(param):
	name = min(param, key=param.get)
	#print(f"Minimum grade: {name} with a score of {param[name]}")
	return (name, param[name])

def get_average_grade(param):
	ortalama = sum(param.values()) / len(param)
	#print(f"Ortalama: {ortalama}")
	return ortalama

def std_dev(mydict):
	deviation = statistics.stdev(list(mydict.values()))
	return deviation

def analyze(param):
	max_grade = get_max_grade(param)
	min_grade = get_min_grade(param)
	ortalama_grade = get_average_grade(param)
	std_deviation = std_dev(param)

	print(f"Out of {len(param)} students: ")
	print("Max grade: ", max_grade)
	print("Min grade: ", min_grade)
	print("Ortalama: ", ortalama_grade)
	print("Std Deviation: ", std_deviation)

def writeToFile(param, filename):
	sorted_data = dict(sorted(param.items()))
	#print(sorted_data)
	f = open(f"{filename}.txt","w")
	for data in sorted_data:
		f.write(f"{data}: {sorted_data[data]}\n")
	return


main()