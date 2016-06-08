# draws object
from collections import OrderedDict
import numpy as np

# globals
LOTTODRAWS = {  '2_1_31_repl':'EZ 2 Lotto',
                '3_0_9_repl':'SwerTres Lotto',
                '4_0_9_repl':'4-digit Lotto',
                '6_0_9_repl':'6-digit Lotto',
                '6_1_42_nrep':'Lotto 6/42',
                '6_1_45_nrep':'Mega Lotto 6/45',
                '6_1_49_nrep':'Super Lotto 6/49',
                '6_1_55_nrep':'Grand Lotto 6/55',
                '6_1_58_nrep':'Ultra Lotto 6/58'  }

LOTTODRAWS = OrderedDict(sorted(LOTTODRAWS.items(), key=lambda(k, v):k))
#keyval = sorted(LOTTODRAWS.items(), key=lambda(k, v):k)

class LottoGame(object):
    
    def __init__(self, draw=None):
        
        if draw == None:
            raise ValueError('No draw specified.')
        
        self.draw = draw
        self.args = self.parse_args()
    
    
    def parse_args(self):
        digits, low, up, samp = self.draw.split('_')
        
        return {'digits':int(digits), 'low':int(low),
                'up':int(up), 'samp':samp}
    
    def generate_result(self):
        repl = {'repl':True, 'nrep':False}
        
        return np.random.choice(xrange(self.args['low'], self.args['up']+1),
                                size=self.args['digits'],
                                replace=repl[self.args['samp']])
