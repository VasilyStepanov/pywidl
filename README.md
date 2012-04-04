PyWIdl
======

Generic code generator from WebIDL interfaces.

pywidl parses WebIDL code using PLY, builds the interface object model and emits
whatever code using user's mako templates or even user's native python module.



Links
-----
 + [github](https://github.com/VasilyStepanov/pywidl)
 + [pypi](http://pypi.python.org/pypi/pywidl)



Installation
------------

Installing with pip:

    pip install pywidl

gentoo users may use [odin overlay](https://github.com/KonstantinGrigoriev/odin-overlay):

    emerge pywidl



WebIDL object model
-------------------

Defined in pywidl/model.py

Common usage in tests/idl.py



autoconf users
---------------

[m4](https://raw.github.com/VasilyStepanov/pywidl/master/m4/pywidl.m4) script
may be useful for you.

You may find m4 usage example in
[libcssom](https://github.com/VasilyStepanov/libcssom) project.



Example usage
-------------

$ cat fragment.idl

    exception GraphicsException {
      DOMString reason;
    };

    interface Paint { };

    interface SolidColor : Paint {
      attribute float red;
      attribute float green;
      attribute float blue;
    };

    interface Pattern : Paint {
      attribute DOMString imageURL;
    };

    [Constructor]
    interface GraphicalWindow {
      readonly attribute unsigned long width;
      readonly attribute unsigned long height;

      attribute Paint currentPaint;

      void drawRectangle(float x, float y, float width, float height);

      void drawText(float x, float y, DOMString text);
    };

$ cat mako.tpl

    // ${foo}
    % for definition in definitions:
    ${definition.name}
    % endfor

$ pywidl -m -o fragment.txt -t mako.tpl fragment.idl -- --foo=bar

$ cat fragment.txt
    
    // bar
    GraphicsException
    Paint
    SolidColor
    Pattern
    GraphicalWindow

$ cat native.py

    def render(definitions=[], source=None, output=None,
      template=None, template_type=None, foo=None, **kwargs):

      with open(output, 'w') as out:
        print >>out, "// %s" % foo
        for definition in definitions:
          print >>out, definition.name

$ PYTHONPATH=".:$PYTHONPATH"
pywidl -n -o fragment.txt -t native fragment.idl -- --foo=bar

$ cat fragment.txt

    // bar
    GraphicsException
    Paint
    SolidColor
    Pattern
    GraphicalWindow

