# minitorch
The full minitorch student suite. 


To access the autograder: 

* Module 0: https://classroom.github.com/a/qDYKZff9
* Module 1: https://classroom.github.com/a/6TiImUiy
* Module 2: https://classroom.github.com/a/0ZHJeTA0
* Module 3: https://classroom.github.com/a/U5CMJec1
* Module 4: https://classroom.github.com/a/04QA6HZK
* Quizzes: https://classroom.github.com/a/bGcGc12k


Train logs for task 1.5 are in log15/
Train logs for 2.5 in log25/

гиперпараметры 1.5: 
для simple и diag
PTS = 50
HIDDEN = 2
RATE = 0.5

для xor и split
PTS = 50
HIDDEN = 10
RATE = 0.5

гиперпараметры 2.5
PTS = 50
HIDDEN = 10
RATE = 0.5


логи 1.5 продублированные:

diag
Epoch  10  loss  25.534176392350652 correct 42
Epoch  20  loss  22.606044708334878 correct 42
Epoch  30  loss  22.152704455534007 correct 42
Epoch  40  loss  22.039870727942382 correct 42
Epoch  50  loss  21.99993456675092 correct 42
Epoch  60  loss  21.97889468829493 correct 42
Epoch  70  loss  21.95815292009097 correct 42
Epoch  80  loss  21.92603585377272 correct 42
Epoch  90  loss  21.868954511119682 correct 42
Epoch  100  loss  21.767460191417797 correct 42
Epoch  110  loss  21.586555798945405 correct 42
Epoch  120  loss  21.2820122734823 correct 42
Epoch  130  loss  20.82764541600949 correct 42
Epoch  140  loss  20.11996996762182 correct 42
Epoch  150  loss  18.672647165753112 correct 42
Epoch  160  loss  16.431097309217282 correct 42
Epoch  170  loss  13.422617664981919 correct 44
Epoch  180  loss  10.767207665561163 correct 47
Epoch  190  loss  8.92656000458443 correct 50
Epoch  200  loss  7.571290099019124 correct 50
Epoch  210  loss  6.564335994264243 correct 50
Epoch  220  loss  5.781077335332728 correct 50
Epoch  230  loss  5.190353962006133 correct 50
Epoch  240  loss  4.712237454384638 correct 50
Epoch  250  loss  4.302885989291579 correct 50
Epoch  260  loss  3.9501187666984796 correct 50
Epoch  270  loss  3.6440437349927532 correct 50
Epoch  280  loss  3.3766764590822604 correct 50
Epoch  290  loss  3.222979434868309 correct 50
Epoch  300  loss  11.914044955622346 correct 45
Epoch  310  loss  5.724460202497918 correct 46
Epoch  320  loss  3.6861733053752945 correct 48
Epoch  330  loss  3.3135066522626335 correct 49
Epoch  340  loss  3.386068091608831 correct 48
Epoch  350  loss  3.8494709840935997 correct 48
Epoch  360  loss  4.178855356168073 correct 48
Epoch  370  loss  3.7869826215214135 correct 48
Epoch  380  loss  3.267075138446192 correct 48
Epoch  390  loss  2.9401884487560155 correct 49
Epoch  400  loss  2.7049727761574656 correct 49
Epoch  410  loss  2.648823184319188 correct 49
Epoch  420  loss  2.8490719479724405 correct 49
Epoch  430  loss  3.593190343690889 correct 48
Epoch  440  loss  4.327129505378512 correct 48
Epoch  450  loss  3.031685685471305 correct 48
Epoch  460  loss  1.8500992413159345 correct 50
Epoch  470  loss  1.570382606174141 correct 50
Epoch  480  loss  1.4819285642864712 correct 50
Epoch  490  loss  1.4175492527690645 correct 50
Epoch  500  loss  1.3597236402614385 correct 50

