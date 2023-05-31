### Move classes out of core.py

The file `core.py` currently has gotten very large and has multiple
classes which are largely independent of each other defined in
it. These classes would move to submodules that were more explicitly
organized by function.

The purpose of this move is to reduce potential conflicts in parallel
development and simply to make the code in the module, some of which
is the most important and critical, easier to read and review.
