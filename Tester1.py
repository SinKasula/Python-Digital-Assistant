import requests
import wolframalpha, wikipedia
api_key = "XTW8YK-5KUHPWA3YQ"
client = wolframalpha.Client(api_key)


def get_wiki(usr_input):
    result = wikipedia.summary(usr_input, sentences=2)
    return result


while True:
    usr_input = input("Question: ")
    try:
        res = client.query(usr_input)
        answer = next(res.results).text
        print(answer)
    except:
        try:
            result = get_wiki(usr_input)
            print(result)
        except:

            topics = wikipedia.search(usr_input)
            if len(topics)>0:
                print(usr_input + " is disambigious, may refer to the following: ")

                for i in range(1,len(topics)):
                    print(i, topics[i])
                choice = int(input("Enter a choice: "))
                assert choice in range(len(topics))
                print(get_wiki(topics[choice]))
            else:
                print("Voila! I could not find result for your query. ")
                continue