simple
Epoch  10  loss  30.0391950636679 correct 39
Epoch  20  loss  23.92913960024228 correct 49
Epoch  30  loss  14.647509767159614 correct 50
Epoch  40  loss  9.567749767842988 correct 50
Epoch  50  loss  7.2056447005352595 correct 50
Epoch  60  loss  5.733915334230428 correct 50
Epoch  70  loss  4.714933020907612 correct 50
Epoch  80  loss  3.995299751953838 correct 50
Epoch  90  loss  3.447452214372415 correct 50
Epoch  100  loss  3.0127714005117303 correct 50
Epoch  110  loss  2.6614015101727597 correct 50
Epoch  120  loss  2.372975806186031 correct 50
Epoch  130  loss  2.1330827032611688 correct 50
Epoch  140  loss  1.9312449765425932 correct 50
Epoch  150  loss  1.7597540757774581 correct 50
Epoch  160  loss  1.615959264940184 correct 50
Epoch  170  loss  1.4917454808452875 correct 50
Epoch  180  loss  1.3830117635491073 correct 50
Epoch  190  loss  1.2872124721873226 correct 50
Epoch  200  loss  1.2023136836322095 correct 50
Epoch  210  loss  1.1266721672355875 correct 50
Epoch  220  loss  1.0596420625706204 correct 50
Epoch  230  loss  0.9998666406449611 correct 50
Epoch  240  loss  0.9454798220441624 correct 50
Epoch  250  loss  0.896643505491924 correct 50
Epoch  260  loss  0.85217413692597 correct 50
Epoch  270  loss  0.8115245061875622 correct 50
Epoch  280  loss  0.7742357075873615 correct 50
Epoch  290  loss  0.7399197575750303 correct 50
Epoch  300  loss  0.7082462102957857 correct 50
Epoch  310  loss  0.6789317329146155 correct 50
Epoch  320  loss  0.6517318992138901 correct 50
Epoch  330  loss  0.6264346650148477 correct 50
Epoch  340  loss  0.6028551326052505 correct 50
Epoch  350  loss  0.5808313132336306 correct 50
Epoch  360  loss  0.5602206698491057 correct 50
Epoch  370  loss  0.5408972753343018 correct 50
Epoch  380  loss  0.5227494604051413 correct 50
Epoch  390  loss  0.5056778541943224 correct 50
Epoch  400  loss  0.48959374211302215 correct 50
Epoch  410  loss  0.4744176818764923 correct 50
Epoch  420  loss  0.46007833098694834 correct 50
Epoch  430  loss  0.44651144849617674 correct 50
Epoch  440  loss  0.43365904124706905 correct 50
Epoch  450  loss  0.4214686305472791 correct 50
Epoch  460  loss  0.40989261974886876 correct 50
Epoch  470  loss  0.3988877467845775 correct 50
Epoch  480  loss  0.38841460855898247 correct 50
Epoch  490  loss  0.3784372463752874 correct 50
Epoch  500  loss  0.36892278341797013 correct 50

