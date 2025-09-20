import discord
import kociemba


visual = """
         ¸.·ˆ·.¸
     ¸.·ˆ·.¸w¸.·ˆ·.¸
 ¸.·ˆ·.¸w¸.·ˆ·.¸w¸.·ˆ·.¸
|·.¸w¸.·ˆ·.¸w¸.·ˆ·.¸w¸.·|
| g |·.¸w¸.·ˆ·.¸w¸.·| r |
|·.¸| g |·.¸w¸.·| r |¸.·|
| g |·.¸| g | r |¸.·| r |
|·.¸| g |·.¸|¸.·| r |¸.·|
| g |·.¸| g | r |¸.·| r |
`·.¸| g |·.¸|¸.·| r |¸.·´
    `·.¸| g | r |¸.·´
        `·.¸|¸.·´
"""

cube = "wwwwwwwwwooooooooogggggggggrrrrrrrrryyyyyyyyybbbbbbbbb"
move = []


#Rotations -------------------------------------------------------------

def x():
  global cube
  cube = list(cube)
  temporary = cube.copy()
  #Transfer White to Blue
  cube[45:54] = temporary[8::-1]
  #Transfer Blue to Yellow
  cube[36:45] = temporary[53:44:-1]
  #Transfer Yellow to Green
  cube[18:27] = temporary[36:45]
  #Transfer Green to White
  cube[0:9] = temporary[18:27]
  
  #Rotation on Right side
  pattern = [6, 2, -2, 4, 0, -4, 2, -2, -6]
  for i in range(len(pattern)):
    cube[i + 27] = temporary[i + 27 + pattern[i]]
  
  #Rotation on Left side
  pattern = [2, 4, 6, -2, 0, 2, -6, -4, -2]
  for i in range(len(pattern)):
    cube[i + 9] = temporary[i + 9 + pattern[i]]

  cube = "".join(cube)


def y():
  global cube
  cube = list(cube)
  temporary = cube.copy()
  #Blue to Red
  cube[27:36] = temporary[45:54]
  #Red to Green
  cube[18:27] = temporary[27:36]
  #Green to Orange
  cube[9:18] = temporary[18:27]
  #Orange to Blue
  cube[45:54] = temporary[9:18]
  
  #Rotation on Top side (Clock-wise)
  pattern = [6, 2, -2, 4, 0, -4, 2, -2, -6]
  for i in range(len(pattern)):
    cube[i + 0] = temporary[i + 0 + pattern[i]]
  
  #Rotation on Bottom side (Counter Clock-wise)
  pattern = [2, 4, 6, -2, 0, 2, -6, -4, -2]
  for i in range(len(pattern)):
    cube[i + 36] = temporary[i + 36 + pattern[i]]
  
  cube = "".join(cube)


def z():
  y()
  y()
  y()
  x()
  y()

#Turns -------------------------------------------------------------

def R():
  global cube
  cube = list(cube)
  temporary = cube.copy()

  cube[2] = temporary[20]
  cube[5] = temporary[23]
  cube[8] = temporary[26]

  cube[20] = temporary[38]
  cube[23] = temporary[41]
  cube[26] = temporary[44]

  cube[38] = temporary[51]
  cube[41] = temporary[48]
  cube[44] = temporary[45]

  cube[51] = temporary[2]
  cube[48] = temporary[5]
  cube[45] = temporary[8]

  pattern = [6, 2, -2, 4, 0, -4, 2, -2, -6]
  for i in range(len(pattern)):
    cube[i + 27] = temporary[i + 27 + pattern[i]]

  cube = "".join(cube)

def L():
  z()
  z()
  R()
  z()
  z()

def U():
  z()
  R()
  z()
  z()
  z()

def D():
  z()
  z()
  z()
  R()
  z()

def F():
  y()
  y()
  y()
  R()
  y()

def B():
  y()
  R()
  y()
  y()
  y()

def M():
  L()
  L()
  L()
  R()
  x()
  x()
  x()


move_list = {
  'R': [R, 1],
  "R'": [R, 3],
  'R2': [R, 2],
  'U': [U, 1],
  "U'": [U, 3],
  'U2': [U, 2],
  'L': [L, 1],
  "L'": [L, 3],
  'L2': [L, 2],
  'B': [B, 1],
  "B'": [B, 3],
  'B2': [B, 2],
  'D': [D, 1],
  "D'": [D, 3],
  'D2': [D, 2],
  'F': [F, 1],
  "F'": [F, 3],
  'F2': [F, 2],
  'M': [M, 1],
  "M'": [M, 3],
  'M2': [M, 2]
}

