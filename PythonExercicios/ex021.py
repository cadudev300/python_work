from playsound3 import playsound
sound = playsound('ice_cube.mp3', block=False)

print('O som esta tocando: ', sound.is_alive())
resp = str(input('Dseja Parar? [envie "s" ] '))
sound.stop()