class Evaluator:

    @staticmethod
    def zip_evaluate(self, words):
        if len(words) != len(self):
            print('-1')
            exit()
        list = []
        res = 0
        cnt = 0
        for i in words:
            list.append((words[cnt], self[cnt]))
            res += len(list[cnt][0]) * list[cnt][1]
            cnt += 1
        return res

    @staticmethod
    def enumerate_evaluate(self, words):
        if len(words) != len(self):
            print('-1')
            exit()
        list = []
        res = 0
        cnt = 0
        for i in words:
            list.append((cnt, words[cnt]))
            res += len(list[cnt][1]) * self[cnt]
            cnt += 1
        return res

# TESTS
#
# SHOULD GIVE "32.0\n32.00"
# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

# SHOULD FIVE -1
words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]

print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))
