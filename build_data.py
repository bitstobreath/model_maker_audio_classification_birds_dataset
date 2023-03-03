# prepare the sound data

import asyncio
import time
import xenocanto_modified as xenocanto

bird_code_to_name = {
  'wbwwre1': 'White-breasted Wood Wren',
  'houspa': 'House Sparrow',
  'redcro': 'Red Crossbill',  
  'chcant2': 'Chestnut-crowned Antpitta',
  'azaspi1': "Azara's Spinetail",   
}

def run():
  for bird_name in bird_code_to_name.values():
      print(bird_name)
      xenocanto.metadata(bird_name)
      start = time.time()
      asyncio.run(xenocanto.download(bird_name))
      end = time.time()
      print("Duration: " + str(int(end - start)) + "s")

if __name__ == '__main__':
   run()