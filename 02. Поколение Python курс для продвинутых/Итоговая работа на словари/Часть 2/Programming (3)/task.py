def build_query_string(params):
    params = sorted(params.items())

    for el in params:
        # result = '&'.join([f'{el[0]}={el[1]}' for el in params])
        # return(result)

        return '&'.join([f'{el[0]}={el[1]}' for el in params])

# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))