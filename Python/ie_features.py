#
#  ___ ___   ___ ___   _ _____ _   _ ___ ___ ___ 
# |_ _| __| | __| __| /_\_   _| | | | _ \ __/ __|
#  | || _|  | _|| _| / _ \| | | |_| |   / _|\__ \
# |___|___|_|_| |___/_/ \_\_|  \___/|_|_\___|___/
#        |___|                                   
#
# information extraction features/rule based
#
def list_of_features():
	"""
	# returns default list of features

	# # Generate Feature Extraction Functions
	# <body>
	# 1. n_numbers - number of digits in string
	# 2. has_apost - existence of apostrophe "'" in string
	# 3. all_caps - string is all capital letters or not
	# 4. n_caps - number of capital letters in string
	# 5. n_lower - number of lower letters in string
	# 6. n_slashes - number of slashes '/' in string
	# 7. n_bslashes - number of backslashes "/" in string
	# 8. n_letters - length of string
	# 9. n_hyphens - number of hyphens '-' in string
	# 10. n_quots - number of quotes ' "" ' in string
	# 11. has_mm - existence of 'mm' in string
	# 12. has_ml -  existence of 'ml in string
	# 13. has_mg - existence of 'mg' in string
	# 14. non_ascii - string contains non-standard text beyond the standard [128 ASCII character set](http://www.asciitable.com), (eg: trademark symbol)
	# </body>
	"""
	# list of functions to apply to df_train to generate features
	list_of_feats = []

	# create some features

	# create some features
	def n_numbers(inputString):
		nums = [x for x in inputString if x.isdigit()]
		return len(nums)
	list_of_feats.append(n_numbers)

	# def has_apost(inputString):
	#	 return int(any("''" in char for char in inputString))
	# list_of_feats.append(has_apost)

	def all_caps(inputString):
		return int(all(char.isupper() for char in inputString))
	list_of_feats.append(all_caps)

	def n_caps(inputString):
		caps = [x for x in inputString if x.isupper()]
		return len(caps)
	list_of_feats.append(n_caps)

	def n_lower(inputString):
		lower = [x for x in inputString if x.islower()]
		return len(lower)
	list_of_feats.append(n_lower)

	def n_slashes(inputString):
		slashes = [x for x in inputString if x == '/']
		return len(slashes)
	list_of_feats.append(n_slashes)

	def n_bslashes(inputString):
		bslashes = [x for x in inputString if x == '\\']
		return len(bslashes)
	list_of_feats.append(n_bslashes)

	def n_letters(inputString):
		return len(inputString)
	list_of_feats.append(n_letters)

	def n_hyphens(inputString):
		h = [x for x in inputString if x == '-']
		return len(h)
	list_of_feats.append(n_hyphens)

	def n_quots(inputString):
		h = [x for x in inputString if x == '"']
		return len(h)
	list_of_feats.append(n_quots)

	def n_quest(inputString):
		h = [x for x in inputString if x == '?']
		return len(h)
	list_of_feats.append(n_quest)

	def n_bang(inputString):
		h = [x for x in inputString if x == '!']
		return len(h)
	list_of_feats.append(n_bang)

	def n_under(inputString):
		h = [x for x in inputString if x == '_']
		return len(h)
	list_of_feats.append(n_under)

	def n_lparan(inputString):
		h = [x for x in inputString if x == '(']
		return len(h)
	list_of_feats.append(n_lparan)

	def n_rparan(inputString):
		h = [x for x in inputString if x == ')']
		return len(h)
	list_of_feats.append(n_rparan)

	# def non_ascii(inputString):
	#	 if len(inputString) == 0:
	#		 return int(False)
	#	 else:
	#		 # list of 128 ascii characters
	#		 ascii = [chr(i) for i in range(128)]
	#		 for s in inputString:
	#			 if s not in ascii:
	#				 return int(True)
	#	 return int(False)
	# list_of_feats.append(non_ascii)

	#################
	# more features #
	#################

	def is_capitalized(inputString):
		if len(inputString) == 0:
			return int(False)
		else:
			return int(inputString[0].isupper())
	list_of_feats.append(is_capitalized)

	#ascii = [chr(i) for i in range(128)]
	#def non_ascii(inputString):
	#	# list of 128 ascii characters
	#	if len(inputString) == 0:
	#		return int(False)
	#	else:
	#		for s in inputString:
	#			if s not in ascii:
	#				return int(True)
	#	return int(False)
	#list_of_feats.append(non_ascii)

	return list_of_feats

