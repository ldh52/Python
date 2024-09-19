from random import randint

def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(numbers, winning_numbers):
    winning_main_numbers = winning_numbers[:6]
    matching_count = len(set(numbers) & set(winning_main_numbers))
    return matching_count

def check(numbers, winning_numbers):
    winning_main_numbers = winning_numbers[:6]
    bonus_number = winning_numbers[6]

    # 일치하는 번호 개수 계산
    match_count = count_matching_numbers(numbers, winning_numbers)

    # 보너스 번호 일치 여부
    bonus_match = bonus_number in numbers

    # 당첨 금액 결정
    if match_count == 6:
        return "10억 원"
    elif match_count == 5 and bonus_match:
        return "5천만 원"
    elif match_count == 5:
        return "100만 원"
    elif match_count == 4:
        return "5만 원"
    elif match_count == 3:
        return "5천 원"
    else:
        return "당첨되지 않았습니다."

# 테스트 코드
participant_numbers = generate_numbers(6)  # 참가자가 뽑은 번호
winning_numbers = draw_winning_numbers()  # 당첨 번호

print("참가자 번호:", participant_numbers)
print("당첨 번호:", winning_numbers)
print("일치하는 번호 개수:", count_matching_numbers(participant_numbers, winning_numbers))
print("당첨 금액:", check(participant_numbers, winning_numbers))
