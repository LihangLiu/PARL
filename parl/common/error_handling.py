#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class LastExpError(Exception):
    """
    Raised when the last element or an element with non-zero game status is
    sampled.

    Attributes:
        message(string): error message
    """

    def __init__(self, idx, status):
        self.message = 'The element at {}'.format(idx)
        if status:
            self.message += ' has game status: {}'.format(status)
        else:
            self.message += ' is the last experience of a game.'


def check_last_exp_error(is_last_exp, idx, game_status):
    if is_last_exp:
        raise LastExpError(idx, game_status)


def check_type_error(type1, type2):
    if type1.__name__ != type2.__name__:
        raise TypeError('{} expected, but {} given.'
                        .format(type1.__name__, type2.__name__))


def check_eq(v1, v2):
    if v1 != v2:
        raise ValueError('{} == {} does not hold'.format(v1, v2))


def check_neq(v1, v2):
    if v1 == v2:
        raise ValueError('{} != {} does not hold'.format(v1, v2))


def check_gt(v1, v2):
    if v1 <= v2:
        raise ValueError('{} > {} does not hold'.format(v1, v2))


def check_geq(v1, v2):
    if v1 < v2:
        raise ValueError('{} >= {} does not hold'.format(v1, v2))


def check_lt(v1, v2):
    if v1 >= v2:
        raise ValueError('{} < {} does not hold'.format(v1, v2))


def check_leq(v1, v2):
    if v1 > v2:
        raise ValueError('{} <= {} does not hold'.format(v1, v2))
