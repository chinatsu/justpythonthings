print(__import__('requests').get("http://ip.jsontest.com/").json()["ip"])
