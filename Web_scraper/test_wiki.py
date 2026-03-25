import wikipedia
import time

def get_wikipedia_text(name:str):
    try:
        summary=wikipedia.summary(name, sentences=5)

        return{
            "Title": name,
            "text" : summary
        }
    except Exception as e:
        return {"error": str(e)}
    
if __name__=="__main__":
    result= get_wikipedia_text("Marie Curie")
    print(result)

    
# start=time.time()

# wiki=wikipediaapi.Wikipedia(language="en", user_agent='AI-Coloring-Book/1.0 (student project)')

# page=wiki.page("Marie Curie")

# print(page.title)
# print(page.summary[:300])

# end=time.time()
# print(f"\ntime take: {end-start:.2f} seconds")