def define_env(env):
   
    @env.macro
    def 백준링크(probName = "백준 문제", probId = "1000"):
        return f'[{probName} {probId}번](https://www.acmicpc.net/problem/{probId})'

    @env.macro
    def PS리포링크(path ="", value = "풀이"):
        return f'[{value}](https://github.com/ndy2/coding-test/blob/master/{path})'
