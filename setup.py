from distutils.core import setup 
import py2exe 
 
setup(name="Mem_py", 
 version="1.0", 
 description="JUEGARDO DE COINCIDENCIAS", 
 author="TOMAS,TOBIAS Y YO", 
 author_email="None", 
 url="None", 
 license="None", 
 scripts=["ejecutar.py"], 
 console=["ejecutar.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)