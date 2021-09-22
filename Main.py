from shuntingYard import shunting_yard
from convertNNF1 import convertNNFMain
from modalClausification import modal_clausification_main
from convertToInput import convertToInputMain
from modalClauses import constructModalClause
from convertAtoms import convertAtoms, convertTrueAndFalse, convertAtoms1
#from modalSat import modal_sat_main
from modalSatNew3 import modal_sat_main
from ConvertTestFormat import ConvertFormat

# string = "(p & q) | []([](r)) | <>(-r)"         #unsat
# string = "(p & q) >> (q & p)"  #sat
# string = "([](p) & [](p)) | <>(- p)"  #sat
# string = "([](p) & [](p)) | <>(- q)"    #unsat
# string = "([](p) | [](p)) | <>(- q)"  #unsat
# string = "[]p1 & <>-p1" #unsat
# string = "(p >> q) | (q >> p)" #sat
# string = "p1 | -p1"   #sat
# string = "(p >> q) >> ((-q) >> (-p))"   #sat
# string = "p1 >> p1"  #sat
# string = "p1&-p1"    #unsat
# string = "[](p>>q)>>([]p>>[]q)"  #sat
# string = "[](p&q)>>([]p&[]q)"    #sat
# string = "(<>(p|q))>>(<>p|<>q)"  #sat
# string = "([]p)|(<>([]p))"   #unsat
# string = "[]p>>[][]p"   #unsat
# string = "[]([]p1>>[]p2)>>[][]([]p1>>[]p2)"         #unsat
# string = "([]([](p)))&(<>(<>(-p)))"     #unsat
# string = " ( []( []([](p >> [] p) >> p) >> (<> [] p >> p) ) >>[] []( []([](p >> [] p) >> p) >> (<> [] p >> p) ))"   #unsat
# string = "( []( []([](p >> [] p) >> p) >>[] []( []([](p >> [] p) >> p) )))"     #unsat
# string = "( []((<> [] p >> p) ) >>[] []((<> [] p >> p) ))"      #unsat
# string = "( []( []([](p >> [] p) >> p) >> (<> [] p) ) >>[] []( []([](p >> [] p) >> p) >> (<> [] p) )) "     #unsat
# string = "( []( (<> [] p >> p) ) >>[] []( (<> [] p >> p) ))"    #unsat

