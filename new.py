def createDictionary ():

  bangla=dict()
  bangla ['i'] = 'ami'
  bangla ['rice'] = 'bhat'
  bangla ['you'] = 'tomake'
  bangla ['love'] = 'bhalobashi'
  bangla ['poop'] = 'gu'
  bangla ['earth'] = 'duniya'
  return bangla

def main ():
  dictionary = createDictionary ()
  x=input('enter to translate: ')
  print (dictionary [x])
  

main()