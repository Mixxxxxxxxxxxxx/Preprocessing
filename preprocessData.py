"""
Name: Tamanna Das
StudentId: 33059047
Description: This part of the program is to derive a clean body from the function preprocess line and splitting the file into question and answer text files
Creation date: 21st October 2022
Last modified date: 4th November 2022
"""

import re
def preprocessline(inputLine):
	"""
	extracts lines from the body section of the file data.xml and cleans each line removing sequence of characters,
	and html tags too including urls
	:param inputLine: lines from the file data.xml as strings
	:return: returns a clean body free from special character references
	"""
	try:
		#searching the body in each line of inputfile and replacing special characters and html tags
		line = re.search("Body=\"(.*)\" />", inputLine).group(1).strip()
		line = line.replace("&lt;", "<")
		line = line.replace("&quot;", '"')
		line = line.replace("amp;", "&")
		line = line.replace("&apos;", "'")
		line = line.replace("&gt;", ">")
		line = line.replace("&#xA;", " ")
		line = line.replace("&#xD;", " ")
		clean_body = re.sub(re.compile('<.+?>'), "", line).strip()
		return clean_body
	except AttributeError:
		line = re.search("Body=\"(.*)\" />", inputLine)

def splitFile(inputFile, outputFile_question, outputFile_answer):
	"""
	Splits the input file data.xml into question.txt and answer.txt where only the body part of the lines from input file is only extracted
	:param inputFile: lines from the file data.xml as strings
	:param outputFile_question: file saving only the questions based upon post type 1
	:param outputFile_answer: file saving only the answers based upon post type 2
	:return:returns two text files question.txt and answer.txt
	"""
	#preprocess the original file, and split them into two files.
	#please call preprocessLine() function within this function
	#write you code here
	with open(inputFile, 'r', encoding="utf-8") as file_open:
		with open(outputFile_question, "w", encoding="utf-8") as question:
			with open(outputFile_answer, "w", encoding="utf-8") as answer:
				file_contents = file_open.readlines()
				# for every line finding the part of the line as post_type
				for line in file_contents:
					post_type = re.findall(r'PostTypeId="(\d+)"', line)
					if post_type:
						# extracting the content of post_type and splitting the file into question / answer based on post_type
						post_type = post_type[0]
						if post_type == '1':
							x = preprocessline(line)
							question.write(x + '\n')
						elif post_type == '2':
							x = preprocessline(line)
							answer.write(x + '\n')
	file_open.close()


if __name__ == "__main__":

	f_data = "data.xml"
	f_question = "question.txt"
	f_answer = "answer.txt"

	splitFile(f_data, f_question, f_answer)
