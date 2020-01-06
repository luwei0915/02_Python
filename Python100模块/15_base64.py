import base64

# Base64 编码
s = b'I like Python'
b64 = base64.b64encode(s)
# b'SSBsaWtlIFB5dGhvbg=='b'SSBsaWtlIFB5dGhvbg=='

# Base64 解码
b64 = b'SSBsaWtlIFB5dGhvbg=='
s = base64.b64decode(b64)
# b'I like Python'
print(s)
