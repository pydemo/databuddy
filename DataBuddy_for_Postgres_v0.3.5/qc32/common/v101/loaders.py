import os
import imp
def load_class(filepath,expected_class):
	class_inst = None
	#expected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)

	if hasattr(py_mod, expected_class):
		class_inst = getattr(py_mod, expected_class)

	return class_inst
def import_module(filepath):
	class_inst = None
	#expected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)
	return py_mod