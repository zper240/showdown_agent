# Module-level code
    def CustomAgent():
        def __init__(self):
            # COPY_FREE_VARS 
            # RESUME 
            False
            # LOAD_FAST self
            # STORE_ATTR opp_switch_team
            # BUILD_LIST 
            # LOAD_FAST self
            # STORE_ATTR switch_guesses
            # BUILD_LIST 
            # LOAD_FAST self
            # STORE_ATTR turns
            0
            # LOAD_FAST self
            # STORE_ATTR last_turn
            False
            # LOAD_FAST self
            # STORE_ATTR print
            True
            # LOAD_FAST self
            # STORE_ATTR record_guess
            None
            # LOAD_FAST self
            # STORE_ATTR last_move
            # LOAD_GLOBAL NULL + Pokemon
            9
            'Landorus-Therian'
            # KW_NAMES ('species',)
            # CALL 
            # LOAD_GLOBAL NULL + Pokemon
            9
            'Glimmora'
            # KW_NAMES ('species',)
            # CALL 
            # LOAD_GLOBAL NULL + Pokemon
            9
            'Great Tusk'
            # KW_NAMES ('species',)
            # CALL 
            # LOAD_GLOBAL NULL + Pokemon
            9
            'Deoxys-Speed'
            # KW_NAMES ('species',)
            # CALL 
            # LOAD_GLOBAL NULL + Pokemon
            9
            'Eternatus'
            # KW_NAMES ('species',)
            # CALL 
            # BUILD_LIST 
            # LOAD_FAST self
            # STORE_ATTR lead_mons
            True
            # LOAD_FAST self
            # STORE_ATTR specific_strats
            True
            # LOAD_FAST self
            # STORE_ATTR consider_stats
            False
            # LOAD_FAST self
            # STORE_ATTR full_random
            # LOAD_GLOBAL NULL + super
            # LOAD_DEREF __class__
            # LOAD_FAST self
            # LOAD_SUPER_ATTR __init__
            # LOAD_FAST args
            'team'
            # LOAD_GLOBAL team
            # BUILD_MAP 
            # LOAD_FAST kwargs
            # DICT_MERGE 
            # CALL_FUNCTION_EX 
            # POP_TOP 
            # LOAD_GLOBAL os
            # LOAD_ATTR path
            # LOAD_ATTR NULL|self + dirname
            # LOAD_GLOBAL os
            # LOAD_ATTR path
            # LOAD_ATTR NULL|self + abspath
            # LOAD_GLOBAL __file__
            # CALL 
            # CALL 
            # STORE_FAST base_dir
            0
            # STORE_FAST i
            # LOAD_GLOBAL os
            # LOAD_ATTR path
            # LOAD_ATTR NULL|self + exists
            # LOAD_GLOBAL os
            # LOAD_ATTR path
            # LOAD_ATTR NULL|self + join
            # LOAD_FAST base_dir
            'battles_'
            # LOAD_FAST i
            # FORMAT_VALUE 
            '.txt'
            # BUILD_STRING 
            # CALL 
            # CALL 
            # jump placeholder
            # LOAD_FAST i
            1
            # BINARY_OP +=
            # STORE_FAST i
            # LOAD_GLOBAL os
            # LOAD_ATTR path
            # LOAD_ATTR NULL|self + exists
            # LOAD_GLOBAL os
            # LOAD_ATTR path
            # LOAD_ATTR NULL|self + join
            # LOAD_FAST base_dir
            'battles_'
            # LOAD_FAST i
            # FORMAT_VALUE 
            '.txt'
            # BUILD_STRING 
            # CALL 
            # CALL 
            # jump placeholder
            # jump placeholder
            # LOAD_GLOBAL os
            # LOAD_ATTR path
            # LOAD_ATTR NULL|self + join
            # LOAD_FAST base_dir
            'battles_'
            # LOAD_FAST i
            # FORMAT_VALUE 
            '.txt'
            # BUILD_STRING 
            # CALL 
            # LOAD_FAST self
            # STORE_ATTR logfile
            # RETURN_CONST None
        def teampreview(self, battle):
            # RESUME 
            # RETURN_CONST '/team 123456'
        def _battle_finished_callback(self, battle):
            # RESUME 
            0
            # STORE_FAST mons_left
            0
            # STORE_FAST comb_hp
            # LOAD_FAST battle
            # STORE_FAST battle_obj
            # LOAD_FAST battle_obj
            # LOAD_ATTR team
            # LOAD_ATTR NULL|self + values
            # CALL 
            # GET_ITER 
            # FOR_ITER to 140
            # STORE_FAST mon
            # LOAD_FAST mon
            # LOAD_ATTR fainted
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mons_left
            1
            # BINARY_OP +=
            # STORE_FAST mons_left
            # LOAD_FAST comb_hp
            # LOAD_FAST mon
            # LOAD_ATTR current_hp_fraction
            # BINARY_OP +=
            # STORE_FAST comb_hp
            # jump placeholder
            # END_FOR 
            0
            # STORE_FAST opps_left
            0
            # STORE_FAST opps_hp
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_opp_team_total
            # CALL 
            # GET_ITER 
            # FOR_ITER to 256
            # STORE_FAST mon
            # LOAD_FAST mon
            # LOAD_ATTR fainted
            # jump placeholder
            # jump placeholder
            # LOAD_FAST opps_left
            1
            # BINARY_OP +=
            # STORE_FAST opps_left
            # LOAD_FAST opps_hp
            # LOAD_FAST mon
            # LOAD_ATTR current_hp_fraction
            # BINARY_OP +=
            # STORE_FAST opps_hp
            # jump placeholder
            # END_FOR 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + log_info
            ',{Battle_End: '
            # LOAD_GLOBAL NULL + str
            # LOAD_FAST battle_obj
            # LOAD_ATTR turn
            # CALL 
            # BINARY_OP +
            ', won = '
            # BINARY_OP +
            # LOAD_GLOBAL NULL + str
            # LOAD_FAST battle_obj
            # LOAD_ATTR won
            # CALL 
            # BINARY_OP +
            ', mons_left = '
            # BINARY_OP +
            # LOAD_GLOBAL NULL + str
            # LOAD_FAST mons_left
            # CALL 
            # BINARY_OP +
            ', comb_hp = '
            # BINARY_OP +
            # LOAD_GLOBAL NULL + str
            # LOAD_FAST comb_hp
            # CALL 
            # BINARY_OP +
            ', opps_left = '
            # BINARY_OP +
            # LOAD_GLOBAL NULL + str
            # LOAD_FAST opps_left
            # CALL 
            # BINARY_OP +
            ', opps_hp = '
            # BINARY_OP +
            # LOAD_GLOBAL NULL + str
            # LOAD_FAST opps_hp
            # CALL 
            # BINARY_OP +
            '}]'
            # BINARY_OP +
            # CALL 
            # POP_TOP 
            # RETURN_CONST None
        def log_info(self, msg):
            # RESUME 
            # LOAD_GLOBAL NULL + open
            # LOAD_FAST self
            # LOAD_ATTR logfile
            'a'
            # CALL 
            # BEFORE_WITH 
            # STORE_FAST f
            # LOAD_FAST f
            # LOAD_ATTR NULL|self + write
            # LOAD_FAST msg
            # CALL 
            # POP_TOP 
            None
            None
            None
            # CALL 
            # POP_TOP 
            # RETURN_CONST None
            # PUSH_EXC_INFO 
            # WITH_EXCEPT_START 
            # jump placeholder
            # RERAISE 
            # POP_TOP 
            # POP_EXCEPT 
            # POP_TOP 
            # POP_TOP 
            # RETURN_CONST None
            # COPY 
            # POP_EXCEPT 
            # RERAISE 
        def choose_move(self, battle):
            # RESUME 
            # LOAD_FAST battle
            # STORE_FAST battle_obj
            None
            # STORE_FAST action
            # LOAD_FAST battle
            # LOAD_ATTR turn
            1
            # COMPARE_OP ==
            # jump placeholder
            False
            # LOAD_FAST self
            # STORE_ATTR opp_switch_team
            # BUILD_LIST 
            # LOAD_FAST self
            # STORE_ATTR switch_guesses
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + TurnState
            # LOAD_FAST battle_obj
            # CALL 
            # BUILD_LIST 
            # LOAD_FAST self
            # STORE_ATTR turns
            # LOAD_FAST battle_obj
            # LOAD_ATTR opponent_username
            'simple-uber'
            # COMPARE_OP ==
            # jump placeholder
            # NOP 
            False
            # LOAD_FAST self
            # STORE_ATTR print
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + log_info
            # LOAD_FAST battle_obj
            # LOAD_ATTR opponent_username
            '[{Battle_Start: '
            # BINARY_OP +
            # LOAD_GLOBAL NULL + str
            # LOAD_FAST battle_obj
            # LOAD_ATTR turn
            # CALL 
            # BINARY_OP +
            ', mon = '
            # BINARY_OP +
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            # BINARY_OP +
            ', opp = '
            # BINARY_OP +
            # LOAD_FAST battle_obj
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR species
            # BINARY_OP +
            '}'
            # BINARY_OP +
            # CALL 
            # POP_TOP 
            # EXTENDED_ARG 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR last_turn
            # LOAD_FAST battle_obj
            # LOAD_ATTR turn
            # COMPARE_OP !=
            # EXTENDED_ARG 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR turns
            # LOAD_ATTR NULL|self + append
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + TurnState
            # LOAD_FAST battle_obj
            # CALL 
            # CALL 
            # POP_TOP 
            # LOAD_FAST self
            # LOAD_ATTR opp_switch_team
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR turns
            -1
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + opp_switched
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # LOAD_FAST self
            # LOAD_ATTR last_move
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_GLOBAL NULL + Move
            'dragontail'
            9
            # CALL 
            # CALL 
            # COMPARE_OP !=
            # CALL 
            # LOAD_FAST self
            # STORE_ATTR opp_switch_team
            # jump placeholder
            True
            # LOAD_FAST self
            # STORE_ATTR record_guess
            # LOAD_FAST self
            # LOAD_ATTR switch_guesses
            -1
            # BINARY_SUBSCR 
            0
            # BINARY_SUBSCR 
            # LOAD_FAST self
            # LOAD_ATTR turns
            -1
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + opp_switched
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # LOAD_FAST self
            # LOAD_ATTR last_move
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_GLOBAL NULL + Move
            'dragontail'
            9
            # CALL 
            # CALL 
            # COMPARE_OP !=
            # CALL 
            # BUILD_TUPLE 
            # LOAD_FAST self
            # LOAD_ATTR switch_guesses
            -1
            # STORE_SUBSCR 
            # LOAD_FAST self
            # LOAD_ATTR turns
            -1
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + mon_fainted
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # CALL 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST self
            # LOAD_ATTR turns
            -1
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + get_dam
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # CALL 
            # STORE_FAST dam_done
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST self
            # LOAD_ATTR turns
            -1
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + mon_fainted
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # CALL 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + log_info
            ',{Mon_Faint: '
            # LOAD_GLOBAL NULL + str
            # LOAD_FAST battle_obj
            # LOAD_ATTR turn
            # CALL 
            # BINARY_OP +
            ', mon = '
            # BINARY_OP +
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + get_mon
            # CALL 
            # LOAD_ATTR species
            # BINARY_OP +
            ', opp = '
            # BINARY_OP +
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + get_opp
            # CALL 
            # LOAD_ATTR species
            # BINARY_OP +
            '}'
            # BINARY_OP +
            # CALL 
            # POP_TOP 
            # LOAD_FAST self
            # LOAD_ATTR turns
            -1
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + opp_fainted
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # CALL 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + log_info
            ',{Opp_Faint: '
            # LOAD_GLOBAL NULL + str
            # LOAD_FAST battle_obj
            # LOAD_ATTR turn
            # CALL 
            # BINARY_OP +
            ', opp = '
            # BINARY_OP +
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + get_opp
            # CALL 
            # LOAD_ATTR species
            # BINARY_OP +
            ', mon = '
            # BINARY_OP +
            # LOAD_FAST self
            # LOAD_ATTR turns
            -2
            # BINARY_SUBSCR 
            # LOAD_ATTR NULL|self + get_mon
            # CALL 
            # LOAD_ATTR species
            # BINARY_OP +
            '}'
            # BINARY_OP +
            # CALL 
            # POP_TOP 
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            None
            # COMPARE_OP !=
            # EXTENDED_ARG 
            # jump placeholder
            # LOAD_FAST battle_obj
            # LOAD_ATTR opponent_active_pokemon
            None
            # COMPARE_OP !=
            # EXTENDED_ARG 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR full_random
            # EXTENDED_ARG 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR consider_stats
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST self
            # LOAD_ATTR specific_strats
            # UNARY_NOT 
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST self
            # LOAD_ATTR consider_stats
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST self
            # LOAD_ATTR specific_strats
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            ('kyogre', 'arceusfairy', 'calyrexice', 'landorustherian', 'necrozmaduskmane')
            # CONTAINS_OP 
            # STORE_FAST consider_stats
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_move
            # LOAD_FAST battle_obj
            False
            # LOAD_FAST consider_stats
            # KW_NAMES ('consider_stats',)
            # CALL 
            # STORE_FAST dam_move
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_ideal_switch
            # LOAD_FAST battle_obj
            # CALL 
            # STORE_FAST switch
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_switch
            # LOAD_FAST battle_obj
            # LOAD_FAST switch
            # CALL 
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST battle_obj
            # LOAD_ATTR fields
            # LOAD_ATTR NULL|self + get
            # LOAD_GLOBAL Field
            # LOAD_ATTR TRICK_ROOM
            0
            # CALL 
            1
            # COMPARE_OP >
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            'calyrexice'
            # COMPARE_OP ==
            # UNARY_NOT 
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            'kyogre'
            # COMPARE_OP ==
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_GLOBAL NULL + sum
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR boosts
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            3
            # COMPARE_OP >
            # UNARY_NOT 
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle_obj
            # CALL 
            # UNARY_NOT 
            # STORE_FAST switch_idea
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST switch_idea
            # jump placeholder
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            'landorustherian'
            # COMPARE_OP ==
            # EXTENDED_ARG 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR fainted
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR specific_strats
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            'landorustherian'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + landorus_method
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST action
            # jump placeholder
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            'necrozmaduskmane'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + necrozma_method
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST action
            # jump placeholder
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            'calyrexice'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + calyrex_method
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST action
            # jump placeholder
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            'arceusfairy'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + arceus_method
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST action
            # jump placeholder
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            'kyogre'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + kyogre_method
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST action
            # jump placeholder
            # NOP 
            # LOAD_FAST action
            None
            # COMPARE_OP !=
            # STORE_FAST move_chosen
            # LOAD_FAST move_chosen
            # jump placeholder
            # LOAD_FAST dam_move
            None
            # COMPARE_OP !=
            # jump placeholder
            # LOAD_FAST switch_idea
            # jump placeholder
            # LOAD_FAST battle_obj
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR fainted
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST dam_move
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle_obj
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # STORE_FAST action
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST switch
            # CALL 
            # STORE_FAST action
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + choose_random_move
            # LOAD_FAST battle_obj
            # CALL 
            # STORE_FAST action
            # LOAD_FAST action
            # LOAD_FAST self
            # STORE_ATTR last_move
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # LOAD_GLOBAL NULL + print
            # LOAD_FAST action
            # CALL 
            # POP_TOP 
            # LOAD_GLOBAL NULL + print
            # CALL 
            # POP_TOP 
            # NOP 
            # LOAD_FAST action
            # RETURN_VALUE 
        def kyogre_method(self, battle):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_resistant
            # LOAD_FAST battle
            # CALL 
            # jump placeholder
            'calmmind'
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # LOAD_FAST_AND_CLEAR mov
            # SWAP 
            # BUILD_LIST 
            # SWAP 
            # FOR_ITER to 102
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            # LIST_APPEND 
            # jump placeholder
            # END_FOR 
            # SWAP 
            # STORE_FAST mov
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.65
            # COMPARE_OP >
            # jump placeholder
            # LOAD_GLOBAL NULL + sum
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR boosts
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            11
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_die_before_move
            # LOAD_FAST battle
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # FOR_ITER to 448
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            'calmmind'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST mov
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # SWAP 
            # POP_TOP 
            # RETURN_VALUE 
            # END_FOR 
            # RETURN_CONST None
            # SWAP 
            # POP_TOP 
            # SWAP 
            # STORE_FAST mov
            # RERAISE 
        def arceus_method(self, battle):
            # RESUME 
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR species
            'koraidon'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR is_terastallized
            # jump placeholder
            # RETURN_CONST None
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # FOR_ITER to 232
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            'judgment'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST mov
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # SWAP 
            # POP_TOP 
            # RETURN_VALUE 
            # END_FOR 
            # LOAD_GLOBAL NULL + sum
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR boosts
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            3
            # COMPARE_OP >
            # jump placeholder
            'dragontail'
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # LOAD_FAST_AND_CLEAR mov
            # SWAP 
            # BUILD_LIST 
            # SWAP 
            # FOR_ITER to 396
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            # LIST_APPEND 
            # jump placeholder
            # END_FOR 
            # SWAP 
            # STORE_FAST mov
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # FOR_ITER to 540
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            'dragontail'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST mov
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # SWAP 
            # POP_TOP 
            # RETURN_VALUE 
            # END_FOR 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            2
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.5
            # COMPARE_OP <
            # jump placeholder
            'recover'
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # LOAD_FAST_AND_CLEAR mov
            # SWAP 
            # BUILD_LIST 
            # SWAP 
            # FOR_ITER to 740
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            # LIST_APPEND 
            # jump placeholder
            # END_FOR 
            # SWAP 
            # STORE_FAST mov
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # FOR_ITER to 884
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            'recover'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST mov
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # SWAP 
            # POP_TOP 
            # RETURN_VALUE 
            # END_FOR 
            # RETURN_CONST None
            # SWAP 
            # POP_TOP 
            # SWAP 
            # STORE_FAST mov
            # RERAISE 
            # SWAP 
            # POP_TOP 
            # SWAP 
            # STORE_FAST mov
            # RERAISE 
        def calyrex_method(self, battle):
            # RESUME 
            # LOAD_FAST battle
            # LOAD_ATTR fields
            # LOAD_ATTR NULL|self + get
            # LOAD_GLOBAL Field
            # LOAD_ATTR TRICK_ROOM
            0
            # CALL 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # FOR_ITER to 220
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            'trickroom'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST mov
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # SWAP 
            # POP_TOP 
            # RETURN_VALUE 
            # END_FOR 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_resistant
            # LOAD_FAST battle
            # CALL 
            # jump placeholder
            'swordsdance'
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # LOAD_FAST_AND_CLEAR mov
            # SWAP 
            # BUILD_LIST 
            # SWAP 
            # FOR_ITER to 322
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            # LIST_APPEND 
            # jump placeholder
            # END_FOR 
            # SWAP 
            # STORE_FAST mov
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.7
            # COMPARE_OP >
            # jump placeholder
            # LOAD_GLOBAL NULL + sum
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR boosts
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            5
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_die_before_move
            # LOAD_FAST battle
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # FOR_ITER to 668
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            'swordsdance'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST mov
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # SWAP 
            # POP_TOP 
            # RETURN_VALUE 
            # END_FOR 
            # RETURN_CONST None
            # SWAP 
            # POP_TOP 
            # SWAP 
            # STORE_FAST mov
            # RERAISE 
        def necrozma_method(self, battle):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_resistant
            # LOAD_FAST battle
            # CALL 
            # jump placeholder
            'dragondance'
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # LOAD_FAST_AND_CLEAR mov
            # SWAP 
            # BUILD_LIST 
            # SWAP 
            # FOR_ITER to 102
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            # LIST_APPEND 
            # jump placeholder
            # END_FOR 
            # SWAP 
            # STORE_FAST mov
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.55
            # COMPARE_OP >
            # jump placeholder
            # LOAD_GLOBAL NULL + sum
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR boosts
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            11
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_die_before_move
            # LOAD_FAST battle
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # FOR_ITER to 448
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            'dragondance'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST mov
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # SWAP 
            # POP_TOP 
            # RETURN_VALUE 
            # END_FOR 
            0.5
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_most_damage
            # LOAD_FAST battle
            True
            # CALL 
            # LOAD_GLOBAL NULL + float
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR max_hp
            # CALL 
            # BINARY_OP /
            # COMPARE_OP >
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_faster
            # LOAD_FAST battle
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            # STORE_FAST heal_more_than_dam
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            2
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.55
            # COMPARE_OP <=
            # jump placeholder
            'morningsun'
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # LOAD_FAST_AND_CLEAR mov
            # SWAP 
            # BUILD_LIST 
            # SWAP 
            # FOR_ITER to 836
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            # LIST_APPEND 
            # jump placeholder
            # END_FOR 
            # SWAP 
            # STORE_FAST mov
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_die_before_move
            # LOAD_FAST battle
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # jump placeholder
            # LOAD_FAST heal_more_than_dam
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # FOR_ITER to 1040
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            'morningsun'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST mov
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # SWAP 
            # POP_TOP 
            # RETURN_VALUE 
            # END_FOR 
            # RETURN_CONST None
            # SWAP 
            # POP_TOP 
            # SWAP 
            # STORE_FAST mov
            # RERAISE 
            # SWAP 
            # POP_TOP 
            # SWAP 
            # STORE_FAST mov
            # RERAISE 
        def landorus_method(self, battle):
            # RESUME 
            False
            # STORE_FAST lead_mon
            # LOAD_FAST self
            # LOAD_ATTR lead_mons
            # GET_ITER 
            # FOR_ITER to 116
            # STORE_FAST mon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR species
            # LOAD_FAST mon
            # LOAD_ATTR species
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            True
            # STORE_FAST lead_mon
            # POP_TOP 
            # jump placeholder
            # END_FOR 
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST battle
            # LOAD_ATTR turn
            1
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST lead_mon
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR species
            'deoxysspeed'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR species
            'eternatus'
            # COMPARE_OP ==
            # jump placeholder
            # RETURN_CONST None
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR moves
            'taunt'
            # BINARY_SUBSCR 
            # STORE_FAST move
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST move
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # RETURN_VALUE 
            # LOAD_FAST battle
            # LOAD_ATTR opponent_side_conditions
            # LOAD_ATTR NULL|self + get
            # LOAD_GLOBAL SideCondition
            # LOAD_ATTR STEALTH_ROCK
            # CALL 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            2
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # GET_ITER 
            # FOR_ITER to 748
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            'stealthrock'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + create_order
            # LOAD_FAST mov
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + should_tera
            # LOAD_FAST battle
            # CALL 
            # KW_NAMES ('terastallize',)
            # CALL 
            # SWAP 
            # POP_TOP 
            # RETURN_VALUE 
            # END_FOR 
            # RETURN_CONST None
        def should_tera(self, battle):
            # RESUME 
            # LOAD_FAST battle
            # LOAD_ATTR used_tera
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR tera_type
            None
            # COMPARE_OP ==
            # jump placeholder
            # RETURN_CONST False
            0
            # STORE_FAST alive
            # LOAD_FAST battle
            # LOAD_ATTR team
            # LOAD_ATTR NULL|self + values
            # CALL 
            # GET_ITER 
            # FOR_ITER to 178
            # STORE_FAST mon
            # LOAD_FAST mon
            # LOAD_ATTR fainted
            # jump placeholder
            # jump placeholder
            # LOAD_FAST alive
            1
            # BINARY_OP +=
            # STORE_FAST alive
            # jump placeholder
            # END_FOR 
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.5
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST alive
            1
            # COMPARE_OP <=
            # jump placeholder
            # RETURN_CONST False
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            1
            # COMPARE_OP >
            # jump placeholder
            # RETURN_CONST True
            # RETURN_CONST False
        def get_most_damage(self, battle, for_opp, switch_mon):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_move
            # LOAD_FAST battle
            # LOAD_FAST for_opp
            # LOAD_FAST switch_mon
            # CALL 
            # STORE_FAST move
            # LOAD_FAST move
            None
            # COMPARE_OP ==
            # jump placeholder
            # RETURN_CONST -1.0
            # LOAD_FAST for_opp
            # jump placeholder
            # LOAD_FAST switch_mon
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # jump placeholder
            # LOAD_FAST switch_mon
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_opponent_switch
            # LOAD_FAST battle
            # CALL 
            0.6
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + guess_opponent_switch
            # LOAD_FAST battle
            # CALL 
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + guess_opponent_switch
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST eval_against
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + estimate_damage
            # LOAD_FAST for_opp
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # jump placeholder
            # LOAD_FAST switch_mon
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # jump placeholder
            # LOAD_FAST switch_mon
            # LOAD_FAST eval_against
            # LOAD_FAST move
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST damage
            # LOAD_FAST damage
            # RETURN_VALUE 
        def get_best_move(self, battle, for_opp, switch_mon, consider_stats):
            # RESUME 
            # BUILD_LIST 
            ('healorder', 'lunarblessing', 'milkdrink', 'moonlight', 'morningsun', 'purify', 'recover', 'rest', 'roost', 'shoreup', 'slackoff', 'softboiled', 'strengthsap', 'synthesis')
            # LIST_EXTEND 
            # STORE_FAST healing_moves
            # LOAD_FAST for_opp
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_opponent_switch
            # LOAD_FAST battle
            # CALL 
            0.6
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + guess_opponent_switch
            # LOAD_FAST battle
            # CALL 
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + guess_opponent_switch
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST eval_against
            # LOAD_FAST switch_mon
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR available_moves
            # jump placeholder
            # LOAD_GLOBAL NULL + list
            # LOAD_FAST switch_mon
            # LOAD_ATTR moves
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            # STORE_FAST move_list
            # LOAD_GLOBAL NULL + len
            # LOAD_FAST move_list
            # CALL 
            0
            # COMPARE_OP ==
            # jump placeholder
            # RETURN_CONST None
            # LOAD_FAST move_list
            0
            # BINARY_SUBSCR 
            # STORE_FAST highest_move
            # LOAD_FAST switch_mon
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # jump placeholder
            # LOAD_FAST switch_mon
            # STORE_FAST mon
            # jump placeholder
            # LOAD_FAST switch_mon
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # jump placeholder
            # LOAD_FAST switch_mon
            # STORE_FAST eval_against
            # LOAD_GLOBAL NULL + len
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR moves
            # CALL 
            0
            # COMPARE_OP ==
            # jump placeholder
            # RETURN_CONST None
            # LOAD_GLOBAL NULL + list
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR moves
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            # STORE_FAST move_list
            # LOAD_FAST move_list
            0
            # BINARY_SUBSCR 
            # STORE_FAST highest_move
            # LOAD_FAST switch_mon
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # jump placeholder
            # LOAD_FAST switch_mon
            # STORE_FAST mon
            -1.0
            # STORE_FAST highest_dam
            # LOAD_FAST move_list
            # GET_ITER 
            # FOR_ITER to 658
            # STORE_FAST move
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + estimate_damage
            # LOAD_FAST mon
            # LOAD_FAST eval_against
            # LOAD_FAST move
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST possible_dam
            # LOAD_FAST possible_dam
            # LOAD_FAST highest_dam
            # COMPARE_OP >
            # jump placeholder
            # jump placeholder
            # LOAD_FAST move
            # STORE_FAST highest_move
            # LOAD_FAST possible_dam
            # STORE_FAST highest_dam
            # jump placeholder
            # END_FOR 
            # BUILD_LIST 
            # STORE_FAST stat_moves
            # LOAD_FAST for_opp
            # jump placeholder
            # LOAD_FAST switch_mon
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST consider_stats
            # jump placeholder
            # LOAD_FAST move_list
            # GET_ITER 
            # FOR_ITER to 788
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR category
            # LOAD_GLOBAL MoveCategory
            # LOAD_ATTR STATUS
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST stat_moves
            # LOAD_ATTR NULL|self + append
            # LOAD_FAST mov
            # CALL 
            # POP_TOP 
            # jump placeholder
            # END_FOR 
            # LOAD_GLOBAL NULL + len
            # LOAD_FAST stat_moves
            # CALL 
            0
            # COMPARE_OP >
            # jump placeholder
            None
            # STORE_FAST heal_move
            None
            # STORE_FAST stat_move
            # LOAD_FAST stat_moves
            # GET_ITER 
            # FOR_ITER to 928
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR id
            # LOAD_FAST healing_moves
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST heal_move
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mov
            # STORE_FAST heal_move
            # jump placeholder
            # LOAD_FAST mov
            # LOAD_ATTR id
            # LOAD_FAST healing_moves
            # CONTAINS_OP 
            # jump placeholder
            # jump placeholder
            # LOAD_FAST stat_move
            None
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mov
            # STORE_FAST stat_move
            # jump placeholder
            # END_FOR 
            # LOAD_FAST heal_move
            None
            # COMPARE_OP !=
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            2
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.5
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST heal_move
            # RETURN_VALUE 
            # LOAD_FAST stat_move
            None
            # COMPARE_OP !=
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_resistant
            # LOAD_FAST battle
            # CALL 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.65
            # COMPARE_OP >
            # jump placeholder
            # LOAD_GLOBAL NULL + sum
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR boosts
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            11
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_die_before_move
            # LOAD_FAST battle
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # jump placeholder
            # LOAD_FAST stat_move
            # RETURN_VALUE 
            # LOAD_FAST highest_dam
            -1.0
            # COMPARE_OP !=
            # jump placeholder
            # LOAD_FAST highest_move
            # RETURN_VALUE 
            # RETURN_CONST None
        def is_faster(self, battle, mon_1, mon_2):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_stats
            # LOAD_FAST mon_1
            # CALL 
            'spe'
            # BINARY_SUBSCR 
            # LOAD_FAST mon_1
            # LOAD_ATTR boosts
            'spe'
            # BINARY_SUBSCR 
            0
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST mon_1
            # LOAD_ATTR boosts
            'spe'
            # BINARY_SUBSCR 
            2
            # BINARY_OP +
            2
            # BINARY_OP /
            # jump placeholder
            2
            2
            # LOAD_FAST mon_1
            # LOAD_ATTR boosts
            'spe'
            # BINARY_SUBSCR 
            # BINARY_OP -
            # BINARY_OP /
            # BINARY_OP *
            # STORE_FAST mon_1_spe
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_stats
            # LOAD_FAST mon_2
            # CALL 
            'spe'
            # BINARY_SUBSCR 
            # LOAD_FAST mon_2
            # LOAD_ATTR boosts
            'spe'
            # BINARY_SUBSCR 
            0
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST mon_2
            # LOAD_ATTR boosts
            'spe'
            # BINARY_SUBSCR 
            2
            # BINARY_OP +
            2
            # BINARY_OP /
            # jump placeholder
            2
            2
            # LOAD_FAST mon_2
            # LOAD_ATTR boosts
            'spe'
            # BINARY_SUBSCR 
            # BINARY_OP -
            # BINARY_OP /
            # BINARY_OP *
            # STORE_FAST mon_2_spe
            # LOAD_FAST mon_1
            # LOAD_ATTR item
            'choicescarf'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mon_1_spe
            1.5
            # BINARY_OP *
            # STORE_FAST mon_1_spe
            # LOAD_FAST mon_2
            # LOAD_ATTR item
            'choicescarf'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mon_2_spe
            1.5
            # BINARY_OP *
            # STORE_FAST mon_2_spe
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_GLOBAL Field
            # LOAD_ATTR TRICK_ROOM
            # LOAD_FAST battle
            # LOAD_ATTR fields
            # LOAD_ATTR NULL|self + keys
            # CALL 
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST mon_1_spe
            # LOAD_FAST mon_2_spe
            # COMPARE_OP <
            # RETURN_VALUE 
            # LOAD_FAST mon_1_spe
            # LOAD_FAST mon_2_spe
            # COMPARE_OP >
            # RETURN_VALUE 
        def should_switch(self, battle, mon):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST mon
            None
            # COMPARE_OP ==
            # jump placeholder
            # RETURN_CONST False
            # LOAD_FAST mon
            # LOAD_ATTR species
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            # COMPARE_OP ==
            # jump placeholder
            # RETURN_CONST False
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.35
            # COMPARE_OP <
            # jump placeholder
            # RETURN_CONST False
            0
            # STORE_FAST hazard_penalty
            # LOAD_FAST battle
            # LOAD_ATTR side_conditions
            # LOAD_ATTR NULL|self + get
            # LOAD_GLOBAL SideCondition
            # LOAD_ATTR STEALTH_ROCK
            # CALL 
            # jump placeholder
            # LOAD_GLOBAL NULL + max
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR NULL|self + damage_multiplier
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR ROCK
            # CALL 
            1
            # CALL 
            # STORE_FAST rock_mult
            # LOAD_FAST hazard_penalty
            0.125
            # LOAD_FAST rock_mult
            # BINARY_OP *
            # BINARY_OP +=
            # STORE_FAST hazard_penalty
            # LOAD_FAST battle
            # LOAD_ATTR side_conditions
            # LOAD_ATTR NULL|self + get
            # LOAD_GLOBAL SideCondition
            # LOAD_ATTR SPIKES
            # CALL 
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR side_conditions
            # LOAD_GLOBAL SideCondition
            # LOAD_ATTR SPIKES
            # BINARY_SUBSCR 
            # STORE_FAST layers
            # LOAD_FAST layers
            # COPY 
            1
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST hazard_penalty
            0.125
            # BINARY_OP +=
            # STORE_FAST hazard_penalty
            # jump placeholder
            # COPY 
            2
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST hazard_penalty
            0.16666666666666666
            # BINARY_OP +=
            # STORE_FAST hazard_penalty
            # jump placeholder
            3
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST hazard_penalty
            0.25
            # BINARY_OP +=
            # STORE_FAST hazard_penalty
            # jump placeholder
            # NOP 
            # LOAD_FAST hazard_penalty
            0
            # BINARY_OP +=
            # STORE_FAST hazard_penalty
            # LOAD_FAST hazard_penalty
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            # COMPARE_OP >=
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR item
            'Heavy-Duty Boots'
            # COMPARE_OP !=
            # jump placeholder
            # RETURN_CONST False
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_most_damage
            # LOAD_FAST battle
            # CALL 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + estimate_stats
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            'hp'
            # BINARY_SUBSCR 
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR current_hp_fraction
            # BINARY_OP *
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_faster
            # LOAD_FAST battle
            # LOAD_FAST mon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            # jump placeholder
            # RETURN_CONST False
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_most_damage
            # LOAD_FAST battle
            # CALL 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + estimate_stats
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            'hp'
            # BINARY_SUBSCR 
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR current_hp_fraction
            # BINARY_OP *
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp_fraction
            0.5
            # COMPARE_OP >
            # jump placeholder
            # RETURN_CONST False
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_opponent_switch
            # LOAD_FAST battle
            # CALL 
            0.6
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + guess_opponent_switch
            # LOAD_FAST battle
            # CALL 
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + guess_opponent_switch
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST eval_against
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # STORE_FAST cur_sc
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST mon
            # CALL 
            # STORE_FAST swi_sc
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST swi_sc
            # LOAD_FAST cur_sc
            1
            # BINARY_OP +
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST swi_sc
            2
            # LOAD_FAST cur_sc
            # BINARY_OP *
            # COMPARE_OP >
            # jump placeholder
            # RETURN_CONST True
            # LOAD_FAST cur_sc
            # LOAD_FAST swi_sc
            1
            # BINARY_OP +
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST cur_sc
            2
            # LOAD_FAST swi_sc
            # BINARY_OP *
            # COMPARE_OP >
            # jump placeholder
            # RETURN_CONST False
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST eval_against
            # LOAD_FAST mon
            # CALL 
            # STORE_FAST mon_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST mon
            # LOAD_FAST eval_against
            # CALL 
            # STORE_FAST opp_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST eval_against
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # STORE_FAST cur_mon_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST eval_against
            # CALL 
            # STORE_FAST cur_opp_mult
            # LOAD_FAST mon_mult
            # LOAD_FAST cur_mon_mult
            # BINARY_OP /
            # STORE_FAST mon_mult_rat
            # LOAD_FAST opp_mult
            # LOAD_FAST cur_opp_mult
            # BINARY_OP /
            # STORE_FAST opp_mult_rat
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST opp_mult_rat
            1
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST mon_mult_rat
            8
            # COMPARE_OP <
            # jump placeholder
            # RETURN_CONST False
            # LOAD_FAST cur_mon_mult
            2
            # COMPARE_OP >=
            # jump placeholder
            # LOAD_FAST cur_opp_mult
            1
            # COMPARE_OP <
            # jump placeholder
            # RETURN_CONST False
            # LOAD_FAST opp_mult_rat
            1
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mon_mult_rat
            4
            # COMPARE_OP >=
            # jump placeholder
            # RETURN_CONST True
            # LOAD_FAST opp_mult_rat
            1
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST opp_mult
            1
            # COMPARE_OP <=
            # jump placeholder
            # LOAD_FAST mon_mult_rat
            2
            # COMPARE_OP >=
            # jump placeholder
            # LOAD_FAST mon_mult
            2
            # COMPARE_OP >=
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_faster
            # LOAD_FAST battle
            # LOAD_FAST mon
            # LOAD_FAST eval_against
            # CALL 
            # jump placeholder
            # RETURN_CONST True
            # LOAD_FAST opp_mult_rat
            0.5
            # COMPARE_OP <=
            # jump placeholder
            # LOAD_FAST opp_mult
            0.5
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST mon_mult
            1
            # COMPARE_OP >=
            # jump placeholder
            # RETURN_CONST True
            # LOAD_FAST opp_mult_rat
            0.5
            # COMPARE_OP <
            # jump placeholder
            # RETURN_CONST True
            # LOAD_FAST cur_mon_mult
            0.5
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST mon_mult_rat
            1
            # COMPARE_OP >
            # jump placeholder
            # RETURN_CONST True
            # RETURN_CONST False
        def is_resistant(self, battle):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            1
            # COMPARE_OP <=
            # STORE_FAST type_res
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_most_damage
            # LOAD_FAST battle
            True
            # CALL 
            0.5
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR current_hp
            # BINARY_OP *
            # COMPARE_OP <
            # STORE_FAST dam_res
            # LOAD_FAST type_res
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST dam_res
            # RETURN_VALUE 
        def get_ideal_switch(self, battle):
            # RESUME 
            None
            # STORE_FAST switch
            False
            # STORE_FAST can_OHKO
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST battle
            # LOAD_ATTR available_switches
            # GET_ITER 
            # EXTENDED_ARG 
            # FOR_ITER to 620
            # STORE_FAST mon
            # LOAD_FAST switch
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mon
            # STORE_FAST switch
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST switch
            # CALL 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST mon
            # CALL 
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST can_OHKO
            # jump placeholder
            # LOAD_FAST mon
            # STORE_FAST switch
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST switch
            # CALL 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST mon
            # CALL 
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR stats
            'spe'
            # BINARY_SUBSCR 
            # LOAD_FAST switch
            # LOAD_ATTR stats
            'spe'
            # BINARY_SUBSCR 
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST can_OHKO
            # jump placeholder
            # LOAD_FAST mon
            # STORE_FAST switch
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + can_OHKO
            # LOAD_FAST battle
            # LOAD_FAST mon
            # CALL 
            # jump placeholder
            # jump placeholder
            # LOAD_FAST can_OHKO
            # jump placeholder
            True
            # STORE_FAST can_OHKO
            # LOAD_FAST mon
            # STORE_FAST switch
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST switch
            # CALL 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST mon
            # CALL 
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST mon
            # STORE_FAST switch
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST switch
            # CALL 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_switch_score
            # LOAD_FAST battle
            # LOAD_FAST mon
            # CALL 
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR stats
            'spe'
            # BINARY_SUBSCR 
            # LOAD_FAST switch
            # LOAD_ATTR stats
            'spe'
            # BINARY_SUBSCR 
            # COMPARE_OP >
            # jump placeholder
            # EXTENDED_ARG 
            # jump placeholder
            # LOAD_FAST mon
            # STORE_FAST switch
            # EXTENDED_ARG 
            # jump placeholder
            # END_FOR 
            # LOAD_FAST switch
            # RETURN_VALUE 
        def will_die_before_move(self, battle, mon):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_most_damage
            # LOAD_FAST battle
            True
            # LOAD_FAST mon
            # CALL 
            # STORE_FAST dam
            # LOAD_FAST dam
            0
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_faster
            # LOAD_FAST battle
            # LOAD_FAST mon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR current_hp_fraction
            0.35
            # COMPARE_OP <
            # RETURN_VALUE 
            # LOAD_FAST mon
            # LOAD_ATTR current_hp_fraction
            0.5
            # COMPARE_OP <
            # RETURN_VALUE 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_faster
            # LOAD_FAST battle
            # LOAD_FAST mon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            # jump placeholder
            1
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR species
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            # COMPARE_OP !=
            # jump placeholder
            2
            # jump placeholder
            1.5
            # STORE_FAST mult
            # LOAD_FAST dam
            # LOAD_FAST mult
            # BINARY_OP *
            # LOAD_FAST mon
            # LOAD_ATTR current_hp
            # COMPARE_OP >
            # STORE_FAST will_kill
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST will_kill
            # RETURN_VALUE 
        def get_switch_score(self, battle, switch):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_opponent_switch
            # LOAD_FAST battle
            # CALL 
            0.6
            # COMPARE_OP <
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + guess_opponent_switch
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST eval_against
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST switch
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST eval_against
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # RETURN_CONST 0.0
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + will_die_before_move
            # LOAD_FAST battle
            # LOAD_FAST switch
            # CALL 
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # RETURN_CONST 0.0
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST eval_against
            # LOAD_FAST switch
            # CALL 
            # STORE_FAST mon_mult
            # LOAD_GLOBAL NULL + max
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST switch
            # LOAD_FAST eval_against
            # CALL 
            0.25
            # CALL 
            # STORE_FAST opp_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST eval_against
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # STORE_FAST cur_mon_mult
            # LOAD_GLOBAL NULL + max
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST eval_against
            # CALL 
            0.25
            # CALL 
            # STORE_FAST cur_opp_mult
            # LOAD_FAST cur_opp_mult
            # LOAD_FAST opp_mult
            # BINARY_OP /
            # LOAD_FAST mon_mult
            # LOAD_FAST cur_mon_mult
            # BINARY_OP /
            # BINARY_OP *
            # STORE_FAST comp
            # LOAD_FAST switch
            # LOAD_ATTR species
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR species
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST comp
            1
            # LOAD_GLOBAL NULL + sum
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR boosts
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            2
            # BINARY_OP /
            # BINARY_OP +
            # BINARY_OP *
            # STORE_FAST comp
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST comp
            # RETURN_VALUE 
        def guess_accuracy_score(self):
            # RESUME 
            0.5
            # STORE_FAST score
            # LOAD_GLOBAL NULL + len
            # LOAD_FAST self
            # LOAD_ATTR switch_guesses
            # CALL 
            0
            # COMPARE_OP ==
            # jump placeholder
            0.3
            # jump placeholder
            # LOAD_GLOBAL NULL + min
            1
            # LOAD_GLOBAL NULL + len
            # LOAD_FAST self
            # LOAD_ATTR switch_guesses
            # CALL 
            # BINARY_OP /
            0.1
            # CALL 
            # STORE_FAST scale
            # LOAD_FAST self
            # LOAD_ATTR switch_guesses
            # GET_ITER 
            # FOR_ITER to 224
            # STORE_FAST guess
            # LOAD_FAST guess
            # UNPACK_SEQUENCE 
            # STORE_FAST sco
            # STORE_FAST res
            # LOAD_FAST res
            # jump placeholder
            # LOAD_FAST score
            3
            # LOAD_FAST scale
            # BINARY_OP *
            # LOAD_FAST sco
            0.5
            # BINARY_OP -
            # BINARY_OP *
            # BINARY_OP +=
            # STORE_FAST score
            # jump placeholder
            # LOAD_FAST score
            # LOAD_FAST scale
            0.5
            # LOAD_FAST sco
            # BINARY_OP -
            # BINARY_OP *
            # BINARY_OP +=
            # STORE_FAST score
            # jump placeholder
            # END_FOR 
            # LOAD_GLOBAL NULL + min
            # LOAD_GLOBAL NULL + max
            # LOAD_FAST score
            0
            # CALL 
            1
            # CALL 
            # STORE_FAST score
            # LOAD_FAST score
            # RETURN_VALUE 
        def will_opponent_switch(self, battle):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST self
            # LOAD_ATTR opp_switch_team
            # jump placeholder
            # RETURN_CONST 0.0
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + guess_opponent_switch
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST switch_mon
            # LOAD_FAST switch_mon
            None
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST switch_mon
            # LOAD_ATTR species
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR species
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST switch_mon
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # STORE_FAST mon_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST switch_mon
            # CALL 
            # STORE_FAST opp_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # STORE_FAST cur_mon_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            # STORE_FAST cur_opp_mult
            # LOAD_FAST opp_mult
            # LOAD_FAST cur_opp_mult
            # BINARY_OP /
            # LOAD_FAST cur_mon_mult
            # LOAD_FAST mon_mult
            # BINARY_OP /
            # BINARY_OP *
            # STORE_FAST comp
            # LOAD_FAST comp
            4
            # COMPARE_OP >
            # jump placeholder
            1.0
            # jump placeholder
            # LOAD_FAST comp
            1
            # COMPARE_OP <
            # jump placeholder
            0.0
            # jump placeholder
            # LOAD_FAST comp
            1
            # BINARY_OP -
            3
            # BINARY_OP /
            # STORE_FAST swap_odds
            # LOAD_FAST self
            # LOAD_ATTR record_guess
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR switch_guesses
            # LOAD_ATTR NULL|self + append
            # LOAD_FAST swap_odds
            False
            # BUILD_TUPLE 
            # CALL 
            # POP_TOP 
            False
            # LOAD_FAST self
            # STORE_ATTR record_guess
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + guess_accuracy_score
            # CALL 
            # LOAD_FAST swap_odds
            # BINARY_OP *
            # STORE_FAST swap_odds
            # LOAD_FAST swap_odds
            # RETURN_VALUE 
            # RETURN_CONST 0.0
        def TurnState():
            def __init__(self, battle):
                # RESUME 
                # LOAD_GLOBAL NULL + deepcopy
                # LOAD_FAST battle
                # CALL 
                # LOAD_FAST self
                # STORE_ATTR _battle_state
                # LOAD_GLOBAL NULL + deepcopy
                # LOAD_FAST battle
                # LOAD_ATTR active_pokemon
                # CALL 
                # LOAD_FAST self
                # STORE_ATTR _mon
                # LOAD_GLOBAL NULL + deepcopy
                # LOAD_FAST battle
                # LOAD_ATTR opponent_active_pokemon
                # CALL 
                # LOAD_FAST self
                # STORE_ATTR _opp
                # RETURN_CONST None
            def get_state(self):
                # RESUME 
                # LOAD_FAST self
                # LOAD_ATTR _battle_state
                # RETURN_VALUE 
            def get_mon(self):
                # RESUME 
                # LOAD_FAST self
                # LOAD_ATTR _mon
                # RETURN_VALUE 
            def get_opp(self):
                # RESUME 
                # LOAD_FAST self
                # LOAD_ATTR _opp
                # RETURN_VALUE 
            def get_dam(self, other):
                # RESUME 
                # LOAD_FAST self
                # LOAD_ATTR NULL|self + get_mon
                # CALL 
                # LOAD_ATTR current_hp
                # STORE_FAST current
                # LOAD_FAST other
                # LOAD_ATTR NULL|self + get_mon
                # CALL 
                # LOAD_ATTR current_hp
                # STORE_FAST last
                # LOAD_GLOBAL NULL + max
                # LOAD_GLOBAL NULL + float
                # LOAD_FAST last
                # LOAD_FAST current
                # BINARY_OP -
                # CALL 
                0
                # CALL 
                # RETURN_VALUE 
            def mon_fainted(self, other):
                # RESUME 
                # LOAD_FAST other
                # LOAD_ATTR _battle_state
                # LOAD_ATTR team
                # LOAD_ATTR NULL|self + values
                # CALL 
                # GET_ITER 
                # FOR_ITER to 228
                # STORE_FAST mon
                # LOAD_FAST self
                # LOAD_ATTR _mon
                # LOAD_ATTR species
                # LOAD_FAST mon
                # LOAD_ATTR species
                # COMPARE_OP ==
                # jump placeholder
                # jump placeholder
                # LOAD_FAST self
                # LOAD_ATTR _mon
                # LOAD_ATTR fainted
                # jump placeholder
                # LOAD_FAST mon
                # LOAD_ATTR fainted
                # jump placeholder
                # POP_TOP 
                # RETURN_CONST True
                # POP_TOP 
                # RETURN_CONST False
                # END_FOR 
                # RETURN_CONST False
            def opp_fainted(self, other):
                # RESUME 
                # LOAD_FAST other
                # LOAD_ATTR _battle_state
                # LOAD_ATTR opponent_team
                # LOAD_ATTR NULL|self + values
                # CALL 
                # GET_ITER 
                # FOR_ITER to 228
                # STORE_FAST mon
                # LOAD_FAST self
                # LOAD_ATTR _opp
                # LOAD_ATTR species
                # LOAD_FAST mon
                # LOAD_ATTR species
                # COMPARE_OP ==
                # jump placeholder
                # jump placeholder
                # LOAD_FAST self
                # LOAD_ATTR _opp
                # LOAD_ATTR fainted
                # jump placeholder
                # LOAD_FAST mon
                # LOAD_ATTR fainted
                # jump placeholder
                # POP_TOP 
                # RETURN_CONST True
                # POP_TOP 
                # RETURN_CONST False
                # END_FOR 
                # RETURN_CONST False
            def opp_switched(self, other, last_move_d_tail):
                # RESUME 
                # LOAD_FAST self
                # LOAD_ATTR _opp
                # LOAD_ATTR species
                # LOAD_FAST other
                # LOAD_ATTR _opp
                # LOAD_ATTR species
                # COMPARE_OP !=
                # jump placeholder
                # LOAD_FAST self
                # LOAD_ATTR NULL|self + opp_fainted
                # LOAD_FAST other
                # CALL 
                # jump placeholder
                # LOAD_FAST last_move_d_tail
                # jump placeholder
                # RETURN_CONST True
                # RETURN_CONST False
            # RESUME 
            __name__
            __module__ = <value>
            'CustomAgent.TurnState'
            __qualname__ = <value>
            'battle'
            Battle
            # BUILD_TUPLE 
            # MAKE_FUNCTION annotations
            __init__ = <value>
            # MAKE_FUNCTION 
            get_state = <value>
            # MAKE_FUNCTION 
            get_mon = <value>
            # MAKE_FUNCTION 
            get_opp = <value>
            # MAKE_FUNCTION 
            get_dam = <value>
            'return'
            bool
            # BUILD_TUPLE 
            # MAKE_FUNCTION annotations
            mon_fainted = <value>
            'return'
            bool
            # BUILD_TUPLE 
            # MAKE_FUNCTION annotations
            opp_fainted = <value>
            (False,)
            'last_move_d_tail'
            bool
            'return'
            bool
            # BUILD_TUPLE 
            # MAKE_FUNCTION defaults, annotations
            opp_switched = <value>
            # RETURN_CONST None
        def get_opp_team_total(self, battle):
            # RESUME 
            # BUILD_LIST 
            # STORE_FAST opp_team
            False
            # STORE_FAST found
            # LOAD_FAST battle
            # LOAD_ATTR teampreview_opponent_team
            # GET_ITER 
            # FOR_ITER to 240
            # STORE_FAST pre_mon
            False
            # STORE_FAST found
            # LOAD_FAST battle
            # LOAD_ATTR opponent_team
            # LOAD_ATTR NULL|self + values
            # CALL 
            # GET_ITER 
            # FOR_ITER to 196
            # STORE_FAST mon
            # LOAD_FAST mon
            # LOAD_ATTR species
            # LOAD_FAST pre_mon
            # LOAD_ATTR species
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            True
            # STORE_FAST found
            # LOAD_FAST opp_team
            # LOAD_ATTR NULL|self + append
            # LOAD_FAST mon
            # CALL 
            # POP_TOP 
            # POP_TOP 
            # jump placeholder
            # END_FOR 
            # LOAD_FAST found
            # jump placeholder
            # jump placeholder
            # LOAD_FAST opp_team
            # LOAD_ATTR NULL|self + append
            # LOAD_FAST pre_mon
            # CALL 
            # POP_TOP 
            # jump placeholder
            # END_FOR 
            # LOAD_FAST opp_team
            # RETURN_VALUE 
        def get_opp_available_switches(self, battle):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_opp_team_total
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST opp_team
            # BUILD_LIST 
            # STORE_FAST switches
            # LOAD_FAST opp_team
            # GET_ITER 
            # FOR_ITER to 184
            # STORE_FAST mon
            # LOAD_FAST mon
            # LOAD_ATTR fainted
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR species
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR species
            # COMPARE_OP !=
            # jump placeholder
            # jump placeholder
            # LOAD_FAST switches
            # LOAD_ATTR NULL|self + append
            # LOAD_FAST mon
            # CALL 
            # POP_TOP 
            # jump placeholder
            # END_FOR 
            # LOAD_FAST switches
            # RETURN_VALUE 
        def is_better_switch(self, mon_mult_1, opp_mult_1, mon_mult_2, opp_mult_2, for_opp):
            # RESUME 
            # LOAD_FAST mon_mult_1
            # LOAD_FAST mon_mult_2
            # COMPARE_OP >=
            # STORE_FAST a
            # LOAD_FAST opp_mult_1
            # LOAD_FAST opp_mult_2
            # COMPARE_OP >=
            # STORE_FAST b
            # LOAD_FAST for_opp
            # STORE_FAST c
            # LOAD_FAST mon_mult_2
            # LOAD_FAST opp_mult_2
            # BINARY_OP /
            1
            # COMPARE_OP >
            # STORE_FAST d
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            8
            # LOAD_FAST a
            # BINARY_OP *
            4
            # LOAD_FAST b
            # BINARY_OP *
            # BINARY_OP +
            2
            # LOAD_FAST c
            # BINARY_OP *
            # BINARY_OP +
            # LOAD_FAST d
            # BINARY_OP +
            # STORE_FAST value
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST value
            # COPY 
            1
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # RETURN_CONST True
            # COPY 
            2
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # RETURN_CONST True
            # COPY 
            4
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # RETURN_CONST True
            # COPY 
            5
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # RETURN_CONST True
            # COPY 
            10
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # RETURN_CONST True
            # COPY 
            11
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # RETURN_CONST True
            # COPY 
            13
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # RETURN_CONST True
            # COPY 
            14
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # RETURN_CONST True
            # POP_TOP 
            # NOP 
            # RETURN_CONST False
        def guess_opponent_switch(self, battle):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_opp_available_switches
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST opp_team
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_GLOBAL NULL + len
            # LOAD_FAST opp_team
            # CALL 
            0
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # RETURN_VALUE 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST opp_team
            0
            # BINARY_SUBSCR 
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # STORE_FAST best_mon_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST opp_team
            0
            # BINARY_SUBSCR 
            # CALL 
            # STORE_FAST best_opp_mult
            None
            # STORE_FAST best_mon
            # LOAD_FAST opp_team
            # GET_ITER 
            # FOR_ITER to 448
            # STORE_FAST mon
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST mon
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # CALL 
            # STORE_FAST mon_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_best_mult
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_FAST mon
            # CALL 
            # STORE_FAST opp_mult
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_better_switch
            # LOAD_FAST best_mon_mult
            # LOAD_FAST best_opp_mult
            # LOAD_FAST mon_mult
            # LOAD_FAST opp_mult
            True
            # CALL 
            # jump placeholder
            # jump placeholder
            # LOAD_FAST self
            # LOAD_ATTR print
            # jump placeholder
            # NOP 
            # LOAD_FAST mon
            # STORE_FAST best_mon
            # LOAD_FAST mon_mult
            # STORE_FAST best_mon_mult
            # LOAD_FAST opp_mult
            # STORE_FAST best_opp_mult
            # jump placeholder
            # END_FOR 
            # LOAD_FAST best_mon
            # RETURN_VALUE 
        def get_best_mult(self, def_mon, atk_mon):
            # RESUME 
            # LOAD_GLOBAL NULL + set
            # CALL 
            # STORE_FAST atk_types
            # LOAD_GLOBAL NULL + len
            # LOAD_FAST atk_mon
            # LOAD_ATTR moves
            # CALL 
            4
            # COMPARE_OP !=
            # jump placeholder
            # LOAD_FAST atk_mon
            # LOAD_ATTR types
            # GET_ITER 
            # FOR_ITER to 136
            # STORE_FAST typ
            # LOAD_FAST atk_types
            # LOAD_ATTR NULL|self + add
            # LOAD_FAST typ
            # CALL 
            # POP_TOP 
            # jump placeholder
            # END_FOR 
            # LOAD_FAST atk_mon
            # LOAD_ATTR is_terastallized
            # jump placeholder
            # LOAD_FAST atk_types
            # LOAD_ATTR NULL|self + add
            # LOAD_FAST atk_mon
            # LOAD_ATTR tera_type
            # CALL 
            # POP_TOP 
            # LOAD_FAST atk_mon
            # LOAD_ATTR moves
            # LOAD_ATTR NULL|self + values
            # CALL 
            # GET_ITER 
            # FOR_ITER to 390
            # STORE_FAST mov
            # LOAD_FAST mov
            # LOAD_ATTR category
            # LOAD_GLOBAL MoveCategory
            # LOAD_ATTR STATUS
            # COMPARE_OP !=
            # jump placeholder
            # jump placeholder
            # LOAD_FAST atk_types
            # LOAD_ATTR NULL|self + add
            # LOAD_FAST mov
            # LOAD_ATTR type
            # CALL 
            # POP_TOP 
            # jump placeholder
            # END_FOR 
            -1
            # STORE_FAST best_mult
            # LOAD_FAST atk_types
            # GET_ITER 
            # FOR_ITER to 458
            # STORE_FAST typ
            # LOAD_FAST def_mon
            # LOAD_ATTR NULL|self + damage_multiplier
            # LOAD_FAST typ
            # CALL 
            # STORE_FAST mult
            # LOAD_FAST mult
            # LOAD_FAST best_mult
            # COMPARE_OP >
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mult
            # STORE_FAST best_mult
            # jump placeholder
            # END_FOR 
            # LOAD_FAST best_mult
            0
            # COMPARE_OP !=
            # jump placeholder
            # LOAD_FAST best_mult
            # RETURN_VALUE 
            0.01
            # RETURN_VALUE 
        def estimate_damage(self, mon, opponent, move, battle):
            # RESUME 
            # LOAD_FAST move
            None
            # COMPARE_OP ==
            # jump placeholder
            # RETURN_CONST 0.0
            # LOAD_FAST move
            # LOAD_ATTR base_power
            # STORE_FAST base_power
            # LOAD_FAST mon
            # LOAD_ATTR level
            # STORE_FAST self_level
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + attack_defense_ratio
            # LOAD_FAST mon
            # LOAD_FAST opponent
            # LOAD_FAST move
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST a_d_ratio
            # LOAD_FAST move
            # LOAD_ATTR category
            # LOAD_GLOBAL MoveCategory
            # LOAD_ATTR STATUS
            # COMPARE_OP !=
            # jump placeholder
            2
            # LOAD_FAST self_level
            # BINARY_OP *
            5
            # BINARY_OP /
            2
            # BINARY_OP +
            50
            # BINARY_OP /
            # LOAD_FAST a_d_ratio
            # BINARY_OP *
            # LOAD_FAST base_power
            # BINARY_OP *
            2
            # BINARY_OP +
            # jump placeholder
            0
            # STORE_FAST unmodified_damage
            # LOAD_FAST unmodified_damage
            # STORE_FAST damage
            # LOAD_FAST battle
            # LOAD_ATTR NULL|self + is_grounded
            # LOAD_FAST opponent
            # CALL 
            # jump placeholder
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR GROUND
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_GLOBAL Field
            # LOAD_ATTR GRAVITY
            # LOAD_GLOBAL NULL + list
            # LOAD_FAST battle
            # LOAD_ATTR fields
            # LOAD_ATTR NULL|self + keys
            # CALL 
            # CALL 
            # CONTAINS_OP 
            # jump placeholder
            0
            # STORE_FAST damage
            # LOAD_FAST mon
            # LOAD_ATTR status
            # LOAD_GLOBAL Status
            # LOAD_ATTR BRN
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST damage
            0.5
            # BINARY_OP *
            # STORE_FAST damage
            # LOAD_FAST opponent
            # LOAD_ATTR NULL|self + damage_multiplier
            # LOAD_FAST move
            # CALL 
            # STORE_FAST effectiveness
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + weather_multiplier
            # LOAD_GLOBAL NULL + list
            # LOAD_FAST battle
            # LOAD_ATTR weather
            # LOAD_ATTR NULL|self + keys
            # CALL 
            # CALL 
            # LOAD_FAST move
            # CALL 
            # STORE_FAST weather
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + abiltiies_multiplier
            # LOAD_FAST mon
            # LOAD_FAST opponent
            # LOAD_FAST move
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST abilities
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + field_multiplier
            # LOAD_FAST mon
            # LOAD_FAST opponent
            # LOAD_FAST move
            # LOAD_FAST battle
            # CALL 
            # STORE_FAST fields
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + stab_multiplier
            # LOAD_FAST mon
            # LOAD_FAST move
            # CALL 
            # STORE_FAST stab
            # LOAD_FAST mon
            # LOAD_ATTR item
            'pixieplate'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FAIRY
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST damage
            1.2
            # BINARY_OP *
            # STORE_FAST damage
            # LOAD_FAST damage
            # LOAD_FAST effectiveness
            # BINARY_OP *
            # LOAD_FAST weather
            # BINARY_OP *
            # LOAD_FAST abilities
            # BINARY_OP *
            # LOAD_FAST fields
            # BINARY_OP *
            # LOAD_FAST stab
            # BINARY_OP *
            # STORE_FAST damage
            # LOAD_FAST damage
            # RETURN_VALUE 
        def attack_defense_ratio(self, mon, opp, move, battle):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_stats
            # LOAD_FAST mon
            # CALL 
            # STORE_FAST mon_st
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_stats
            # LOAD_FAST opp
            # CALL 
            # STORE_FAST opp_st
            # LOAD_FAST move
            # LOAD_ATTR category
            # LOAD_GLOBAL MoveCategory
            # LOAD_ATTR PHYSICAL
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mon_st
            'atk'
            # BINARY_SUBSCR 
            # LOAD_FAST mon
            # LOAD_ATTR boosts
            'atk'
            # BINARY_SUBSCR 
            0
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR boosts
            'atk'
            # BINARY_SUBSCR 
            2
            # BINARY_OP +
            2
            # BINARY_OP /
            # jump placeholder
            2
            2
            # LOAD_FAST mon
            # LOAD_ATTR boosts
            'atk'
            # BINARY_SUBSCR 
            # BINARY_OP -
            # BINARY_OP /
            # BINARY_OP *
            # STORE_FAST attack
            # LOAD_FAST opp_st
            'def'
            # BINARY_SUBSCR 
            # LOAD_FAST opp
            # LOAD_ATTR boosts
            'def'
            # BINARY_SUBSCR 
            0
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST opp
            # LOAD_ATTR boosts
            'def'
            # BINARY_SUBSCR 
            2
            # BINARY_OP +
            2
            # BINARY_OP /
            # jump placeholder
            2
            2
            # LOAD_FAST opp
            # LOAD_ATTR boosts
            'def'
            # BINARY_SUBSCR 
            # BINARY_OP -
            # BINARY_OP /
            # BINARY_OP *
            # STORE_FAST defense
            # LOAD_GLOBAL Weather
            # LOAD_ATTR SNOW
            # LOAD_FAST battle
            # LOAD_ATTR weather
            # LOAD_ATTR NULL|self + keys
            # CALL 
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_GLOBAL Weather
            # LOAD_ATTR SNOWSCAPE
            # LOAD_FAST battle
            # LOAD_ATTR weather
            # LOAD_ATTR NULL|self + keys
            # CALL 
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR ICE
            # LOAD_FAST opp
            # LOAD_ATTR types
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST defense
            1.5
            # BINARY_OP *
            # STORE_FAST defense
            # LOAD_FAST attack
            # LOAD_FAST defense
            # BINARY_OP /
            # RETURN_VALUE 
            # LOAD_FAST move
            # LOAD_ATTR category
            # LOAD_GLOBAL MoveCategory
            # LOAD_ATTR SPECIAL
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mon_st
            'spa'
            # BINARY_SUBSCR 
            # LOAD_FAST mon
            # LOAD_ATTR boosts
            'spa'
            # BINARY_SUBSCR 
            0
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR boosts
            'spa'
            # BINARY_SUBSCR 
            2
            # BINARY_OP +
            2
            # BINARY_OP /
            # jump placeholder
            2
            2
            # LOAD_FAST mon
            # LOAD_ATTR boosts
            'spa'
            # BINARY_SUBSCR 
            # BINARY_OP -
            # BINARY_OP /
            # BINARY_OP *
            # STORE_FAST attack
            # LOAD_FAST opp_st
            'spd'
            # BINARY_SUBSCR 
            # LOAD_FAST opp
            # LOAD_ATTR boosts
            'spd'
            # BINARY_SUBSCR 
            0
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST opp
            # LOAD_ATTR boosts
            'spd'
            # BINARY_SUBSCR 
            2
            # BINARY_OP +
            2
            # BINARY_OP /
            # jump placeholder
            2
            2
            # LOAD_FAST opp
            # LOAD_ATTR boosts
            'spd'
            # BINARY_SUBSCR 
            # BINARY_OP -
            # BINARY_OP /
            # BINARY_OP *
            # STORE_FAST defense
            # LOAD_GLOBAL Weather
            # LOAD_ATTR SANDSTORM
            # LOAD_FAST battle
            # LOAD_ATTR weather
            # LOAD_ATTR NULL|self + keys
            # CALL 
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR ROCK
            # LOAD_FAST opp
            # LOAD_ATTR types
            # CONTAINS_OP 
            # jump placeholder
            1.5
            # LOAD_FAST defense
            # BINARY_OP *
            # STORE_FAST defense
            # LOAD_FAST attack
            # LOAD_FAST defense
            # BINARY_OP /
            # RETURN_VALUE 
            0
            # STORE_FAST attack
            1
            # STORE_FAST defense
            # LOAD_FAST attack
            # LOAD_FAST defense
            # BINARY_OP /
            # RETURN_VALUE 
        def weather_multiplier(self, weathers, move):
            # RESUME 
            1.0
            # STORE_FAST mult
            # LOAD_FAST weathers
            # GET_ITER 
            # FOR_ITER to 378
            # STORE_FAST weather
            # LOAD_FAST weather
            # LOAD_GLOBAL Weather
            # LOAD_ATTR SUNNYDAY
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FIRE
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mult
            1.5
            # BINARY_OP *
            # STORE_FAST mult
            # jump placeholder
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR WATER
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mult
            0.5
            # BINARY_OP *
            # STORE_FAST mult
            # jump placeholder
            # LOAD_FAST weather
            # LOAD_GLOBAL Weather
            # LOAD_ATTR RAINDANCE
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FIRE
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mult
            0.5
            # BINARY_OP *
            # STORE_FAST mult
            # jump placeholder
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR WATER
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mult
            1.5
            # BINARY_OP *
            # STORE_FAST mult
            # jump placeholder
            # END_FOR 
            # LOAD_FAST mult
            # RETURN_VALUE 
        def abiltiies_multiplier(self, mon, opp, move, battle):
            # RESUME 
            1.0
            # STORE_FAST mult
            # LOAD_FAST mon
            # LOAD_ATTR ability
            # STORE_FAST abil
            # LOAD_FAST opp
            # LOAD_ATTR ability
            # STORE_FAST obil
            # LOAD_FAST obil
            None
            # COMPARE_OP !=
            # EXTENDED_ARG 
            # jump placeholder
            # LOAD_FAST obil
            # LOAD_ATTR NULL|self + lower
            # CALL 
            # COPY 
            'dry skin'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FIRE
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mult
            1.25
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR WATER
            # COMPARE_OP ==
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'earth eater'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR GROUND
            # COMPARE_OP ==
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            # COPY 
            'filter'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # COPY 
            'prism armor'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # COPY 
            'solid rock'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # POP_TOP 
            # jump placeholder
            # POP_TOP 
            # POP_TOP 
            # LOAD_FAST opp
            # LOAD_ATTR NULL|self + damage_multiplier
            # LOAD_FAST move
            # CALL 
            2
            # COMPARE_OP >=
            # jump placeholder
            # LOAD_FAST mult
            0.75
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'flash fire'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'fluffy'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR category
            # LOAD_GLOBAL MoveCategory
            # LOAD_ATTR PHYSICAL
            # COMPARE_OP ==
            # jump placeholder
            0.5
            # LOAD_FAST mult
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FIRE
            # COMPARE_OP ==
            # jump placeholder
            2
            # LOAD_FAST mult
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'heatproof'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FIRE
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mult
            0.5
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'ice face'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR category
            # LOAD_GLOBAL MoveCategory
            # LOAD_ATTR PHYSICAL
            # COMPARE_OP ==
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'levitate'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR GROUND
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_GLOBAL Field
            # LOAD_ATTR GRAVITY
            # LOAD_GLOBAL NULL + list
            # LOAD_FAST battle
            # LOAD_ATTR fields
            # LOAD_ATTR NULL|self + keys
            # CALL 
            # CALL 
            # CONTAINS_OP 
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'motor drive'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR ELECTRIC
            # COMPARE_OP ==
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            # COPY 
            'multiscale'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # COPY 
            'shadow shield'
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # POP_TOP 
            # jump placeholder
            # POP_TOP 
            # POP_TOP 
            # LOAD_FAST opp
            # LOAD_ATTR current_hp_fraction
            1
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mult
            0.5
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'purifying salt'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR GHOST
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mult
            0.5
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'sap sipper'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR GRASS
            # COMPARE_OP ==
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'thick fat'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR ICE
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FIRE
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mult
            0.5
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'volt absorb'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR ELECTRIC
            # COMPARE_OP ==
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'water absorb'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR WATER
            # COMPARE_OP ==
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'water bubble'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FIRE
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mult
            0.5
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # COPY 
            'well-baked body'
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FIRE
            # COMPARE_OP ==
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            'wonder guard'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST opp
            # LOAD_ATTR NULL|self + damage_multiplier
            # LOAD_FAST move
            # CALL 
            2
            # COMPARE_OP <
            # jump placeholder
            0
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # NOP 
            # LOAD_FAST mult
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
        def field_multiplier(self, mon, opp, move, battle):
            # RESUME 
            1.0
            # STORE_FAST mult
            # LOAD_FAST battle
            # LOAD_ATTR fields
            # LOAD_ATTR NULL|self + keys
            # CALL 
            # GET_ITER 
            # EXTENDED_ARG 
            # FOR_ITER to 638
            # STORE_FAST field
            # LOAD_FAST field
            # COPY 
            # LOAD_GLOBAL Field
            # LOAD_ATTR ELECTRIC_TERRAIN
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR ELECTRIC
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mult
            1.5
            # BINARY_OP *
            # STORE_FAST mult
            # jump placeholder
            # COPY 
            # LOAD_GLOBAL Field
            # LOAD_ATTR GRASSY_TERRAIN
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR GRASS
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mult
            1.5
            # BINARY_OP *
            # STORE_FAST mult
            # jump placeholder
            # COPY 
            # LOAD_GLOBAL Field
            # LOAD_ATTR MUD_SPORT
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR ELECTRIC
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mult
            0.5
            # BINARY_OP *
            # STORE_FAST mult
            # jump placeholder
            # COPY 
            # LOAD_GLOBAL Field
            # LOAD_ATTR PSYCHIC_TERRAIN
            # COMPARE_OP ==
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR PSYCHIC
            # COMPARE_OP ==
            # jump placeholder
            # jump placeholder
            # LOAD_FAST mult
            1.5
            # BINARY_OP *
            # STORE_FAST mult
            # jump placeholder
            # LOAD_GLOBAL Field
            # LOAD_ATTR WATER_SPORT
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_GLOBAL PokemonType
            # LOAD_ATTR FIRE
            # COMPARE_OP ==
            # jump placeholder
            # EXTENDED_ARG 
            # jump placeholder
            # LOAD_FAST mult
            0.5
            # BINARY_OP *
            # STORE_FAST mult
            # EXTENDED_ARG 
            # jump placeholder
            # NOP 
            # LOAD_FAST mult
            # STORE_FAST mult
            # EXTENDED_ARG 
            # jump placeholder
            # END_FOR 
            # LOAD_FAST mult
            # RETURN_VALUE 
        def stab_multiplier(self, mon, move):
            # RESUME 
            1.0
            # STORE_FAST mult
            # LOAD_FAST mon
            # LOAD_ATTR _terastallized
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR tera_type
            # LOAD_FAST move
            # LOAD_ATTR type
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR tera_type
            # LOAD_FAST mon
            # LOAD_ATTR original_types
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST mult
            2
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # LOAD_FAST mon
            # LOAD_ATTR _terastallized
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR tera_type
            # LOAD_FAST move
            # LOAD_ATTR type
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST mult
            1.5
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # LOAD_FAST mon
            # LOAD_ATTR _terastallized
            # jump placeholder
            # LOAD_FAST move
            # LOAD_ATTR type
            # LOAD_FAST mon
            # LOAD_ATTR original_types
            # CONTAINS_OP 
            # jump placeholder
            # LOAD_FAST mult
            1.5
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
            # LOAD_FAST mult
            1.0
            # BINARY_OP *
            # STORE_FAST mult
            # LOAD_FAST mult
            # RETURN_VALUE 
        def estimate_stats(self, opp):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_attack_mon
            # LOAD_FAST opp
            # CALL 
            # STORE_FAST is_attack_mon
            # LOAD_FAST opp
            # LOAD_ATTR base_stats
            # STORE_FAST opp_bs
            252
            # STORE_FAST EV_MAX
            0
            # STORE_FAST EV_MIN
            # LOAD_FAST opp
            # LOAD_ATTR level
            # STORE_FAST lvl
            # BUILD_MAP 
            # STORE_FAST est_stats
            # LOAD_GLOBAL NULL + abs
            # LOAD_FAST opp_bs
            'def'
            # BINARY_SUBSCR 
            # LOAD_FAST opp_bs
            'spd'
            # BINARY_SUBSCR 
            # BINARY_OP -
            # CALL 
            25
            # COMPARE_OP >
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST opp_bs
            'hp'
            # BINARY_SUBSCR 
            125
            # COMPARE_OP <
            # STORE_FAST hp_boost
            # LOAD_FAST opp_bs
            # LOAD_ATTR NULL|self + keys
            # CALL 
            # GET_ITER 
            # EXTENDED_ARG 
            # FOR_ITER to 804
            # STORE_FAST st
            # LOAD_FAST st
            # COPY 
            'hp'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST hp_boost
            # jump placeholder
            # LOAD_FAST is_attack_mon
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST EV_MAX
            # STORE_FAST ev
            # jump placeholder
            # COPY 
            'def'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST hp_boost
            # jump placeholder
            # LOAD_FAST opp_bs
            'def'
            # BINARY_SUBSCR 
            # LOAD_FAST opp_bs
            'spd'
            # BINARY_SUBSCR 
            # COMPARE_OP <=
            # jump placeholder
            # LOAD_FAST hp_boost
            # jump placeholder
            # LOAD_FAST is_attack_mon
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST EV_MAX
            # STORE_FAST ev
            # jump placeholder
            # COPY 
            'spd'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST hp_boost
            # jump placeholder
            # LOAD_FAST opp_bs
            'def'
            # BINARY_SUBSCR 
            # LOAD_FAST opp_bs
            'spd'
            # BINARY_SUBSCR 
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST hp_boost
            # jump placeholder
            # LOAD_FAST is_attack_mon
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST EV_MAX
            # STORE_FAST ev
            # jump placeholder
            # COPY 
            'atk'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST is_attack_mon
            # jump placeholder
            # LOAD_FAST opp_bs
            'atk'
            # BINARY_SUBSCR 
            # LOAD_FAST opp_bs
            'spa'
            # BINARY_SUBSCR 
            # COMPARE_OP >=
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST EV_MAX
            # STORE_FAST ev
            # jump placeholder
            # COPY 
            'spa'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST is_attack_mon
            # jump placeholder
            # LOAD_FAST opp_bs
            'atk'
            # BINARY_SUBSCR 
            # LOAD_FAST opp_bs
            'spa'
            # BINARY_SUBSCR 
            # COMPARE_OP <
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST EV_MAX
            # STORE_FAST ev
            # jump placeholder
            'spe'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_FAST is_attack_mon
            # jump placeholder
            # LOAD_FAST EV_MAX
            # STORE_FAST ev
            # jump placeholder
            # NOP 
            # LOAD_FAST EV_MIN
            # STORE_FAST ev
            2
            # LOAD_FAST opp_bs
            # LOAD_FAST st
            # BINARY_SUBSCR 
            # BINARY_OP *
            31
            # BINARY_OP +
            # LOAD_FAST ev
            4
            # BINARY_OP /
            # BINARY_OP +
            # LOAD_FAST lvl
            # BINARY_OP *
            100
            # BINARY_OP /
            # STORE_FAST base_calc
            # LOAD_FAST st
            'hp'
            # COMPARE_OP ==
            # jump placeholder
            # LOAD_GLOBAL NULL + int
            # LOAD_FAST base_calc
            # LOAD_FAST lvl
            # BINARY_OP +
            10
            # BINARY_OP +
            # CALL 
            # STORE_FAST stat
            # jump placeholder
            # LOAD_FAST is_attack_mon
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST ev
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_GLOBAL NULL + bool
            # LOAD_FAST opp_bs
            'spe'
            # BINARY_SUBSCR 
            130
            # COMPARE_OP >
            # CALL 
            # LOAD_GLOBAL NULL + bool
            # LOAD_FAST st
            'spe'
            # COMPARE_OP ==
            # CALL 
            # BINARY_OP ^
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST is_attack_mon
            # UNARY_NOT 
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_GLOBAL NULL + bool
            # LOAD_FAST opp_bs
            'def'
            # BINARY_SUBSCR 
            # LOAD_FAST opp_bs
            'spd'
            # BINARY_SUBSCR 
            # COMPARE_OP <
            # CALL 
            # LOAD_GLOBAL NULL + bool
            # LOAD_FAST st
            'spd'
            # COMPARE_OP ==
            # CALL 
            # BINARY_OP ^
            # STORE_FAST nature_boost
            # LOAD_GLOBAL NULL + int
            # LOAD_GLOBAL NULL + float
            # LOAD_FAST base_calc
            5
            # BINARY_OP +
            # CALL 
            # LOAD_FAST nature_boost
            # jump placeholder
            1.1
            # jump placeholder
            1.0
            # BINARY_OP *
            # CALL 
            # STORE_FAST stat
            # LOAD_FAST est_stats
            # LOAD_ATTR NULL|self + update
            # LOAD_FAST st
            # LOAD_FAST stat
            # BUILD_MAP 
            # CALL 
            # POP_TOP 
            # EXTENDED_ARG 
            # jump placeholder
            # END_FOR 
            # LOAD_FAST est_stats
            # RETURN_VALUE 
        def is_attack_mon(self, mon):
            # RESUME 
            # LOAD_FAST mon
            # LOAD_ATTR base_stats
            'atk'
            # BINARY_SUBSCR 
            130
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR base_stats
            'spa'
            # BINARY_SUBSCR 
            130
            # COMPARE_OP >
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR base_stats
            'spe'
            # BINARY_SUBSCR 
            130
            # COMPARE_OP >
            # jump placeholder
            # RETURN_CONST True
            # RETURN_CONST False
        def is_special_mon(self, mon):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_attack_mon
            # LOAD_FAST mon
            # CALL 
            # STORE_FAST is_attack
            # LOAD_FAST is_attack
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR base_stats
            'spa'
            # BINARY_SUBSCR 
            # LOAD_FAST mon
            # LOAD_ATTR base_stats
            'atk'
            # BINARY_SUBSCR 
            # COMPARE_OP >
            # STORE_FAST is_special
            # LOAD_FAST is_special
            # RETURN_VALUE 
            # LOAD_FAST mon
            # LOAD_ATTR base_stats
            'spd'
            # BINARY_SUBSCR 
            # LOAD_FAST mon
            # LOAD_ATTR base_stats
            'def'
            # BINARY_SUBSCR 
            # COMPARE_OP >
            # STORE_FAST is_special
            # LOAD_FAST is_special
            # RETURN_VALUE 
        def can_OHKO(self, battle, mon):
            # RESUME 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_most_damage
            # LOAD_FAST battle
            False
            # LOAD_FAST mon
            # CALL 
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # LOAD_ATTR current_hp_fraction
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + get_stats
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            'hp'
            # BINARY_SUBSCR 
            # BINARY_OP *
            # COMPARE_OP >
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + is_faster
            # LOAD_FAST battle
            # LOAD_FAST mon
            # LOAD_FAST battle
            # LOAD_ATTR opponent_active_pokemon
            # CALL 
            # COPY 
            # jump placeholder
            # POP_TOP 
            # LOAD_FAST battle
            # LOAD_ATTR active_pokemon
            # LOAD_ATTR fainted
            # RETURN_VALUE 
        def get_stats(self, mon):
            # RESUME 
            # LOAD_GLOBAL NULL + list
            # LOAD_FAST mon
            # LOAD_ATTR stats
            # LOAD_ATTR NULL|self + values
            # CALL 
            # CALL 
            0
            # BINARY_SUBSCR 
            None
            # COMPARE_OP !=
            # jump placeholder
            # LOAD_FAST mon
            # LOAD_ATTR stats
            # RETURN_VALUE 
            # LOAD_FAST self
            # LOAD_ATTR NULL|self + estimate_stats
            # LOAD_FAST mon
            # CALL 
            # RETURN_VALUE 
        # MAKE_CELL __class__
        # RESUME 
        __name__
        __module__ = <value>
        'CustomAgent'
        __qualname__ = <value>
        # LOAD_CLOSURE __class__
        # BUILD_TUPLE 
        # MAKE_FUNCTION closure
        __init__ = <value>
        'battle'
        AbstractBattle
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        teampreview = <value>
        'battle'
        AbstractBattle
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        _battle_finished_callback = <value>
        'msg'
        str
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        log_info = <value>
        'battle'
        AbstractBattle
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        choose_move = <value>
        'battle'
        Battle
        'return'
        SingleBattleOrder
        None
        # BINARY_OP |
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        kyogre_method = <value>
        'battle'
        Battle
        'return'
        SingleBattleOrder
        None
        # BINARY_OP |
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        arceus_method = <value>
        'battle'
        Battle
        'return'
        SingleBattleOrder
        None
        # BINARY_OP |
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        calyrex_method = <value>
        'battle'
        Battle
        'return'
        SingleBattleOrder
        None
        # BINARY_OP |
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        necrozma_method = <value>
        'battle'
        Battle
        'return'
        SingleBattleOrder
        None
        # BINARY_OP |
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        landorus_method = <value>
        'battle'
        Battle
        'return'
        bool
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        should_tera = <value>
        (False, None)
        'battle'
        Battle
        'for_opp'
        bool
        'switch_mon'
        Optional
        Pokemon
        # BINARY_SUBSCR 
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION defaults, annotations
        get_most_damage = <value>
        (None, False)
        'battle'
        Battle
        'for_opp'
        bool
        'switch_mon'
        Optional
        Pokemon
        # BINARY_SUBSCR 
        'consider_stats'
        bool
        'return'
        Optional
        Move
        # BINARY_SUBSCR 
        # BUILD_TUPLE 
        # MAKE_FUNCTION defaults, annotations
        get_best_move = <value>
        'battle'
        Battle
        'mon_1'
        Pokemon
        'mon_2'
        Pokemon
        'return'
        bool
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        is_faster = <value>
        'battle'
        Battle
        'mon'
        Optional
        Pokemon
        # BINARY_SUBSCR 
        'return'
        bool
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        should_switch = <value>
        'battle'
        Battle
        'return'
        bool
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        is_resistant = <value>
        'battle'
        Battle
        'return'
        Optional
        Pokemon
        # BINARY_SUBSCR 
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        get_ideal_switch = <value>
        'battle'
        Battle
        'mon'
        Pokemon
        'return'
        bool
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        will_die_before_move = <value>
        'battle'
        Battle
        'switch'
        Pokemon
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        get_switch_score = <value>
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        guess_accuracy_score = <value>
        'battle'
        Battle
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        will_opponent_switch = <value>
        # PUSH_NULL 
        # LOAD_BUILD_CLASS 
        # MAKE_FUNCTION 
        'TurnState'
        # CALL 
        TurnState = <value>
        'battle'
        Battle
        'return'
        list
        Pokemon
        # BINARY_SUBSCR 
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        get_opp_team_total = <value>
        'battle'
        Battle
        'return'
        list
        Pokemon
        # BINARY_SUBSCR 
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        get_opp_available_switches = <value>
        'mon_mult_1'
        float
        'opp_mult_1'
        float
        'mon_mult_2'
        float
        'opp_mult_2'
        float
        'for_opp'
        bool
        'return'
        bool
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        is_better_switch = <value>
        'battle'
        Battle
        'return'
        Optional
        Pokemon
        # BINARY_SUBSCR 
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        guess_opponent_switch = <value>
        'def_mon'
        Pokemon
        'atk_mon'
        Pokemon
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        get_best_mult = <value>
        'mon'
        Pokemon
        'opponent'
        Pokemon
        'move'
        Optional
        Move
        # BINARY_SUBSCR 
        'battle'
        Battle
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        estimate_damage = <value>
        'mon'
        Pokemon
        'opp'
        Pokemon
        'move'
        Move
        'battle'
        Battle
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        attack_defense_ratio = <value>
        'weathers'
        list
        Weather
        # BINARY_SUBSCR 
        'move'
        Move
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        weather_multiplier = <value>
        'mon'
        Pokemon
        'opp'
        Pokemon
        'move'
        Move
        'battle'
        Battle
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        abiltiies_multiplier = <value>
        'mon'
        Pokemon
        'opp'
        Pokemon
        'move'
        Move
        'battle'
        Battle
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        field_multiplier = <value>
        'mon'
        Pokemon
        'move'
        Move
        'return'
        float
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        stab_multiplier = <value>
        'opp'
        Pokemon
        'return'
        dict
        str
        int
        # BUILD_TUPLE 
        # BINARY_SUBSCR 
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        estimate_stats = <value>
        'mon'
        Pokemon
        'return'
        bool
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        is_attack_mon = <value>
        'mon'
        Pokemon
        'return'
        bool
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        is_special_mon = <value>
        'battle'
        Battle
        'mon'
        Pokemon
        'return'
        bool
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        can_OHKO = <value>
        'mon'
        Pokemon
        'return'
        dict
        str
        int
        # BUILD_TUPLE 
        # BINARY_SUBSCR 
        # BUILD_TUPLE 
        # MAKE_FUNCTION annotations
        get_stats = <value>
        # LOAD_CLOSURE __class__
        # COPY 
        __classcell__ = <value>
        # RETURN_VALUE 
    # RESUME 
    0
    ('AbstractBattle', 'Battle', 'Field', 'Move', 'MoveCategory', 'Pokemon', 'PokemonType', 'SideCondition', 'Status', 'Weather')
    # IMPORT_NAME poke_env.battle
    # IMPORT_FROM AbstractBattle
    AbstractBattle = <value>
    # IMPORT_FROM Battle
    Battle = <value>
    # IMPORT_FROM Field
    Field = <value>
    # IMPORT_FROM Move
    Move = <value>
    # IMPORT_FROM MoveCategory
    MoveCategory = <value>
    # IMPORT_FROM Pokemon
    Pokemon = <value>
    # IMPORT_FROM PokemonType
    PokemonType = <value>
    # IMPORT_FROM SideCondition
    SideCondition = <value>
    # IMPORT_FROM Status
    Status = <value>
    # IMPORT_FROM Weather
    Weather = <value>
    # POP_TOP 
    0
    ('Player',)
    # IMPORT_NAME poke_env.player
    # IMPORT_FROM Player
    Player = <value>
    # POP_TOP 
    0
    ('SingleBattleOrder',)
    # IMPORT_NAME poke_env.player.battle_order
    # IMPORT_FROM SingleBattleOrder
    SingleBattleOrder = <value>
    # POP_TOP 
    0
    ('Optional',)
    # IMPORT_NAME typing
    # IMPORT_FROM Optional
    Optional = <value>
    # POP_TOP 
    0
    ('deepcopy',)
    # IMPORT_NAME copy
    # IMPORT_FROM deepcopy
    deepcopy = <value>
    # POP_TOP 
    0
    None
    # IMPORT_NAME os
    os = <value>
    '\nCrunchie (Landorus-Therian) @ Rocky Helmet  \nAbility: Intimidate  \nShiny: Yes  \nTera Type: Ground  \nEVs: 252 Atk / 4 SpD / 252 Spe  \nJolly Nature  \n- Stealth Rock  \n- Earthquake  \n- Taunt  \n- Stone Edge  \n\nBallet (Arceus-Fairy) @ Pixie Plate  \nAbility: Multitype  \nShiny: Yes  \nTera Type: Water  \nEVs: 240 HP / 252 Def / 16 Spe  \nBold Nature  \n- Judgment  \n- Earth Power  \n- Dragon Tail  \n- Recover  \n\nWheels (Koraidon) @ Choice Scarf  \nAbility: Orichalcum Pulse  \nTera Type: Fire  \nEVs: 252 Atk / 4 SpD / 252 Spe  \nAdamant Nature  \n- Collision Course  \n- Dragon Claw  \n- Flare Blitz  \n- Crunch  \n\nFlounder (Kyogre) @ Heavy-Duty Boots  \nAbility: Drizzle  \nShiny: Yes  \nTera Type: Poison  \nEVs: 248 HP / 164 Def / 80 SpA / 16 Spe  \nBold Nature  \nIVs: 0 Atk  \n- Origin Pulse  \n- Thunder  \n- Calm Mind  \n- Ice Beam  \n\nSharp (Necrozma-Dusk-Mane) @ Occa Berry  \nAbility: Prism Armor  \nShiny: Yes  \nTera Type: Steel  \nEVs: 252 Atk / 4 SpD / 252 Spe  \nAdamant Nature  \n- Dragon Dance  \n- Photon Geyser  \n- Morning Sun  \n- Sunsteel Strike  \n\nBreak (Calyrex-Ice) @ Weakness Policy  \nAbility: As One (Glastrier)  \nTera Type: Ground  \nEVs: 248 HP / 252 Atk / 8 SpD  \nBrave Nature  \nIVs: 0 Spe  \n- Trick Room  \n- Swords Dance  \n- Glacial Lance  \n- High Horsepower  \n'
    team = <value>
    # PUSH_NULL 
    # LOAD_BUILD_CLASS 
    # MAKE_FUNCTION 
    'CustomAgent'
    Player
    # CALL 
    CustomAgent = <value>
    # RETURN_CONST None