from stop_words import get_stop_words
from nltk.corpus import stopwords
from nltk.tag import pos_tag
import codecs

stop_words = list(get_stop_words('en'))  # About 900 stopwords
nltk_words = list(stopwords.words('english'))  # About 150 stopwords
stop_words.extend(nltk_words)

output = [w for w in stop_words if not w in nltk_words]
unwanted_words = ['united', 'states', 'supreme', 'court', 'footnote', 'of', 'et', 'al',
                  'thus', 'since', 'hence', 'shall', 'upon']
stop_words.extend(unwanted_words)

for i in range(1, 2501):
    read_file = 'RawCases/' + str(i) + '.txt'
    write_file = 'StopWordsRemovedCases/' + str(i) + '.txt'
    case = codecs.open(read_file, 'r', 'iso-8859-1').read()
    case = case.replace("[", "")
    case = case.replace("]", "")

    tagged_case = pos_tag(case.split())
    word_tokens = [word for word, pos in tagged_case if pos != 'NNP']

    # tokenize the whole file into words and get their lowercase form
    # word_tokens = [w.lower() for w in word_tokenize(case)]

    # remove stop words
    new_tokens = [w for w in word_tokens if w.lower() not in stop_words]

    new_case = ""

    for token in new_tokens:
        if token.isalpha() and len(token) > 1:
            new_case += token + "\n"

    case_write = open(write_file, "w")
    case_write.write(new_case)
    case_write.flush()

    print(str(i) + " completed")
