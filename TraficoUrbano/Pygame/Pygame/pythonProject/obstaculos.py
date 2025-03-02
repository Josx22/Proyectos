#COLLISIONS

#COLLISIONS LEVEL 1
def casa_colisión(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 492 <= jugador_pos_mundo_x <= 494 and 80 <= jugador_pos_mundo_y <= 172:
        distancia_x -= 5
    if 482 <= jugador_pos_mundo_x <= 576 and 180 <= jugador_pos_mundo_y <= 182:
        distancia_y += 5
    if 572 <= jugador_pos_mundo_x <= 574 and 80 <= jugador_pos_mundo_y <= 172:
        distancia_x += 5
    if 488 <= jugador_pos_mundo_x <= 580 and 85 <= jugador_pos_mundo_y <= 87:
        distancia_y -=5


    return distancia_x, distancia_y
def casa_grande_colision(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 52 <= jugador_pos_mundo_x <= 320 and 232 <= jugador_pos_mundo_y <= 234:
        distancia_y +=5
    if 340 <= jugador_pos_mundo_x <= 342 and -30 <= jugador_pos_mundo_y <= 234:
        distancia_x +=5

    return distancia_x, distancia_y
def lago_limite1(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 344 <= jugador_pos_mundo_x <= 1450 and -6 <= jugador_pos_mundo_y <= -4:
        distancia_y +=5
    if 642 <= jugador_pos_mundo_x <= 644 and 0 <= jugador_pos_mundo_y <= 396:
        distancia_x -=5
    if 550 <= jugador_pos_mundo_x <= 638 and 395 <= jugador_pos_mundo_y <= 397:
        distancia_y -=5
    if 542 <= jugador_pos_mundo_x <= 544 and 387 <= jugador_pos_mundo_y <= 443:
        distancia_x -=5
    if 266 <= jugador_pos_mundo_x <= 546 and 459 <= jugador_pos_mundo_y <= 560:
        distancia_y -=5
    if 61 <= jugador_pos_mundo_x <= 63 and 240 <= jugador_pos_mundo_y <= 440:
        distancia_x +=5
    if 49 <= jugador_pos_mundo_x <= 169 and 412 <= jugador_pos_mundo_y <= 414:
        distancia_y -=5
    if 257 <= jugador_pos_mundo_x <= 369 and 416 <= jugador_pos_mundo_y <= 418:
        distancia_y -=5
    if 361 <= jugador_pos_mundo_x <= 363 and 408 <= jugador_pos_mundo_y <= 454:
        distancia_x +=5

    return distancia_x, distancia_y
def lago_limite2(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 264 <= jugador_pos_mundo_x <= 524 and 596 <= jugador_pos_mundo_y <= 598:
        distancia_y +=5
    if 96 <= jugador_pos_mundo_x <=160 and 596 <= jugador_pos_mundo_y <= 598:
        distancia_y +=5
    if 90 <= jugador_pos_mundo_x <= 92 and 594 <= jugador_pos_mundo_y <= 794:
        distancia_x +=5
    if 93 <= jugador_pos_mundo_x <= 133 and 796 <= jugador_pos_mundo_y <= 798:
        distancia_y -=5
    if 140 <= jugador_pos_mundo_x <= 1128 and 842 <= jugador_pos_mundo_y <= 844:
        distancia_y -=5
    if 589 <= jugador_pos_mundo_x <= 590 and 794 <= jugador_pos_mundo_y <= 838:
        distancia_x -=5
    if 581 <= jugador_pos_mundo_x <= 737 and 798 <= jugador_pos_mundo_y <= 800:
        distancia_y -=5
    if 733 <= jugador_pos_mundo_x <= 735 and 752 <= jugador_pos_mundo_y <= 792:
        distancia_x -=5
    if 734 <= jugador_pos_mundo_x <= 736 and 592 <= jugador_pos_mundo_y <= 676:
        distancia_x -=5
    if 639 <= jugador_pos_mundo_x <= 741 and 593 <= jugador_pos_mundo_y <= 595:
        distancia_y +=5
    if 685 <= jugador_pos_mundo_x <= 687 and 536 <= jugador_pos_mundo_y <= 588:
        distancia_x -=5
    if 525 <= jugador_pos_mundo_x <= 685 and 542 <= jugador_pos_mundo_y <= 544:
        distancia_y +=5
    if 536 <= jugador_pos_mundo_x <= 538 and 540 <= jugador_pos_mundo_y <= 590:
        distancia_x +=5

    return distancia_x, distancia_y

def lago_limite3(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 1038 <= jugador_pos_mundo_x <= 1040 and 757 <= jugador_pos_mundo_y <= 841:
        distancia_x +=5
    if 1138 <= jugador_pos_mundo_x <= 1386 and 889 <= jugador_pos_mundo_y <= 891:
        distancia_y -=5
    if 1390 <= jugador_pos_mundo_x <= 1392 and 797 <= jugador_pos_mundo_y <= 893:
        distancia_x -=5
    if 1382 <= jugador_pos_mundo_x <= 1450 and 789 <= jugador_pos_mundo_y <= 791:
        distancia_y -=5
    if 1434 <= jugador_pos_mundo_x <= 1436 and 549 <= jugador_pos_mundo_y <= 641:
        distancia_x -=5
    if 1346 <= jugador_pos_mundo_x <= 1448 and 545 <= jugador_pos_mundo_y <= 547:
        distancia_y +=5
    if 1142 <= jugador_pos_mundo_x <= 1270 and 545 <= jugador_pos_mundo_y <= 547:
        distancia_y +=5
    if 1134 <= jugador_pos_mundo_x <= 1136 and 549 <= jugador_pos_mundo_y <= 593:
        distancia_x +=5
    if 1030 <= jugador_pos_mundo_x <= 1032 and 589 <= jugador_pos_mundo_y <= 673:
        distancia_x +=5

    return distancia_x, distancia_y
def lago_limite4(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 1353 <= jugador_pos_mundo_x <= 1450 and 388 <= jugador_pos_mundo_y <= 390:
        distancia_y -=5
    if 1226 <= jugador_pos_mundo_x <= 1270 and 388 <= jugador_pos_mundo_y <= 390:
        distancia_y -=5
    if 1238 <= jugador_pos_mundo_x <= 1240 and 344 <= jugador_pos_mundo_y <= 420:
        distancia_x +=5
    if 1134 <= jugador_pos_mundo_x <= 1136 and 296 <= jugador_pos_mundo_y <= 360:
        distancia_x +=5
    if 1034 <= jugador_pos_mundo_x <= 1134 and 292 <= jugador_pos_mundo_y <= 294:
        distancia_y -=5
    if 1035 <= jugador_pos_mundo_x <= 1037 and 4 <= jugador_pos_mundo_y <= 304:
        distancia_x +=5
    if 1338 <= jugador_pos_mundo_x <= 1040 and 346 <= jugador_pos_mundo_y <= 402:
        distancia_x -=5
    if 1338 <= distancia_x <= 1450 and 345 <= jugador_pos_mundo_y <= 347:
        distancia_y -=5

    return distancia_x, distancia_y
def arbol1(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 536 <= jugador_pos_mundo_x <= 538 and 249 <= jugador_pos_mundo_y <= 325:
        distancia_x =0
    if 540 <= jugador_pos_mundo_x <= 576 and 330 <= jugador_pos_mundo_y <= 332:
        distancia_y =0
    if 584 <= jugador_pos_mundo_x <= 586 and 236 <= jugador_pos_mundo_y <= 332:
        distancia_x =0
    if 540 <= jugador_pos_mundo_x <= 576 and 226 <= jugador_pos_mundo_y <= 228:
        distancia_y =0

    return distancia_x, distancia_y
def arbol2(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 1192 <= jugador_pos_mundo_x <= 1194 and 198 <= jugador_pos_mundo_y <=274:
        distancia_x -=5
    if 1230 <= jugador_pos_mundo_y <= 1232 and 196 <= jugador_pos_mundo_y <= 276:
        distancia_x +=5
    if 1190 <= jugador_pos_mundo_x <= 1222 and 275 <= jugador_pos_mundo_y <= 277:
        distancia_y +=5
    if  1190 <= jugador_pos_mundo_x <= 1222 and 184 <= jugador_pos_mundo_y <= 186:
        distancia_y -=5
    return distancia_x, distancia_y
def fuente(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 1090 <= jugador_pos_mundo_x <= 1090 and 6 <= jugador_pos_mundo_y <= 76:
        distancia_x -=5
    if 1094 <= jugador_pos_mundo_x <= 1226 and 70 <= jugador_pos_mundo_y <= 72:
        distancia_y +=5
    if 1226 <= jugador_pos_mundo_x <= 1228 and 2 <= jugador_pos_mundo_y <= 70:
        distancia_x +=5
    return distancia_x, distancia_y
def puente1(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 174 <= jugador_pos_mundo_x <= 176 and 430 <= jugador_pos_mundo_y <= 590:
        distancia_x +=5
    if 236 <= jugador_pos_mundo_x  <= 238 and 434 <= jugador_pos_mundo_y <= 582:
        distancia_x -=5
    return distancia_x, distancia_y
def puente2(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 740 <= jugador_pos_mundo_x <= 1032 and 678 <= jugador_pos_mundo_y <= 680:
        distancia_y +=5
    if 740 <= jugador_pos_mundo_x <= 1032 and 742 <= jugador_pos_mundo_y <= 744:
        distancia_y -=5
    return distancia_x, distancia_y
def puente3(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y):
    if 1278 <= jugador_pos_mundo_x <= 1280 and 383 <= jugador_pos_mundo_y <= 539:
        distancia_x +=5
    if 1342 <= jugador_pos_mundo_x <= 1344 and 383 <= jugador_pos_mundo_y <= 539:
        distancia_x -=5
    return distancia_x, distancia_y

#COLLISIONS LEVEL 2
def paredes_colision(jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y, nivel):

    if 26 <= jugador_pos_mundo_x <= 1450 and 890 <= jugador_pos_mundo_y <= 892:
        distancia_y -= 5
    if 1346 <= jugador_pos_mundo_x <= 1450 and 290 <= jugador_pos_mundo_y <= 292:
        distancia_y += 5
    if 1342 <= jugador_pos_mundo_x <= 1344 and 72 <= jugador_pos_mundo_y <= 280:
        distancia_x -= 5
    if 1770 <= jugador_pos_mundo_x <= 1172 and 54 <= jugador_pos_mundo_y <= 286:
        distancia_x += 5
    if 1050 <= jugador_pos_mundo_x <= 117 and 284 <= jugador_pos_mundo_y <= 286:
        distancia_y += 5
    if 1042 <= jugador_pos_mundo_x <= 1044 and -30 <= jugador_pos_mundo_y <= 286:
        distancia_x -= 5
    if 1048 <= jugador_pos_mundo_x <= 1168 and 282 <= jugador_pos_mundo_y <= 284:
        distancia_y +=5
    return distancia_x, distancia_y
def lago_nivel_2 (jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y, nivel):
    if 240 <= jugador_pos_mundo_x <= 242 and 328 <= jugador_pos_mundo_y <= 472:
        distancia_x -=5
    if  240 <= jugador_pos_mundo_x <= 242 and 552 <= jugador_pos_mundo_y <= 712:
        distancia_x -=5
    if 55 <= jugador_pos_mundo_x <= 459 and 712 <= jugador_pos_mundo_y <= 714:
        distancia_y -=5
    if 552 <= jugador_pos_mundo_x <= 554 and 332 <= jugador_pos_mundo_y <= 480:
        distancia_x +=5
    if 553 <= jugador_pos_mundo_x <= 555 and 556 <= jugador_pos_mundo_y <= 882:
        distancia_x +=5
    if 239 <= jugador_pos_mundo_x <= 547 and 322 <= jugador_pos_mundo_y <= 334:
        distancia_y -=5

    return distancia_x, distancia_y
def puente_nivel_2 (jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y, nivel):
    if 235 <= jugador_pos_mundo_x <= 547 and 482 <= jugador_pos_mundo_y <= 484:
        distancia_y +=5
    if 243 <= jugador_pos_mundo_x <= 534 and 534 <= jugador_pos_mundo_y <= 546:
        distancia_y -=5
    return distancia_x, distancia_y

#COLLISIONS LEVEL 3
def paredes_abajo_nivel3 (jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y, nivel):
    if 140 <= jugador_pos_mundo_x <= 1168 and 432 <= jugador_pos_mundo_y <= 464:
        distancia_y -=5
    if 141 <= jugador_pos_mundo_x <= 240 and 351 <= jugador_pos_mundo_y <= 353:
        distancia_y +=5
    if 356 <= jugador_pos_mundo_x <= 740 and 387 <= jugador_pos_mundo_y <= 389:
        distancia_y -=5
    if 1192 <= jugador_pos_mundo_x <= 1364 and 383 <= jugador_pos_mundo_y <= 385:
        distancia_y -=5
    if 328 <= jugador_pos_mundo_x <= 768 and 305 <= jugador_pos_mundo_y <= 307:
        distancia_y +=5
    if 788 <= jugador_pos_mundo_x <= 1132 and 357 <= jugador_pos_mundo_y <= 359:
        distancia_y +=5
    if 1144 <= jugador_pos_mundo_x <= 1376 and 301 <= jugador_pos_mundo_y <= 303:
        distancia_y +=5
    if 1368 <= jugador_pos_mundo_x <= 1370 and 302 <= jugador_pos_mundo_y  <= 381:
        distancia_x -=5
    if 1180 <= jugador_pos_mundo_x <= 1182 and 385 <= jugador_pos_mundo_y <= 387:
        distancia_x -=5
    if 1140 <= jugador_pos_mundo_x <= 1142 and 305 <= jugador_pos_mundo_y <= 353:
        distancia_x +=5
    if 772 <= jugador_pos_mundo_x <= 774 and 309 <= jugador_pos_mundo_y <= 361:
        distancia_x -=5
    return distancia_x, distancia_y
def paredes_arriba_nivel3 (jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y, nivel):
    if 244 <= jugador_pos_mundo_x <= 246 and -30 <= jugador_pos_mundo_y <= 354:
        distancia_x +=5
    if 324 <= jugador_pos_mundo_x <= 346 and 200 <= jugador_pos_mundo_y <= 308:
        distancia_x -=5
    if 332 <= jugador_pos_mundo_x <= 334 and -30 <= jugador_pos_mundo_y <= 106:
        distancia_x -=5
    if 333 <= jugador_pos_mundo_x <= 384 and 114 <= jugador_pos_mundo_y <= 116:
        distancia_y +=5
    if 384 <= jugador_pos_mundo_x <= 472 and 9 <= jugador_pos_mundo_y <= 11:
        distancia_y +=5
    if 474 <= jugador_pos_mundo_x <= 476 and 8 <= jugador_pos_mundo_y <= 145:
        distancia_x -=5
    if 486 <= jugador_pos_mundo_x <= 634 and 153 <= jugador_pos_mundo_y <= 155:
        distancia_y +=5
    if 636 <= jugador_pos_mundo_x <= 638 and 10 <= jugador_pos_mundo_y <= 154:
        distancia_x +=5
    if 644 <= jugador_pos_mundo_x <= 876 and 3 <= jugador_pos_mundo_y <= 5:
        distancia_y +=5
    if 880 <= jugador_pos_mundo_x <= 882 and 14 <= jugador_pos_mundo_y <= 210:
        distancia_x -=5
    if 884 <= jugador_pos_mundo_x <= 886 and 214 <= jugador_pos_mundo_y <= 216:
        distancia_y +=5
    if 992 <= jugador_pos_mundo_x <= 994 and 158 <= jugador_pos_mundo_y <= 215:
        distancia_x +=5
    if 996 <= jugador_pos_mundo_x <= 1288 and 150 <= jugador_pos_mundo_y <= 152:
        distancia_y +=5
    if 1286 <= jugador_pos_mundo_x <= 1289 and -30 <= jugador_pos_mundo_y <=154:
        distancia_x +=5
    if 384 <= jugador_pos_mundo_x <= 396 and 5 <= jugador_pos_mundo_y <= 101:
        distancia_x +=5


    return distancia_x, distancia_y
def paredes_medio_nivel3 (jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y, nivel):
    if 318 <= jugador_pos_mundo_x <= 442 and 192 <= jugador_pos_mundo_y <= 194:
        distancia_y -=5
    if 438 <= jugador_pos_mundo_x <= 440 and 184 <= jugador_pos_mundo_y <= 236:
        distancia_x +=5
    if 440 <= jugador_pos_mundo_x <= 726 and 232 <= jugador_pos_mundo_y <= 234:
        distancia_y -=5
    if 722 <= jugador_pos_mundo_x <=  724 and 92 <= jugador_pos_mundo_y <= 233:
        distancia_x -=5
    if 730 <= jugador_pos_mundo_x <= 786 and 91 <= jugador_pos_mundo_y <= 93:
        distancia_y -=5
    if 792 <= jugador_pos_mundo_x <= 794 and 95 <= jugador_pos_mundo_y <= 283:
        distancia_x +=5
    if 788 <= jugador_pos_mundo_x <= 1072 and 291 <= jugador_pos_mundo_y <= 293:
        distancia_y -=5
    if 1080 <= jugador_pos_mundo_x <= 1082 and 244 <= jugador_pos_mundo_y <= 287:
        distancia_x -=5
    if 1072 <= jugador_pos_mundo_x <= 1450 and 235 <= jugador_pos_mundo_y <= 237:
        distancia_y -=5
    return distancia_x, distancia_y

#COLLISIONS LEVEL 4
def paredes_nivel4 (jugador_pos_mundo_x, jugador_pos_mundo_y, distancia_x, distancia_y, nivel):
    if 10 <= jugador_pos_mundo_x <= 12 and -38 <= jugador_pos_mundo_y <= 134:
        distancia_x +=5
    if 10 <= jugador_pos_mundo_x <= 12 and 246 <= jugador_pos_mundo_y <= 450:
        distancia_x +=5
    if 22 <= jugador_pos_mundo_x <= 1485 and 414 <= jugador_pos_mundo_y <= 416:
        distancia_y -=5
    if 1465 <= jugador_pos_mundo_x <= 1467 and -52 <= jugador_pos_mundo_y <=504:
        distancia_x -=5
    if -15 <= jugador_pos_mundo_x <= 1453 and -22 <= jugador_pos_mundo_y <= -20:
        distancia_y +=5
    return distancia_x, distancia_y