split
Epoch  10  loss  32.6031643093961 correct 36
Epoch  20  loss  31.36009019462977 correct 33
Epoch  30  loss  30.08250483388527 correct 34
Epoch  40  loss  28.461717404586494 correct 35
Epoch  50  loss  26.33040213343514 correct 37
Epoch  60  loss  23.40026844036007 correct 41
Epoch  70  loss  36.098895765595316 correct 28
Epoch  80  loss  20.004189244808195 correct 44
Epoch  90  loss  17.596797053733265 correct 46
Epoch  100  loss  16.541065615462486 correct 46
Epoch  110  loss  16.551756689040783 correct 44
Epoch  120  loss  20.62207533256935 correct 40
Epoch  130  loss  24.763413740540546 correct 39
Epoch  140  loss  9.767028589050916 correct 47
Epoch  150  loss  9.716745482281794 correct 47
Epoch  160  loss  7.661249234318119 correct 48
Epoch  170  loss  9.133935502468546 correct 47
Epoch  180  loss  11.65070264905027 correct 46
Epoch  190  loss  6.435112321868543 correct 48
Epoch  200  loss  13.696080410518864 correct 44
Epoch  210  loss  5.313838781791457 correct 49
Epoch  220  loss  4.9164680063637505 correct 49
Epoch  230  loss  15.305220788957866 correct 42
Epoch  240  loss  8.410683069435715 correct 48
Epoch  250  loss  8.13509196662559 correct 48
Epoch  260  loss  7.370317544413031 correct 48
Epoch  270  loss  7.065653778677752 correct 48
Epoch  280  loss  4.551180039921821 correct 49
Epoch  290  loss  5.116056976926082 correct 48
Epoch  300  loss  5.392467718857985 correct 48
Epoch  310  loss  4.715833447844177 correct 49
Epoch  320  loss  4.867711850169128 correct 49
Epoch  330  loss  4.617774646808252 correct 49
Epoch  340  loss  4.882000354410335 correct 49
Epoch  350  loss  4.8516242108621235 correct 48
Epoch  360  loss  4.172583591040391 correct 49
Epoch  370  loss  4.127745647110219 correct 49
Epoch  380  loss  3.8514590815383314 correct 49
Epoch  390  loss  3.589057726985982 correct 49
Epoch  400  loss  8.383864942639985 correct 48
Epoch  410  loss  4.490028281116175 correct 49
Epoch  420  loss  4.3630175133768265 correct 49
Epoch  430  loss  4.286981584286839 correct 47
Epoch  440  loss  4.628156122093703 correct 48
Epoch  450  loss  6.3691199825067955 correct 48
Epoch  460  loss  4.665835275009212 correct 48
Epoch  470  loss  3.1797232987239186 correct 49
Epoch  480  loss  4.725477184602697 correct 48
Epoch  490  loss  2.577175471050406 correct 49
Epoch  500  loss  3.9809087386089925 correct 49

xor
Epoch  10  loss  31.402881488369225 correct 32
Epoch  20  loss  29.55598618651551 correct 32
Epoch  30  loss  26.560511237866113 correct 35
Epoch  40  loss  27.597992803130534 correct 32
Epoch  50  loss  24.690275611771437 correct 35
Epoch  60  loss  23.097476100036527 correct 36
Epoch  70  loss  20.53310223182056 correct 39
Epoch  80  loss  18.703931194096274 correct 40
Epoch  90  loss  17.48716484822759 correct 41
Epoch  100  loss  15.576550409047304 correct 43
Epoch  110  loss  13.064871500465859 correct 45
Epoch  120  loss  10.84015152170589 correct 47
Epoch  130  loss  8.37282093399071 correct 48
Epoch  140  loss  7.173875994900698 correct 48
Epoch  150  loss  6.667534157240758 correct 48
Epoch  160  loss  7.359329765959098 correct 48
Epoch  170  loss  4.503527623325375 correct 48
Epoch  180  loss  3.505101746543201 correct 49
Epoch  190  loss  3.7052053484217757 correct 49
Epoch  200  loss  4.255293587398742 correct 48
Epoch  210  loss  4.033233789009514 correct 48
Epoch  220  loss  3.340540202147739 correct 49
Epoch  230  loss  2.714944234223705 correct 49
Epoch  240  loss  2.460067924085896 correct 49
Epoch  250  loss  2.4082538752418716 correct 49
Epoch  260  loss  2.583949494004259 correct 49
Epoch  270  loss  2.4620000438531027 correct 49
Epoch  280  loss  1.6807312596564075 correct 49
Epoch  290  loss  1.2982069026416196 correct 50
Epoch  300  loss  1.1299092486486144 correct 50
Epoch  310  loss  1.0093775048685125 correct 50
Epoch  320  loss  0.9156017593765516 correct 50
Epoch  330  loss  0.8528690572627761 correct 50
Epoch  340  loss  0.8057776036147177 correct 50
Epoch  350  loss  0.765675947870125 correct 50
Epoch  360  loss  0.7300758257276994 correct 50
Epoch  370  loss  0.697692620536857 correct 50
Epoch  380  loss  0.6678895237861824 correct 50
Epoch  390  loss  0.6402086116589343 correct 50
Epoch  400  loss  0.614657568113102 correct 50
Epoch  410  loss  0.5907547047049477 correct 50
Epoch  420  loss  0.5683664704836929 correct 50
Epoch  430  loss  0.5473491692189212 correct 50
Epoch  440  loss  0.5276950655473736 correct 50
Epoch  450  loss  0.5094684686344713 correct 50
Epoch  460  loss  0.49194440412813484 correct 50
Epoch  470  loss  0.4756221284317283 correct 50
Epoch  480  loss  0.4603448286779101 correct 50
Epoch  490  loss  0.44567885937373053 correct 50
Epoch  500  loss  0.4318645590694483 correct 50


