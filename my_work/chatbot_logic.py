# Taken from https://engineering.semantics3.com/a-simplified-guide-to-grpc-in-python-6c4e25f0c506


def message_to_send(x):

  if x=="hi":
    return 'hello, how can i help you'

  elif x=="good afternoon":
    return "good afternoon, how you doing"

  elif x== 'Do you think you can really help me?':
    return 'Yes, Of Course I can!'
  
  elif x == 'How can I contact You?':
      return 'You can call me on 8906803353, 24*7!'
  elif x == 'What is the purpose of this chat?':
      return 'Not everything has a Purpose, LOL!'
  elif x == 'How do I know you?':
      return 'It is very simple... I am the server, You are My client!'
  elif x == 'Was this a joke?':
      return 'I do not know.. Do I seem like a Joker to you??'
  elif x == ' I am so tired of talking to you!':
      return ' That is because you are RUNNING in your thoughts while talking to me!!'
  elif x == ' That is it. I no longer want to talk to you! This chat is over...':
      return 'Well, In that case you can talk to my creators Shankar and Ankit.'
  elif x == 'Not that drama again.. I know you are good at it! Okay, I forgive you..':
      return 'I knew it.. Love you too!'
     
  else:
    return "type something please"



'''  


  elif x == 'Do you think you can really help me?':
      return 'Yes, Of Course I can!'
  elif x == 'How can I contact You?':
      return 'You can call me on 8906803353, 24*7!'
  elif x == 'What is the purpose of this chat?':
      return 'Not everything has a Purpose, LOL!'
  elif x == 'How do I know you?':
      return 'It is very simple... I am the server, You are My client!'
  elif x == 'Was this a joke?':
      return 'I do not know.. Do I seem like a Joker to you??'
  elif x == ' I am so tired of talking to you!':
      return ' That is because you are RUNNING in your thoughts while talking to me!!'
  elif x == ' That is it. I no longer want to talk to you! This chat is over...':
      return 'Well, you all are the same. Leave me alone all the time. It seems my heart will break again!'
  elif x == 'Not that drama again.. I know you are good at it! Okay, I forgive you..':
      return 'I knew it.. Love you too!'

  elif x=="exit" or "bye":
      pass
  else:
      return 'Do not be mad at me please. Say something!'

'''
