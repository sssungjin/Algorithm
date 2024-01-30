def solution(score):
    half = len(score) // 2
    if sum(score[:half]) == sum(score[half:]):
        print("LUCKY")
    else:
        print("READY")

def main():
    score = list(map(int, input()))
    solution(score)

if __name__ == "__main__":
    main()