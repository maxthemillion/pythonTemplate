
/scripts or /bin for that kind of command-line interface stuff
/tests for your tests
/lib for your C-language libraries
/doc for most documentation
/apidoc for the Epydoc-generated API docs.
And the top-level directory can contain README's, Config's and whatnot.


I recommend putting all of this under the "name-of-my-product" directory. So, if you're writing an application named quux, the directory that contains all this stuff is named  /quux.

Another project's PYTHONPATH, then, can include /path/to/quux/foo to reuse the QUUX.foo module.

In my case, since I use Komodo Edit, my IDE cuft is a single .KPF file. I actually put that in the top-level /quux directory, and omit adding it to SVN.

