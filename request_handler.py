from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from data_requests import (
    get_all_entries,
    get_all_moods,
    get_single_entry,
    update_entry,
    create_entry,
    delete_entry
)
from data_requests.tag_request import get_all_tags

class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        

    def parse_url(self, path):
        path_params = path.split('/')
        resource = path_params[1]
        
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass
        return (resource, id)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        response = {}
        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            if id is not None:
                response = f'{get_single_entry(id)}'
            else:
                response = f'{get_all_entries()}'
        elif resource == "moods":
            response = f'{get_all_moods()}'
        elif resource == "tags":
            response = f'{get_all_tags()}'
        
        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, _) = self.parse_url(self.path)

        new_response = None

        if resource == "entries":
            new_response = create_entry(post_body)

        self.wfile.write(f'{new_response}'.encode())

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            update_entry(id, post_body)

        self.wfile.write("".encode())

    def do_DELETE(self):
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            delete_entry(id)

        self.wfile.write("".encode())


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
