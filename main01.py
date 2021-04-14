# -*- coding: shift-jis -*-

from __future__ import unicode_literals#参考:https://qiita.com/tadokoro/items/131268c9a0fd1cf85bf4


#20210414
#WEBアプリkdbもどきもどき作成
#csvを読み込んで、json形式に変換し、javascriptでそのjsonをクライアントのブラウザに読み込ませたい。
#pythonではcsv読み込み→json変換→出力までを行う。

#参考：https://qiita.com/motoki1990/items/0274d8bcf1a97fe4a869


import csv

#csv_file = open("./TEST_STOCK.csv", "r", encoding="ms932", errors="", newline="" )
#csv_file = open("./companylist.csv", "r", encoding="shift-jis", errors="", newline="" )
csv_file = open("./companylist.csv", "r", encoding="utf-8", errors="", newline="" )

#リスト形式
#f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#辞書形式
f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

import json
#ココ重要！！
# json.dump関数でファイルに書き込む
for row in f:
	fw = open( "json\TEST_STOCK_" + row['コード'] + ".json",'w')
	json.dump(row,fw,ensure_ascii=False,indent=4)

def jsonprint():
	header = next(f)
	print(header)
	for row in f:
		#row１つ１つが辞書
		#row[0]で必要な項目を取得することができる
		#print(row['コード'])
		print(row)
#jsonprint()

#参考：https://qiita.com/wakaba130/items/5f54aed913156dc4438f
import json
import collections as cl

def write_dict_json():
    name_list = ["honoka", "eri", "kotori", "umi", "rin", "maki", "nozomi", "hanayo", "niko"]
    height = [157,162,159,159,155,161,159,156,154]
    BWH = [[78, 58, 82],[88, 60, 84],[80, 58, 80],[76, 58, 80],
           [75, 59, 80],[78, 56, 83],[90, 60, 82],[82, 60, 83],[74, 57, 79]]

    ys = cl.OrderedDict()
    #ys = f
    for i in range(len(name_list)):
        data = cl.OrderedDict()
        data["BWH"] = BWH[i]
        data["height"] = height[i]

        ys[name_list[i]] = data

    #print("{}".format(json.dumps(ys,indent=4)))

    fw = open("TEST_STOCK.json",'w')
    #ココ重要！！
    # json.dump関数でファイルに書き込む
    json.dump(ys,fw,indent=4)



#write_dict_json()