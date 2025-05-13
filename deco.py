def decor1(g):
    def wrap():
        print("🎀🎀🎀🎗🎗🎗🎁🎁🎁")
        return g().upper()

    return wrap


def decor2(f):
    def wrap():
        # print(f)
        return print(f().split())

    return wrap


@decor2
@decor1
def get_name():
    name = input("Enter Your Name:")
    name = "✨✨✨" + "   Welcome   " + name + "🎉🎉🎉"

    return name


print(get_name())
