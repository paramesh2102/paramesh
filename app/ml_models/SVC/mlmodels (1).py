

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# Sample categorical data
categories = ['cat', 'dog', 'fish', 'dog', 'cat']

# Create a dictionary to map categories to numerical labels
label_mapping = {category: label for label, category in enumerate(set(categories))}

# Create a reverse mapping dictionary to map numerical labels back to categories
reverse_mapping = {label: category for category, label in label_mapping.items()}

# Create a lambda function for label encoding and reverse decoding
label_encode_decode = lambda data, mapping: [mapping[category] for category in data]

# Encode the original categories
encoded_labels = label_encode_decode(categories, label_mapping)

# Decode the encoded labels back to original categories
decoded_categories = label_encode_decode(encoded_labels, reverse_mapping)

print("Original Categories:", categories)
print("Encoded Labels:", encoded_labels)
print("Decoded Categories:", decoded_categories)

label_encode_decode([1,0], reverse_mapping)

import pandas as pd

data=pd.read_csv('processeddata.csv')

data.head(2)

l1=['dst_host_srv_serror_rate', 'service_ecr_i', 'flag_RSTO',
       'service_urh_i', 'flag_OTH', 'dst_host_serror_rate', 'diff_srv_rate',
       'dst_host_same_src_port_rate', 'serror_rate', 'flag_RSTOS0',
       'wrong_fragment', 'protocol_type_icmp', 'logged_in', 'srv_serror_rate',
       'dst_host_same_srv_rate', 'flag_RSTR', 'is_host_login',
       'is_guest_login', 'srv_diff_host_rate', 'service_eco_i', 'flag_REJ',
       'flag_S0', 'service_red_i', 'dst_host_srv_count', 'count',
       'same_srv_rate', 'service_pop_3', 'protocol_type_udp',
       'dst_host_srv_diff_host_rate', 'flag_SF', 'srv_count',
       'dst_host_diff_srv_rate', 'flag_S3', 'num_failed_logins', 'land',
       'flag_SH', 'flag_S2', 'flag_S1', 'service_urp_i', 'protocol_type_tcp',
       'service_ftp']

x=data[l1]
y=data['Class']

x.head(2)

y.head(2)







# Sample categorical data
categories = list(y)
# Create a dictionary to map categories to numerical labels
label_mapping = {category: label for label, category in enumerate(set(categories))}

# Create a reverse mapping dictionary to map numerical labels back to categories
reverse_mapping = {label: category for category, label in label_mapping.items()}

# Create a lambda function for label encoding and reverse decoding
label_encode_decode = lambda data, mapping: [mapping[category] for category in data]

# Encode the original categories
encoded_labels = label_encode_decode(categories, label_mapping)

len(y)

len(encoded_labels)

y_encoded=pd.Series(encoded_labels)

y=y_encoded





# Split the data into a training set and a testing set (e.g., 80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Choose a machine learning algorithm (Decision Tree Classifier in this example)
model = SVC()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")

X_train.head(2)

X_test.head(2)

y_pred

mindf=pd.read_csv('mindf.csv')
maxdf=pd.read_csv('maxdf.csv')

inputvar=['dst_host_srv_serror_rate', 'service_ecr_i', 'flag_RSTO',
       'service_urh_i', 'flag_OTH', 'dst_host_serror_rate', 'diff_srv_rate',
       'dst_host_same_src_port_rate', 'serror_rate', 'flag_RSTOS0',
       'wrong_fragment', 'protocol_type_icmp', 'logged_in', 'srv_serror_rate',
       'dst_host_same_srv_rate', 'flag_RSTR', 'is_host_login',
       'is_guest_login', 'srv_diff_host_rate', 'service_eco_i', 'flag_REJ',
       'flag_S0', 'service_red_i', 'dst_host_srv_count', 'count',
       'same_srv_rate', 'service_pop_3', 'protocol_type_udp',
       'dst_host_srv_diff_host_rate', 'flag_SF', 'srv_count',
       'dst_host_diff_srv_rate', 'flag_S3', 'num_failed_logins', 'land',
       'flag_SH', 'flag_S2', 'flag_S1', 'service_urp_i', 'protocol_type_tcp',
       'service_ftp']



new_data = np.array([[3 for i in range(11,52)]])
newdf = pd.DataFrame(new_data, columns=inputvar)
targetdf = (newdf - mindf) / (maxdf - mindf)
targetdf

model.predict(targetdf)

l=list(model.predict(targetdf))

l

# Decode the encoded labels back to original categories
decoded_categories = label_encode_decode(l, reverse_mapping)

decoded_categories

result=decoded_categories[0]

result

pickle.dump(model, open('SVC.pkl','wb'))

len(data['Class'].value_counts())

