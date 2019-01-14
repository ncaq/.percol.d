percol.view.PROMPT = "<blue>Input:</blue> %q"
percol.view.RPROMPT = "(%F) [%i/%I]"

percol.import_keymap({
    "C-a" : lambda percol: percol.command.beginning_of_line(),
    "C-b" : lambda percol: percol.command.delete_backward_char(),
    "C-d" : lambda percol: percol.command.delete_forward_char(),
    "C-e" : lambda percol: percol.command.end_of_line(),
    "C-g" : lambda percol: percol.cancel(),
    "C-h" : lambda percol: percol.command.backward_char(),
    "C-j" : lambda percol: percol.finish(),
    "C-k" : lambda percol: percol.command.kill_end_of_line(),
    "C-m" : lambda percol: percol.finish(),
    "C-n" : lambda percol: percol.command.select_next(),
    "C-s" : lambda percol: percol.command.forward_char(),
    "C-t" : lambda percol: percol.command.select_previous(),
    "C-v" : lambda percol: percol.command.select_next_page(),
    "C-y" : lambda percol: percol.command.yank(),
    "M-<" : lambda percol: percol.command.select_top(),
    "M->" : lambda percol: percol.command.select_bottom(),
    "M-b" : lambda percol: percol.command.delete_backward_word(),
    "M-h" : lambda percol: percol.command.backward_word(),
    "M-s" : lambda percol: percol.command.forward_word(),
    "M-v" : lambda percol: percol.command.select_previous_page(),
})
