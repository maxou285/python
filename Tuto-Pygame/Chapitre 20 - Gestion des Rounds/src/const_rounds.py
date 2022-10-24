##########################################################################################
# Tous les rounds sont ici définis suivant le format suivant :
#   [ couleur de fond, la carte des briques ]
##########################################################################################

ROUNDS = [

    # Round 1
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'],
            ['red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   ],
            ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'],
            ['blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  ],
            ['pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  ],
            ['green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' ]
        ]
    ],         

    # Round 2
    [   (0, 128, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['white' , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['white' , 'orange', None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['white' , 'orange', 'cyan'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['white' , 'orange', 'cyan'  , 'green' , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['white' , 'orange', 'cyan'  , 'green' , 'red'   , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['white' , 'orange', 'cyan'  , 'green' , 'red'   , 'blue'  , None    , None    , None    , None    , None    , None    , None    ],
            ['white' , 'orange', 'cyan'  , 'green' , 'red'   , 'blue'  , 'pink'  , None    , None    , None    , None    , None    , None    ],
            ['white' , 'orange', 'cyan'  , 'green' , 'red'   , 'blue'  , 'pink'  , 'yellow', None    , None    , None    , None    , None    ],
            ['white' , 'orange', 'cyan'  , 'green' , 'red'   , 'blue'  , 'pink'  , 'yellow', 'white' , None    , None    , None    , None    ],
            ['white' , 'orange', 'cyan'  , 'green' , 'red'   , 'blue'  , 'pink'  , 'yellow', 'white' , 'orange', None    , None    , None    ],
            ['white' , 'orange', 'cyan'  , 'green' , 'red'   , 'blue'  , 'pink'  , 'yellow', 'white' , 'orange', 'cyan'  , None    , None    ],
            ['white' , 'orange', 'cyan'  , 'green' , 'red'   , 'blue'  , 'pink'  , 'yellow', 'white' , 'orange', 'cyan'  , 'green' , None    ],
            ['silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'red'   ]
        ]
    ],         

    # Round 3
    [   (0, 0, 64),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['white' , 'white' , 'white' , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'white' , 'white' , 'white' ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['blue'  , 'blue'  , 'blue'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'cyan'  , 'cyan'  , 'cyan'  ]
        ]
    ],

    # Round 4
    [   (128, 0, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'orange', 'cyan'  , 'green' , 'silver', 'blue'  , None    , 'yellow', 'white' , 'orange', 'cyan'  , 'green' , None    ],
            [None    , 'cyan'  , 'green' , 'silver', 'blue'  , 'pink'  , None    , 'white' , 'orange', 'cyan'  , 'green' , 'silver', None    ],
            [None    , 'green' , 'silver', 'blue'  , 'pink'  , 'yellow', None    , 'orange', 'cyan'  , 'green' , 'silver', 'blue'  , None    ],
            [None    , 'silver', 'blue'  , 'pink'  , 'yellow', 'white' , None    , 'cyan'  , 'green' , 'silver', 'blue'  , 'pink'  , None    ],
            [None    , 'blue'  , 'pink'  , 'yellow', 'white' , 'orange', None    , 'green' , 'silver', 'blue'  , 'pink'  , 'yellow', None    ],
            [None    , 'pink'  , 'yellow', 'white' , 'orange', 'cyan'  , None    , 'silver', 'blue'  , 'pink'  , 'yellow', 'white' , None    ],
            [None    , 'yellow', 'white' , 'orange', 'cyan'  , 'green' , None    , 'blue'  , 'pink'  , 'yellow', 'white' , 'orange', None    ],
            [None    , 'white' , 'orange', 'cyan'  , 'green' , 'silver', None    , 'pink'  , 'yellow', 'white' , 'orange', 'cyan'  , None    ],
            [None    , 'orange', 'cyan'  , 'green' , 'silver', 'blue'  , None    , 'yellow', 'white' , 'orange', 'cyan'  , 'green' , None    ],
            [None    , 'cyan'  , 'green' , 'silver', 'blue'  , 'pink'  , None    , 'white' , 'orange', 'cyan'  , 'green' , 'silver', None    ],
            [None    , 'green' , 'silver', 'blue'  , 'pink'  , 'yellow', None    , 'orange', 'cyan'  , 'green' , 'silver', 'blue'  , None    ],
            [None    , 'silver', 'blue'  , 'pink'  , 'yellow', 'white' , None    , 'cyan'  , 'green' , 'silver', 'blue'  , 'pink'  , None    ],
            [None    , 'blue'  , 'pink'  , 'yellow', 'white' , 'orange', None    , 'green' , 'silver', 'blue'  , 'pink'  , 'yellow', None    ],
            [None    , 'pink'  , 'yellow', 'white' , 'orange', 'cyan'  , None    , 'silver', 'blue'  , 'pink'  , 'yellow', 'white' , None    ]
        ]
    ],

    # Round 5
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , 'yellow', None    , None    , None    , None    , None    , 'yellow', None    , None    , None    ],
            [None    , None    , None    , 'yellow', None    , None    , None    , None    , None    , 'yellow', None    , None    , None    ],
            [None    , None    , None    , None    , 'yellow', None    , None    , None    , 'yellow', None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'yellow', None    , None    , None    , 'yellow', None    , None    , None    , None    ],
            [None    , None    , None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    , None    , None    ],
            [None    , None    , None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    , None    , None    ],
            [None    , None    , 'silver', 'silver', 'red'   , 'silver', 'silver', 'silver', 'red'   , 'silver', 'silver', None    , None    ],
            [None    , None    , 'silver', 'silver', 'red'   , 'silver', 'silver', 'silver', 'red'   , 'silver', 'silver', None    , None    ],
            [None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    ],
            [None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    ],
            [None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    ],
            [None    , 'silver', None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    , 'silver', None    ],
            [None    , 'silver', None    , 'silver', None    , None    , None    , None    , None    , 'silver', None    , 'silver', None    ],
            [None    , 'silver', None    , 'silver', None    , None    , None    , None    , None    , 'silver', None    , 'silver', None    ],
            [None    , None    , None    , None    , 'silver', 'silver', None    , 'silver', 'silver', None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'silver', 'silver', None    , 'silver', 'silver', None    , None    , None    , None    ]
        ]
    ],

    # Round 6
    [   (0, 128, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ],
            ['blue'  , None    , 'gold'  , 'orange', 'gold'  , 'orange', 'gold'  , 'orange', 'gold'  , 'orange', 'gold'  , None    , 'blue'  ],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ],
            ['orange', None    , 'orange', None    , 'gold'  , None    , 'orange', None    , 'gold'  , None    , 'orange', None    , 'orange'],
            ['blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  ]
        ]
    ],

    # Round 7
    [   (0, 0, 92),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , 'yellow', 'yellow', 'pink'  , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'yellow', 'yellow', 'pink'  , 'pink'  , 'blue'  , None    , None    , None    , None    ],
            [None    , None    , None    , 'yellow', 'yellow', 'pink'  , 'pink'  , 'blue'  , 'blue'  , 'red'   , None    , None    , None    ],
            [None    , None    , None    , 'yellow', 'pink'  , 'pink'  , 'blue'  , 'blue'  , 'red'   , 'red'   , None    , None    , None    ],
            [None    , None    , 'yellow', 'pink'  , 'pink'  , 'blue'  , 'blue'  , 'red'   , 'red'   , 'green' , 'green' , None    , None    ],
            [None    , None    , 'pink'  , 'pink'  , 'blue'  , 'blue'  , 'red'   , 'red'   , 'green' , 'green' , 'cyan'  , None    , None    ],
            [None    , None    , 'pink'  , 'blue'  , 'blue'  , 'red'   , 'red'   , 'green' , 'green' , 'cyan'  , 'cyan'  , None    , None    ],
            [None    , None    , 'blue'  , 'blue'  , 'red'   , 'red'   , 'green' , 'green' , 'cyan'  , 'cyan'  , 'orange', None    , None    ],
            [None    , None    , 'blue'  , 'red'   , 'red'   , 'green' , 'green' , 'cyan'  , 'cyan'  , 'orange', 'orange', None    , None    ],
            [None    , None    , 'red'   , 'red'   , 'green' , 'green' , 'cyan'  , 'cyan'  , 'orange', 'orange', 'white' , None    , None    ],
            [None    , None    , None    , 'green' , 'green' , 'cyan'  , 'cyan'  , 'orange', 'orange', 'white' , None    , None    , None    ],
            [None    , None    , None    , 'green' , 'cyan'  , 'cyan'  , 'orange', 'orange', 'white' , 'white' , None    , None    , None    ],
            [None    , None    , None    , None    , 'cyan'  , 'orange', 'orange', 'white' , 'white' , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , 'orange', 'orange', 'white' , None    , None    , None    , None    , None    ]
        ]
    ],

    # Round 8
    [   (92, 0, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  , None    ],
            [None    , 'gold'  , 'gold'  , None    , 'gold'  , None    , None    , None    , 'gold'  , None    , 'gold'  , 'gold'  , None    ],
            [None    , None    , None    , None    , None    , None    , 'white' , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , 'gold'  , 'orange', 'gold'  , None    , None    , None    , 'gold'  , None    ],
            [None    , None    , None    , 'gold'  , None    , None    , 'cyan'  , None    , None    , 'gold'  , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , 'green' , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , 'gold'  , None    , None    , 'red'   , None    , None    , 'gold'  , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , 'gold'  , 'blue'  , 'gold'  , None    , None    , None    , 'gold'  , None    ],
            [None    , None    , None    , None    , None    , None    , 'pink'  , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , 'gold'  , None    , 'gold'  , None    , None    , None    , 'gold'  , None    , 'gold'  , 'gold'  , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  , None    ],
            [None    , None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    , None    ]
        ]
    ],

    # Round 9
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , None    , 'gold'  , None    ],
            [None    , 'gold'  , 'green' , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , 'green' , 'gold'  , None    ],
            [None    , 'gold'  , 'cyan'  , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , 'cyan'  , 'gold'  , None    ],
            [None    , 'gold'  , 'gold'  , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , 'gold'  , 'gold'  , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'pink'  , 'white' , 'white' , 'white' , 'yellow', None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'pink'  , 'orange', 'orange', 'orange', 'yellow', None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'pink'  , 'cyan'  , 'cyan'  , 'cyan'  , 'yellow', None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'pink'  , 'green' , 'green' , 'green' , 'yellow', None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'pink'  , 'red'   , 'red'   , 'red'   , 'yellow', None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'pink'  , 'blue'  , 'blue'  , 'blue'  , 'yellow', None    , None    , None    , None    ]
        ]
    ],

    # Round 10
    [   (0, 144, 0),
        [
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , 'blue'  , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , 'blue'  , 'cyan'  , 'blue'  , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , 'blue'  , 'cyan'  , 'white' , 'cyan'  , 'blue'  , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , 'blue'  , 'cyan'  , 'white' , 'cyan'  , 'white' , 'cyan'  , 'blue'  , None    , None    ],
            [None    , 'gold'  , None    , 'blue'  , 'cyan'  , 'white' , 'cyan'  , 'silver', 'cyan'  , 'white' , 'cyan'  , 'blue'  , None    ],
            [None    , 'gold'  , None    , None    , 'blue'  , 'cyan'  , 'white' , 'cyan'  , 'white' , 'cyan'  , 'blue'  , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , 'blue'  , 'cyan'  , 'white' , 'cyan'  , 'blue'  , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , 'blue'  , 'cyan'  , 'blue'  , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , 'blue'  , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  ]
        ]
    ],

    # Round 11
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    ],
            [None    , 'silver', None    , None    , None    , None    , None    , None    , None    , None    , None    , 'silver', None    ],
            [None    , 'silver', None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    , 'silver', None    ],
            [None    , 'silver', None    , 'silver', None    , None    , None    , None    , None    , 'silver', None    , 'silver', None    ],
            [None    , 'silver', None    , 'silver', None    , 'silver', 'silver', 'silver', None    , 'silver', None    , 'silver', None    ],
            [None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    ],
            [None    , 'silver', None    , 'silver', None    , 'silver', 'silver', 'silver', None    , 'silver', None    , 'silver', None    ],
            [None    , 'silver', None    , 'silver', None    , None    , None    , None    , None    , 'silver', None    , 'silver', None    ],
            [None    , 'silver', None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    , 'silver', None    ],
            [None    , 'silver', None    , None    , None    , None    , None    , None    , None    , None    , None    , 'silver', None    ],
            [None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    ]
        ]
    ],

    # Round 12
    [   (128, 0, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  ],
            [None    , None    , None    , None    , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , 'pink'  , None    ],
            [None    , 'gold'  , 'white' , None    , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , None    , None    ],
            [None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    ],
            [None    , 'gold'  , None    , None    , 'gold'  , 'green' , None    , 'gold'  , None    , None    , 'gold'  , None    , None    ],
            [None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    ],
            [None    , 'gold'  , None    , 'orange', 'gold'  , None    , None    , 'gold'  , None    , 'blue'  , 'gold'  , None    , None    ],
            [None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    ],
            [None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    ],
            [None    , 'gold'  , None    , None    , 'gold'  , None    , 'red'   , 'gold'  , None    , None    , 'gold'  , None    , None    ],
            [None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    ],
            [None    , 'gold'  , 'cyan'  , None    , 'gold'  , None    , None    , 'gold'  , None    , None    , 'gold'  , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , None    , None    , None    , None    , 'yellow'],
            [None    , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  ]
        ]
    ],

    # Round 13
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'yellow', 'yellow', 'yellow', None    , 'white' , 'white' , 'white' , None    , 'yellow', 'yellow', 'yellow', None    ],
            [None    , 'pink'  , 'pink'  , 'pink'  , None    , 'orange', 'orange', 'orange', None    , 'pink'  , 'pink'  , 'pink'  , None    ],
            [None    , 'blue'  , 'blue'  , 'blue'  , None    , 'cyan'  , 'cyan'  , 'cyan'  , None    , 'blue'  , 'blue'  , 'blue'  , None    ],
            [None    , 'red'   , 'red'   , 'red'   , None    , 'green' , 'green' , 'green' , None    , 'red'   , 'red'   , 'red'   , None    ],
            [None    , 'green' , 'green' , 'green' , None    , 'red'   , 'red'   , 'red'   , None    , 'green' , 'green' , 'green' , None    ],
            [None    , 'cyan'  , 'cyan'  , 'cyan'  , None    , 'blue'  , 'blue'  , 'blue'  , None    , 'cyan'  , 'cyan'  , 'cyan'  , None    ],
            [None    , 'orange', 'orange', 'orange', None    , 'pink'  , 'pink'  , 'pink'  , None    , 'orange', 'orange', 'orange', None    ],
            [None    , 'white' , 'white' , 'white' , None    , 'yellow', 'yellow', 'yellow', None    , 'white' , 'white' , 'white' , None    ]
        ]
    ],

    # Round 14
    [   (0, 128, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  ],
            ['gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  ],
            ['blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['orange', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'orange'],
            ['gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  ],
            ['white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['cyan'  , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'cyan'  ],
            ['gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  ],
            ['red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   ],
            ['gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  ]
        ]
    ],

    # Round 15
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['cyan'  , 'white' , 'gold'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'gold'  , 'white' , 'cyan'  ],
            ['cyan'  , 'white' , 'yellow', 'gold'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'gold'  , 'green' , 'white' , 'cyan'  ],
            ['cyan'  , 'white' , 'yellow', 'yellow', 'gold'  , 'cyan'  , 'cyan'  , 'cyan'  , 'gold'  , 'green' , 'green' , 'white' , 'cyan'  ],
            ['cyan'  , 'white' , 'yellow', 'yellow', 'yellow', 'gold'  , 'white' , 'gold'  , 'green' , 'green' , 'green' , 'white' , 'cyan'  ],
            ['cyan'  , 'white' , 'yellow', 'yellow', 'yellow', 'yellow', 'white' , 'green' , 'green' , 'green' , 'green' , 'white' , 'cyan'  ],
            ['cyan'  , 'white' , 'yellow', 'yellow', 'yellow', 'yellow', 'white' , 'green' , 'green' , 'green' , 'green' , 'white' , 'cyan'  ],
            ['cyan'  , 'white' , 'yellow', 'yellow', 'yellow', 'yellow', 'white' , 'green' , 'green' , 'green' , 'green' , 'white' , 'cyan'  ],
            ['cyan'  , 'silver', 'yellow', 'yellow', 'yellow', 'yellow', 'white' , 'green' , 'green' , 'green' , 'green' , 'silver', 'cyan'  ],
            ['cyan'  , 'cyan'  , 'silver', 'yellow', 'yellow', 'yellow', 'white' , 'green' , 'green' , 'green' , 'silver', 'cyan'  , 'cyan'  ],
            ['cyan'  , 'cyan'  , 'cyan'  , 'silver', 'yellow', 'yellow', 'white' , 'green' , 'green' , 'silver', 'cyan'  , 'cyan'  , 'cyan'  ],
            ['cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'silver', 'yellow', 'white' , 'green' , 'silver', 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  ],
            ['cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'silver', 'white' , 'silver', 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  ]
        ]
    ],

    # Round 16
    [   (128, 0, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , 'gold'  , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'white' , 'white' , None    , 'white' , 'white' , None    , None    , None    , None    ],
            [None    , None    , 'white' , 'white' , None    , None    , 'gold'  , None    , None    , 'white' , 'white' , None    , None    ],
            ['white' , 'white' , None    , None    , 'orange', 'orange', None    , 'orange', 'orange', None    , None    , 'white' , 'white' ],
            [None    , None    , 'orange', 'orange', None    , None    , 'gold'  , None    , None    , 'orange', 'orange', None    , None    ],
            ['orange', 'orange', None    , None    , 'yellow', 'yellow', None    , 'yellow', 'yellow', None    , None    , 'orange', 'orange'],
            [None    , None    , 'yellow', 'yellow', None    , None    , 'gold'  , None    , None    , 'yellow', 'yellow', None    , None    ],
            ['yellow', 'yellow', None    , None    , 'green' , 'green' , None    , 'green' , 'green' , None    , None    , 'yellow', 'yellow'],
            [None    , None    , 'green' , 'green' , None    , None    , 'gold'  , None    , None    , 'green' , 'green' , None    , None    ],
            ['green' , 'green' , None    , None    , 'red'   , 'red'   , None    , 'red'   , 'red'   , None    , None    , 'green' , 'green' ],
            [None    , None    , 'red'   , 'red'   , None    , None    , 'gold'  , None    , None    , 'red'   , 'red'   , None    , None    ],
            ['red'   , 'red'   , None    , None    , 'blue'  , 'blue'  , None    , 'blue'  , 'blue'  , None    , None    , 'red'   , 'red'   ],
            [None    , None    , 'blue'  , 'blue'  , None    , None    , None    , None    , None    , 'blue'  , 'blue'  , None    , None    ],
            ['blue'  , 'blue'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'blue'  , 'blue'  ]
        ]
    ],

    # Round 17
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , 'silver', None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , 'blue'  , 'blue'  , 'blue'  , 'silver', 'green' , 'green' , None    , None    , None    , None    ],
            [None    , None    , 'blue'  , 'blue'  , 'blue'  , 'white' , 'white' , 'white' , 'green' , 'green' , 'green' , None    , None    ],
            [None    , None    , 'blue'  , 'blue'  , 'white' , 'white' , 'white' , 'white' , 'white' , 'green' , 'green' , None    , None    ],
            [None    , 'blue'  , 'blue'  , 'blue'  , 'white' , 'white' , 'white' , 'white' , 'white' , 'green' , 'green' , 'green' , None    ],
            [None    , 'blue'  , 'blue'  , 'blue'  , 'white' , 'white' , 'white' , 'white' , 'white' , 'green' , 'green' , 'green' , None    ],
            [None    , 'blue'  , 'blue'  , 'blue'  , 'white' , 'white' , 'white' , 'white' , 'white' , 'green' , 'green' , 'green' , None    ],
            [None    , 'silver', None    , None    , 'silver', None    , 'silver', None    , 'silver', None    , None    , 'silver', None    ],
            [None    , None    , None    , None    , None    , None    , 'silver', None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , 'silver', None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , 'silver', None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'gold'  , None    , 'gold'  , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'gold'  , 'gold'  , 'gold'  , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    ]
        ]
    ],

    # Round 18
    [   (0, 128, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['orange', None    , 'gold'  , 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'gold'  , None    , 'orange'],
            ['orange', None    , 'gold'  , 'gold'  , 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'gold'  , 'gold'  , None    , 'orange'],
            ['orange', None    , 'gold'  , None    , 'gold'  , 'yellow', 'yellow', 'yellow', 'gold'  , None    , 'gold'  , None    , 'orange'],
            ['orange', None    , 'gold'  , None    , 'pink'  , 'gold'  , 'yellow', 'gold'  , 'cyan'  , None    , 'gold'  , None    , 'orange'],
            ['orange', None    , 'gold'  , None    , 'pink'  , None    , 'silver', None    , 'cyan'  , None    , 'gold'  , None    , 'orange'],
            ['orange', None    , 'gold'  , None    , 'pink'  , None    , 'green' , None    , 'cyan'  , None    , 'gold'  , None    , 'orange'],
            ['orange', None    , 'gold'  , None    , 'pink'  , None    , 'green' , None    , 'cyan'  , None    , 'gold'  , None    , 'orange'],
            ['orange', None    , 'gold'  , None    , 'pink'  , None    , 'green' , None    , 'cyan'  , None    , 'gold'  , None    , 'orange'],
            ['orange', None    , 'gold'  , None    , 'pink'  , None    , 'green' , None    , 'cyan'  , None    , 'gold'  , None    , 'orange'],
            ['orange', 'gold'  , 'gold'  , 'gold'  , 'pink'  , None    , 'green' , None    , 'cyan'  , 'gold'  , 'gold'  , 'gold'  , 'orange']
        ]
    ],

    # Round 19
    [   (0, 0, 96),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , None    , None    ],
            [None    , None    , 'green' , 'red'   , 'blue'  , 'pink'  , 'gold'  , 'pink'  , 'blue'  , 'red'   , 'green' , None    , None    ],
            [None    , None    , 'green' , 'red'   , 'blue'  , 'pink'  , 'gold'  , 'pink'  , 'blue'  , 'red'   , 'green' , None    , None    ],
            [None    , None    , 'green' , 'red'   , 'blue'  , 'pink'  , 'gold'  , 'pink'  , 'blue'  , 'red'   , 'green' , None    , None    ],
            [None    , None    , 'green' , 'red'   , 'blue'  , 'pink'  , 'yellow', 'pink'  , 'blue'  , 'red'   , 'green' , None    , None    ],
            [None    , None    , 'green' , 'red'   , 'blue'  , 'pink'  , 'gold'  , 'pink'  , 'blue'  , 'red'   , 'green' , None    , None    ],
            [None    , None    , 'green' , 'red'   , 'blue'  , 'pink'  , 'gold'  , 'pink'  , 'blue'  , 'red'   , 'green' , None    , None    ],
            [None    , None    , 'green' , 'red'   , 'blue'  , 'pink'  , 'gold'  , 'pink'  , 'blue'  , 'red'   , 'green' , None    , None    ],
            [None    , None    , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , None    , None    ]
        ]
    ],

    # Round 20
    [   (128, 0, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['gold'  , 'white' , 'gold'  , 'orange', 'gold'  , 'cyan'  , 'gold'  , 'green' , 'gold'  , 'red'   , 'gold'  , 'blue'  , 'gold'  ],
            ['gold'  , 'pink'  , 'gold'  , 'silver', 'gold'  , 'silver', 'gold'  , 'silver', 'gold'  , 'silver', 'gold'  , 'yellow', 'gold'  ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['gold'  , 'pink'  , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  ],
            ['gold'  , None    , 'gold'  , 'pink'  , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  ],
            ['gold'  , None    , 'gold'  , None    , 'gold'  , 'pink'  , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  ],
            ['gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , 'pink'  , 'gold'  , None    , 'gold'  , None    , 'gold'  ],
            ['gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , 'pink'  , 'gold'  , None    , 'gold'  ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'pink'  , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , 'pink'  , 'gold'  , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , 'pink'  , 'gold'  , None    , 'gold'  , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , 'pink'  , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    ],
            [None    , None    , None    , 'pink'  , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    , None    , None    ],
            [None    , 'pink'  , None    , None    , None    , None    , 'gold'  , None    , None    , None    , None    , None    , None    ]
        ]
    ],

    # Round 21
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'gold'  , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , 'gold'  , None    , 'red'   , 'red'   , 'red'   , None    , 'gold'  , None    , 'white' , None    ],
            [None    , 'gold'  , None    , 'gold'  , None    , 'green' , 'green' , 'green' , None    , 'gold'  , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , 'gold'  , None    , 'blue'  , 'blue'  , 'blue'  , None    , 'gold'  , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , 'gold'  , None    , 'white' , 'white' , 'white' , None    , 'gold'  , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , 'gold'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'gold'  , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  , None    ],
            [None    , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , None    ]
        ]
    ],

    # Round 22
    [   (0, 128, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'],
            ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['red'   , 'red'   , 'gold'  , None    , 'gold'  , 'red'   , 'red'   , 'red'   , 'gold'  , None    , 'gold'  , 'red'   , 'red'   ],
            ['red'   , 'red'   , 'gold'  , None    , 'gold'  , 'red'   , 'red'   , 'red'   , 'gold'  , None    , 'gold'  , 'red'   , 'red'   ],
            ['red'   , 'red'   , 'gold'  , None    , 'gold'  , 'red'   , 'red'   , 'red'   , 'gold'  , None    , 'gold'  , 'red'   , 'red'   ],
            ['red'   , 'red'   , 'gold'  , None    , 'gold'  , 'red'   , 'red'   , 'red'   , 'gold'  , None    , 'gold'  , 'red'   , 'red'   ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' ],
            ['white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' , 'white' ]
        ]
    ],

    # Round 23
    [   (0, 0, 96),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver'],
            [None    , None    , 'silver', 'green' , 'silver', None    , 'silver', 'green' , 'silver', None    , 'silver', 'green' , 'silver'],
            [None    , None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver'],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    ],
            [None    , 'silver', 'red'   , 'silver', None    , 'silver', 'red'   , 'silver', None    , 'silver', 'red'   , 'silver', None    ],
            [None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    , None    ],
            ['silver', 'blue'  , 'silver', None    , 'silver', 'blue'  , 'silver', None    , 'silver', 'blue'  , 'silver', None    , None    ],
            ['silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    , 'silver', 'silver', 'silver', None    , None    ]
        ]
    ],

    # Round 24
    [   (128, 0, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , 'white' , 'white' , 'white' , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , 'white' , 'white' , 'white' , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , 'white' , 'white' , 'white' , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'white' , 'white' , 'white' , 'white' , 'white' , None    , None    , None    , None    ],
            [None    , None    , None    , None    , 'white' , 'blue'  , 'white' , 'blue'  , 'white' , None    , None    , None    , None    ],
            [None    , None    , None    , 'white' , 'blue'  , 'blue'  , 'white' , 'blue'  , 'blue'  , 'white' , None    , None    , None    ],
            [None    , None    , None    , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , None    , None    , None    ],
            [None    , None    , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , None    , None    ],
            [None    , None    , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , None    , None    ],
            [None    , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , None    ],
            ['blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  ]
        ]
    ],

    # Round 25
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   ],
            ['green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' , 'green' ],
            ['blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  ],
            ['gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'silver', 'silver', 'silver', 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  ],
            ['gold'  , 'red'   , 'red'   , 'red'   , 'gold'  , None    , None    , None    , 'gold'  , 'blue'  , 'blue'  , 'blue'  , 'gold'  ],
            ['gold'  , 'red'   , 'red'   , 'red'   , 'gold'  , None    , None    , None    , 'gold'  , 'blue'  , 'blue'  , 'blue'  , 'gold'  ],
            ['gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  ],
            ['gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  ],
            ['gold'  , None    , None    , None    , 'gold'  , 'green' , 'green' , 'green' , 'gold'  , None    , None    , None    , 'gold'  ],
            ['gold'  , None    , None    , None    , 'gold'  , 'green' , 'green' , 'green' , 'gold'  , None    , None    , None    , 'gold'  ],
            ['gold'  , 'silver', 'silver', 'silver', 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'silver', 'silver', 'silver', 'gold'  ]
        ]
    ],

    # Round 26
    [   (0, 128, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , 'gold'  , 'silver', 'silver', 'silver', 'gold'  , None    , None    , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , None    , None    , None    , None    , None    ],
            ['gold'  , None    , None    , 'cyan'  , 'cyan'  , 'cyan'  , None    , None    , 'gold'  , None    , None    , None    , None    ],
            ['gold'  , None    , 'green' , 'green' , 'green' , 'green' , 'green' , None    , 'gold'  , None    , None    , None    , None    ],
            ['gold'  , None    , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , None    , 'gold'  , None    , None    , None    , None    ],
            ['gold'  , None    , None    , 'pink'  , 'pink'  , 'pink'  , None    , None    , 'gold'  , None    , None    , None    , None    ],
            [None    , 'gold'  , None    , None    , None    , None    , None    , 'gold'  , None    , None    , None    , None    , None    ],
            [None    , None    , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , None    , None    , None    , None    , None    , None    ]
        ]
    ],

    # Round 27
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'],
            ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'],
            ['silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver'],
            ['red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   ],
            ['silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver']
        ]
    ],

    # Round 28
    [   (128, 0, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  ],
            ['blue'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'pink'  , 'gold'  , 'pink'  , 'gold'  , 'gold'  , 'gold'  , 'gold'  , 'blue'  ],
            ['blue'  , 'gold'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  , 'blue'  ],
            ['blue'  , 'gold'  , 'pink'  , None    , None    , None    , None    , None    , None    , None    , 'pink'  , 'gold'  , 'blue'  ],
            ['blue'  , 'gold'  , 'pink'  , 'pink'  , None    , None    , None    , None    , None    , 'pink'  , 'pink'  , 'gold'  , 'blue'  ],
            ['blue'  , 'gold'  , 'pink'  , 'pink'  , 'pink'  , None    , None    , None    , 'pink'  , 'pink'  , 'pink'  , 'gold'  , 'blue'  ],
            [None    , 'blue'  , 'gold'  , 'pink'  , 'pink'  , 'pink'  , None    , 'pink'  , 'pink'  , 'pink'  , 'gold'  , 'blue'  , None    ],
            [None    , None    , 'blue'  , 'gold'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'gold'  , 'blue'  , None    , None    ],
            [None    , None    , None    , 'blue'  , 'gold'  , 'pink'  , 'pink'  , 'pink'  , 'gold'  , 'blue'  , None    , None    , None    ],
            [None    , None    , None    , None    , 'blue'  , 'gold'  , 'pink'  , 'gold'  , 'blue'  , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , 'blue'  , 'pink'  , 'blue'  , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , 'blue'  , None    , None    , None    , None    , None    , None    ]
        ]
    ],

    # Round 29
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'gold'  , None    , 'gold'  , 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'],
            ['pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'gold'  , None    , 'gold'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  ],
            ['gold'  , 'gold'  , 'white' , 'gold'  , 'gold'  , 'gold'  , None    , 'gold'  , 'gold'  , 'gold'  , 'white' , 'gold'  , 'gold'  ],
            ['blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'gold'  , None    , 'gold'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  ],
            ['red'   , 'red'   , 'red'   , 'red'   , 'red'   , 'gold'  , None    , 'gold'  , 'red'   , 'red'   , 'red'   , 'red'   , 'red'   ],
            ['green' , 'green' , 'green' , 'green' , 'green' , 'gold'  , None    , 'gold'  , 'green' , 'green' , 'green' , 'green' , 'green' ],
            ['silver', 'silver', 'white' , 'silver', 'silver', 'gold'  , None    , 'gold'  , 'silver', 'silver', 'white' , 'silver', 'silver'],
            ['cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'gold'  , None    , 'gold'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  , 'cyan'  ],
            ['orange', 'orange', 'orange', 'orange', 'orange', 'gold'  , None    , 'gold'  , 'orange', 'orange', 'orange', 'orange', 'orange'],
            ['white' , 'white' , 'white' , 'white' , 'white' , 'gold'  , None    , 'gold'  , 'white' , 'white' , 'white' , 'white' , 'white' ]
        ]
    ],

    # Round 30
    [   (0, 0, 128),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['yellow', 'pink'  , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['yellow', 'pink'  , 'blue'  , 'red'   , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['yellow', 'pink'  , 'blue'  , 'red'   , 'green' , 'cyan'  , None    , None    , None    , None    , None    , None    , None    ],
            ['yellow', 'pink'  , 'blue'  , 'red'   , 'green' , 'cyan'  , 'orange', 'white' , None    , None    , None    , None    , None    ],
            ['yellow', 'pink'  , 'blue'  , 'red'   , 'green' , 'cyan'  , 'orange', 'white' , 'yellow', 'pink'  , None    , None    , None    ],
            ['silver', 'pink'  , 'blue'  , 'red'   , 'green' , 'cyan'  , 'orange', 'white' , 'yellow', 'pink'  , 'blue'  , 'red'   , None    ],
            [None    , 'gold'  , 'silver', 'red'   , 'green' , 'cyan'  , 'orange', 'white' , 'yellow', 'pink'  , 'blue'  , 'red'   , 'green' ],
            [None    , None    , None    , 'gold'  , 'silver', 'cyan'  , 'orange', 'white' , 'yellow', 'pink'  , 'blue'  , 'red'   , 'green' ],
            [None    , None    , None    , None    , None    , 'gold'  , 'silver', 'white' , 'yellow', 'pink'  , 'blue'  , 'red'   , 'green' ],
            [None    , None    , None    , None    , None    , None    , None    , 'gold'  , 'silver', 'pink'  , 'blue'  , 'red'   , 'green' ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  , 'silver', 'red'   , 'green' ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , 'gold'  , 'silver']
        ]
    ],

    # Round 31
    [   (0, 0, 96),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            ['green' , None    , 'red'   , None    , 'blue'  , None    , 'pink'  , None    , 'yellow', None    , 'white' , None    , 'orange'],
            ['silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver'],
            [None    , 'blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'orange', None    , 'white' , None    ],
            [None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    ],
            ['cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  , None    , 'pink'  , None    , 'yellow', None    , 'white' ],
            ['silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver'],
            [None    , 'pink'  , None    , 'blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    , 'orange', None    ],
            [None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    ],
            ['orange', None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  , None    , 'pink'  , None    , 'yellow'],
            ['silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver'],
            [None    , 'yellow', None    , 'pink'  , None    , 'blue'  , None    , 'red'   , None    , 'green' , None    , 'cyan'  , None    ],
            [None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    ],
            ['orange', None    , 'cyan'  , None    , 'green' , None    , 'red'   , None    , 'blue'  , None    , 'pink'  , None    , 'yellow'],
            ['silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver', None    , 'silver']
        ]
    ],

    # Round 32
    [   (128, 0, 0),
        [
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , 'green' , 'green' , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , 'red'   , 'red'   , 'red'   , 'red'   , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , 'blue'  , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    ],
            [None    , None    , 'gold'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , 'pink'  , None    , None    ],
            [None    , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , 'gold'  , None    , None    ],
            [None    , None    , 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', None    , None    ],
            [None    , None    , 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', 'silver', None    , None    ]
        ]
    ]
]