import importlib


class LammpsPotential:
    def __init__(self,
                 potential_data,
                 structure,
                 potential_filename='None'):

        self._names = [site.name for site in structure.kinds]
        self._type = potential_data.dict.pair_style
        self._data = potential_data.dict.data

        self._potential_filename = potential_filename

        try:
            self._potential_module = importlib.import_module('.{}'.format(self._type), __name__)
        except ImportError:
            raise ImportError('This lammps potential is not implemented')

    def get_potential_file(self):
        return self._potential_module.generate_LAMMPS_potential(self._data)

    def get_input_potential_lines(self):
        return self._potential_module.get_input_potential_lines(self._data,
                                                                potential_filename=self._potential_filename,
                                                                names=self._names)