def list_of_features_str():
	"""
		counts how many instances of each in container list
	"""
	import string
	list_of_feats_str = []
	f_names = []
	# let's dynamically create some features

	container = list(set(['7','st','nd','rd','th',
				'4','1','2','3','5','8','9','0',
				'amo','ment','ity',
				 'fiv','on','s','al','at',
				 'tions','ive',
				 'tin','ant','ium','ing','ion','ment','ial'
				 ,'ed','ly','ome','ic','ive','ar',
				 'ry','es','ness',
				 'min','ate','ity'
				 ,'app','prev','pen','inter',
				 'tri','bi'
	]))


	for c in container:
		#func_str = 'def has_'+c+'(inputString): return int("'+c+'" in inputString.lower())'
		#print(func_str)
		#f_names.append('has_'+c)

		func_str = 'def n_'+c+'(inputString): return int(inputString.lower().count("'+c+'"))'

		#funciton names
		f_names.append('n_'+c)

		# full feature function string
		list_of_feats_str.append(func_str)

	#letter_bag = list(string.ascii_lowercase)
	#for c in letter_bag:
	#	func_str = 'def n_'+c+'(inputString): return len([x for x in inputString.lower() if x=="'+c+'"])'
	#	f_names.append('n_'+c)
	#	list_of_feats_str.append(func_str)

	return f_names, list_of_feats_str




######################################
#
# sentence level features
#
######################################
def general_sentence_number(df, word_col='Word'):
	"""
		Adds the sentence number to the dataframe (does NOT reset for documents) 
		- useful for validation purposes to split only sentences.
	"""

	# we want to find the end of the sentences by the '.'
	sentence_end_separators = set(['.',';',':','?','!'])
	sentence_ends = df[df[word_col].isin(sentence_end_separators)].index.tolist()

	# quick function find sentence numbers
	sentence_counter = 0
	sentence_column = []
	sentence_ends_temp = sentence_ends
	for row in range(df.shape[0]):
		sentence_column.append(sentence_counter)
		if len(sentence_ends_temp)>0 and row == sentence_ends_temp[0]:
			sentence_ends_temp.pop(0)
			sentence_counter+=1

	# this creates a column with the sentence number in it
	df['general_sentence_number'] = sentence_column
	return df,'general_sentence_number'



def sentence_number(df,word_col):
	"""
		Adds the sentence number to the dataframe -
		useful for validation purposes.

	"""
	# we want to find the end of the sentences by the '.'
	sentence_ends = df[df[word_col]=='.'].index.tolist()
	full_index = df.index.tolist()

	# quick function find sentence numbers
	sentence_counter = 0
	sentence_column = []
	sentence_ends_temp = sentence_ends
	for row in range(df.shape[0]):
		sentence_column.append(sentence_counter)
		if len(sentence_ends_temp)>0 and row == sentence_ends_temp[0]:
			sentence_ends_temp.pop(0)
			sentence_counter+=1
	# this creates a column with the sentence number in it
	df['Sentence_num'] = sentence_column
	return df,'Sentence_num'



def sentence_number_per_document(df,word_col='token',doc_col='txt_file'):
	"""
		Adds the sentence number to the dataframe -
		useful for validation purposes.

	"""
	# sentence
	# we want to find the end of the document by grouping
	df['row_num_temp'] = df.index.tolist()
	doc_ends = df.groupby(doc_col).min().reset_index()['row_num_temp'].tolist()

	# column no longer needed
	del df['row_num_temp']


	# we want to find the end of the sentences by the '.'
	sentence_ends = df[df[word_col]=='.'].index.tolist()
	full_index = df.index.tolist()

	# quick function find sentence numbers
	sentence_counter = 0
	sentence_column = []
	sentence_ends_temp = sentence_ends
	doc_ends = set(doc_ends)

	for row in range(df.shape[0]):
		# restart at end of sentence
		if len(sentence_ends_temp)>0 and row == sentence_ends_temp[0]:
			sentence_ends_temp.pop(0)
			sentence_counter+=1

		# when you hit the document end, refresh the counter
		if row in doc_ends:
			#doc_ends_temp.pop(0)
			sentence_counter = 0

		sentence_column.append(sentence_counter)

	# this creates a column with the sentence number in it
	df['Sentence_num_per_doc'] = sentence_column
	return df,'Sentence_num_per_doc'


