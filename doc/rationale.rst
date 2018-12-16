Why the Aurora Web Application Framework was develop
====================================================

The python web framework ecosystem is big [#]_ but we fell that most of the
offers were inadequately designed and expose the user to non Pythonic 
constructs. Some of the issues found are discussed bellow.

One issue present on many Web frameworks is the use of global objects (thread 
local on some cases) to make interfaces more simpler [#]_ [#]_. Some of this 
frameworks for example provide a global request object [#]_ or a global 
response object [#]_. This particular case is very counter intuitive because a 
Web response is a consequence of a  specific Web request. In general 
presenting global objects violates the second principle of the 
`Zen of Python`_.

Another issue presented on many frameworks is the promotion of interface 
polymorphism on code implemented by the framework user. A common case is the
polymorphism of the return value of request handlers [#]_ [#]_. The latter is
counter intuitive because the framework user expect to produce a Web response
for each Web request it process. And in many cases what is returned do not
have a direct translation into a Web response and require additional components
to make this work. Thus moving user code dependency declaration from the 
interface into the implementation details. This violates the second principle
and the thirteenth principle from the `Zen of Python`_.

..  - component requirements gets replaced by the framework (because you need the 
..    framework to provide the component requirements trough the use of a global 
..    object or the request object) and the real component requirement expression 
..    is at the component implementation and not at the component interface

.. _Zen of Python: https://www.python.org/dev/peps/pep-0020/
.. [#] https://wiki.python.org/moin/WebFrameworks
.. [#] https://docs.djangoproject.com/en/2.1/ref/contrib/messages/
.. [#] http://flask.pocoo.org/docs/1.0/quickstart/#sessions
.. [#] http://flask.pocoo.org/docs/1.0/quickstart/#accessing-request-data
.. [#] https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/advanced-features.html#use-global-response-objects
.. [#] https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/advanced-features.html#return-what-you-want-from-your-views
.. [#] http://web2py.com/books/default/chapter/29/04/the-core#Conditional-models