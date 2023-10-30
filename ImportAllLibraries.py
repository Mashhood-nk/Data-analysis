"""
Machine Learning Data Preprocessing and Analysis Script

This script imports essential libraries for data preprocessing and analysis in a machine learning context.
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import *
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import accuracy_score, log_loss
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV