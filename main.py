import pandas as pd
import numpy as np
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def fun(list):
    index = []
    for i in range(0, len(list)):
        msg = list[i]["Msg"]
        if not isinstance(msg, str) and math.isnan(msg):
            index.append(list[i])

    for i in index:
        list.remove(i)
    return list


def getDataType(msg):
    if msg.endswith("Bool"):
        return 'BoolData'
    elif msg.endswith("Float32") or msg.endswith("Int8"):
        return 'NumberData'
    elif msg.endswith("Imu"):
        return "ImuData"
    elif msg.endswith("Range"):
        return "RangeData"
    elif msg.endswith("Twist"):
        return "TwistData"
    elif msg.endswith("TwistStamped"):
        return "TwistStampedData"
    elif msg.endswith("NavSatFix"):
        return "NavSatFixData"
    elif msg.endswith("TimeReference"):
        return "TimeReferenceData"
    else:
        return ""


def read_file():
    df = pd.read_excel(r'C:\Users\karmi\Desktop\Software-Hardware Information.xlsx',
                       usecols=["Name", "Msg"])

    items = df.to_dict(orient='records')

    items = fun(items)

    for item in items:
        sep = ""
        full_name = item["Name"]
        full_msg = sep.join(str(item["Msg"]).split(".")[:-1])

        name = str(item["Name"]).split("/")
        name = name[1:]
        na = ""
        for word in name:
            na = na + word.title() + ""

        topic_name = na + "Topic"
        data_name = getDataType(full_msg)
        if data_name == "":
            data_name = na + "Data"
        # print(topic_name)
        className = "export class " + topic_name + " {\n" \
                                                   "\tname = '" + str(full_name) + "';\n" \
                                                                                   "\tmsg = '" + str(full_msg) + "';\n" \
                                                                                                                 "\tdata?: " + data_name + ";\n}"
        print(className)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
