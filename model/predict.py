import sys
from sklearn.model_selection import train_test_split

def load_data():
    data = []
    tar  = []
    with open("train.txt") as f:
        counter = 0
        for line in f:
            counter += 1
            split_res = line.strip().split("\t")
            data_item = [float(item) for item in split_res[3:-1]]
            tar_item  = int(split_res[-1])
            data.append(data_item)
            tar.append(tar_item)
            if counter == 50000:
                break
    return data, tar

def ml_stragety(opt):
    data, tar = load_data()
    print "load data ......"
    x_train, x_test, y_train, y_test = train_test_split(data, tar, test_size=0.2, random_state=0)

    clf = None

    if opt == "dest":
        from sklearn.tree import DecisionTreeClassifier 
        clf = DecisionTreeClassifier()
    elif opt == "svm":
        from sklearn import svm
        clf = svm.SVC(kernel='linear', C=1)
    elif opt == "knn":
        from sklearn.neighbors import KNeighborsClassifier
        clf = KNeighborsClassifier()
    elif opt == "lr":
        from sklearn.linear_model import LogisticRegression
        clf = LogisticRegression(penalty='l2')
    elif opt == "rf":
        from sklearn.ensemble import RandomForestClassifier
        clf = RandomForestClassifier(n_estimators=8)
    elif opt == "gbdt":
        from sklearn.ensemble import GradientBoostingClassifier
        clf = GradientBoostingClassifier(n_estimators=200)
    elif opt == "ada":
        from sklearn.ensemble import  AdaBoostClassifier
        clf = AdaBoostClassifier()
    elif opt == "gnb":
        from sklearn.naive_bayes import GaussianNB
        clf = GaussianNB()
    elif opt == "ld":
        from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
        clf = LinearDiscriminantAnalysis()
    elif opt == "qd":
        from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
        clf = QuadraticDiscriminantAnalysis()
    elif opt == "nb":
        from sklearn.naive_bayes import MultinomialNB
        clf = MultinomialNB(alpha=0.01)

    print "fit data ......"
    clf.fit(x_train, y_train)
    print clf.score(x_test, y_test)

if __name__ == "__main__":
    opt = sys.argv[1]