def rev_sentence_number_per_document(df,word_col='token',doc_col='txt_file'):
	"""
		Adds the sentence number to the dataframe -
		useful for validation purposes.

	"""
	# sentence
	df_temp = df.copy(deep=True)

	df_temp = df_temp.reset_index(drop=True)

	# sort backwards
	df_temp = df_temp.sort_index(ascending=False).reset_index(drop=True)

	# sentence
	# we want to find the end of the document by grouping
	df_temp['row_num_temp'] = df_temp.index.tolist()
	doc_ends = df_temp.groupby(doc_col).min().reset_index()['row_num_temp'].tolist()

	# column no longer needed
	del df_temp['row_num_temp']


	# we want to find the end of the sentences by the '.'
	sentence_ends = df_temp[df_temp[word_col]=='.'].index.tolist()
	full_index = df_temp.index.tolist()

	# quick function find sentence numbers
	sentence_counter = 0
	sentence_column = []
	sentence_ends_temp = sentence_ends
	doc_ends = set(doc_ends)

	for row in range(df_temp.shape[0]):
		# restart at end of sentence
		if len(sentence_ends_temp)>0 and row == sentence_ends_temp[0]:
			sentence_ends_temp.pop(0)
			sentence_counter+=1

		# when you hit the document end, refresh the counter
		if row in doc_ends:
			#doc_ends_temp.pop(0)
			sentence_counter = 0

		sentence_column.append(sentence_counter)


	# reverse the sentence
	sentence_column.reverse()

	# this creates a column with the sentence number in it
	df['rev_Sentence_num_per_doc'] = sentence_column
	return df,'rev_Sentence_num_per_doc'







def position_in_sentence(df,word_col='token',doc_col='txt_file'):
	"""
		Adds the sentence number to the dataframe -
		useful for validation purposes.

	"""
	# sentence
	# we want to find the end of the document by grouping
	df['row_num_temp'] = df.index.tolist()
	doc_ends = set(df.groupby(doc_col).min().reset_index()['row_num_temp'].tolist())

	# column no longer needed
	del df['row_num_temp']


	# we want to find the end of the sentences by the '.'
	sentence_ends = set(df[df[word_col]=='.'].index.tolist())
	full_index = df.index.tolist()

	# quick function find sentence numbers
	sentence_counter = 0
	sentence_column = []
	sentence_ends_temp = sentence_ends
	doc_ends = set(doc_ends)

	for row in range(df.shape[0]):

		# when you hit the document end, refresh the counter
		if row in doc_ends or row in sentence_ends:
			#doc_ends_temp.pop(0)
			sentence_counter = 0
		else:
			sentence_counter += 1

		sentence_column.append(sentence_counter)

	# this creates a column with the sentence number in it
	df['position_num_in_doc'] = sentence_column
	return df,'position_num_in_doc'



def rev_position_in_sentence(df,word_col='token',doc_col='txt_file'):
	"""
		position in each sentence

	"""
	# sentence
	df_temp = df.copy(deep=True)

	df_temp = df_temp.reset_index(drop=True)

	# sort backwards
	df_temp = df_temp.sort_index(ascending=False).reset_index(drop=True)

	# sentence
	# we want to find the end of the document by grouping
	df_temp['row_num_temp'] = df_temp.index.tolist()
	doc_ends = df_temp.groupby(doc_col).min().reset_index()['row_num_temp'].tolist()

	# column no longer needed
	del df_temp['row_num_temp']


	# we want to find the end of the sentences by the '.'
	sentence_ends = set(df_temp[df_temp[word_col]=='.'].index.tolist())
	full_index = (df_temp.index.tolist())

	# quick function find sentence numbers
	sentence_counter = 0
	sentence_column = []
	sentence_ends_temp = sentence_ends
	doc_ends = set(doc_ends)

	for row in range(df_temp.shape[0]):
		# restart at end of sentence
		#if len(sentence_ends_temp)>0 and row == sentence_ends_temp[0]:
		#	sentence_ends_temp.pop(0)
		#	sentence_counter+=1

		# when you hit the document end, refresh the counter
		if row in doc_ends or row in sentence_ends:
			#doc_ends_temp.pop(0)
			sentence_counter = 0
		else:
			sentence_counter+= 1
		sentence_column.append(sentence_counter)


	# reverse the sentence
	sentence_column.reverse()

	# this creates a column with the sentence number in it
	df['rev_position_num_in_doc'] = sentence_column
	return df,'rev_position_num_in_doc'





def word_counter_features(df, section_headers, word_col='token',doc_col='txt_file'):
	#
	# function counts the number of words after section headers that a particular token is
	# the counter resets when it hits either a section header or a new document
	#
	#print('[ie]: word_counter_features...')

	# init dict of filename, section header and index of occrence
	dicts = {}

	# get all tokens as a list of tokens
	l = df[word_col].values
	l = [i.lower() for i in l]

	# do only lower case
	section_headers = [i.lower() for i in section_headers]
	section_headers = set(section_headers)

	# get the file index numbers
	df['temp_index'] = df.reset_index().index
	file_index = set(df.groupby(doc_col).first()['temp_index'].tolist())
	del df['temp_index']

	# init for this filename
	dicts = {}

	# loop over the sections we will search for
	import pyprind
	#pbar = pyprind.ProgBar(len(section_headers), width=60, bar_char='=',title='[ie]: finding section headers -> '+str(len(section_headers)))

	features = []
	# first find where everything is
	for col in section_headers:
		#pbar.update()
		feature_name = 'tokens_after_subset_'+col

		# find the indices
		#indices = set([i for i, x in enumerate(l) if col in x])

		# loop over the rows, if in index, then reset counter
		counter = 0
		col_list = []
		for i in range(df.shape[0]):
			if i in file_index:
				counter = 0

			elif col in l[i]:
				counter += 1
			col_list.append(counter)

		df[feature_name] = col_list
		features.append(feature_name)

	return df, features