логи 2.5 продублированные:

diag
Epoch  10  loss  15.983030800701444 correct 44
Epoch  20  loss  14.013617100828863 correct 44
Epoch  30  loss  12.275805823805035 correct 44
Epoch  40  loss  10.492241926730864 correct 44
Epoch  50  loss  8.589800870117775 correct 45
Epoch  60  loss  6.848124931398279 correct 47
Epoch  70  loss  5.484606272948501 correct 48
Epoch  80  loss  4.501924743601471 correct 48
Epoch  90  loss  3.784814254855893 correct 49
Epoch  100  loss  3.297966002565254 correct 49
Epoch  110  loss  2.95777417286198 correct 50
Epoch  120  loss  2.6799580373769967 correct 50
Epoch  130  loss  2.4366874257431244 correct 50
Epoch  140  loss  2.2483172600875694 correct 50
Epoch  150  loss  2.0823452581119244 correct 50
Epoch  160  loss  1.9314989322090659 correct 50
Epoch  170  loss  1.797184218200572 correct 50
Epoch  180  loss  1.6746137447024176 correct 50
Epoch  190  loss  1.56419196907827 correct 50
Epoch  200  loss  1.4609596476229558 correct 50
Epoch  210  loss  1.3660236204084821 correct 50
Epoch  220  loss  1.279849877506566 correct 50
Epoch  230  loss  1.1993681412838533 correct 50
Epoch  240  loss  1.1257870227018028 correct 50
Epoch  250  loss  1.058871697766949 correct 50
Epoch  260  loss  0.9972236560743243 correct 50
Epoch  270  loss  0.9434611612901512 correct 50
Epoch  280  loss  0.8888956007240979 correct 50
Epoch  290  loss  0.8415884673572518 correct 50
Epoch  300  loss  0.7938048005104021 correct 50
Epoch  310  loss  0.7530360808543877 correct 50
Epoch  320  loss  0.7117584585773111 correct 50
Epoch  330  loss  0.6768848676209882 correct 50
Epoch  340  loss  0.6436957431585657 correct 50
Epoch  350  loss  0.6115229406830881 correct 50
Epoch  360  loss  0.5830506371455945 correct 50
Epoch  370  loss  0.5577289862820113 correct 50
Epoch  380  loss  0.5327674733812271 correct 50
Epoch  390  loss  0.5089112684591518 correct 50
Epoch  400  loss  0.4869530687061434 correct 50
Epoch  410  loss  0.4662124512346522 correct 50
Epoch  420  loss  0.4467939128236961 correct 50
Epoch  430  loss  0.4272493648193898 correct 50
Epoch  440  loss  0.4100812654308742 correct 50
Epoch  450  loss  0.39370089437485917 correct 50
Epoch  460  loss  0.3757695099897105 correct 50
Epoch  470  loss  0.36005482824069507 correct 50
Epoch  480  loss  0.34530283932458106 correct 50
Epoch  490  loss  0.33198639609924796 correct 50
Epoch  500  loss  0.3195237075553988 correct 50

