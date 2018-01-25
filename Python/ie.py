#
#  ___ ___   
# |_ _| __| 
#  | || _|  
# |___|___|
#                                     
#
#
#

def split_into_sentences(text):
    import re
    caps = '([A-Z])'
    prefixes = '(Mr|St|Mrs|Ms|Dr) {0,1}[.]'
    suffixes = '(Inc|Ltd|Jr|Sr|Co)'
    starters = '(Mr|Mrs|Ms|Dr|He\\s|She\\s|It\\s|They\\s|Their\\s|Our\\s|We\\s|But\\s|However\\s|That\\s|This\\s|Wherever)'
    acronyms = '([A-Z][.][A-Z][.](?:[A-Z][.])?)'
    websites = '[.](com|net|org|io|gov)'
    digits = '([0-9])'
    text = ' ' + text + '  '
    text = text.replace('\n', ' ')
    text = re.sub(prefixes, '\\1<prd>', text)
    text = re.sub(websites, '<prd>\\1', text)
    if 'Ph.D' in text:
        text = text.replace('Ph.D.', 'Ph<prd>D<prd>')
    text = re.sub('\\s' + caps + '[.] ', ' \\1<prd> ', text)
    text = re.sub(acronyms + ' ' + starters, '\\1<stop> \\2', text)
    text = re.sub(caps + '[.]' + caps + '[.]' + caps + '[.]', '\\1<prd>\\2<prd>\\3<prd>', text)
    text = re.sub(caps + '[.]' + caps + '[.]', '\\1<prd>\\2<prd>', text)
    text = re.sub(' ' + suffixes + '[.] ' + starters, ' \\1<stop> \\2', text)
    text = re.sub(' ' + suffixes + '[.]', ' \\1<prd>', text)
    text = re.sub(' ' + caps + '[.]', ' \\1<prd>', text)
    text = re.sub(digits + '[.]' + digits, '\\1<prd>\\2', text)
    if '"' in text:
        text = text.replace('."', '".')
    if '!' in text:
        text = text.replace('!"', '"!')
    if '?' in text:
        text = text.replace('?"', '"?')
    text = text.replace('.', '.<stop>')
    text = text.replace('?', '?<stop>')
    text = text.replace('!', '!<stop>')
    text = text.replace('<prd>', '.')
    sentences = text.split('<stop>')
    sentences = sentences[:-1]
    sentences = [ s.strip() for s in sentences ]
    return sentences


def _removeNonAscii(s):
    return ''.join((i for i in s if ord(i) < 128))


def fill_non_ascii(s):
    return ''.join(((i if ord(i) < 128 else ' ') for i in s))


def has_header(filename):
    """
            Determines whether the file has expected header or not. (Word and Tag).
            Args:
                    filename (str): filename for the dataframe we wantt to check
            Returns:
                    boolean : true, has header 'token' and 'Tag'
    """
    import pandas as pd
    df = pd.read_csv(filename, sep='\t')
    col_head = list(df.columns)
    return 'token' in col_head and 'Tag' in col_head


def list_of_word_features(df, word_col = 'token', num_iter = 3):
    list_of_word_features = []
    list_of_word_features.append(word_col)
    for k in range(0, num_iter):
        df['nw_' + str(k)] = add_next_feat(df[word_col], k + 1)
        df['pw_' + str(k)] = add_prev_feat(df[word_col], k + 1)
        list_of_word_features.append('nw_' + str(k))
        list_of_word_features.append('pw_' + str(k))

    return (df, list_of_word_features)


def add_pos_features(df, features = [], num_iter_pos = 3):
    features.append('PoS_num')
    for k in range(0, num_iter_pos):
        df['PoS_num_n_' + str(k)] = add_next_feat_num(df['PoS_num'], k + 1)
        df['PoS_num_p_' + str(k)] = add_prev_feat_num(df['PoS_num'], k + 1)
        features.append('PoS_num_n_' + str(k))
        features.append('PoS_num_p_' + str(k))

    return (df, features)


