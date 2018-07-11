import json
def application (environ, start_response):
    # Sorting and stringifying the environment key, value pairs
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)
    #返回给前台的数据必须是二进制的。
    response_body = response_body.encode()

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    try:
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
        print("---数据的长度是%s---" % str(request_body_size))
    except (ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size)
    #这个 decode 就是整个下午的收获
    request_body = json.loads(request_body.decode())
    print("--接收到的内容是--%s----" % str(request_body))
    return [response_body]
