def camelcase(sentence):
    """
    Convert a sentence to camelCase
    for example: "hello world" -> "helloWorld"
    """
    title = sentence.title()
    upper_camel_cased = title.replace(" ", "")

    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def instructions():
    print("This program converts a sentence into camelCase format.")

def banner():
    """ Display Program name"""
    message = "Camel Case Program"
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars} \n')


def main():
    instructions()
    banner()
    sentence = input("Enter a sentence: ")
    output = camelcase(sentence)
    print(output)

if __name__ == "__main__":
    main()