def Detector(msg_content):
  if str(msg_content) in move_list:
    for i in range(0, move_list[msg_content][1]):
      move_list[msg_content][0]()
    
    return True



#Display function
def display(cube, visual):
  visual = list(visual)
  cube = list(cube)
  visual[30] = cube[0]
  visual[47] = cube[3]
  visual[55] = cube[1]
  visual[68] = cube[6]
  visual[76] = cube[4]
  visual[84] = cube[2]
  visual[92] = cube[18]
  visual[98] = cube[7]
  visual[106] = cube[5]
  visual[112] = cube[29]
  visual[122] = cube[19]
  visual[128] = cube[8]
  visual[134] = cube[28]
  visual[144] = cube[21]
  visual[152] = cube[20]
  visual[156] = cube[27]
  visual[164] = cube[32]
  visual[174] = cube[22]
  visual[186] = cube[31]
  visual[196] = cube[24]
  visual[204] = cube[23]
  visual[208] = cube[30]
  visual[216] = cube[35]
  visual[226] = cube[25]
  visual[238] = cube[34]
  visual[256] = cube[26]
  visual[260] = cube[33]

  return "".join(visual)



#Solver Functions
def translate_kociemba():
  global cube
  cube = list(cube)
  temp = cube.copy()
  #switching the faces
  cube[9:18] = temp[27:36]
  cube[27:36] = temp[36:45]
  cube[36:45] = temp[9:18]

  cube = "".join(cube)


def translate_normal():
  global cube
  cube = list(cube)
  temp = cube.copy()
  #switching the faces
  cube[9:18] = temp[9:18]
  cube[27:36] = temp[27:36]
  cube[36:45] = temp[36:45]

  cube = "".join(cube)


def translate_tile_normal():
  global cube
  translation_map = {
    "U": "w", "D": "y", "F": "g", "B": "b", "L": "o", "R": "r"
  }
  cube = ''.join(translation_map[c] for c in cube)


def translate_tile_kociemba():
  global cube
  translation_map = {
    "w": "U", "y": "D", "g": "F", "b": "B", "o": "L", "r": "R"
  }
  cube = ''.join(translation_map[c] for c in cube)


def solver():
  global cube
  global move
  translate_kociemba()
  translate_tile_kociemba()
  x = kociemba.solve(cube).split()
  for i in x:
    move.append(i)
  translate_normal()
  translate_tile_normal()





class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    global cube
    global move
    
    if str(message.author) == "tastysnacc":#this is a joke loooool
      await message.channel.send("Hiii!!! wazaaaaap!!!!!!!!!!!")


    #Detects if someone said a command for a Move ---------------------------------------------------------------
    if Detector(message.content):
      await message.channel.send(f"```{display(cube, visual)}```")
    #------------------------------------------------------------------------------------------------------------

    if message.content == "Pong!":
      await message.channel.send("!ping")
    
    if message.content == "wysi":
      await message.channel.send("wysi boizzzzz")
    
    if message.content == ".":
      await message.channel.send("Can I ping pon spam plz")

    if message.content.lower() == "cube":
      await message.channel.send(f"```{display(cube, visual)}\nCube String:{cube}```")

    if message.content.lower() == "reset":
      await message.channel.send(f"```Cube String Deleted:{cube}```")
      cube = "wwwwwwwwwooooooooogggggggggrrrrrrrrryyyyyyyyybbbbbbbbb"
      await message.channel.send(f"```{display(cube, visual)}```")
      move = []

    #Solver
    if "solveplz:" in message.content[:9]:
      #Remove the "solveplz:" text in order to get Cube String
      message.content = list(message.content)[9:]
      cube = "".join(message.content)
      try:
        solver()
        await message.channel.send(f"Solution:{move}")
        await message.channel.send("reset")
      except:
        await message.channel.send("Dude, come on, why would you do this. How could you man.")
        await message.channel.send("I'm so mad to the point I'm gonna RESET THE CUBE >:(")
        cube = "wwwwwwwwwooooooooogggggggggrrrrrrrrryyyyyyyyybbbbbbbbb"
        await message.channel.send(f"```{display(cube, visual)}```")

    if "moveplz:" in message.content[:8]:
      message.content = message.content[8:].split(" ")

      try:
        for x in message.content:
          for y in range(0, move_list[x][1]):
            move_list[x][0]()
          await message.channel.send(f"```{display(cube, visual)}```")

      except:
        await message.channel.send("Ok man, VEEEERY funny.")

        
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')