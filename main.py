def define_env(env):
   
    @env.macro
    def boj(probName = "백준 문제", probId = "1000"):
        return f'[{probName} {probId}번](https://www.acmicpc.net/problem/{probId})'

    @env.macro
    def prgrms(probName = "프로그래머스 문제", probId = "1000"):
        return f'[{probName}](https://school.programmers.co.kr/learn/courses/30/lessons/{probId})'

    @env.macro
    def ps(path ="", value = "풀이"):
        return f'[{value}](https://github.com/ndy2/coding-test/blob/master/{path})'
