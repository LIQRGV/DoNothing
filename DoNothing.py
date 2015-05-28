class DoNothing(object):

    class Nothing(object):
        def doNothing(self, conditional):
            pass

    class DoingNothing(Nothing):
        def doNothing(self, conditional):
            if conditional:
                self.doNothing(False)
            else:
                return


def didNothing(toDo, decision):
    toDo.doNothing(decision)


def main():
    decision = input("Input please\n")
    if decision:
        didNothing(DoNothing().DoingNothing(), decision)
    else:
        return


main()

