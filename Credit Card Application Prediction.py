from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def data_pre_processing(df):
    data = pd.read_csv(r"CC_data.csv") #Please find the dataset attached
    # Replace "?" with NaN
    df = data.copy()
#     data_info = df.info()
#     data_describe = df.describe()
#     print(data_info)
#     print( data_describe)
    df.replace('?', np.NaN, inplace=True)
    # Convert Age to numeric
    df["Age"] = pd.to_numeric(df["Age"]) 
    #Imputing missing values for numerical columns with mean value
    df.fillna(df.mean(), inplace=True)  
    return df

def imputeWithMode(df):
    for col in df:
        if df[col].dtypes == 'object':
            df[col] = df[col].fillna(df[col].mode().iloc[0]) # Fill data with most frequent values
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
        # # Looping for each object type column
        # Using label encoder to convert into numeric types
    for col in df:
        if df[col].dtypes == 'object':
            df[col] = le.fit_transform(df[col])
    return df       

def model(df):
    df = df.drop(['DriversLicense', 'ZipCode'], axis=1) #low correlation
    df = df.values
    X, y = df[:, 0:13], df[:, 13]

    # Spliting the data into training and testing sets
    X_train, X_test, y_train, Y_test = train_test_split(X,y,test_size=0.2,random_state=123)

    return X_train, X_test, y_train, Y_test,X

def minMaxScalar(X_train,X_test,X):
    scaler = MinMaxScaler(feature_range=(0, 1))
    # Scaling X_train and X_test
    rescaledX_train = scaler.fit_transform(X_train)
    rescaledX_test = scaler.transform(X_test)
    rescaledX = scaler.transform(X)
    return rescaledX_train, rescaledX_test, rescaledX


def log_reg(df):
    # Import LogisticRegression
    from sklearn.linear_model import LogisticRegression
    # Fitting logistic regression with default parameter values
    logreg = LogisticRegression(solver = 'lbfgs')
    logreg.fit(rescaledX_train, y_train)
    # Import confusion_matrix
    from sklearn.metrics import confusion_matrix
    # Using the trained model to predict instances from the test set
    y_pred = logreg.predict(rescaledX_test)
    # Getting the accuracy score of predictive model
    print("Logistic regression classifier has accuracy of: ", logreg.score(rescaledX_test, Y_test))
    print("Evaluate the confusion_matrix")
    print(confusion_matrix(Y_test, y_pred))
    
    df1 = df.drop(['Approved'], axis=1)
    features = df1.columns
    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier(n_estimators=500)
    rf.fit(rescaledX_train, y_train)
    importances = rf.feature_importances_
    indices = np.argsort(importances)
    plt.title('Feature Importances')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Relative Importance')
    plt.show()

    

if __name__ == '__main__':
    #Please find the dataset attached
    credit_card_df = pd.read_csv(r"CC_data.csv")    #read data
    cc_df=data_pre_processing(credit_card_df)
    cc_df=imputeWithMode(cc_df)    
    X_train, X_test, y_train, Y_test,X = model(cc_df)
    rescaledX_train, rescaledX_test,rescaledX = minMaxScalar(X_train,X_test,X)
    log_reg(cc_df)
    
