def solution(letter):
    # 모스 부호와 알파벳을 매핑하는 딕셔너리
    morse_code = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
        '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
        '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
        '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
        '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
        '--..': 'z'
    }
    
    # 주어진 문자열을 공백으로 나눠서 모스 부호 리스트로 변환
    morse_letters = letter.split(' ')
    
    # 모스 부호를 알파벳으로 변환하여 리스트에 저장
    decoded_letters = [morse_code[morse] for morse in morse_letters]
    
    # 리스트를 문자열로 변환하여 반환
    return ''.join(decoded_letters)

# 예제 사용
print(solution(".... . .-.. .-.. ---"))  # "hello"
print(solution(".--. -.-- - .... --- -."))  # "python"
