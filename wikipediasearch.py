import wikipedia
from speak import speak

def search_on_wikipedia(query=None):
    to_replace = ('search','what','where','when','who','how','which','show','say','according','tell','wikipedia')
    if query!= None:
        to_search=''
        for word in query.split():
            if word not in to_replace:
                to_search+= f"{word} "
        try:
            results = wikipedia.summary(to_search, sentences = 2)
            speak(f'According to wikipedia, {results}')
        except:
            speak(f'Sorry sir, I was unable to search {query} on wikipedia.')
    else:
        from takecommand import take_command
        count = 0
        while count <2:
            speak('Please, say your query sir.')
            command = take_command()
            to_search=''
            for word in command.split():
                if word not in to_replace:
                    to_search+= f"{word} "
            try:
                results = wikipedia.summary(to_search, sentences = 2)
                speak(f'According to wikipedia, {results}')
                break
            except:
                speak(f'Sorry sir, I was unable to search {query} on wikipedia.')
                count+=1