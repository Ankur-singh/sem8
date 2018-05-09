def tagged_sents_to_readable_file(tagged_sents, file_name):
	text = ""
	for i in tagged_sents:
		for j in i:
			text += str(j[0])+'\t\t'+str(j[1])+'\n'

	f = open(file_name, "w")
	f.write(text)
	f.close()
	
	return text


