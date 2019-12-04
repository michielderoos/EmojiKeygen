import baseconvert

def convert_variable_base(key, input_base, output_base):
	bc = baseconvert.BaseConverter(input_base=input_base, output_base=output_base)
	converted = list(bc(key))
	return converted
