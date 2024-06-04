#coding:utf8
import json, copy

def explode(splitString, string):
    return string.split(splitString) if string else []

def implode(joinString, arr):
    return joinString.join(list(map(str, arr)))

def parseString(s):
    if s is None:
        return ''

    if isinstance(s, bytes):
        return s.decode('utf-8')
    return str(s)

def parseFloat(string):
    try:
        return float(string)
    except:
        return 0

def parseInt(string):
    if isinstance(string, bytes):
        string = string.decode('utf-8')

    try:
        return int(string)
    except:
        return 0

def parseJson(string, default={}):
    try:
        result = json.loads(string)
        if isinstance(result, dict) or isinstance(result, list):
            return result
        else:
            return copy.deepcopy(default)
    except:
        return copy.deepcopy(default)

def parseRmb(price):
    return round(1.0*price/100.0, 2)

def parseRmbCent(priceString):
    if isinstance(priceString, str):
        priceString = priceString.strip()

    return int(round(parseFloat(priceString) * 100, 0))

"""
一般报表
result = [{'k': 'k', 'kk': 'kk'},]
keys = ['kk', 'k']
keyDesc = {'k': u'单k', 'kk': u'双k'}
"""
def excelXlsx(result, keys, keyDesc):
    import xlsxwriter, io

    sf = io.BytesIO()
    workbook = xlsxwriter.Workbook(sf, {'constant_memory': True})
    sheet = workbook.add_worksheet()

    xIndex = 0
    for nn, key in enumerate(keys):
        sheet.write(xIndex, nn, keyDesc.get(key, ''))

    for item in result:
        xIndex += 1
        for nn, key in enumerate(keys):
            sheet.write(xIndex, nn, item.get(key, ''))
    workbook.close()

    content = sf.getvalue()
    sf.close()
    return content

def getFileSuffix(name):
    suffix = ""
    index = name.rfind('.')
    if index > -1:
        suffix = name[index:]
    return suffix

