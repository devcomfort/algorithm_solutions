from functools import reduce
import re
from typing import List, Tuple, Union

MBTI = "RTCFJMAN"


def MBTI_indexer(chr: str) -> Union[int, None]:
    """
    MBTI 유형 정보를 인덱스로 지정하는 코드
    """
    global MBTI

    if chr in MBTI:
        return MBTI.index(chr)
    return None


def get_scores(surveys: str, choices: int) -> Tuple[str, int]:
    def score_normalizezr(score: int) -> int:
        """
        점수 일반화 함수
        1 ~ 7 -> -3 ~ 3
        """
        return score - 4

    def get_score(survey: str, choice: int) -> Tuple[str, int]:
        """
        점수 정보 일반화
        어떤 성격 유형에 얼마의 정보를 획득했는지 알 수 있다.
        """
        return (survey[int(choice > 0)], abs(choice))

    choices = list(map(score_normalizezr, choices))
    results = list(map(
        lambda v: get_score(*v), zip(surveys, choices)
    ))

    return results


def as_a_result(scores: List[Tuple[str, int]]):
    """
    ## 결과 정리 함수

    `get_scores` 함수를 통해 나온 결과물을 정리하여 성격 유형으로 최종 결과를 도출함.
    """

    # 결과 리스트 초기화
    numeric_scores = [0 for _ in MBTI]

    # 결과 리스트 정리
    for value in scores:
        literal, score = value

        if literal in MBTI:
            index = MBTI.index(literal)
            numeric_scores[index] = numeric_scores[index] + score

    # 결과 MBTI 도출
    RESULT = ""

    for i in range(4):
        index_a, index_b = i * 2, i * 2 + 1
        scores = [numeric_scores[index_a], numeric_scores[index_b]]

        if scores[0] == scores[1]:
            # 대립하는 두 가지 MBTI 성격 유형의 점수가 같은 경우,
            # 두 문자 중 사전상으로 우선하는 글자를 지정합니다.
            if ord(MBTI[index_a]) < ord(MBTI[index_b]):
                RESULT = RESULT + MBTI[index_a]
            else:
                RESULT = RESULT + MBTI[index_b]
        elif scores[0] < scores[1]:
            RESULT = RESULT + MBTI[index_b]
        else:
            RESULT = RESULT + MBTI[index_a]

    return RESULT


def solution(survey, choices):
    return as_a_result(
        get_scores(
            survey,
            choices
        )
    )
