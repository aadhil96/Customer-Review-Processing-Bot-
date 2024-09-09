!pip install langchain
!pip install langchain_community
!pip install langchain_openai

from google.colab import userdata

openai_api_key = userdata.get('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_core.output_parsers.string import StrOutputParser

from langchain.schema.runnable import RunnablePassthrough
llm = ChatOpenAI(temperature=0, openai_api_key = openai_api_key)

original_review_prompt = ChatPromptTemplate.from_template("""
Translate the following review to English. If the review is already in English,
then output the review as is : {review}
""")

summary_creation_prompt = ChatPromptTemplate.from_template("""
Create a concise summary of the following in few sentences:
{english_review}
""")

original_language_prompt = ChatPromptTemplate.from_template("""
What language is the fllowing review in? : \n\n {review}
""")

find_sentiment_prompt = ChatPromptTemplate.from_template("""
You are an expert in reading text and identifying the sentiment of the customer
who wrote the text. Using all of the inputs below, find the stentiment of the review.

Review : {review}
English Review : {english_review}
Summary : {summary}
Original Review Language : {review_language}

Determine the sentiment of the review.
""")

build_email_response_prompt = ChatPromptTemplate.from_template("""
You are an expert customer service agent who handles a lot of angry, unhappy as well
happy and polite customers. Your task is to generate an email response for a customer who
has written a review. Your response should thank them for their feedback.
If the sentiment of the review is positive or neutral, thank them for being an esteemed customer.
If the sentiment is negative, apologize for the inconvinience and suggest them to
reach out to the customer care team for resolution. In your response be very specific and
informative by using the specific details from the customer feedback.
Your response should be concise and professional.
Sign the email with your name as "Generative Geek".

Review : {review}
English Review : {english_review}
Summary : {summary}
Original Review Language : {review_language}
Sentiment : {sentiment}

""")

original_review_chain = original_review_prompt | llm | StrOutputParser()
summary_creation_chain = summary_creation_prompt | llm | StrOutputParser()
original_language_chain = original_language_prompt | llm | StrOutputParser()
find_sentiment_chain = find_sentiment_prompt | llm | StrOutputParser()
build_email_response_chain = build_email_response_prompt | llm | StrOutputParser()

final_chain = ({"english_review":original_review_chain, "review": RunnablePassthrough()}
               | RunnablePassthrough.assign(summary = summary_creation_chain)
               | RunnablePassthrough.assign(review_language = original_language_chain)
               | RunnablePassthrough.assign(sentiment = find_sentiment_chain)
               | RunnablePassthrough.assign(automated_email = build_email_response_chain)
               )

review = """Voici une critique très négative pour un t-shirt mal ajusté et inconfortable :

Je déconseille fortement cet achat. Dès le premier essai, il était évident que ce t-shirt n'était absolument pas à la hauteur des attentes. Le tissu est rigide et irritant, provoquant une gêne continue. La coupe est si mal ajustée qu'elle semble avoir été conçue sans aucune considération pour la forme humaine. Les manches sont trop serrées, le torse trop lâche, créant une apparence peu flatteuse. En plus de cela, après un seul lavage, il a perdu sa forme. Un désastre total. Passez votre chemin!

"""

result = final_chain.invoke(review)

print(result)

def print_review_response_email(review):
  print("Analysing....")
  result = final_chain.invoke(review)
  print("Analysis done.")
  print("\n")

  print(f"Review: {review}")
  print("\n")
  print(f"Sentiment: {result['sentiment']}")
  print("\n")
  print(f"Automated Email: \n\n{result['automated_email']}")
  print("\n")
  
print_review_response_email(review)

review = """
Ich bin absolut begeistert von meiner neuen Waschmaschine! Sie übertrifft meine Erwartungen in jeder Hinsicht. Die innovative Technologie sorgt dafür, dass meine Wäsche immer perfekt sauber und frisch herauskommt. Besonders beeindruckt hat mich die Vielzahl an Programmen, die für jede Art von Textilien geeignet sind.

Die Bedienung ist kinderleicht, und die Maschine arbeitet angenehm leise. Der Energiesparmodus und die hohe Effizienz haben meine Stromrechnung bereits positiv beeinflusst. Der Kundenservice war ebenfalls erstklassig – schnell, hilfsbereit und professionell.

Vielen Dank an [Unternehmen], dass Sie ein so herausragendes Produkt entwickelt haben. Ich werde es definitiv all meinen Freunden und meiner Familie weiterempfehlen!

"""

print_review_response_email(review)