simple
Epoch  10  loss  14.826750657159556 correct 50
Epoch  20  loss  5.53623410182388 correct 50
Epoch  30  loss  2.7893424601725325 correct 50
Epoch  40  loss  1.7900087795176893 correct 50
Epoch  50  loss  1.3044785610341678 correct 50
Epoch  60  loss  1.016302310017661 correct 50
Epoch  70  loss  0.8252268273199755 correct 50
Epoch  80  loss  0.6901556700821991 correct 50
Epoch  90  loss  0.5901739483009483 correct 50
Epoch  100  loss  0.512961145740794 correct 50
Epoch  110  loss  0.4516069859813812 correct 50
Epoch  120  loss  0.40223304800234316 correct 50
Epoch  130  loss  0.3616299556282009 correct 50
Epoch  140  loss  0.3277712040866202 correct 50
Epoch  150  loss  0.2992129874676197 correct 50
Epoch  160  loss  0.274736221912216 correct 50
Epoch  170  loss  0.253766398737864 correct 50
Epoch  180  loss  0.23557202203107105 correct 50
Epoch  190  loss  0.2195696069276598 correct 50
Epoch  200  loss  0.2054748793709349 correct 50
Epoch  210  loss  0.19292309202715538 correct 50
Epoch  220  loss  0.18166124984567267 correct 50
Epoch  230  loss  0.17152302434542538 correct 50
Epoch  240  loss  0.162338455114947 correct 50
Epoch  250  loss  0.1539925163185508 correct 50
Epoch  260  loss  0.1464039562150728 correct 50
Epoch  270  loss  0.13944911387291983 correct 50
Epoch  280  loss  0.13305373031910536 correct 50
Epoch  290  loss  0.12715555018917707 correct 50
Epoch  300  loss  0.12170107415282744 correct 50
Epoch  310  loss  0.11664408001646777 correct 50
Epoch  320  loss  0.11194440170573666 correct 50
Epoch  330  loss  0.10756702626388964 correct 50
Epoch  340  loss  0.10348128172294843 correct 50
Epoch  350  loss  0.09966019100164614 correct 50
Epoch  360  loss  0.09611879588161185 correct 50
Epoch  370  loss  0.09280204000595631 correct 50
Epoch  380  loss  0.08967450406512402 correct 50
Epoch  390  loss  0.08672903756520031 correct 50
Epoch  400  loss  0.08395082272758288 correct 50
Epoch  410  loss  0.0813265374339665 correct 50
Epoch  420  loss  0.0788453303067533 correct 50
Epoch  430  loss  0.0764953938251212 correct 50
Epoch  440  loss  0.07426680830568992 correct 50
Epoch  450  loss  0.07215081273010107 correct 50
Epoch  460  loss  0.07013945826902315 correct 50
Epoch  470  loss  0.06822517386299182 correct 50
Epoch  480  loss  0.06640168435904407 correct 50
Epoch  490  loss  0.06466294958006323 correct 50
Epoch  500  loss  0.06300344075194786 correct 50

split
Epoch  10  loss  32.60316430939611 correct 36
Epoch  20  loss  31.36009019462977 correct 33
Epoch  30  loss  30.08250483388527 correct 34
Epoch  40  loss  28.461717404586498 correct 35
Epoch  50  loss  26.33040213343514 correct 37
Epoch  60  loss  23.400268440360076 correct 41
Epoch  70  loss  36.098895765595344 correct 28
Epoch  80  loss  20.00418924480819 correct 44
Epoch  90  loss  17.59679705373326 correct 46
Epoch  100  loss  16.54106561546249 correct 46
Epoch  110  loss  16.551756689040793 correct 44
Epoch  120  loss  20.622075332569356 correct 40
Epoch  130  loss  24.763413740540337 correct 39
Epoch  140  loss  9.767028589050922 correct 47
Epoch  150  loss  9.716745482281812 correct 47
Epoch  160  loss  7.66124923431809 correct 48
Epoch  170  loss  9.133935502468358 correct 47
Epoch  180  loss  11.650702649052041 correct 46
Epoch  190  loss  6.435112321868815 correct 48
Epoch  200  loss  13.696080410509241 correct 44
Epoch  210  loss  5.313838781790786 correct 49
Epoch  220  loss  4.9164680063625354 correct 49
Epoch  230  loss  15.305220788930555 correct 42
Epoch  240  loss  8.410683069471196 correct 48
Epoch  250  loss  8.135091966625868 correct 48
Epoch  260  loss  7.370317544411072 correct 48
Epoch  270  loss  7.065653778681902 correct 48
Epoch  280  loss  4.55118003992203 correct 49
Epoch  290  loss  5.116056976926876 correct 48
Epoch  300  loss  5.392467718858161 correct 48
Epoch  310  loss  4.7158334478445765 correct 49
Epoch  320  loss  4.8677118501694405 correct 49
Epoch  330  loss  4.6177746468085825 correct 49
Epoch  340  loss  4.882000354410512 correct 49
Epoch  350  loss  4.851624210862477 correct 48
Epoch  360  loss  4.172583591040511 correct 49
Epoch  370  loss  4.127745647110494 correct 49
Epoch  380  loss  3.851459081538817 correct 49
Epoch  390  loss  3.589057726986153 correct 49
Epoch  400  loss  8.383864942638716 correct 48
Epoch  410  loss  4.490028281116321 correct 49
Epoch  420  loss  4.363017513376727 correct 49
Epoch  430  loss  4.286981584286643 correct 47
Epoch  440  loss  4.628156122093835 correct 48
Epoch  450  loss  6.369119982507121 correct 48
Epoch  460  loss  4.66583527500939 correct 48
Epoch  470  loss  3.1797232987238884 correct 49
Epoch  480  loss  4.725477184603024 correct 48
Epoch  490  loss  2.5771754710505155 correct 49
Epoch  500  loss  3.98090873860902 correct 49

