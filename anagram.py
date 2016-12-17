def anagramSolution1(str1, str2):
	if len(str1) < len(str2):
		return False

	list2 = list(str2)

	pos1 = 0
	stillWork = True
	while pos1 < len(str1) and stillWork:
		pos2 = 0
		found = False
		while pos2 < len(list2) and not found:
			if str1[pos1] == list2[pos2]:
				found = True
			else:
				pos2 += 1
		if found:
			list2[pos2] = None
			pos1 += 1
		else:
			stillWork = False

	return stillWork


def anagramSolution2(str1, str2):
	list1 = list(str1)
	list2 = list(str2)
	list1.sort()
	list2.sort()

	allWork = True
	pos1 = 0
	while pos1 < len(list1) and allWork:
		if list1[pos1] == list2:
			pos1 += 1
		else:
			allWork = False

	return allWork


def anagramSolution3(str1, str2):
	list1 = [0] * 26
	list2 = [0] * 26

	for i in str1:
		pos = ord(i) - ord('a')
		list1[pos] += 1

	for i in str2:
		pos = ord(i) - ord('a')
		list2[pos] += 1

	for i in range(len(list1)):
		if list1[i] != list2[i]:
			return False

	return True


print(anagramSolution3('abcd','dcba'))