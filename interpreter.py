from linkedList import LinkedList


class Interpreter:

    def __init__(self, file_text: str):
        self.text = file_text
        self.chars = "><+-.,[]"
        self.string = ""

    def execute(self):
        link_list = LinkedList()
        link_list.push()
        for char in self.text:
            if char in self.chars:
                if char == ">":
                    link_list.right()
                elif char == "<":
                    link_list.left()
                elif char == "+":
                    link_list.current_node_inc()
                elif char == "-":
                    link_list.current_node_dec()
                elif char == ".":
                    ascii_int = link_list.current_node_get_value()
                    self.string += chr(ascii_int)
                elif char == ",":
                    user_input = input(">")
                    for user_char in user_input:
                        link_list.current_node_set_value(ord(user_char))
                        link_list.right()