xor
Epoch  10  loss  31.402881488369218 correct 32
Epoch  20  loss  29.55598618651551 correct 32
Epoch  30  loss  26.560511237866116 correct 35
Epoch  40  loss  27.597992803130552 correct 32
Epoch  50  loss  24.690275611771437 correct 35
Epoch  60  loss  23.097476100036523 correct 36
Epoch  70  loss  20.53310223182056 correct 39
Epoch  80  loss  18.703931194096278 correct 40
Epoch  90  loss  17.48716484822761 correct 41
Epoch  100  loss  15.5765504090473 correct 43
Epoch  110  loss  13.064871500465868 correct 45
Epoch  120  loss  10.840151521705883 correct 47
Epoch  130  loss  8.372820933990733 correct 48
Epoch  140  loss  7.173875994900704 correct 48
Epoch  150  loss  6.667534157240734 correct 48
Epoch  160  loss  7.359329765959092 correct 48
Epoch  170  loss  4.503527623325394 correct 48
Epoch  180  loss  3.5051017465432084 correct 49
Epoch  190  loss  3.705205348421783 correct 49
Epoch  200  loss  4.2552935873987465 correct 48
Epoch  210  loss  4.033233789009503 correct 48
Epoch  220  loss  3.340540202147723 correct 49
Epoch  230  loss  2.714944234223711 correct 49
Epoch  240  loss  2.460067924085884 correct 49
Epoch  250  loss  2.4082538752418627 correct 49
Epoch  260  loss  2.583949494004206 correct 49
Epoch  270  loss  2.46200004385309 correct 49
Epoch  280  loss  1.680731259656428 correct 49
Epoch  290  loss  1.29820690264164 correct 50
Epoch  300  loss  1.1299092486486388 correct 50
Epoch  310  loss  1.0093775048685274 correct 50
Epoch  320  loss  0.9156017593765576 correct 50
Epoch  330  loss  0.852869057262779 correct 50
Epoch  340  loss  0.8057776036147182 correct 50
Epoch  350  loss  0.7656759478701247 correct 50
Epoch  360  loss  0.7300758257277006 correct 50
Epoch  370  loss  0.6976926205368563 correct 50
Epoch  380  loss  0.6678895237861827 correct 50
Epoch  390  loss  0.6402086116589344 correct 50
Epoch  400  loss  0.6146575681131031 correct 50
Epoch  410  loss  0.590754704704949 correct 50
Epoch  420  loss  0.5683664704836945 correct 50
Epoch  430  loss  0.5473491692189212 correct 50
Epoch  440  loss  0.5276950655473733 correct 50
Epoch  450  loss  0.5094684686344711 correct 50
Epoch  460  loss  0.49194440412813417 correct 50
Epoch  470  loss  0.4756221284317288 correct 50
Epoch  480  loss  0.4603448286779099 correct 50
Epoch  490  loss  0.44567885937373164 correct 50
Epoch  500  loss  0.4318645590694479 correct 50


