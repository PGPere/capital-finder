from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    # http://localhost:3000/api/define?word=python
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "name" in dic:
            url = "https://restcountries.com/v2/name/{name}"
            r = requests.get(url + dic["name"])
            data = r.json()
            # definitions = []
            # for name_data in data:
            #     definition = name_data["meanings"][0]["definitions"][0]["definition"]
            #     definitions.append(definition)
            message = str(data[0].capital)

        else:
            message = "Give me a capital"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
