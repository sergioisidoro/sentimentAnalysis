import jellyfish

string1 = 'ola mae como estas me chamo rui pedro o'
string2 = 'me pedro mae estas ola rui como chamo'
string3 = ' ola mae tudo optimo e contigo eu sou o rui miguel e tenho o pedro como amigo me'


print string1.replace(string2, '')
print string3.replace(string1, '')
print string1.replace(string3, '')

noise_words_set = {'me', 'pedro', 'mae', 'estas', 'ola', 'rui', 'como', 'chamo'}
print [' '.join(w for w in string3.split() if w.lower() not in noise_words_set)]

features = [feat.split() for feat in [string1, string2, string3]]
test_feat = set(features[0])
test_distance = []

for feat_list in features[1:]:
	i = 0
	a = []
	for word in feat_list:
		if word not in test_feat:
			a.append(word)
		else:
			i += 1
	test_distance.append(abs((len(features[0])-i) - len(a)))

print test_distance
lklk = [1, 2 , 3, 5 , 7, 3, 4, 5, 3]

print lklk.index(3)
i = 2
everything = [ 1, 0]
print (everything[i - 2]+1)/(everything[i -1]+1)
