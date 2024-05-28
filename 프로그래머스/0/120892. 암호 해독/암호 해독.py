def solution(cipher, code):
    decrypted = cipher[code-1::code] # code의 배수 번째 글자만 추출
    return decrypted