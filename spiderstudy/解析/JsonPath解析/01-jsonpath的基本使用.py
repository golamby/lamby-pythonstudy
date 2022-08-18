import json
import jsonpath

with open('../../../data/jsonpath_use.json', mode='r', encoding='utf-8') as f:
    res = json.load(f)

# author_list = jsonpath.jsonpath(res,'$..author')
author_list = jsonpath.jsonpath(res, '$.store.book[*].author')
print(author_list)

result = jsonpath.jsonpath(res,'$.store.*[?(@.price > 10,@.isbn)]')
print(result)

result = jsonpath.jsonpath(res,'$.store.*[?(@.category && @.price < 10)]')
print(result)

result = jsonpath.jsonpath(res,'$.store.book[0]')
print(result)
