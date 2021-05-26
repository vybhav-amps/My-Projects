import pandas as pd

messages = pd.read_csv('SMSSpam', sep='\t',names=["label", "message"])

import re
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()

y=pd.get_dummies(messages['label'])
y=y.iloc[:,1].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(X_train, y_train)

y_pred=spam_detect_model.predict(X_test)

from sklearn.metrics import confusion_matrix 
matrix=confusion_matrix(y_test,y_pred)

from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)

c=[]
a="Hello! I'm Sunny"
a = re.sub('[^a-zA-Z]', ' ', a)
a = a.lower()
a = a.split()
    
a = [ps.stem(word) for word in a if not word in stopwords.words('english')]
a = ' '.join(a)
c.append(a)
    
m = cv.fit_transform(c).toarray()
spam_detect_model.predict(m)