#unsat 16you jie guo in lin
#string = "((((((((((((((((((((((((((((((((~((box(((dia p1) & (box(dia p1))) -> p2)) v (box((p2 & (box p2)) -> (dia p1))))) v (~((box(((p1 -> (box p2)) & (box(p1 -> (box p2)))) -> p2)) v (box((p2 & (box p2)) -> (p1 -> (box p2))))))) v ((~((box(((dia p2) & (box(dia p2))) -> p3)) v (box((p3 & (box p3)) -> (dia p2))))) v (~((box(((p2 -> (box p3)) & (box(p2 -> (box p3)))) -> p3)) v (box((p3 & (box p3)) -> (p2 -> (box p3)))))))) v ((~((box(((dia p3) & (box(dia p3))) -> p4)) v (box((p4 & (box p4)) -> (dia p3))))) v (~((box(((p3 -> (box p4)) & (box(p3 -> (box p4)))) -> p4)) v (box((p4 & (box p4)) -> (p3 -> (box p4)))))))) v ((~((box(((dia p4) & (box(dia p4))) -> p5)) v (box((p5 & (box p5)) -> (dia p4))))) v (~((box(((p4 -> (box p5)) & (box(p4 -> (box p5)))) -> p5)) v (box((p5 & (box p5)) -> (p4 -> (box p5)))))))) v ((~((box(((dia p5) & (box(dia p5))) -> p6)) v (box((p6 & (box p6)) -> (dia p5))))) v (~((box(((p5 -> (box p6)) & (box(p5 -> (box p6)))) -> p6)) v (box((p6 & (box p6)) -> (p5 -> (box p6)))))))) v ((~((box(((dia p6) & (box(dia p6))) -> p7)) v (box((p7 & (box p7)) -> (dia p6))))) v (~((box(((p6 -> (box p7)) & (box(p6 -> (box p7)))) -> p7)) v (box((p7 & (box p7)) -> (p6 -> (box p7)))))))) v ((~((box(((dia p7) & (box(dia p7))) -> p8)) v (box((p8 & (box p8)) -> (dia p7))))) v (~((box(((p7 -> (box p8)) & (box(p7 -> (box p8)))) -> p8)) v (box((p8 & (box p8)) -> (p7 -> (box p8)))))))) v ((~((box(((dia p8) & (box(dia p8))) -> p9)) v (box((p9 & (box p9)) -> (dia p8))))) v (~((box(((p8 -> (box p9)) & (box(p8 -> (box p9)))) -> p9)) v (box((p9 & (box p9)) -> (p8 -> (box p9)))))))) v ((~((box(((dia p9) & (box(dia p9))) -> p10)) v (box((p10 & (box p10)) -> (dia p9))))) v (~((box(((p9 -> (box p10)) & (box(p9 -> (box p10)))) -> p10)) v (box((p10 & (box p10)) -> (p9 -> (box p10)))))))) v ((~((box(((dia p10) & (box(dia p10))) -> p11)) v (box((p11 & (box p11)) -> (dia p10))))) v (~((box(((p10 -> (box p11)) & (box(p10 -> (box p11)))) -> p11)) v (box((p11 & (box p11)) -> (p10 -> (box p11)))))))) v ((~((box(((dia p11) & (box(dia p11))) -> p12)) v (box((p12 & (box p12)) -> (dia p11))))) v (~((box(((p11 -> (box p12)) & (box(p11 -> (box p12)))) -> p12)) v (box((p12 & (box p12)) -> (p11 -> (box p12)))))))) v ((~((box(((dia p12) & (box(dia p12))) -> p13)) v (box((p13 & (box p13)) -> (dia p12))))) v (~((box(((p12 -> (box p13)) & (box(p12 -> (box p13)))) -> p13)) v (box((p13 & (box p13)) -> (p12 -> (box p13)))))))) v ((~((box(((dia p13) & (box(dia p13))) -> p14)) v (box((p14 & (box p14)) -> (dia p13))))) v (~((box(((p13 -> (box p14)) & (box(p13 -> (box p14)))) -> p14)) v (box((p14 & (box p14)) -> (p13 -> (box p14)))))))) v ((~((box(((dia p14) & (box(dia p14))) -> p15)) v (box((p15 & (box p15)) -> (dia p14))))) v (~((box(((p14 -> (box p15)) & (box(p14 -> (box p15)))) -> p15)) v (box((p15 & (box p15)) -> (p14 -> (box p15)))))))) v ((~((box(((dia p15) & (box(dia p15))) -> p16)) v (box((p16 & (box p16)) -> (dia p15))))) v (~((box(((p15 -> (box p16)) & (box(p15 -> (box p16)))) -> p16)) v (box((p16 & (box p16)) -> (p15 -> (box p16)))))))) v ((~((box(((dia p16) & (box(dia p16))) -> p17)) v (box((p17 & (box p17)) -> (dia p16))))) v (~((box(((p16 -> (box p17)) & (box(p16 -> (box p17)))) -> p17)) v (box((p17 & (box p17)) -> (p16 -> (box p17)))))))) v ((~((box(((dia p17) & (box(dia p17))) -> p18)) v (box((p18 & (box p18)) -> (dia p17))))) v (~((box(((p17 -> (box p18)) & (box(p17 -> (box p18)))) -> p18)) v (box((p18 & (box p18)) -> (p17 -> (box p18)))))))) v ((~((box(((dia p18) & (box(dia p18))) -> p19)) v (box((p19 & (box p19)) -> (dia p18))))) v (~((box(((p18 -> (box p19)) & (box(p18 -> (box p19)))) -> p19)) v (box((p19 & (box p19)) -> (p18 -> (box p19)))))))) v ((~((box(((dia p19) & (box(dia p19))) -> p20)) v (box((p20 & (box p20)) -> (dia p19))))) v (~((box(((p19 -> (box p20)) & (box(p19 -> (box p20)))) -> p20)) v (box((p20 & (box p20)) -> (p19 -> (box p20)))))))) v ((~((box(((dia p20) & (box(dia p20))) -> p21)) v (box((p21 & (box p21)) -> (dia p20))))) v (~((box(((p20 -> (box p21)) & (box(p20 -> (box p21)))) -> p21)) v (box((p21 & (box p21)) -> (p20 -> (box p21)))))))) v ((~((box(((dia p21) & (box(dia p21))) -> p22)) v (box((p22 & (box p22)) -> (dia p21))))) v (~((box(((p21 -> (box p22)) & (box(p21 -> (box p22)))) -> p22)) v (box((p22 & (box p22)) -> (p21 -> (box p22)))))))) v ((~((box(((dia p22) & (box(dia p22))) -> p23)) v (box((p23 & (box p23)) -> (dia p22))))) v (~((box(((p22 -> (box p23)) & (box(p22 -> (box p23)))) -> p23)) v (box((p23 & (box p23)) -> (p22 -> (box p23)))))))) v ((~((box(((dia p23) & (box(dia p23))) -> p24)) v (box((p24 & (box p24)) -> (dia p23))))) v (~((box(((p23 -> (box p24)) & (box(p23 -> (box p24)))) -> p24)) v (box((p24 & (box p24)) -> (p23 -> (box p24)))))))) v ((~((box(((dia p24) & (box(dia p24))) -> p25)) v (box((p25 & (box p25)) -> (dia p24))))) v (~((box(((p24 -> (box p25)) & (box(p24 -> (box p25)))) -> p25)) v (box((p25 & (box p25)) -> (p24 -> (box p25)))))))) v ((~((box(((dia p25) & (box(dia p25))) -> p26)) v (box((p26 & (box p26)) -> (dia p25))))) v (~((box(((p25 -> (box p26)) & (box(p25 -> (box p26)))) -> p26)) v (box((p26 & (box p26)) -> (p25 -> (box p26)))))))) v ((~((box(((dia p26) & (box(dia p26))) -> p27)) v (box((p27 & (box p27)) -> (dia p26))))) v (~((box(((p26 -> (box p27)) & (box(p26 -> (box p27)))) -> p27)) v (box((p27 & (box p27)) -> (p26 -> (box p27)))))))) v ((~((box(((dia p27) & (box(dia p27))) -> p28)) v (box((p28 & (box p28)) -> (dia p27))))) v (~((box(((p27 -> (box p28)) & (box(p27 -> (box p28)))) -> p28)) v (box((p28 & (box p28)) -> (p27 -> (box p28)))))))) v ((~((box(((dia p28) & (box(dia p28))) -> p29)) v (box((p29 & (box p29)) -> (dia p28))))) v (~((box(((p28 -> (box p29)) & (box(p28 -> (box p29)))) -> p29)) v (box((p29 & (box p29)) -> (p28 -> (box p29)))))))) v ((~((box(((dia p29) & (box(dia p29))) -> p30)) v (box((p30 & (box p30)) -> (dia p29))))) v (~((box(((p29 -> (box p30)) & (box(p29 -> (box p30)))) -> p30)) v (box((p30 & (box p30)) -> (p29 -> (box p30)))))))) v ((~((box(((dia p30) & (box(dia p30))) -> p31)) v (box((p31 & (box p31)) -> (dia p30))))) v (~((box(((p30 -> (box p31)) & (box(p30 -> (box p31)))) -> p31)) v (box((p31 & (box p31)) -> (p30 -> (box p31)))))))) v ((box((box p16) -> p16)) v (box((box p16) -> p16)))) v ((((((((((((((((((((((((((((((~((box(((dia p32) & (box(dia p32))) -> p33)) v (box((p33 & (box p33)) -> (dia p32))))) v (~((box(((p32 -> (box p33)) & (box(p32 -> (box p33)))) -> p33)) v (box((p33 & (box p33)) -> (p32 -> (box p33))))))) v ((~((box(((dia p33) & (box(dia p33))) -> p34)) v (box((p34 & (box p34)) -> (dia p33))))) v (~((box(((p33 -> (box p34)) & (box(p33 -> (box p34)))) -> p34)) v (box((p34 & (box p34)) -> (p33 -> (box p34)))))))) v ((~((box(((dia p34) & (box(dia p34))) -> p35)) v (box((p35 & (box p35)) -> (dia p34))))) v (~((box(((p34 -> (box p35)) & (box(p34 -> (box p35)))) -> p35)) v (box((p35 & (box p35)) -> (p34 -> (box p35)))))))) v ((~((box(((dia p35) & (box(dia p35))) -> p36)) v (box((p36 & (box p36)) -> (dia p35))))) v (~((box(((p35 -> (box p36)) & (box(p35 -> (box p36)))) -> p36)) v (box((p36 & (box p36)) -> (p35 -> (box p36)))))))) v ((~((box(((dia p36) & (box(dia p36))) -> p37)) v (box((p37 & (box p37)) -> (dia p36))))) v (~((box(((p36 -> (box p37)) & (box(p36 -> (box p37)))) -> p37)) v (box((p37 & (box p37)) -> (p36 -> (box p37)))))))) v ((~((box(((dia p37) & (box(dia p37))) -> p38)) v (box((p38 & (box p38)) -> (dia p37))))) v (~((box(((p37 -> (box p38)) & (box(p37 -> (box p38)))) -> p38)) v (box((p38 & (box p38)) -> (p37 -> (box p38)))))))) v ((~((box(((dia p38) & (box(dia p38))) -> p39)) v (box((p39 & (box p39)) -> (dia p38))))) v (~((box(((p38 -> (box p39)) & (box(p38 -> (box p39)))) -> p39)) v (box((p39 & (box p39)) -> (p38 -> (box p39)))))))) v ((~((box(((dia p39) & (box(dia p39))) -> p40)) v (box((p40 & (box p40)) -> (dia p39))))) v (~((box(((p39 -> (box p40)) & (box(p39 -> (box p40)))) -> p40)) v (box((p40 & (box p40)) -> (p39 -> (box p40)))))))) v ((~((box(((dia p40) & (box(dia p40))) -> p41)) v (box((p41 & (box p41)) -> (dia p40))))) v (~((box(((p40 -> (box p41)) & (box(p40 -> (box p41)))) -> p41)) v (box((p41 & (box p41)) -> (p40 -> (box p41)))))))) v ((~((box(((dia p41) & (box(dia p41))) -> p42)) v (box((p42 & (box p42)) -> (dia p41))))) v (~((box(((p41 -> (box p42)) & (box(p41 -> (box p42)))) -> p42)) v (box((p42 & (box p42)) -> (p41 -> (box p42)))))))) v ((~((box(((dia p42) & (box(dia p42))) -> p43)) v (box((p43 & (box p43)) -> (dia p42))))) v (~((box(((p42 -> (box p43)) & (box(p42 -> (box p43)))) -> p43)) v (box((p43 & (box p43)) -> (p42 -> (box p43)))))))) v ((~((box(((dia p43) & (box(dia p43))) -> p44)) v (box((p44 & (box p44)) -> (dia p43))))) v (~((box(((p43 -> (box p44)) & (box(p43 -> (box p44)))) -> p44)) v (box((p44 & (box p44)) -> (p43 -> (box p44)))))))) v ((~((box(((dia p44) & (box(dia p44))) -> p45)) v (box((p45 & (box p45)) -> (dia p44))))) v (~((box(((p44 -> (box p45)) & (box(p44 -> (box p45)))) -> p45)) v (box((p45 & (box p45)) -> (p44 -> (box p45)))))))) v ((~((box(((dia p45) & (box(dia p45))) -> p46)) v (box((p46 & (box p46)) -> (dia p45))))) v (~((box(((p45 -> (box p46)) & (box(p45 -> (box p46)))) -> p46)) v (box((p46 & (box p46)) -> (p45 -> (box p46)))))))) v ((~((box(((dia p46) & (box(dia p46))) -> p47)) v (box((p47 & (box p47)) -> (dia p46))))) v (~((box(((p46 -> (box p47)) & (box(p46 -> (box p47)))) -> p47)) v (box((p47 & (box p47)) -> (p46 -> (box p47)))))))) v ((~((box(((dia p47) & (box(dia p47))) -> p48)) v (box((p48 & (box p48)) -> (dia p47))))) v (~((box(((p47 -> (box p48)) & (box(p47 -> (box p48)))) -> p48)) v (box((p48 & (box p48)) -> (p47 -> (box p48)))))))) v ((~((box(((dia p48) & (box(dia p48))) -> p49)) v (box((p49 & (box p49)) -> (dia p48))))) v (~((box(((p48 -> (box p49)) & (box(p48 -> (box p49)))) -> p49)) v (box((p49 & (box p49)) -> (p48 -> (box p49)))))))) v ((~((box(((dia p49) & (box(dia p49))) -> p50)) v (box((p50 & (box p50)) -> (dia p49))))) v (~((box(((p49 -> (box p50)) & (box(p49 -> (box p50)))) -> p50)) v (box((p50 & (box p50)) -> (p49 -> (box p50)))))))) v ((~((box(((dia p50) & (box(dia p50))) -> p51)) v (box((p51 & (box p51)) -> (dia p50))))) v (~((box(((p50 -> (box p51)) & (box(p50 -> (box p51)))) -> p51)) v (box((p51 & (box p51)) -> (p50 -> (box p51)))))))) v ((~((box(((dia p51) & (box(dia p51))) -> p52)) v (box((p52 & (box p52)) -> (dia p51))))) v (~((box(((p51 -> (box p52)) & (box(p51 -> (box p52)))) -> p52)) v (box((p52 & (box p52)) -> (p51 -> (box p52)))))))) v ((~((box(((dia p52) & (box(dia p52))) -> p53)) v (box((p53 & (box p53)) -> (dia p52))))) v (~((box(((p52 -> (box p53)) & (box(p52 -> (box p53)))) -> p53)) v (box((p53 & (box p53)) -> (p52 -> (box p53)))))))) v ((~((box(((dia p53) & (box(dia p53))) -> p54)) v (box((p54 & (box p54)) -> (dia p53))))) v (~((box(((p53 -> (box p54)) & (box(p53 -> (box p54)))) -> p54)) v (box((p54 & (box p54)) -> (p53 -> (box p54)))))))) v ((~((box(((dia p54) & (box(dia p54))) -> p55)) v (box((p55 & (box p55)) -> (dia p54))))) v (~((box(((p54 -> (box p55)) & (box(p54 -> (box p55)))) -> p55)) v (box((p55 & (box p55)) -> (p54 -> (box p55)))))))) v ((~((box(((dia p55) & (box(dia p55))) -> p56)) v (box((p56 & (box p56)) -> (dia p55))))) v (~((box(((p55 -> (box p56)) & (box(p55 -> (box p56)))) -> p56)) v (box((p56 & (box p56)) -> (p55 -> (box p56)))))))) v ((~((box(((dia p56) & (box(dia p56))) -> p57)) v (box((p57 & (box p57)) -> (dia p56))))) v (~((box(((p56 -> (box p57)) & (box(p56 -> (box p57)))) -> p57)) v (box((p57 & (box p57)) -> (p56 -> (box p57)))))))) v ((~((box(((dia p57) & (box(dia p57))) -> p58)) v (box((p58 & (box p58)) -> (dia p57))))) v (~((box(((p57 -> (box p58)) & (box(p57 -> (box p58)))) -> p58)) v (box((p58 & (box p58)) -> (p57 -> (box p58)))))))) v ((~((box(((dia p58) & (box(dia p58))) -> p59)) v (box((p59 & (box p59)) -> (dia p58))))) v (~((box(((p58 -> (box p59)) & (box(p58 -> (box p59)))) -> p59)) v (box((p59 & (box p59)) -> (p58 -> (box p59)))))))) v ((~((box(((dia p59) & (box(dia p59))) -> p60)) v (box((p60 & (box p60)) -> (dia p59))))) v (~((box(((p59 -> (box p60)) & (box(p59 -> (box p60)))) -> p60)) v (box((p60 & (box p60)) -> (p59 -> (box p60)))))))) v ((~((box(((dia p60) & (box(dia p60))) -> p61)) v (box((p61 & (box p61)) -> (dia p60))))) v (~((box(((p60 -> (box p61)) & (box(p60 -> (box p61)))) -> p61)) v (box((p61 & (box p61)) -> (p60 -> (box p61))))))))"
#unsat
#string = "((((dia(~((box(~p1)) -> (box(box(~p1)))))) v (box(dia(box p0)))) v (box((~(box p1)) -> (box(~(box p1)))))) v (((dia((box p1) & (dia(dia(~p1))))) v (dia(((((box(dia p0)) & (box((~p0) v (box p3)))) v (dia((box(dia(box((~p0) v (box p3))))) & (box(dia p0))))) v ((box(dia p0)) & (dia(dia(box((~p0) v (box p3))))))) v (dia(((dia(box(dia p0))) & p0) & (dia((~p0) v (box p3)))))))) v (dia((box(dia p1)) & (dia(dia(box(~p1)))))))) v (dia p4)"
#string = "((((((((((((((((~((box(((dia p1) & (box(dia p1))) -> p2)) v (box((p2 & (box p2)) -> (dia p1))))) v (~((box(((p1 -> (box p2)) & (box(p1 -> (box p2)))) -> p2)) v (box((p2 & (box p2)) -> (p1 -> (box p2))))))) v ((~((box(((dia p2) & (box(dia p2))) -> p3)) v (box((p3 & (box p3)) -> (dia p2))))) v (~((box(((p2 -> (box p3)) & (box(p2 -> (box p3)))) -> p3)) v (box((p3 & (box p3)) -> (p2 -> (box p3)))))))) v ((~((box(((dia p3) & (box(dia p3))) -> p4)) v (box((p4 & (box p4)) -> (dia p3))))) v (~((box(((p3 -> (box p4)) & (box(p3 -> (box p4)))) -> p4)) v (box((p4 & (box p4)) -> (p3 -> (box p4)))))))) v ((~((box(((dia p4) & (box(dia p4))) -> p5)) v (box((p5 & (box p5)) -> (dia p4))))) v (~((box(((p4 -> (box p5)) & (box(p4 -> (box p5)))) -> p5)) v (box((p5 & (box p5)) -> (p4 -> (box p5)))))))) v ((~((box(((dia p5) & (box(dia p5))) -> p6)) v (box((p6 & (box p6)) -> (dia p5))))) v (~((box(((p5 -> (box p6)) & (box(p5 -> (box p6)))) -> p6)) v (box((p6 & (box p6)) -> (p5 -> (box p6)))))))) v ((~((box(((dia p6) & (box(dia p6))) -> p7)) v (box((p7 & (box p7)) -> (dia p6))))) v (~((box(((p6 -> (box p7)) & (box(p6 -> (box p7)))) -> p7)) v (box((p7 & (box p7)) -> (p6 -> (box p7)))))))) v ((~((box(((dia p7) & (box(dia p7))) -> p8)) v (box((p8 & (box p8)) -> (dia p7))))) v (~((box(((p7 -> (box p8)) & (box(p7 -> (box p8)))) -> p8)) v (box((p8 & (box p8)) -> (p7 -> (box p8)))))))) v ((~((box(((dia p8) & (box(dia p8))) -> p9)) v (box((p9 & (box p9)) -> (dia p8))))) v (~((box(((p8 -> (box p9)) & (box(p8 -> (box p9)))) -> p9)) v (box((p9 & (box p9)) -> (p8 -> (box p9)))))))) v ((~((box(((dia p9) & (box(dia p9))) -> p10)) v (box((p10 & (box p10)) -> (dia p9))))) v (~((box(((p9 -> (box p10)) & (box(p9 -> (box p10)))) -> p10)) v (box((p10 & (box p10)) -> (p9 -> (box p10)))))))) v ((~((box(((dia p10) & (box(dia p10))) -> p11)) v (box((p11 & (box p11)) -> (dia p10))))) v (~((box(((p10 -> (box p11)) & (box(p10 -> (box p11)))) -> p11)) v (box((p11 & (box p11)) -> (p10 -> (box p11)))))))) v ((~((box(((dia p11) & (box(dia p11))) -> p12)) v (box((p12 & (box p12)) -> (dia p11))))) v (~((box(((p11 -> (box p12)) & (box(p11 -> (box p12)))) -> p12)) v (box((p12 & (box p12)) -> (p11 -> (box p12)))))))) v ((~((box(((dia p12) & (box(dia p12))) -> p13)) v (box((p13 & (box p13)) -> (dia p12))))) v (~((box(((p12 -> (box p13)) & (box(p12 -> (box p13)))) -> p13)) v (box((p13 & (box p13)) -> (p12 -> (box p13)))))))) v ((~((box(((dia p13) & (box(dia p13))) -> p14)) v (box((p14 & (box p14)) -> (dia p13))))) v (~((box(((p13 -> (box p14)) & (box(p13 -> (box p14)))) -> p14)) v (box((p14 & (box p14)) -> (p13 -> (box p14)))))))) v ((~((box(((dia p14) & (box(dia p14))) -> p15)) v (box((p15 & (box p15)) -> (dia p14))))) v (~((box(((p14 -> (box p15)) & (box(p14 -> (box p15)))) -> p15)) v (box((p15 & (box p15)) -> (p14 -> (box p15)))))))) v ((box((box p8) -> p8)) v (box((box p8) -> p8)))) v ((((((((((((((~((box(((dia p16) & (box(dia p16))) -> p17)) v (box((p17 & (box p17)) -> (dia p16))))) v (~((box(((p16 -> (box p17)) & (box(p16 -> (box p17)))) -> p17)) v (box((p17 & (box p17)) -> (p16 -> (box p17))))))) v ((~((box(((dia p17) & (box(dia p17))) -> p18)) v (box((p18 & (box p18)) -> (dia p17))))) v (~((box(((p17 -> (box p18)) & (box(p17 -> (box p18)))) -> p18)) v (box((p18 & (box p18)) -> (p17 -> (box p18)))))))) v ((~((box(((dia p18) & (box(dia p18))) -> p19)) v (box((p19 & (box p19)) -> (dia p18))))) v (~((box(((p18 -> (box p19)) & (box(p18 -> (box p19)))) -> p19)) v (box((p19 & (box p19)) -> (p18 -> (box p19)))))))) v ((~((box(((dia p19) & (box(dia p19))) -> p20)) v (box((p20 & (box p20)) -> (dia p19))))) v (~((box(((p19 -> (box p20)) & (box(p19 -> (box p20)))) -> p20)) v (box((p20 & (box p20)) -> (p19 -> (box p20)))))))) v ((~((box(((dia p20) & (box(dia p20))) -> p21)) v (box((p21 & (box p21)) -> (dia p20))))) v (~((box(((p20 -> (box p21)) & (box(p20 -> (box p21)))) -> p21)) v (box((p21 & (box p21)) -> (p20 -> (box p21)))))))) v ((~((box(((dia p21) & (box(dia p21))) -> p22)) v (box((p22 & (box p22)) -> (dia p21))))) v (~((box(((p21 -> (box p22)) & (box(p21 -> (box p22)))) -> p22)) v (box((p22 & (box p22)) -> (p21 -> (box p22)))))))) v ((~((box(((dia p22) & (box(dia p22))) -> p23)) v (box((p23 & (box p23)) -> (dia p22))))) v (~((box(((p22 -> (box p23)) & (box(p22 -> (box p23)))) -> p23)) v (box((p23 & (box p23)) -> (p22 -> (box p23)))))))) v ((~((box(((dia p23) & (box(dia p23))) -> p24)) v (box((p24 & (box p24)) -> (dia p23))))) v (~((box(((p23 -> (box p24)) & (box(p23 -> (box p24)))) -> p24)) v (box((p24 & (box p24)) -> (p23 -> (box p24)))))))) v ((~((box(((dia p24) & (box(dia p24))) -> p25)) v (box((p25 & (box p25)) -> (dia p24))))) v (~((box(((p24 -> (box p25)) & (box(p24 -> (box p25)))) -> p25)) v (box((p25 & (box p25)) -> (p24 -> (box p25)))))))) v ((~((box(((dia p25) & (box(dia p25))) -> p26)) v (box((p26 & (box p26)) -> (dia p25))))) v (~((box(((p25 -> (box p26)) & (box(p25 -> (box p26)))) -> p26)) v (box((p26 & (box p26)) -> (p25 -> (box p26)))))))) v ((~((box(((dia p26) & (box(dia p26))) -> p27)) v (box((p27 & (box p27)) -> (dia p26))))) v (~((box(((p26 -> (box p27)) & (box(p26 -> (box p27)))) -> p27)) v (box((p27 & (box p27)) -> (p26 -> (box p27)))))))) v ((~((box(((dia p27) & (box(dia p27))) -> p28)) v (box((p28 & (box p28)) -> (dia p27))))) v (~((box(((p27 -> (box p28)) & (box(p27 -> (box p28)))) -> p28)) v (box((p28 & (box p28)) -> (p27 -> (box p28)))))))) v ((~((box(((dia p28) & (box(dia p28))) -> p29)) v (box((p29 & (box p29)) -> (dia p28))))) v (~((box(((p28 -> (box p29)) & (box(p28 -> (box p29)))) -> p29)) v (box((p29 & (box p29)) -> (p28 -> (box p29))))))))"



