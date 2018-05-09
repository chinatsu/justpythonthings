# equals print(datetime.datetime.now().strftime("%A")), which is just about as ugly as a oneliner
print(getattr(getattr(getattr(__import__("datetime"), "datetime"), "now")(), "strftime")("%A"))
