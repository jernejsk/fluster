# Fluster - testing framework for decoders conformance
# Copyright (C) 2020, Fluendo, S.A.
#  Author: Ruben Gonzalez <rgonzalezs@fluendo.com>, Fluendo, S.A.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from fluster.codec import Codec, OutputFormat
from fluster.decoder import Decoder, register_decoder
from fluster.utils import file_checksum, run_command


@register_decoder
class H266JCTVTDecoder(Decoder):
    '''VVdeC H.266/VVC reference decoder implementation'''
    name = "VVdeC-H266"
    description = "VVdeC H.266/VVC reference decoder"
    codec = Codec.H266
    binary = 'vvdecapp'

    def decode(self, input_filepath: str, output_filepath: str, output_format: OutputFormat, timeout: int,
               verbose: bool) -> str:
        '''Decodes input_filepath in output_filepath'''
        run_command([self.binary, '-b', input_filepath,
                     '-o', output_filepath], timeout=timeout, verbose=verbose)
        return file_checksum(output_filepath)
