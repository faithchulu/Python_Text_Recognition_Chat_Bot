import re
import random
#import long_responses as long

#from long responses file
R_EATING = 'I don\'t like eating anything because I\'m a bot, obviously! '

def unknown():
    reponse = ['Could you please re-phrase that?',
    '...',
    'Sound about right',
    'What does that mean?'
    ][random.randrange(4)]
    
    return reponse

# end of long responses 

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainity = 0
    has_required_words = True 

#counts how many words are present in each predifined message
    for word in user_message:
        if word in recognised_words:
            message_certainity += 1

#calculates percent of recognised words from user inputs
    percentage = float(message_certainity)/float(len(recognised_words))

#check that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)


    #Response-------------------------------------------------------------------------------------------
    response('Hello!', ['hi', 'hello', 'hey', 'whatsapp', 'sup'], single_response = True )
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words = ['how'])
    response('Thank you!', ['i', 'love', 'you'], required_words =['love', 'you'])
    response('My name is Rose Gold.', ['what', 'is', 'your', 'name'], required_words = ['what', 'name'])
    response('Nice to meet you!', ['my', 'name', 'is'], required_words=['my', 'name'])
    response('Yes?', ['rosegold', 'rose', 'gold'], single_response=True)
    response('Thats great', ['i', 'am', 'fine', 'alright', 'good', 'great'], required_words=['i', 'am'])
    response(R_EATING, ['what','you','eat', 'eating'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return unknown() if highest_prob_list[best_match] < 1 else best_match
    
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#respomse system
while True:
    print('Bot: ' + get_response(input('You: ')))