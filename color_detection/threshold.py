rgb_frame = pd.DataFrame(columns=["Category", "label", "R", "G", "B"])
rgb_frame["Category"] = train_labels
from sklearn.preprocessing import LabelEncoder

LE = LabelEncoder()
rgb_frame["label"] = LE.fit_transform(rgb_frame["Category"])


label_list = list()

for i in set(y):
    label_r_list = []
    label_g_list = []
    label_b_list = []
    for j in rgb_frame[rgb_frame["label"] == i]["RGB"]:
        label_r_list.append(j[0])
        label_g_list.append(j[1])
        label_b_list.append(j[2])

    label_list.append(i)
    label_list.append(sum(label_r_list) / len(label_r_list))
    label_list.append(sum(label_g_list) / len(label_g_list))
    label_list.append(sum(label_b_list) / len(label_b_list))
