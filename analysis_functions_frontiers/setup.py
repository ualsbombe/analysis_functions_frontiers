# -*- coding: utf-8 -*-

from distutils.core import setup
setup(name='analysis_functions_frontiers',
      version='1.0',
      description='IO, Operation and Plot methods for the article: Group analysis in MNE-Python of evoked response from a tactile stimulation paradigm: a pipeline for reproducibility at every step of processing, going from individual sensor space representations to an across-group source space representation',
      author=u'Lau Møller Andersen',
      author_email='lau.moller.andersen@ki.se, ualsbombe@gmail.com',
      url='None_at_the_moment',
      packages=['analysis_functions_frontiers/io_functions', 'analysis_functions_frontiers/operations_functions', 'analysis_functions_frontiers/plot_functions'],
      )
