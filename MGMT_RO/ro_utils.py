# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 15:46:53 2024

@author: ifrommer
"""
def adjusted_flow(x, attr = 1, w_or = False):
    msg = 'which is adjusted by '
    adj_x = x
    if attr != 1:
        msg += f'\n attraction factor of {attr}'
        adj_x = x * attr
    if w_or:
        msg += f'\n outer ring weight of {w_or}'
        adj_x = adj_x * w_or
    if attr == 1 and not(w_or): 
        msg = ''
    else:
        msg += f'\n to {adj_x}'
        print(msg)
    
    return adj_x, msg

x = 140
adj_x, msg = adjusted_flow(x, 1, .5)
#if msg:
#   print(f'Flow of {x}',msg,f'\n to {adj_x}')
    