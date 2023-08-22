"""
Name:Tamanna Das
Student ID: 33059047
Description: Parser class to create functions that can be used to create visualization
Creation date: 23rd October 2022
Last modified date: 4th November 2022
"""


import re
class Parser:
	"""Parser class to create functions that can be used to create visualization"""
	input_file = "data.xml"
	def __init__(self, inputString):
		"""
		This method acts as a constructor to create the objects of the class parser
		:param inputString: a string from the input file data.xml
		"""
		self.inputString = inputString
		self.ID = self.getID()
		self.type = self.getPostType()
		self.dateQuarter = self.getDateQuarter()
		self.cleanBody = self.getCleanedBody()

	def __str__(self):
		"""
		This method is used to return the parser objects in a specified formatted string
		:return: a string containing all the parameters of class parser
		"""
		#print ID, Question/Answer/Others, creation date, the main content
		#write your code here
		return f"{self.ID};;;{self.type};;;{self.dateQuarter};;;{self.cleanBody}"

	def getID(self):
		"""
		This method is used to get the IDs of the posts in each input string
		:return: Ids of posts in each input string
		"""
		try:
			input_handler = open(self.inputString, 'r', encoding='UTF-8')
		except:
			print("Error in opening file : data.xml.")
		# empty list to store the IDs
		Id_list = []
		lines = input_handler.readlines()
		# for every line finding the part in each line containing the ID using regex and appending it to a list Id_list
		for line in lines:
			Id = re.findall(r'Id="(\d+)"', line)
			if Id:
				Id = Id[0]
				Id_list.append(int(Id))
			input_handler.close()
		return (Id_list)
		

	def getPostType(self):
		"""
		This method is used to get the post types as questions and answers for every post in the input file
		:return: a list of strings containing questions and answers
		"""
		try:
			input_handler = open(self.inputString, 'r', encoding='UTF-8')
		except:
			print("Error in opening file : data.xml.")
		Post_type_Id = []
		lines = input_handler.readlines()
		# for every line we find the content containing post type id and it's contents using regex and appending it to a list post_type_id
		for line in lines:
			post_type = re.findall(r'PostTypeId="(\d+)"', line)
			if post_type:
				post_type = post_type[0]
				# for every post post type is 1 then we retrun the string as question and if it's 2 then we append it as answer in the list
				for post in post_type:
					if post == "1":
						Post_type_Id.append("Question")
					elif post == "2":
						Post_type_Id.append("Answer")
					else:
						Post_type_Id.append("Others")
		#print(Post_type_Id)
			input_handler.close()
		return Post_type_Id



		

	def getDateQuarter(self):
		"""
		This method is used to return a list of strings containing year and quarter for each post
		:return: a list of strings containing "yearquarter"
		"""
		try:
			input_handler = open(self.inputString, 'r', encoding='UTF-8')
		except:
			print("Error in opening file : data.xml.")
		lines = input_handler.readlines()
		Dates = []
		# for every line we find the creation date content using regex
		for line in lines:
			date_type = re.findall(r'CreationDate="(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}).(\d+)"', line)
			# if it's a date_type then we append each line to the list dates
			if date_type:
				Dates.append(date_type)
		list = []
		# for every date in dates we create a list to append only the body of creation date
		for date in Dates:
			list.append(date[0])
		date = []
		# for every item in list we append the 1st part of the string to list date and the 2nd part of the string to list quarter
		for item in list:
			date.append(item[0])
		quarter = []
		for item in list:
			quarter.append(item[1])
		# we create a list_c to join the year and quarter for every creation date in each post and finally append it to a list of string where each string represents a year and it's quarter as '2015Q1' etc.
		list_c = [(date[i], quarter[i]) for i in range(0, len(date))]
		date_quarter = []
		for x in list_c:
			if x[1] == '01' or x[1] == '02' or x[1] == '03':
				date_quarter.append(x[0] + 'Q1')
			elif x[1] == '04' or x[1] == '05' or x[1] == '06':
				date_quarter.append(x[0] + 'Q2')
			elif x[1] == '07' or x[1] == '08' or x[1] == '09':
				date_quarter.append(x[0] + 'Q3')
			elif x[1] == '10' or x[1] == '11' or x[1] == '12':
				date_quarter.append(x[0] + 'Q4')
		return date_quarter

		

	def getCleanedBody(self):
		"""
		This method is used to extract the clean body free from special characters and html tags and urls
		:return: a clean body for each post
		"""
		with open(self.inputString, 'r+', encoding="utf-8") as file_open:
			file_contents = file_open.readlines()
			# extracts lines from the body section of the file data.xml and cleans each line removing sequence of characters,
			# and html tags too including urls and append it to a empty list called lines
			lines = []
			for inputLine in file_contents:
				try:
					line = re.search("Body=\"(.*)\" />", inputLine).group(1).strip()
					line = line.replace("&lt;", "<")
					line = line.replace("&quot;", '"')
					line = line.replace("amp;", "&")
					line = line.replace("&apos;", "'")
					line = line.replace("&gt;", ">")
					line = line.replace("&#xA;", " ")
					line = line.replace("&#xD;", " ")
					clean_body = re.sub(re.compile('<.+?>'), "", line).strip()
					lines.append(clean_body + '\n')
				# return clean_body
				except AttributeError:
					line = re.search("Body=\"(.*)\" />", inputLine)
			return lines
		file_open.close()






	def getVocabularySize(self):
		"""
		This method is used to returns the vocabulary size or unique words in the clean body of each post
		:return: the list of unique words in the cleaned body converted into lower case
		"""
		x = self.getCleanedBody()
		lines = []
		# removing punctuation from the clean body and appending it a empty list lines as seperate lines
		for string in x:
			clean_data = re.sub(r'[^ 0-9a-zA-Z](?!(?<=\d\.)\d)', '', string)
			lines.append(clean_data + '\n')
		# converting each line in lines to lower and finding unique words for each line and appending it to a list unique
		unique = []
		for line in lines:
			line = line.lower().split()
			line = len(set(line))
			unique.append(line)
		# line = len(line)
		# unique.append(line)
		return unique






