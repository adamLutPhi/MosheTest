#__main__.py
#~\\pytest\\__main__.py

"""# ref: PEP-3122
Source: https://peps.python.org/pep-3122/#:~:text=__main__%20module%20attribute,-Another%20proposal%20was%20to%20add

ref: Stack-Overflow:
Source: https://stackoverflow.com/questions/64150674/python-command-line-sys-argv-if-name-main
"""

import sys

# Iniitial error : no sys.main delegate function

#>>AttributeError: module 'sys' has no attribute 'main'
#>>if __name__== sys.main:
#>>    pass 

class main(object):

    def __init__(cls) -> None :
        pass

    def main() -> None:
    
        # here: code raise exceptions,  on error
        # note: the `None` return type

        if __name__ == '__main__':
            main()

#instesad of this:        
#if __name__ == '__main__':
#    pass

"""
def main() -> None:
    # usually, we would be code-raising exceptions on error
    # Note the `None` return type

    if __name__ == '__main__':
        main()
"""
#only call the `static` function
main.main()
