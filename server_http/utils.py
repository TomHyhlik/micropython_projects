
CONTENT = b"""\
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8

Hello #%d from MicroPython!
<h1>header</h1>

<a href="/pica"> <button type="button">Click Me!</button> </a>
"""


CONTENT2 = b"""\
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8

BUTTON CLICKED!
<h1>header</h1>

<a href="/"> <button type="button">Back to home!</button> </a>
"""