string = "((~((((box((((p1 & (box p1)) & p1) -> p2) v ((~p1) -> (~((box p2) & p2))))) & (box((box(((p1 & (box p1)) & p1) -> p2)) v ((~p1) -> (~((box p2) & p2)))))) & (box((((p1 & (box p1)) & p1) -> p2) v (box((~p1) -> (~((box p2) & p2))))))) -> ((box(((p1 & (box p1)) & p1) -> p2)) v (box((~p1) -> (~((box p2) & p2))))))) v ((box((p3 & (box p3)) -> p3)) v (box((p3 & (box p3)) -> p3)))) v ((~((((box((((p2 & (box p2)) & p2) -> p3) v ((~p2) -> (~((box p3) & p3))))) & (box((box(((p2 & (box p2)) & p2) -> p3)) v ((~p2) -> (~((box p3) & p3)))))) & (box((((p2 & (box p2)) & p2) -> p3) v (box((~p2) -> (~((box p3) & p3))))))) -> ((box(((p2 & (box p2)) & p2) -> p3)) v (box((~p2) -> (~((box p3) & p3))))))) v (~((((box((((p3 & (box p3)) & p3) -> p4) v ((~p3) -> (~((box p4) & p4))))) & (box((box(((p3 & (box p3)) & p3) -> p4)) v ((~p3) -> (~((box p4) & p4)))))) & (box((((p3 & (box p3)) & p3) -> p4) v (box((~p3) -> (~((box p4) & p4))))))) -> ((box(((p3 & (box p3)) & p3) -> p4)) v (box((~p3) -> (~((box p4) & p4))))))))"



def Main(string):
    string = ConvertFormat(string)
    #print(string)
    string = "-("+string+")"
    sy = shunting_yard(string)
    #print(sy)
    nnf = convertNNFMain(sy)
    #print(nnf)
    nnf = convertAtoms1(nnf)
    #print(nnf)
    clauses = modal_clausification_main(nnf)
    #print(clauses)
    clauses = convertAtoms(clauses)
    #print(clauses)
    clauses = constructModalClause(clauses)
    modal_sat_main(clauses)

Main(string)