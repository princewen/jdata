from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import pandas as pd
import time

train = pd.read_csv('train.csv', index_col=0)
predict = ['u_buy_cart_raito','u_buy_browse_ratio','u_buy_click_ratio','u_buy_favor_ratio',
            'p_buy_cart_ratio','p_buy_browse_ratio','p_buy_click_ratio','p_buy_favor_ratio']
test = pd.read_csv('test.csv', index_col=0)

train_x = train[predict]
train_y = train['label']
test_x = test[predict]

ss = StandardScaler()

for c in predict:

    train_x[c] = ss.fit_transform(train_x[c])
    test_x[c] = ss.fit_transform(test_x[c])


def predict(model_name, train_x, train_y, test_x):
    if model_name == 'xgbc':
        model = XGBClassifier()
    elif model_name == 'rfc':
        model = RandomForestClassifier()

    model.fit(train_x, train_y)
    y = model.predict(test_x)

    # y = [t for t in y if t == 1]

    df = pd.DataFrame({'user_id': test_x['user_id'], 'sku_id': test_x['sku_id'],'label':y})
    df = df[df['label'] == 1][['user_id', 'sku_id']]
    df.to_csv('result' + str(time.time()) + '.csv')




