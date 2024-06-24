def test_var_args(*argv, **kwargs):
	for k in kwargs:

		print("another arg  *argv:  ", kwargs[k])

test_var_args(name='biruk', skill='kacking')
