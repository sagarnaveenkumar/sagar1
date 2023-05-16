# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str) -> None:
        print(f">>> Multi-line Comment\n{data}") if "\n" in data else print(f">>> Single-line Comment\n{data}")

    def handle_data(self, data: str) -> None:
        if data != "\n":
            print(f">>> Data\n{data}")

N = int(input())
parser = MyHTMLParser()

parser.feed("\n".join([input() for _ in range(N)]))
