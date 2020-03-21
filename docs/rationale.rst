Why the Aurora Web Application Framework exist
==============================================

The python web framework ecosystem is big [1]_ but we fell that most of the
existing frameworks were inadequately designed and expose the user to non 
Pythonic constructs. Some of the issues found are discussed bellow.

One issue present on many Web frameworks is the use of global objects (thread 
local on some cases) to make interfaces more simpler [2]_ [3]_. Some of this 
frameworks for example provide a global request object [4]_ or a global 
response object [5]_. This particular case is very counter intuitive because a 
Web response is a consequence of a  specific Web request. In general 
presenting global objects violates the second principle of the 
`Zen of Python`_.

Another issue presented on many frameworks is the promotion of interface 
polymorphism on code implemented by the user. A common case is the polymorphism 
of the return value of request handlers [6]_ [7]_. The latter is counter 
intuitive because the framework user expect to produce a Web response for each 
request it process. And in many cases what is returned do not have a direct
translation into a Web response and require additional components to make this 
work. Thus moving user code dependency declaration from the interface into the 
implementation details. This violates the second principle and the thirteenth 
principle from the `Zen of Python`_.

.. _Zen of Python: https://www.python.org/dev/peps/pep-0020/
.. [1] https://wiki.python.org/moin/WebFrameworks
.. [2] https://docs.djangoproject.com/en/2.1/ref/contrib/messages/
.. [3] http://flask.pocoo.org/docs/1.0/quickstart/#sessions
.. [4] http://flask.pocoo.org/docs/1.0/quickstart/#accessing-request-data
.. [5] https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/advanced-features.html#use-global-response-objects
.. [6] https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/advanced-features.html#return-what-you-want-from-your-views
.. [7] http://web2py.com/books/default/chapter/29/04/the-core#Conditional-models