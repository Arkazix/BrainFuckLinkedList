from .linkedList import LinkedList


class Interpreter:

    def __init__(self, file_text: str):
        self.chars = "><+-.,[]"
        self.text = file_text
        self.current_idx = 0
        self.string = ""

    def get_string(self) -> str:
        return self.string

    def execute(self) -> LinkedList:
        link_list = LinkedList()
        link_list.push()
        while self.current_idx < len(self.text):
            char = self.text[self.current_idx]
            if char in self.chars:
                if char == ">":
                    self.current_idx += 1
                    link_list.right()
                elif char == "<":
                    self.current_idx += 1
                    link_list.left()
                elif char == "+":
                    self.current_idx += 1
                    link_list.current_node_inc()
                elif char == "-":
                    self.current_idx += 1
                    link_list.current_node_dec()
                elif char == ".":
                    self.current_idx += 1
                    ascii_int = link_list.current_node_get_value()
                    self.string += chr(ascii_int)
                elif char == ",":
                    self.current_idx += 1
                    user_input = input(">")
                    i = 0
                    for user_char in user_input:
                        link_list.current_node_set_value(ord(user_char))
                        i += 1
                        if i != len(user_input):
                            link_list.right()
                elif char == "[":
                    curr_node_value = link_list.current_node_get_value()
                    if curr_node_value == 0:
                        self.goto_next_closed_bracket()
                    self.current_idx += 1
                elif char == "]":
                    self.goto_last_open_bracket()
            else:
                self.current_idx += 1

        return link_list

    def goto_next_closed_bracket(self):
        """
        Goto to the next closed bracket in the code.
        [+--[]-]
        ⇧  =>  ⬆
        """
        current_char = self.text[self.current_idx]
        bracket = {"[": 1, "]": -1}
        bracket_number = 0
        while (current_char != "]" or bracket_number != 1) and \
                self.current_idx != len(self.text) - 1:
            if current_char in bracket:
                bracket_number += bracket[current_char]
            self.current_idx += 1
            current_char = self.text[self.current_idx]
        if (self.current_idx == len(self.text) - 1) and (current_char != ']' or bracket_number != 1):
            raise Exception("Unclaused bracket.")
    
    def goto_last_open_bracket(self):
        """
        Goto to the last open bracket in the code.
        [+--[]-]
        ⬆  <=  ⇧
        """
        current_char = self.text[self.current_idx]
        bracket = {"[": -1, "]": 1}
        bracket_number = 0
        while (current_char != "[" or bracket_number != 1) and \
                self.current_idx != 0:
            if current_char in bracket:
                bracket_number += bracket[current_char]
            self.current_idx -= 1
            current_char = self.text[self.current_idx]
        if (self.current_idx == 0) and (current_char != '[' or bracket_number != 1):
            raise Exception("Unclaused bracket.")