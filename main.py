# Data Processing
import pandas as pd
import numpy as np

# Modelling
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

# Tree Visualisation
from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz

#To install the required libraries, uncomment the following line and run it in your terminal:
#pip install --user -r requirements.txt

print("Libraries imported successfully")
# Load the dataset

#charge dataset
dataset = pd.read_csv('student_depression_dataset.csv')