def apply_features(df, list_of_feats, list_of_word_features, features = []):
    """
            from list of features, apply to the columns of words.
            Args:
                    df (data frame)
                    list_of_feats (func list): list of functions to apply
                    list_of_word_features (str list): list of column names on which to apply fuctions
                    features (str list): original feature list
            returns
                    df (data frame): final table
                    features: final feature list (concat all list of word features)
    """
    import pyprind
    pbar = pyprind.ProgBar(len(list_of_feats), width=60, bar_char='=', title='Creating Features...')
    debug = False
    feat_counter = 0
    for func in list_of_feats:
        for w in list_of_word_features:
            df[func.__name__ + '_' + w] = df[w].apply(lambda x: func(x))
            if len(set(df[func.__name__ + '_' + w].values)) >= 2:
                features.append(func.__name__ + '_' + w)
            elif debug:
                print ('Warning, feature has no info...', func.__name__ + '_' + w)
            else:
                features.append(func.__name__ + '_' + w)

        feat_counter += 1
        pbar.update()

    print (pbar)
    print ('[apply_features]: completed.')
    return (df, features)


def clean_features(df, features, debug = True):
    """
            Will remove all features that have only 1 value in the training set df
            Args:
                    df (dataframe): data frame to test
            Returns:
                    final_features (str list): cleaned list of features
    """
    clean_features = []
    for f in features:
        if len(set(df[f].values)) >= 2:
            clean_features.append(f)
        elif debug:
            print ('Warning, feature has no info...', f)

    return clean_features


def add_next_feat(feat, k):
    """ Will add kth next feature generator.
            Args:
                    feat (list): list of features
            Returns:
    
    """
    return list(feat[k:]) + list([''] * k)


def add_prev_feat(feat, k):
    """ Will add kth previous feature generator.
            Args:
                    feat (list): list of features
            Returns:
    
    """
    return list([''] * k) + list(feat[:-k])


def add_next_feat_num(feat, k):
    """ Will add kth next feature generator.
            Args:
                    feat (list): list of features
            Returns:
                    num list
    """
    return list(feat[k:]) + list([-1] * k)


def add_prev_feat_num(feat, k):
    """ Will add kth previous feature generator.
            Args:
                    feat (list): list of features
            Returns:
                    num list
    """
    return list([-1] * k) + list(feat[:-k])


def generate_class_dicts(classes):
    """ Generate class dictionary to ints and reverse dictionary of ints to class.
    
            Args:
                    classes (str list): List of classes
            Returns:
                    class_dict (dict): classes where key = (string), values = (int)
                    reverse_class_dict (dict): classes where key = (int) , values = (string)
    """
    class_dict = {}
    reverse_class_dict = {}
    counter = 0
    for i in sorted(classes):
        class_dict[i] = counter
        reverse_class_dict[counter] = i
        counter += 1

    return (class_dict, reverse_class_dict)


def postagdict(df, isTest = False):
    pos_class_dict, pos_rev_class_dict = generate_class_dicts(set(df['PoS']))
    df['PoS_num'] = df['PoS'].apply(lambda x: pos_class_dict[x])
    if not isTest:
        tag_class_dict, tag_rev_class_dict = generate_class_dicts(set(df['Tag']))
        df['Tag_num'] = df['Tag'].apply(lambda x: tag_class_dict[x])
    return df


def add_feat(df, list_of_feats, num_iter = 3):
    """
    Add features to given data frame
    
    Input
    -----
    df - dataframe containing word and PoS and maybe Tag
    list_of_feats - list of features to add to dataframe
    num_iter - number of words before and after current word to add more features
    
    Output
    ------
    df - dataframe with more features
    features - list of features added to dataframe
    """
    import time
    a = time.time()
    list_of_word_features = []
    for k in range(0, num_iter_word):
        df['nw_' + str(k)] = add_next_feat(df['token'], k + 1)
        df['pw_' + str(k)] = add_prev_feat(df['token'], k + 1)
        list_of_word_features.append('nw_' + str(k))
        list_of_word_features.append('pw_' + str(k))

    feat_counter = 0
    features = []
    list_of_word_features.append('token')
    for func in list_of_feats:
        for w in list_of_word_features:
            df[w + '_' + str(feat_counter)] = df[w].apply(lambda x: func(x))
            if len(set(df[w + '_' + str(feat_counter)].values)) >= 2:
                features.append(w + '_' + str(feat_counter))
            else:
                continue

        feat_counter += 1
        print ('Completed adding %d features for current set, %d left to complete' % (feat_counter, len(list_of_feats) - feat_counter))

    print (time.time() - a, 'seconds')
    features.append('PoS_num')
    return (df, features)
