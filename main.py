from subprocess import call as execute
from typing import ForwardRef
from volconvert import convert_human_to_nir_values
from binaryman import to_binary, to_string
import winsound
from time import sleep

frequencies = [3_000, 4_000, 5_000]

"""
  The first frequency = off (0)
  The second frequency = on (1)
  The third frequency = next

  The next message tells the receiver that it is time to receive the second bit
"""

def frequency_player(bit):
  if bit == 0:
    winsound.Beep(frequencies[0], 500)
    print("Played 0")
  else:
    winsound.Beep(frequencies[1], 500)
    print("Played 1")
  winsound.Beep(frequencies[2], 500)
  print("Played next")

  return None

class App():

  def __init__(self) -> None:
    # self.main()
    self.sender()

  def main(self):
    print("""
    1) Start as a sender
    2) Start as a receiver
    """)
    
    if input("> ") == 1:
      self.sender()
    else:
      self.receiver()
  
  def sender(self):
    message = input("Message: ")
    print("Press enter to start sending")
    input()

    for i in range(1,10):
      print(f"Holding for {i} second(s)")

    message_in_binary_list = to_binary(message)

    print(message_in_binary_list)
    for count,binary in enumerate(message_in_binary_list, start=1):
      print(f"Binary Pair {count}")
      for bit in binary:
        frequency_player(int(bit))
    
    print(f"Sent: {message_in_binary_list}")
  
  def receiver():

    """
      Deal with this shit tomorrow
    """
    received_bits = ""
    input("Press ENTER to start receiving")

App()