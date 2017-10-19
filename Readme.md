# Kraken Report Parsers

Various parsing scripts for Kraken reports.

Kraken reports have the following format:

```
 15.81	120098	120098	U	0	unclassified
 84.19	639475	1261	-	1	root
 82.61	627500	0	-	131567	  cellular organisms
 82.61	627500	879	D	2	    Bacteria
 82.47	626383	222	P	1239	      Firmicutes
 82.43	626137	91	C	186801	        Clostridia
 82.42	626045	578	O	186802	          Clostridiales
 82.34	625426	3	F	186804	            Peptostreptococcaceae
 82.34	625423	460	G	1481960	              Peptoclostridium
 82.28	624962	396258	S	1496	                Peptoclostridium difficile
 29.00	220297	220297	-	272563	                  Peptoclostridium difficile 630
  1.09	8317	8317	-	699034	                  Peptoclostridium difficile BI1
  0.01	65	65	-	645462	                  Peptoclostridium difficile CD196
  0.00	25	25	-	645463	                  Peptoclostridium difficile R20291
  0.00	1	1	S	1511	                [Clostridium] sticklandii
  0.00	35	0	F	31979	            Clostridiaceae
  0.00	34	9	G	1485	              Clostridium
  0.00	24	24	S	1502	                Clostridium perfringens
  0.00	1	0	S	1491	                Clostridium botulinum
  0.00	1	0	-	36826	                  Clostridium botulinum A
  0.00	1	1	-	441771	                    Clostridium botulinum A str. Hall
  0.00	1	0	G	114627	              Alkaliphilus
  0.00	1	0	S	208226	                Alkaliphilus metalliredigens
  0.00	1	1	-	293826	                  Alkaliphilus metalliredigens QYMF
  0.00	3	1	F	186807	            Peptococcaceae
  0.00	2	0	G	79206	              Desulfosporosinus
  0.00	2	0	S	79209	                Desulfosporosinus meridiei
  0.00	2	2	-	768704	                  Desulfosporosinus meridiei DSM 13257
  0.00	2	0	-	186813	            unclassified Clostridiales
  0.00	2	0	-	39779	              unclassified Clostridiales (miscellaneous)
  0.00	2	2	S	245018	                butyrate-producing bacterium SSC/2
  0.00	1	0	F	541000	            Ruminococcaceae
  0.00	1	0	G	1508657	              Ruminiclostridium
  0.00	1	1	S	1515	                Ruminiclostridium thermocellum
  0.00	1	0	O	485256	          Natranaerobiales
  0.00	1	0	F	485255	            Natranaerobiaceae
  0.00	1	0	G	375928	              Natranaerobius
  0.00	1	0	S	375929	                Natranaerobius thermophilus
  0.00	1	1	-	457570	                  Natranaerobius thermophilus JW/NM-WN-LF
  0.00	24	6	C	91061	        Bacilli
  0.00	17	0	O	1385	          Bacillales
  0.00	10	0	F	186817	            Bacillaceae
  0.00	8	0	G	1386	              Bacillus
  0.00	6	3	-	86661	                Bacillus cereus group
  0.00	2	1	S	1396	                  Bacillus cereus
  0.00	1	1	-	405532	                    Bacillus cereus B4264
  0.00	1	0	S	1428	                  Bacillus thuringiensis
  0.00	1	1	-	1195464	                    Bacillus thuringiensis MC28
  0.00	2	0	-	653685	                Bacillus subtilis group
  0.00	1	0	S	1390	                  Bacillus amyloliquefaciens
  0.00	1	1	-	1091041	                    Bacillus amyloliquefaciens IT-45
  0.00	1	0	S	1423	                  Bacillus subtilis
  0.00	1	1	-	936156	                    Bacillus subtilis BSn5
  ```