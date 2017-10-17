from __future__ import unicode_literals
from prompt_toolkit.filters import ViInsertMode
from prompt_toolkit.key_binding.input_processor import KeyPress
from prompt_toolkit.keys import Keys
from pygments.token import Token

from ptpython.layout import CompletionVisualisation

__all__ = (
    'configure',
)


def configure(repl):
    # Show function signature (bool).
    repl.show_signature = False

    # Show docstring (bool).
    repl.show_docstring = True
    
    # Ask for confirmation on exit.
    repl.confirm_exit = False
    
    # Enable input validation. (Don't try to execute when the input contains
    # syntax errors.)
    repl.enable_input_validation = True
    
    # Use this colorscheme for the code.
    repl.use_code_colorscheme('monokai')
    
    # Show completions. (NONE, POP_UP, MULTI_COLUMN or TOOLBAR)
    repl.completion_visualisation = CompletionVisualisation.POP_UP

    # When CompletionVisualisation.POP_UP has been chosen, use this
    # scroll_offset in the completion menu.
    repl.completion_menu_scroll_offset = 0

    # Show line numbers (when the input contains multiple lines.)
    repl.show_line_numbers = True

    # Show status bar.
    repl.show_status_bar = False

    # When the sidebar is visible, also show the help text.
    repl.show_sidebar_help = False

    # Highlight matching parethesis.
    repl.highlight_matching_parenthesis = False    
    
    # Vi mode.
    repl.vi_mode = True
    
    # Don't insert a blank line after the output.
    repl.insert_blank_line_after_output = False    
    
    # Complete while typing. (Don't require tab before the
    # completion menu is shown.)
    repl.complete_while_typing = True    