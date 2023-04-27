def dec_to_hex(decimal_num):
    """
    10진수를 16진수로 변환하는 함수
    """
    hex_num = hex(decimal_num)[2:]  # Ox 제거
    return hex_num.upper()


print(dec_to_hex(255))  # 'FF'
