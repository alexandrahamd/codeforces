import requests
from crontab import CronTab


def get_request_problems():
    '''функция изъятия задач'''
    response = requests.get(f"https://codeforces.com/api/problemset.problems")
    result = response.json()['result']['problems']
    return result


def get_request_statistics():
    '''функция изъятия колличества решений'''
    response = requests.get(f"https://codeforces.com/api/problemset.problems")
    result = response.json()['result']['problemStatistics']
    return result


# def get_all_tags():
#     problems = get_request_problems()
#     all_tags = []
#
#     for item_problem in problems:
#         for tag in item_problem['tags']:
#             all_tags.append(tag)
#
#     return set(all_tags)


def get_data():
    '''функия формирования данных'''
    data_problems = get_request_problems()
    data_statistics = get_request_statistics()

    result_data = []

    for i in range(len(data_problems)):
        name = data_problems[i]['name']
        number = str(data_problems[i]['contestId'])
        tags = data_problems[i]['tags']
        index = data_problems[i]['index']
        solvedCount = data_statistics[i]['solvedCount']
        try:
            rating = int(data_problems[i]['rating'])
        except:
            rating = 'null'

        result_data.append({'number': number + index, 'name': name,
                            'tags': tags, 'rating': rating,
                            'solvedCount': solvedCount})
    return result_data