######################################
#
# Document level features
#
######################################
def section_header_features(df, section_headers, word_col='token',doc_col='txt_file'):
	#
	# function counts the number of words after section headers that a particular token is
	# the counter resets when it hits either a section header or a new document
	#
	#print('[ie]: section_header_features...')
	# this really needs to be abstracted... to be a common tokenizer
	from nltk.tokenize.regexp import RegexpTokenizer
	#tokenizer = RegexpTokenizer('[\-\.\,\;]|\w+|\$[\d\.]+|\S+')
	tokenizer = RegexpTokenizer('[\$\-\.\,\;]|\w+|\$[\d\.]+|\S+')


	# init dict of filename, section header and index of occrence
	dicts = {}

	# get all tokens as a list of tokens
	l = df[word_col].values
	#l = [i.lower() for i in l]

	# do only lower case
	#section_headers = [i.lower() for i in section_headers]
	section_headers = set(section_headers)

	# init for this filename
	dicts = {}

	# loop over the sections we will search for
	import pyprind
	import brat
	#pbar = pyprind.ProgBar(len(section_headers), width=60, bar_char='=',title='[ie]: finding section headers -> '+str(len(section_headers)))

	# first find where everything is
	for h in section_headers:
		#pbar.update()
		# tokenize into list
		sl = tokenizer.tokenize(h)
		#sl = [i.lower() for i in sl]

		# final all instances in the text of sl, and take only the start
		sts = [x[0] for x in brat.find_all_sub_list(sl, l)]

		# keep this list in the dict
		dicts[h] = sts

	#print(pbar)

	df['temp_index'] = df.reset_index().index
	file_index = set(df.groupby(doc_col).first()['temp_index'].tolist())
	del df['temp_index']

	features = []

	# then save to the data frame
	for col in dicts:
		feature_name = 'tokens_after_'+col
		#print('[ie]: section_header_features,',feature_name)
		col_list = []
		counter = 0

		# set of end points where the substring detected
		d = set(dicts[col])

		# loop over the rows, if in index, then reset counter
		counter = 0
		for i in range(df.shape[0]):
			if i in file_index:
				counter = 0
			elif i in d:
				counter += 1
			col_list.append(counter)

		df[feature_name] = col_list
		features.append(feature_name)

	return df, features




# fixme
def position_in_document(df, doc_col='txt_file'):
	"""
		Adds the sentence number to the dataframe, restarts count for each doc_col group - useful feature

	"""

	# we want to find the end of the document by grouping
	df['row_num_temp'] = df.index

	# get indices
	sentence_ends = set(df.groupby(doc_col).min().reset_index()['row_num_temp'].tolist())

	full_index = df.index.tolist()

	# delete the temp column
	del df['row_num_temp']

	# quick function find sentence numbers
	sentence_counter = 0
	sentence_column = []
	sentence_ends_temp = sentence_ends
	for row in range(df.shape[0]):
		if row in sentence_ends:
			sentence_counter = 0
		else:
			sentence_counter+= 1
		sentence_column.append(sentence_counter)



	# this creates a column with the sentence number in it
	df['Doc_pos_num'] = sentence_column
	return df,'Doc_pos_num'

#
def rev_position_in_document(df, doc_col='txt_file'):
	"""
		Adds the sentence number to the dataframe - useful for validation purposes.

	"""
	df_temp = df.copy(deep=True)

	# reverse the data framae
	df_temp = df_temp.reset_index(drop=True)

	# sort backwards
	df_temp = df_temp.sort_index(ascending=False).reset_index(drop=True)

	# sort backwards
	#df_temp = df_temp.sort_values(by='index',ascending=False).reset_index(drop=True)


	# we want to find the end of the document by grouping
	df_temp['row_num_temp'] = df_temp.index.tolist()

	# get indices
	sentence_ends = set(df_temp.groupby(doc_col).min().reset_index()['row_num_temp'].tolist()  )
	full_index = df_temp.index.tolist()


	# delete the temp column
	del df_temp['row_num_temp']

	# quick function find sentence numbers
	sentence_counter = 0
	sentence_column = []
	sentence_ends_temp = sentence_ends
	for row in range(df_temp.shape[0]):
		if row in sentence_ends:
			sentence_counter = 0
		else:
			sentence_counter+= 1

		sentence_column.append(sentence_counter)

	# reverse the sentence
	sentence_column.reverse()

	# this creates a column with the sentence number in it
	df['rev_Doc_pos_num'] = sentence_column
	return df,'rev_Doc_pos_num'
