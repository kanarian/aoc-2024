import re
inp_test="""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


inp_real=""" (who() what())>when()why()'mul(454,153)mul(565,994)(mul(890,533)#mul(875,768)+'-^where()}when()mul(103,598)[mul(401,600)when()from()how()+mul(928,225)why():mul(909,344)when()'?where():(what()mul(972,219)${/ mul(402,908)who()&where()~where()mul(60,961)#]$mul(459,473))})~mul(143,89),select()mul(772,463)mul(742,92)<(]},select()[%^when()don't()select()from()mul(776,917)+!!why()when(485,399)what(720,754)from()&mul(746,260)where()*who()~&/from()what()]what()mul(694,820)%why(16,195)when()'why() [when()why():do()when(),'<?{who()mul(296,514)%mul(442,333)when()-,why()[!:+from()mul(774,695)}where()*-!%mul(834,493){-&(??mul(240,739)from()@@}@mul(796,837)[;mul(301,618)mul(933,68)+%}/$<mul(879,769)'&('#-mul(314,537);who()where(134,686) where(975,359){how(900,557)mul(134,21)when() !*!$^mul(670,298)*!}:-how(429,820)~]mul(414,322)-select()?what()when()]>#from()(mul(200,440)/]mul(58,834)@<select()mul(966,435)<+;mul(98,983)<;,;how()&'@mul(727,703)!?>!!mul(175,542)mul(363,28)]}don't()+[{<@/,mul(103,154)mul(808,942)$where()why()from()[mul(780,395)^why()#-!:~why()+mul(879,633)<[where()!what()-,mul(6,80)how()?)^select()<}when()]how()mul(385,345)~?don't()<)'mul(557,404)+;/<;}%?//mul(586,270);^&,^}'&:mul(914,485)>,$mul(616,138)'[/-mul(786,357)&why()where(490,893)/-}*}mul(967,485)!'mul(664,982),when()^why()$%(,why()mul(826,970)$*~'),+when()-mul(586,837)+;(/%{[what(201,897)mul(540,583)don't()}mul(358,207)mul(988,94)$#&<?+why()mul(82,18):from()select()!~mul(805,768)&+! how()what()?select())mul(779,277)[>}mul(580,42)#select(190,243){*%*from()mul(491,435)* mul(345,720)+#{)/,'<},mul(529,664)? don't()'mul(925,474)}:!?]mul(655,353)when()'how()(don't()how()^/where())select()select()^~{mul(39,73)['[<^)/!;<mul(367,290)$select()when()^when()>mul(338,323) ~* who()what()where()mul(746,703)mul(70,40);/<select()mul(557,879)*>:!mul(89,464)when()how()~?;~}mul(669,359)+mul(64,989)why()what()where(478,19)^from()$mul(49,43):why()mul(946,368)who()%?{'why()mul(754,618)select()}^mul(925,787)how()select()<^;{}}%mul(857,178)@?$;)%what()['mul(343[<^mul(622,524)$#{&where();@how() #mul(572,8)who(244,369)/*;;mul(22,910)how()?who(200,683)#what()why()mul(9,541)don't() %>mul(583,678)mul(977,618)mul(846,566):@mul(601,58)%mul(12,677)^#[how()?do()&'%how(985,614);@? 'mul(295,467)}@mul(462,179)[from(946,303)@what(236,293),from(572,15)^mul(602,286/*:(select()!mul(950,26){^}]-mul(541,949){/select() from(202,590)what()]select()~mul(931,833)^/}where()*mul(665,272)*'where()>} :]mul(470,26))mul(945,496)%-!;-* mul(958,735)+mul(292,844)where()mul(323,887)select()how()why()%~why(974,789){!/:mul(890,844)&]{'mul(727,812)?mul(521,348)']~,mul(604#what(201,469)]{'how()#[mul(68,187){#+%* when()+when()mul(270,65)select())how();! %where()]@mul(267,348)from()select()who(579,714)where()mul(359,887why()who(120,403)from()&!)do()mul(614,872)select()[:who()'>>?]who()mul(373!:>&mul(13,848)~how()who()+*what()&mul(214,262)/where(941,723)mul(34,526){ }( ~from()){ mul(648,400)mul(946,270)
where()<mul(672,282)&'>,mul(156,431)when(444,909)mul(10,765)#mul(393,855)how()@&from()mul(538,109)[%^-<(how()}how()mul(841,917)~ ]^! ^select()mul(624,87))what()&[-'/&)mul(113+from()how()why()]&>mul(82,319)&:''where()/<;mul(882,75)>/^#/how()!mul(481,243)}*!what()#}#mul(93,825)>'(!where()(&mul(417,293)>[{*()}how(349,243))mul(577,515)}mul(644,588)why()~~what()'why(658,231)]where()mul(260,870)mul(82,64)$+>,&$where()$why()where()mul(513,597),when()why()&mul(559,679/why();~{mul(876,302)/+why(921,489);%@from(){do()&+from()mul(646,666)how() }^;{!?mul?),$*mul(244,591)<)select()(<where()(!mul(708,996)/*@;;:mul(760,261)when(338,104)mul(870,299)!}(mul(269,625) who(553,681)&mul}[#{who()%what(){,when()mul(723,486)-/?{mul(475,745)&%select()%'who()<?:mul(117,765):{>^select()where(454,602)when(){mul(201,421)) ,when()$/$;#;mul(715,512)~-mul(110select())&/;>:^')+mul(525,861)mul(94,520)select();mul(200,362)mul(662,110)what()[';mul(706,110)mul(524,196{ from()%/from()when()select()*mul(952,760)@<@(mul(359,289:?[!:mul(788,331)>(-mul(790,172)~/';(#mul(744,504)}@!#:!)where()mul!why()<+mul(24,595)($/why()&(<mul(872,460%where()[who()mul(962,669):<+-from()]mul(454,164)-,what()@+'mul(10,853)-@@){}what()mul(909,997) ^why()@!/from()$]mul(97,897)?mul(935,220)why()[:*)^) #/mul(301,584)@where()how()mul(609,313)':mul(949from();who())who()who()mul(491,372)!>>'why()}/mul(809,414)mul(202,168)& where(){- ]where()where()<mul(281,296);&mul(625,586)!/{]&+>who()>^mul(543,106){don't():/('why()when()[):#mul(261,544)why()-+mul(325,976)-why()& what()who()%*&;mul(309,586)from()~;mul(527,332)]how()when()mul(266,71)mul(383,68)how()from()}how()[{;who()why()mul(479,649)-who()>mul(954,835))(,'?)why(),mul(73,982)-+mul(275,963)?:*>+%%}%mul(159,868)[{mul(849,590)where()how()when()mul(380,542),'{mul(716,261)@$what()[where(961,898)+#;mul(102,332))mul(151,993)who(433,641)what()!],{<why()#mul(449,110)?from()~how()how()how(425,48)where()~mulwhen()mul(427,877)when()+!<who(),>}mul(225,989)from()$>'/>mul(271,482)(]when(703,790)$['&don't()^ mul(292,747)why();;from()why() #[??mul(675,831)*/<{when()%mul(82,353)?~(~@from()-mul/,when()[+', /why()mul(531,95)')<&#]#!<mul(172,129)mul(543,657-[<,:,:@mul(458,222)mul(640,872)^mul(45,292)!&#+mul(859,346)[:+^$how()(<when()mul(247,266)mul(468,925)&select()^who()~))mul(184,981)from() when()+select()>where()<when()mul(420,131)+-select(379,472)-$from())mul(402,68)what()#mul(278,846)#who()~)?mul(287,731)-- mul(989,728)#$when():mul(470,964why()$ )-?,':from()from()mul(54,842)}mul(581,400),{$select()select()how()mul(531##mul(272,787)['{(don't(),[how()?@where()@-^-mul(55,325)#,][?mul(437,664)+-select()what():/%'mul(569,297))'?/*{mul(40,581)^how()where()!who()#[mul(828,836)$why(819,535)who()#/>$>select()[mul(326,511)/:#::when()(do();mul(960,765$mul(947,618)!from(704,544)-);select()}mul(278,843)&+-&)!}select()why()mul(333,183)!~mul(360,636)}@mul(43,235)& ~*how()~&>$~mul(163,420);@' mul(328,120)&}#)what()~[~!mul(892,685);from())*select()]from(),mul(454,194)!what(598,913)~what()who()*),*who()mul(651,343)~'mul(311,104)~%~how(){when(){mul(348,414)
!who()when(),mul(565,187)'who()mul(573,606)/]<why())mul(29,128)%from()select();]where()'%mul(515,513):'why()/<&#%-mul(54,420)what()mul(253,192)}how()+mul(344,599[$who()#what()@from(850,461)mul(670,417)why()!mul(77,694)who()::+who()(^mul(580,475)(>/?^{do()when(),mul(301,391)select()!]%mul(662,532)why():>mul(317,266)-]/!#?~what(395,165)mul(882,259)(how(){%)from(355,754)from(){?+mul(251,179)+}$^-[mul(244,700), $$mul(989,641)how()&>[{(@when()!mul(17,250)why()mul(516,948)/from()&)](~who(),mul(936,726)from()who()mul(642,108){?/*<mul(421,307) mul(954,385)@-who()-]why()do()mul(152,214)?)what()what() ){select()/mul(88,987)(&;^where(687,768)mul(592,288)>:who()](-)[mul(234,936)//select(){don't()}!mul(711,979)when()why()~( what()%from()^:mul(970,839)who()~$from()how()mul(525,184)(*}from())mul(592,712)select()where()from()do()/!from()@%* /:mul(796,770)[select()mul(737,95)*who()mul(538,295)from()when()mul(202,997)mul(920,622)[^,'^{~&mul(890,310)-#mul##$what()how(),*{]what()'mul(753,51)why()from()%+*-mul(44,560)^/who() how()mul(846,745),$ mul(884,965)?];@;'mul(607,810)]don't()?mul(15,474)*^%where()>,#- mul(381,876)>]'how()[]?when()mul(350,528)&>%%#*;mul(465,783)?/from()'mul(109,659)*'mul(260,549))where(427,3)mul(750,184)mul(514,568)+ <mul(142,867)do(){ mul(197,631)*[~![mul(592,975)>where(838,713) ~$]{what()mul(505,954)<>;-#:mulwhat()[!]why()mul(899,266)%}>select()?]'mul(936,764),~mul(189,689)}^mul(474,190)<;&>]how()/{mul(271,843)>}why(522,791)what()do()#/^where()%when()!mul(284,340)##[why() when()>{mul(998,539)*[*):'>'mul(577,914)[*)who()mul(305,505)who()!@how()'}when()mul(331,543))mul(91,478)(where(196,348)&:]>?mul(560,724)where(872,560)<% what()*where()]select()do()(what()-~mul(229,896){?~when()mul(826,622)&(#mul(451,442))what()mul(866,906)how()$-&where()>-([mul(199,824)!~)$/<:mul(727,123)do()$*-#-@+where()select()$mul(612,415)who()$#,who()>/from()mul(967*who();%@}how()/why()}mul(106,998)how():(;&mul(345,702)mul(275,94)]#>{mul(426,479)why()<;~what()$!+@'mul(40,71)&when()*%mul(973,215),what(),mul(709,788)who()):mul(205,236)~mul(50,81)+how()%~/mul(748,800)(}}mul(124,528)mul(129,959)%[&[select()mul(547,292);who()>???why()+who()mul(442,582):how()>select(92,760);+mul(440,501)@/@>#&:mul(764,753select()%:how()where(202,288) mul(613,367)how()?mulselect(255,7);[;why()/$ mul(351,228){mul(312]+!^#+,why()what(327,951)mul(134,668)&<why(575,717) $-('mul(810,445),mul(731,60)^:mul(695,596)~*^;/mul(570,879)why()where()where() select()what();(from()<mul(11~what()select()how()$-<%mul(335,108)~[)mul(759,937)mul(93,397)when()>&?'!why()where()mul(172,288)+mul(90,27):';*@how()/what()mul(272,960)select(845,387)don't()<select(142,144)how(){}mul(525,125)mul(513,731)from()@,@}why():;:don't()+why()mul(758,764)@,:mul(248,570)/!mul(352,81)what()/?<::what(),}^mul(723,61)'$'^don't()!-from()$**^mul(340,35)where()why(16,588):-mul(895,416)$how()!where()'~{'+,mul@where()<(who():<mul(857,771)}mul(231 when())+mul(494,721)#!/usr/bin/perlmul(361,116)
(^*mul(552,797)mul(235,864)[%@~}~mul(222,585))where()where()/{^#@mul(3,798)what()what()where()why()#how()&mul(607!who()+select()what(315,999)/mul(322,478)'when(),why(885,556)select(747,859)^}how()#mul(994,4)what()</(mul(534,885)who())};from()why()}from()~what()mul(858,35!:why()what()what()mul(716,993)why()>}--}}?)mul(509,779)-)mul(682,498))from()#mul(69,525)%-?>>mul(68,359)/mul(923,989from()~mul(132,353)mul(980,998) (where()}*>&how()[mul(570,289)*~mul(388,859)how(829,278)[<]who();<who()[mul(833,723;mul(208,875)>mul(199,174)*~:[what()^}#who()>mul(221,636)*-()%-when()from()mul&}who()[mul(725,983)>#!who(592,5)%mul(85,978)what()'mul(178,305)[[?:#->#! mul(374,804)<$&{->++mul(446,37)-#&}%)mul(19,914who()(# ;mul(959,330)what()>#who()who();mul(228,273)from()+}/&why(783,754)from()(#mul(649,849)*why(){why()(who()?!why()from()mul(344,447):how()+when(144,750)what()mul(217,542)where())%mul(253,8),$how()%[>#from(),:mul(174,127)-:when()-don't()where()(when()& ]^from()mul(263,164)mul(873,530)::@select()mul(459,547)why()!}$*mul(674,506)<mul(665,313)@mul(310,284)when()how()#;+({@~mul(655,423)(?where(868,382)where()@mul(190,467))-when()~how()mul(71,646)where()how() mul(362,510)>*]~don't()mul(570,150)what()do()<'^)~mul$mul(508,426)/why()mul(155,774)~?from()![mul(670,674)select()?^when()from()]{mul(736,574){>'~^mul(248,37where()@:where(938,730)select()!'>,;mul(827,796):what()%where()!/how(231,307)mul(88,489)@!!mul(173,890)how()[- +what()+$~mul(244,436)(why(),[,-;[<%mul(991,950)%mul(804,561)&:,mul(442,575)}~what(523,563)?+ how()/}[mul(866,343)]:where()where()>$mul(423,440)~>[mul(259,864))@ {^mul(256,238)[:]*$$mul(206,916)*}!what(937,263)select()}don't()'*&mul(630,249),mul(521,101)<where()?where()how()from()select()<when():mul(185,154)$*<(do()]{mul(231,307)$*@* why()select()%'@mul(564,503)@ !@mul(245,476)who()how()$@~select()>/who()!mul(884%/&;^from()mul(846,533);}why()?;mul(538,765)+,([ !}@]{mul(98,545) ~how(703,291)]#)~[[mul(588,167)*-+mul(246,51);+from(){;;what()/:?mul(921,460)<@where()mul(674,502)/)select()%~what()?)mul(406,916)>/mul(501,656)]mul(979,533)/why()*select()where(),^mul(370,549)^~how()why()+,how()@mul(168,884)',<$]mul(377,183)+$<mul(48,619)who(625,236)who()#where()}mul(43,845)why()(?~mul(575,269)&who()why()(!where()-]mul(482,691)where(745,121)from()^/{mul(784,137)@where()(#do():-%]''{mul(901,539)/@who()%<mul(979,206)mul(705,493))>mul(425,602)when()~'>when(),when()%mul(231,25)[why();'!mul(879,941/who()mul(658,479)why()where()*mulwhen()mul(486,551)where()?,)~ what(221,542)/;mul(260*how()~~why()mul(571,395)mul(319,33)where()mul(313,612)select(458,89)when()?from(),)[%^[mul(489,554){mul(482,42)from();mul(911,838)from()what()&/when()when()mul(748,509)/!&who()mul(98,104)what()',how(660,701)^mul(904,678)&}'mul(498,173select()% -from()!when()mul(918,395)?<<@mulhow()/from()][don't()+select()who()what():^^@mul(826,867)select()^[@mul(673,493)select()@(select()mul(152,937),why(955,595)select()where()-'mulwhere()~?mul(572,408)when(606,22){~*(mul(971,805),how(402,696)')}who()&@*who()mul(76,96){where()mul(711,3)*-+~where()mul(812,534[select()!#(how()mul(799,474)>mul(251,649)(from()what();-do()~;]what(),what(393,86)?mul(892,224)who()mul(635,260)mul(300,39)
}>select()>@why(364,672)who():where()mul(385who()))>when()why()&>mul(276,702)&:mul(192,782)/:)@mul(948,155)[!don't())what(),what()mul(747,717)#?$mul(967,489)when()who()why()#mul(961,811)what()mul(307,623)~}from()how(),mul(669,93)^ &select()how()mul(105,129)?])*)mul(246,433):)how()mul(941,140)<[ ;&*mul(580,48);%%'why()what()( %mul(189,229)]'<@)/mul(741,684)[mul(632,558)'@what()what()mul(986,227)<how(584,802)$mul(698)@;+%+;mul(704,986){{how()where()what()from()where()$do()where()why()*-mul(752,877);where()//*?*><?mul(33,338)where()where()[>select()/from()*when()@mul(747,356)mul(674,720)mul(10,513))]#]-mulwhat()select(501,639)mul(114,558)[}$]who()mul(759,134)#who()/@*mul(444,475)!@+don't()#when()}where()[where()',select(){mul(206,80)/<what(230,519)-mul(424,213)>!&how()+]^mul(847,293)+(mul(837,220)/!#!mul(613,470)<mul(93,129)who()from()>#where()from()&$mul(29,370how()]&<where()from(283,113)mul(336,151)select();-from()'why()when()how()(what()mul(467,47){{??mul(513,543);)mul(397,402)mul(428,472)who()~{mul(262,609)how()from(){'  /who()select()mul(778,88)~>/-where()%from())> mul(251,617)-why()~^don't()##~mul(176,935)[;%@?^,don't()!mul(564,493-(&+@'[<*;mul(241,470)<>}mul(684,534):?<do()mul(336,113)>[>?+:mul(835,881)mul(901,992)mul(595,306what()% mul(333,684),what(910,959);^what(),where()'mul(493,314)}-what()&who(231,428)where()>' <mul(754,558)how()+what(734,212)]how()$)^mul(991,39))-'}{mul(459,367);@^-?]?$?mul(32,624)how())mul(741,402)*@]when()mul(559,247)when()don't()((,[}-why(692,780)({{mul(788,419)how() -)mul(710,838)mul(952,75)/!#')[([<mul(547,553)(@<!~]#+who()+mul(597,266)>[where(),]who()mul(215,607)&'mul}select()^%<!mul(523,490);';)(@}>/what()do()&mul(735,766)#%$']*;/+do()~what()how();$#[/select()mul(73,86),who()#who()?*<mul(285,423)'@don't()-!$};where()^%mul(846,592)mul(129,272)[)<when()>[mul(839,173)&$$[why(349,377){why()>why()mul(49,44)@'};!)*;mul(265,467)why()}'mul(561,416)}]-mul(334,113)mul(126,247)}mul(536,247){?mul(780,762)<from()~-] @+$mul(416,370)$mul(617,551)who(647,22){<':}!when()how()mul(541#what())~select()where(257,55)?when(446,792)mul(654,34)mul(30,36)^+'}*mul(835,84};)mul(348,922)who()what(424,481))$(!@^[mul(934,712[>,how()<'who()what()%<?mul(909,44)how()~(do()[<]+[mul(30,114)select()where()[>what()mul(324,650)* ^)mul(116,480)&  %>,mul(722,539)-who()mul(69,643))+select()<'mul(398,585)mul(635,160),!{}mul(218,149))(why()[when(),mul(4,152)@what()*@>@how()mul(78,645)@*#}#select()({mul(196,97)when()@what()+why(287,586)when(){mul(908,484{%-where(){'from()mul(254,416)how()}*(how()#@}mul(670,932)mul(741,232)&'!?@$mul(775,804);),,!mul(757,128)/?'!mul(47,297) $/,,:@~select()?mul(604,497);mul(770,711)+mul?where()/mul(777,175)^>where()<#mul(376,176)~){}mul(758,497)!){%where(), mul(360,122,mul(54,973)):mul(248,44)[where()^mul(162,809))*what()^?+}what()how()why()mul(839,131)mul(913,94) why(),why()'mul(459,43)<-from(),#%{]%/mul(733,345){,/+<[?mul(292,416)& [>/^why(408,559)mul(648,879)#)$ +how()where()#mul(708,178)
how()*[mul(560,727)*when()from(); >~]'&mul(90,393)$~from()mul(578,828)mul(710,50)?+@what()@+!;mul(250,79)when())'mul(523,730)+*}^*mul(698,766)<-why()-/:!/select(),don't(),mul-+[where()$,mul(238,155)}(&<>;[!do()where()(mul(246,69)?from()where()!mul(385,209)who())<(when()!,[;mul(567@<})>mul(214,524)}#%>[mul(429,28) who(){from(664,943)>?mul(747,239)+!!who(75,291)(where()&from()mul(363,660)why()~mul(971,115)when()what()where()']do()/#/;<+)mul(313,612)(why()@<mul(886,716)>[why()#from()where()how()^where(929,904)@do()*from(936,438)[ when()+:mul(772,586]*mul(843,866)<}+[/&^-when()mul(62,918)[mul(602,984)&@~where()how()^when()>'/mul(3,2)<]mul(134,654)<-};mul(456,534)/({ what()do();,*select()]^)mul(528,106)<>mul(157,393)  &where()mul(697,508)mul(793,680)+[<mul(176,69),-}-']how()@+mul(311,266))mul(771,898)from()+why()mul(441,294)$>?%$~~%don't()mul(882,564)mul(954,646)]&%how()mul(322,840)~select()mul(589,361);#!<mul(617,898)/@<when()'mul(118,907),mul(140,382)&@$^select()$when(617,295);do()&$<^&when()+*mul(132,674)^]/(:;}*}/do()@':' mul(900,79)/select())][mul(238,573)-what()how(){)@%$-;mul(266,561)when()@:!'mul(150,805)>#mul(781,972)mul(764,49)*?^}where()mul(698,69)]<&(what()[^<&mul(438,77)?@who()who()when()mul(712,314))^? mul(806,50)]},@(mul(522,258))mul(750,831)^mul(2,167)where()@@what()[)select()mul(480,518); ^&how()%]mul(856,366)select()}when()/]!#?%where()mul(246,951)~why()&%/{^mul(771,634)# {how()when()>+#![mul(489,260)!::?'<how()&>from()mul(527,396)&})mul(557,921)$>[!mul(551,664)>[mul(868,16)}:how()how()^;/mul(641,963) {mul(130,436)>~?<@+]mul(745,360):)[/?]@mul(796,631)where())why()~~mul(191,523)how()mul(902,53)-what()where()who()!from()mul(908,532)who()how():${@#mul(998,383)$,[:;mul(154,723)]]+ &%<],mul(279,823)<when()who()]]don't()<; ]%[what()mul(55,665)$from()from()' mul(412,420),-[where()from()mul(853,815)/from()<*^><mul(379,392)why()>{who()mul(171,633)&^when()<mul(881,444),select()/-<[^@ !mul(547,699)}' when(201,621)mul(147,38)$where() ~how()${do(){<mul(185,208)}[[mul(596,100)what()why()![?don't()%(;mul(827,857)^from(),who())}mul(114,321);^from()&)$^mul(889,568):why()~!*mul(775,388)^where()/mul(90,546)<#}[what()><}'from()mul(408,866)select()#how()?mul(818,40)where():$)when()[&who())mul(203,389){why(717,710)where()$}])~how()mul(608,627))how()where()$-why()/mul(296,533){mul(341,534));$#/<mul(858,725)[where()}:from();when()&mul(703,386)where()from()#^how()&>-^mul(501,854)^^+>what()]how()*:+mul(69,163)*;mul(810,823)-when()/)(mul(825,165)what()>])~@/mul(495,234)?] mul(918,879)]^';%)when()#?mul(656,686)*;<where();mul(461,612) @when()what()[('what()mul(838,164)@}/;~mul(96,648);!{<])~mul(817,690)select()*~select()(why())}mul(7,265)(]mul(459,756)mul(909,698)&-do()$where()%~-~mul(622,257)select()where()*!(mul(764,419)?()*when()}"""

inp = inp_real

def find_active(string):
    res = ""
    is_active = True
    for curIdx, el in enumerate(string):
        if is_active:
            res += el
        if curIdx >= 6 and string[curIdx-6:curIdx+1] == "don't()" and is_active:
            is_active = False
        if curIdx >= 3 and string[curIdx-3:curIdx+1] == "do()" and not is_active:
            is_active = True
    return res

def find_all_mults_in_string(string):
    z = re.findall(pattern=r'mul\((\d+),(\d+)\)',string=string)
    res = 0
    for match in z:
        elOne, elTwo = [int(l) for l in match]
        res +=elOne*elTwo
    return res

res = find_all_mults_in_string(find_active(inp))
print(res)