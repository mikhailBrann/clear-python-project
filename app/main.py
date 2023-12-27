import requests

if __name__ == '__main__':
    with requests.get(' https://www.cbr-xml-daily.ru/daily_json.js') as course_request:
        print(course_request.text)