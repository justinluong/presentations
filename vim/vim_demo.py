########################################################################################
# Navigating Code
########################################################################################

### Basic Navigation ###

# G -> End of file
# h -> Left
# l -> Right
# j -> Down
# k -> Up
# 0 -> Start of line
# $ -> End of line
# w -> Start of next word
# e -> End of current/next word
# b -> Start of current/previous word

def func_one(arg1, arg2):
    return """
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a
type specimen book.
    """

### Modifying Code ###

# a -> Enter insert mode after current character
# Esc -> Exit insert mode
# o -> Enter insert mode in new line
# x -> Delete character
# dw -> Delete word
# dd -> Delete line

def func_two(arg1, arg2):
    """
    Lorem Ipsum is simply dumm hel the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    """
    project = "gcp-example-project-dev"
    return project

### Other Useful Commands ###
# shift + v -> Select line
# x -> Cut
# p -> Paste
# y -> Copy (Yank)
# v -> Select mode
# u -> Undo

def func_three(arg1, arg2):
    """
    Lorem Ipsum is simply dumm hel the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    """
    project = "gcp-example-project"
    bucket = "gs://example/bucket"
    region = "us-central1"
    details = [
        "project",
        "bucket",
        "region"
    ]
    return details


def func_four(arg1, arg2):
    """
    Lorem Ipsum is simply dumm hel the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    """
    pass


### Basic Navigation Continued ###
# gg -> Beginning of file