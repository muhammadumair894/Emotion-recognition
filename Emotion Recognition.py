import Algorithmia

client = Algorithmia.client("simUSwqPtOxKOh/tsQxXPr6AGnh1")

#path = "https://upload.wikimedia.org/wikipedia/commons/4/4e/Monroecirca1953.jpg"
path = r"https://yt3.ggpht.com/a/AGF-l78RiH4GMxCdTTyd-G6hedbhX2LCIdNXejRCaQ=s900-c-k-c0xffffffff-no-rj-mo"
input = {
    "image": path,
    "numResults": 7
}

algo = client.algo('deeplearning/EmotionRecognitionCNNMBP/0.1.2')

result = algo.pipe(input).result

print(result)