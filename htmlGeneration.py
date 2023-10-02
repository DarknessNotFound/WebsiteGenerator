def GenerateHTML(title, text, filename):
    f = open(filename, "x")
    f.write(f"<!DOCTYPE html>\n<html>\n<body>\n<h1>\n\t{title}\n</h1>\n<p>\t{text}</p>\n</body>\n</html>")
    f.close
    return None

def main():
    title = input("Enter Title: ")
    text = input("Enter some text: ")
    filename = input("Input file name: ")
    GenerateHTML(title, text, filename)


if __name__ == "__main__":
    main()