#load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pylot as plt
from sklearn import model_selection #it is used for automatic model selection
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbours import KNeighboursClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
#it imports every algo and use model based on accuracy calculation
#I think we need some 
#will use image processing package
