import requests
from matplotlib import pyplot as plt

with open("lenna.png", "wb") as img_f:
    img_f.write(requests.get("https://i.stack.imgur.com/nL4u3.png").content)