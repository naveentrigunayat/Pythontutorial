#                                          Package



Packages are a way of structuring Python’s module namespace by using “dotted module names”. 
A package can have one or more modules which means, a package is collection of modules and packages. 
A package can contain packages. 
Package is nothing but a Directory/Folder



#                                   Creating Package


Package is nothing but a Directory/Folder which MUST contain a special file called __init__.py. 
__init__.py file can be empty, it indicates that the directory it contains is a Python package, 
so it can be imported the same way a module can be imported



#                                   How to use Package


Syntax:- import packageName.moduleName
Syntax:- import packageName.subPackageName.moduleName
Ex:- import Admin.service
Ex:- import Admin.Common.footer



How to Access Variable, Function, Method, Class etc. ?
Syntax:- packageName.moduleName.functionName()
Syntax:- packageName.subPackageName.moduleName.functionName()
Ex:- Admin.service.admin_service( )
Ex:- Admin.Common.footer.admin_common_footer( )


Syntax:- from packageName import moduleName
Syntax:- from packageName.subPackageName import moduleName
Ex:- from Admin import service
Ex:- from Admin.Common import footer


How to Access Variable, Function, Method, Class etc.
Syntax:- moduleName.functionName()
Ex:-
service.admin_service( )
footer.admin_common_footer( )


Syntax:- from packageName.moduleName import fun_name
Syntax:- from packageName.subPackageName.moduleName import fun_name
Ex:- from Admin.service import admin_service
Ex:- from Admin.Common.footer import admin_common_footer

How to Access Variable, Function, Method, Class etc.
Syntax:- functionName()
Ex:-
admin_service( )
admin_common_footer( )


Syntax:- from packageName import *
Syntax:- from packageName.subPackageName import *
Ex:- from Admin import *
Ex:- from Admin.Common import *

How to Access Variable, Function, Method, Class etc.
Syntax:- moduleName.functionName()
Ex:-
service.admin_service( )
footer.admin_common_footer( )



#                                       __all__


if a package’s __init__.py code defines a list named __all__, 
it is taken to be the list of module names that should be imported when from package import * is encountered. 
__all__ = [‘dashboard’, ‘service’, ‘product’]
