# -*- coding=utf-8 -*-

"""Generator of admissible cells problems.

USAGE:
    python3 adm_cells_generator.py
"""


from __future__ import division

from pathlib import Path
from random import randrange, sample


# ============================================================================ #
#                                MAIN GENERATOR                                #
# ============================================================================ #
def adm_cell_generator(n_row, n_col, n_inst, dir_path, step=1):
    """Generator admissible cells instances.

    Parameters
    ----------
    n_row : int
        Number of rows
    n_col : int
        Number of columns
    n_inst : int
        Number of instances to generate
    dir_path : Path
        The directory in which there will be the instances
    step : int, optional
        The mult number of row and column numbers between each instance,
        by default 1
    """
    dir_path.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------------ #
    # Generate all the instances
    # ------------------------------------------------------------------------ #
    for k in range(n_inst):

        inst_path = dir_path / f'admissible_cells_{k}.data'
        with open(inst_path, 'w') as f_out:

            # Header
            # ------
            f_out.write(f'{n_row}\t{n_col}\n')

            # Admissible cells
            # ----------------
            f_out.write('ADMISSIBLE {\n')
            for i in range(n_row):
                n_adm = randrange(n_col)
                for j in sample([all_col for all_col in range(n_col)], n_adm):
                    f_out.write(f'\t{i}\t{j}\n')
            f_out.write('}\n')

            # Row limits
            # ----------
            f_out.write('ROW_LIMIT {\n')
            for i in range(n_row):
                i_limit = randrange(n_col * 3)
                f_out.write(f'\t{i}\t{i_limit}\n')
            f_out.write('}\n')

            # Column limits
            # -------------
            f_out.write('COLUMN_LIMIT {\n')
            for j in range(n_col):
                j_limit = randrange(n_row * 3)
                f_out.write(f'\t{j}\t{j_limit}\n')
            f_out.write('}')

        n_row += int(step * n_row)
        n_col += int(step * n_col)


if __name__ == '__main__':
    adm_cell_generator(10, 15, 5, Path('./'), step=1.5)
