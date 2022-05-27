from unittest import result


class Term:
    type_ : str
    data : str
    args_ : list()

    def andTerm(self, term):
        return self

    def orTerm(self, term):
        return self

    def notTerm(self, term):
        return self

    # A term is initialized with:
    # 1. Data(data) which is the content of the term.
    # 2. Type(type_) which is type of the term. A term could either be ATOM, VARIABLE or PREDICATE.
    # 3. Arguements(args_) which are the list of terms attached to a predicate
    def __init__(self, data, type_, args_):
        self.data = data
        self.type_ = type_
        self.args_ = args_

    # This allows python to print the term in a predicate calculus format DFS
    def __repr__(self):
        if self.type_ == "VARIABLE" or self.type_ == "ATOM":
            return self.data
        elif self.type_ == "PREDICATE":
            if len(self.args_) > 0:
                temp = ""
                for i in range(len(self.args_) - 1):
                    temp += repr(self.args_[i]) + ", "
                temp += repr(self.args_[len(self.args_) - 1])
                return f"{self.data}({temp})"
            else:
                return f"{self.data}()"
        else:
            return "_"


# this function return general unifier of two terms
def unify(term_1: Term, term_2: Term):
    eq = [[term_1, term_2]]
    subset = {}
    while len(eq) > 0:
        ab = eq.pop()
        if repr(ab[0]) != repr(ab[1]):
            if ab[0].type_ == "VARIABLE":
                subset[repr(ab[0])] = ab[1]
                if ab[1].type_ == "PREDICATE" and varInPredicate(ab[0], ab[1]):
                    return (subset, False)
            elif ab[1].type_ == "VARIABLE":
                subset[repr(ab[1])] = ab[0]
                if ab[0].type_ == "PREDICATE" and varInPredicate(ab[1], ab[0]):
                    return (subset, False)             
            elif ab[0].type_ == "PREDICATE" and ab[1].type_ == "PREDICATE"\
                and (ab[0].data == ab[1].data) and (len(ab[0].args_) == len(ab[1].args_)):
                n = len(ab[0].args_)
                for i in range(n):
                    eq.append([ab[0].args_[i], ab[1].args_[i]])
            else:
                return ({}, False)
    return (subset, True)


def varInPredicate(varTerm: Term, predTerm: Term):
    queue = predTerm.args_.copy()
    while len(queue) > 0:
        head = queue.pop()
        if (varTerm.data == head.data) and head.type_ == "VARIABLE":
            return True
        elif head.type_ == "PREDICATE":
            queue += head.args_.copy()
        else:
            continue
    return False

def resolve(facts, parent_term, childTerm):
    pass


if __name__ == "__main__":
    term_1 = Term("Q", "PREDICATE", [Term("P", "PREDICATE", [Term("X", "VARIABLE", [])]), Term("2", "ATOM", [])])
    term_2 = Term("Q", "PREDICATE", [Term("P", "PREDICATE", [Term("X", "VARIABLE", [])]), Term("X", "VARIABLE", [])])
    term_3 = Term("Q", "PREDICATE", [Term("X", "VARIABLE", []), Term("Y", "VARIABLE", [])])
    # source = Term("X", "VARIABLE", [])
    # target = Term("2", "ATOM", [])
    # print(f"{source} :: {target} :: {term_1}")
    # c = replace(source, target, term_1)
    # print(c)
    # print(term_1)
    print(f"{term_2} :: {term_1}")
    # print(unify(term_2, term_1))
    result = unify(term_2, term_1)
    print(f"Substitution set: {result[0]}\nCan be unified? {result[1]}")
    # print(
    #     varInPredicate(
    #         Term("X", "VARIABLE", []), 
    #         Term("Q", "PREDICATE", [Term("P", "PREDICATE", [Term("X", "VARIABLE", [])]), Term("Y", "VARIABLE", [])])
    #         )
    #     )

