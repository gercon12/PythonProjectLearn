#Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

#is_balanced("({a+b})")     --> True
#is_balanced("))((a+b}{")   --> False
#is_balanced("((a+b))")     --> True
#is_balanced("))")          --> False
#is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True


from collections import deque  # Import deque for an efficient stack backend

class Stack:
    def __init__(self):
        # Use deque as the internal container (O(1) push/pop from the right)
        self.container = deque()

    def push(self, val):
        # Push an element onto the top of the stack
        self.container.append(val)

    def pop(self):
        # Remove and return the top element; raises IndexError if the stack is empty
        return self.container.pop()

    def peek(self):
        # Return the top element without removing it
        return self.container[-1]

    def is_empty(self):
        # Return True if the stack has no elements
        return len(self.container) == 0

    def size(self):
        # Return the number of elements in the stack
        return len(self.container)

    def count(self, val):
        # Count how many times 'val' appears in the stack
        return self.container.count(val)


def is_balanced(exp):
    """
    Check whether all bracket characters in 'exp' are balanced and properly nested.
    We consider (), {}, and [] as valid bracket pairs.
    Non-bracket characters are ignored.
    """
    s = Stack()                       # Create a fresh, empty stack

    for ch in exp:                    # Iterate through the expression character by character
        if ch in "({[":               # If it's an opening bracket...
            s.push(ch)                # ...push it to remember we need a matching closer later
        elif ch in ")}]":             # If it's a closing bracket...
            if s.is_empty():          # ...there must be a previous opening bracket to match
                return False          # No opening bracket available → not balanced
            top = s.pop()             # Pop the most recent opening bracket
            # Check that the types of brackets match ((), {}, [])
            if (ch == ")" and top != "(") or \
               (ch == "}" and top != "{") or \
               (ch == "]" and top != "["):
                return False          # Mismatched pair → not balanced
        # Any other character is ignored

    return s.is_empty()               # Balanced only if no unmatched openings remain


# ---- Example usage / quick tests (prints True/False) ----
tests = [
    "({a+b})",                        # True: properly nested
    "({a+b]}",                        # False: } closes { but ] appears
    "((a+b))",                        # True
    "((a+b)",                         # False: one '(' left unmatched
    "function(x) { return [x, (x+1)]; }",  # True: mixed bracket types, all matched
    "())("                            # False: wrong order
]

for t in tests:
    print(f"{t!r} -> {is_balanced(t)}")



# Ejemplo de uso
print(is_balanced("({a+b})"))     #--> True
print(is_balanced("))((a+b}{"))   #--> False
print(is_balanced("((a+b))"))     #--> True
print(is_balanced("))"))          #--> False
print(is_balanced("[a+b]*(x+2y)*{gg+kk}")) #--> True
