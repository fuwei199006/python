#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wells
# @Date:   2015-12-29 15:00:32
# @Last Modified by:   wells
# @Last Modified time: 2015-12-29 15:12:36
class student(object):
    def __init__(self, name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s' % (self.name,self.score))

bart=student("fuwei",90)
bart.print_score()
print(type(bart))
print(isinstance(bart,student))
        