import random;
from sklearn.linear_model import LinearRegression

print("Jeena Vinod Kumar, 32")
feature_set = []
target_set = []

number_of_rows = 200
random_number_limit = 2000
for i in range(0, number_of_rows):
    x = random.randint(0, random_number_limit)
    y = random.randint(0, random_number_limit)
    z = random.randint(0, random_number_limit)
    print("x=", x, "/t y=", y, "/t z=", z);
    function = (10 * x) + (2 * y) + (3 * z)
    feature_set.append([x, y, z])
    target_set.append(function)
model = LinearRegression()
model.fit(feature_set, target_set)
test_set = [[193, 1651, 983]]
prediction = model.predict(test_set)
print("Prediction:" + str(prediction) + '/t coefficient )' + str(model.coef_))
