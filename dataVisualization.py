"""

Description: This part is used to create visualization by calling methods from the parser class
Creation date: 27th October 2022
Last modified date: 4th November 2022
"""



import numpy as np
import matplotlib.pyplot as plt
from parser_33059047 import *

def visualizeWordDistribution(input_file, outputImage):
	"""
	This method is used to show vocabulary size distribution for each post
	:param input_file: the file given which is data.xml
	:param outputImage: the image / graph as an output
	:return: saves the output image in the local directory
	"""
	# calling the method vocabulary size from class parser to get the number of unique words in each post and sorting the list
	p = Parser(input_file)
	word_count = p.getVocabularySize()
	word_count.sort()
	range_count = []
	new_list = {}
	x = []
	# dividing the vocabulary size into ranges and appending it to the list range_count
	for word in word_count:
		if word in range(0, 11):
			range_count.append("0-10")
		elif word in range(11, 21):
			range_count.append("10-20")
		elif word in range(21, 31):
			range_count.append("20-30")
		elif word in range(31, 41):
			range_count.append("30-40")
		elif word in range(41, 51):
			range_count.append("40-50")
		elif word in range(51, 61):
			range_count.append("50-60")
		elif word in range(61, 71):
			range_count.append("60-70")
		elif word in range(71, 81):
			range_count.append("70-80")
		elif word in range(81, 91):
			range_count.append("80-90")
		elif word in range(91, 101):
			range_count.append("90-100")
		elif word > 100:
			range_count.append("others")
	for x in range_count:
		new_list[x] = (new_list[x] + 1) if (x in new_list) else 1
	# creating a list by extracting the values of ranges from the dictionary
	new_list = list(new_list.values())
	# plotting the graph of vocabulary size of each post with x-axis as ranges and y-axis with the count and saving the image in the local repository

	x = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100', 'Others']
	y = new_list
	plt.bar(x, y, align='center')
	plt.xlabel("Vocabulary Size")
	plt.ylabel("Number of posts with a certain vocabulary size")
	plt.plot()
	plt.savefig(outputImage)



def visualizePostNumberTrend(inputFile, outputImage):
	"""
	This method is used to get the number of questions and answers in each quarter of year
	:param inputFile: the file given which is data.xml
	:param outputImage: the image / graph as an output
	:return: saves the output image in the local directory
	"""

	# calling the post type and date quarter from class parser
	p = Parser(inputFile)
	Type_of_post = p.getPostType()
	Quarters = p.getDateQuarter()
	# zipping together the quarter and post types and converting it to a list and sorting it
	l = list(zip(Quarters, Type_of_post))
	l.sort()
	count_map = {}
	for i in l:
		count_map[i] = count_map.get(i, 0) + 1
	question_answer = {}
	question = {}
	# if others is there in keys of the dictionary we are not counting it and if it's question then we display it
	question_answer = {k: v for k, v in count_map.items() if 'Others' not in k}

	question = {k: v for k, v in count_map.items() if 'Question' in k}
	# creating two lists of keys of the dictionary question and values of the dictionary question
	question_keys = list(question.keys())
	question_count_quarter = list(question.values())
	# creating a list to append the first element in the list question_keys as keys_question
	keys_question = []
	for i in question_keys:
		keys_question.append(i[0])
	# zipping the two lists together to get the number of question posts in each quarter
	ques_dict = dict(zip(keys_question, question_count_quarter))
	# we repeat the same process as done for questions for answers too and then plotting the graph and saving the output in local repository
	answer = {k: v for k, v in count_map.items() if 'Answer' in k}
	answer_count_quarter = list(answer.values())
	answer_keys = list(answer.keys())
	keys_answer = []
	for i in answer_keys:
		keys_answer.append(i[0])
	answer_dict = dict(zip(keys_answer, answer_count_quarter))
	myList = ques_dict.items()
	myList2 = answer_dict.items()
	x2, y2 = zip(*myList2)
	x1, y1 = zip(*myList)
	plt.rcParams["figure.figsize"] = [7.50, 3.50]
	plt.rcParams["figure.autolayout"] = True
	fig = plt.figure()
	plt.plot(x1, y1, label="Question")
	plt.plot(x2, y2, label="Answer")
	plt.xlabel("Quarter per year")
	plt.ylabel("Number of Posts")
	# plt.plot()
	plt.legend()
	spacing = 0.100
	fig.subplots_adjust(bottom=spacing)
	plt.plot()
	#plt.show()
	plt.savefig(outputImage)


if __name__ == "__main__":

	f_data = "data.xml"
	f_wordDistribution = "wordNumberDistribution.png"
	f_postTrend = "postNumberTrend.png"

	visualizeWordDistribution(f_data, f_wordDistribution)
	visualizePostNumberTrend(f_data, f_postTrend)
