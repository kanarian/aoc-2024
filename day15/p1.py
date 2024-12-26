inp_test="""########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

inp_big_test="""##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
inp_real="""##################################################
#..O#.O.#..OO...O.....O....OO...OO....O...O....O.#
#..............O..OO....O.O....#O.O.....#..OO....#
#O....O.O...O.#.O.O..O..#......O...O......O.O....#
#.#.OO.....#O.O..O.......#......O.#..OO...O....O.#
#..O.O.OOO.O.O....#O.#.O..O..OO..O....O..O...OO..#
#.OOO....#..OOO.OOOO.O.O..O..O#..O#........OO.O.O#
#........OOOO.O.#OO....O.O.O.OOO...#...O.......OO#
#.O......#OO..O..OOO..#...O.........OO.#.........#
#O#..O...#...OO.#..OO.O..OO...O..O......OO...OO..#
#.....O.OO...OOOO..O..#O...O...O.....O#.#.....O..#
#..O.........O..OO..O..O#.OOO.#.#..OO....#O.O....#
#..O..#.O....#.O.O.....OO..OO.#.OO.....O.....#O..#
#.OOOOO.........O..##O#O.......O.O#O#.O..#O......#
#O.O...O...#.O.#O......#.O#OOO...#..........O.#..#
#....O.##..OO#OO....O.....#.......OO..........OO.#
#..OOO.O.OO#.....OO.#.O..O#.O......O..OO.O#.O....#
#....O....#O..O..#...O...O...#....O.#.O.##O....OO#
#...OO.OO......OOO.OOO.#.O...O.O.OO......O....#..#
#.O.#OO..O.....OOO...OO.....#O.....O...........O.#
#..O...O.O.OO..#O...O.O.O.O.#O....OO.....OOO.....#
#OO.O..O...OO.#OOOOOO.O.O.......OO.......#....O..#
#O.O#....#...OO......#O..O.......#..O...OO#OOO...#
#....OOO...OOO.O.O.....O...O..O#O......O.#O......#
#O.#OO..#O.........O.O..@...#...O..O#........O...#
#.....O......O..#.OO..#.....#...........#.OO.....#
#O.......O.#.....O..OOOO.O.O.O..#O.O..O..O..O..#.#
#....O...O.#O.#....O...O......O..OOO.OO..OOO....O#
##.OO..O.O.#.....O..O......O.O.O.#.O.O...#..#..#.#
#.#..#.O..O#..#..O...#.O..O....O.O.O.....O.......#
##O..O.....OO##O.....#O.O.O.#O.O#OO.O#.OO........#
#.OO....O.....O..#......O.OO#..O..O.O..#O..#.....#
#...OO.OO...#......O.O.O............#..#O....OO..#
#.OO.O.OOOO.OO.....O.#O.....O.......O......#....O#
#.....O.O...#............#O..O....#.O....O..#.OOO#
#...##O..O#...#OO.O...O.....OOOO..#O..O#O........#
#...O....OO..#.#........OO......O..#O.......O.O.O#
#...OO.OO....O..OO#.OO.O.......O.....O..O...OOOO.#
#...O.O..O.O....#...#.........O...O...O.#OO..O...#
#...........O#.O.O..OO.....#...O.O.......O#OO....#
#..#O..O..#OOO..O...#OO.......O..#OOO.##O......O.#
#.##.O......#....OOO.........O.....O.......#..O..#
#O#....O.......O...#O..#.....#..O....O.#.O.OO...O#
#.#O.....O#..O.#....O.OOO...#...OO....O...###..O.#
#O.O..#..#.......O..........O.O...OO..O..#...OO..#
#O###.O..OO..O.OO..#.O..O#...O.......#O..#OO.O.OO#
#OO..O....O.OO#...OO...#.O.....O..O.#O..OOO......#
#OO#..O......OO...O..O.#..O.O.....O.OOOOO.O....O.#
#....OO..O#....OO........O..O....O#...OO....O....#
##################################################

>vvv^<<<<<>^<^vv<v<<>v>^^^>^>v^<<>>^>v<^>><<v<v^>^><vv><><v>v><><>>v<<v^^<<>>^>>>>><v^<>^<>^^vv<<v^><<<^v><vv>^^<>v^^><^vv<^v<>^v^^^^<>vv^>><v<>^>^v>^>v>v<>>v<^vvvv<^<<^v><>vv><>^>^><>v<v<^v<><vv><>>v<^>>>^>><v<><^v<vvv^><v<>><^^><>>vv<vv><>^><^vvv>v<vvvvv<vv^^v<>><^^v>vv><>^^<<<^v>v>>>>>>v<^^^v<vv>vv<v>>^>^v^^^>^^>^<>><>v>v<v^^<^>>v<<><<^<<<><<<>^>v<>v<v^v>vv^^v^>^^v>>>><^v^<<>>v><><^>v^<v^>^^>^>>>vvvv>^v<>v><>^>^^<^>^<>v<v>>>>v<>v><<^^^>>^v>>^><<v>>>>^>>>><<<^>vvv<^v>>>v>vv^^vv><^>v>vv>><<>><^>>^^v>>v>v><>^<^v<v>^<>>v<^^>>v>^<v<^>>v>>^vv><<v>^^^<vv>>><v><v<<^><<^<>vv^><>v<<<<<^<^>><>v^<^<v^vv>v^^^<<<^v^v^^<v^vvv>v>v^>v>v>><><>vvv^v<>v<>>^v<^^v>><>v<vv<<^v^^>^^vv^<^<<v>^<>>v><v>>v>v>v<<>><^^v>v^<v<v<<<>v<<v^v>^>^^>>vv<vvvv^<<><><<vvvv>vvv^<<<>>^>^><<<^><>>>v^<^^<<v^<v^<<v^><v<v<v^^^>v>>^^^<<>>^><<>>><v^<v<^<><<<<<<<<^^>v^>v<vv>v<<>^>>>^v><^^>v>v><<<>v<v><>vvv>vv>v<>^v^vv^^vv><<^vvv>v>>^^<^>vv<v><<<^>vvv^^v>v>^^<><<>>><>^^^<<<<vvv>v>v<v^<<<^v<><<>>v^>>v>^>>vv^>^^>>><^vv>>v<^><^v>v^<^<v
>>v<<v><^vvv^<><^vvvv<<>^><vvvv><^^^^><^^v<<vv^^^v<^>>><<><<^>><<vv^^^<<vv>^<<v^<<<<>>>>^>vv^<<v^v<<>^vv<>^v^^^><>^<^v>>v^<vv>v>^<^v^>><>v>v^<<^^>><<^vv^^><^>>><v<<<v^>v^<^>vv<^^v>v<<^v>v<<<vvv<v^^<^<^><<>^^<^<<<v^>^v^<v>><<<<^<^v>>>>^vvv^<<>^><^v^>v^>><^vv<^vvv>v><<<<<>^>v<v>^v^v^^>v^^v<^>>vvv>^<>vv>vv<^v^v<>vv<v^><v^v^>>^^v^>^v^^<v<<^><^^>v^><><vv<v><v>><^v>^vvvv^><v<vv><^v>^<v^<^v>v>>>^v><>>v<^^v<<>>>^<^^^^^<vv>>>>vv>^>><<>vv^<<>>v<vv^^^<>vv<^<>v><vv^<<v<^v<v>^<^v^>^>vv^>v<^^^^>v><vv>v<>>>v^v><<v^v>>^>>>^<><<v>v^<>^>>>vv^^<<><^v^<<>^<<>>><<<<<>^>^v^<^vv>^^><v>>><vv<v^<vvv<<v><>vv^v>v^<>>v^<v<><v<><<v>^vv>v^v><^^<v>^<v<>^v>v<<<>v><<v^^<v^^>vv^><v<>><>>><v><^>^v^^v<vv<v<v<<^<<><^<^<>>^>v>^v>vv>>v>v>vv><><<v<^^v^^v<^<<^><<v<^^<<>^<^^<v>^>>>vv^^<^<v<vvvv><^v^v<^^v>^>>v>^v>^v<><<v<^^>^vvv><^<<<<><^vvvv<<^v<>^vv<^><^v<v>><^^<^vv>><<v>^^vv^<v^><^>^>v^^^^>^^^>vv<v^^<^^>^^<v><<<^vv><^v^v^>v><>vvv^><<v^v<<vv^>>><vv^<v>^>>vv>>^<^v^^vv>>^>^<>^v^^>>v^><>^v^v^^^>v^v^<v^vv<<><^^^><^^>v<><>v>^^<^>>
vv^><>vv^^><<^vv><v>>>><<^^<<vvv^^<^v^>><^v^<<><><>v><>v><<>v<>>v>v<vvv^>>vv<v<^v>>^^v>^^>v^v^^^><<vv^vvv<<^^<><v^^>^<>^>>><v>v^v^v<>^<>v<vv><v<v^^<<>^<^>>>v^>v^<<vv><><^<v>^<>>>v>^v<<<>^^<>v>>^vvv<^>>^>>^<><v^vv>v^v^^^>>^<>>vv^^^>vv^<>^v^<v^<>^>>^>>v>^>><^^^^^<vvv><v<<><v^<^>>>>^^>^>^<v>v<vv^^^vv<<<v<^^^^<>><^^vvv^vvv^<vv^v^vv<>^>vvv<<vvv<v^>><>>^<v>v>>>v^>v^v><>^>v<<^vvv<>^>^<>v<^^>v<>>>vv<<>^^<<<<vvv<v<^v>v^^<v^<v<>^v^v>^>^^v><^^^v^^<<vv><vvv^v<^>>v^^^^><<<v><><>v<><<<<>^<vvvv>v^v>v^<<^<>v^><<><><<<<v<^^^v^v^v^><^>vv^>^v>>v<v^>^<^<<^vv<>vvv>^<>>>^>><v^<<^<v^><<><>^^<vv<<v>>v>^v<>^v<>>^v<v><>^>><^>^v>v<^^^>^<^vv<^vv>^<^^<<^v^<vv^>>v^>v<^<>^^>vv<^<>vvv<^vv<<vv>vvv<^vv<<<^^<v^v<^v>^>vv<vvvvv>^<<v>^v^v^>^<>>v>><v^>v>>>>>v<>v><><^>v^^^v>^vv^<<v<>v>^>^>v<>><^>v<<vv^>v>>v<vv^>vvv>^<^^vvvv<>v>^>^<v<^^>>^^v^^<v<^^<v^vvv^>v^>^<v>>>>v>v<v>>v^<<v^v><<^>^<<>^>>>v^v><^<v^^>v>>>vv^<v^v<>vvvv<v>^^<><^v>^<<^>v><^<^>>^v>vv>v^>><>^<<^>>><<v>vv^v^>^<<vv<<>>><<^><v>^<>^>>^>vvv^<v>v<<<<<vv^>^<vv<^<v>>^<<
>v<>^v^v<^^>v<>>>^>v^vv^^v<^^v<^v^^<<>><>>>^^^^>>v>v<v<v><<<^<><v<><^v^^v<^><v>>^v>v>>vv><><v<v^<^v<><<v<<>^<v<^^v<<<<v>>v>vv>^>vv^<^v^vv><><^>>vv<<<^>v^v<v^vv<vv<>>>^^v<vvv^<v>v^v>^>^v<^^v<><>>>^<<<><v<^v<<>^><>vvvv>vvv<><^><vvvv>vv^v>><vv<v>^v<v<>>^<vv<>>><>v>v^^v>^vvv^>v><<<^v>v<<<^^<><<><<<v>^^v<^>^^v<^<><<<^<^>v>^v^><v^^^>^^vvv^v<<<>>^>>^^^>v^<<<>>><<>v>>>v^>>^^v>v^<>^^v^><<^>^<<<>^<>^v>>><<>>^^>v<vv<<<^>>>v^v^^^v^^v>^>vv>>>>^v<^>v^<v>>v<<><^^^>>^<<^><<^>^^><<<>><<<<^>^<v^><^<v<<^^>^vv>>^<^>><>>>^v^<<v>^v^><>v^^^^^v<v>>v^v>vv><v>>^>^>^<>^v<^>vvvv<>>^>vv^^v>^^>>>^v^<<vv^v>^<^<><>>v<<<>><^v^^<^v>^v<v^<vvv<>>^>^v>>^<<^>^<<^<>^v<^>vv>^^>><<>vv><v^^v^^<^^<^^<^<v>v>>v>>>vv<>^v>>>v<vv>v<>>><<<^>>v^>><><v^<^<>^^^^vv>>v>>>v<vv>>vv^>v^^<v^<>^>v^v<^><<v>v>^<v^vvv><>>>^>>>>vv<v^v>v<<^><>v<<v>v<<<<^^v<<v<<vv^^>>vvv<v^vv>v^<v<>v^<<vv>^v^>vv>^><<><>v^><>^v<^^v<^^v>><<<^<<v>v<^^v><v><>^^vv^<<>^<>><^v<v^^<>><<^>v>>><^^^^v<<^<>v^>^v^>>^<>v>vvvv<^v<^vvv^>^>^vv<<<v>><<^^v^v>v^>vv^^<vv>^^><<^<vv>vv<<v
><^>^^<<<<<<v>>v^^^<<^<vv^^<<^^>>><v<^><>^>^v<><^<v^v<<<>>^<<v><v<>v<>vvv>>^vv^v^^v<^^<v><<><>>>^^v<<<<<^v><^<><^<vv<<v^^>>v<^v<^>^>v>^>>v^<<>>>><>v^<^<^><<>v<<>v^>vv^v>^<^>><<<<><v<>^><^<<^<^^>v>v>><<^>v>v>v^<^vv^^<<><><^v<>v^>><<v>>v^v>>^><<v^<v^v>^^>vvv>>v<><^^^^<<v><^>v<^v^v<vv^^^^>v>>^>><<vv<<v><^><><>v^v>v^^^^v<>^<v>v^v>v<^<><>vv<v^>v^^v>v^><<<^v^^<v^>v^<v>><<<>>v^^>>>^<>vvv^vvv>v^^<v^^^>^^vvv^>>vvvv^<<vv>>^<v<><>^>^v<^>>^v^>><><<>><<>><<^^<><<<>><>v>^^^><><^><>v<<^v^<<<>><>v^>>^^>>^^v<<vv>^^><<<vv>v>vv^<vv<>^v>>v^v^v>^v<>v<>^^^v>>>>^>v^^<^v<^<><^>^^^>^>>^<<vv<<>>><<^^<>v<v>v<<v^>^^^^>^<<<^><v^^<^>^^>v><^v><>^<^<v>^>^vv>vvvvv^>vv^>vv><>vvv^<<v^>vv<>v>vv<>v<vv<^<v>>><>>vvv^v<><>^v<^<><<>v<^<><^v>^<>><<>^v<>>>><<^^>>v>^v><><>^<v>^^v>^^^>^v^<v<<v^^<>^<^v^vvv^>>>>>v>^>^v^><<^v<<v<<v<^>^^>^<><v^>>^v>^>^^v>>>^<><>^^v>v>vv<>>><><>>^>>v<v<<^>v<<><><v><<^>>^^<v>>><^><v^^>><v<vv<^^v<v^vvv<^^v>^><vv>><^v<^v<><>vv^v^<<vv>>^vv<><<<>v>>v<^<v^v<^<^>vvv><^<<^^>v<v^v><>^v>>>v<<v^<vv><v<>>>^v^vvv<
v<>^<<>^<^<><vv<<<<><<v^<vv<vvv>v<<<^<>v^>^^>><>>>vvvv<^<^<<>>vv<<>>v^v>^v>>v>^<<v<<^>>v^v<><v^v>>v>v<<<<v>vvv<vv><>vv^<^<v^>v><>vv^^>v<<><<><v<<^><^<<>><v<^^><<<^vv>>v^v>>vvv>vvv^><v<^<>^<^v<v><><^<v^>>v>v>><<>>><>vv>vv^<^^<v^^vvv<>><^><^<^<v<>v^^v<v^>vv><^^<^>v>>^<>>>^>>v^>^<<<vv>v<vv^<><^v<^v^>>^v>><v^v^>>><vv>>^>^v<^<^^><<v<><v><>^<v<><>v>>^>>^v>v<<v>>>^v^<<><><<<>>v<<^<v<^^<^v>>^v<<^><<<^><<^^<v^><^<^^>>>^v^v^v>vv>><>vv^vv<v^<v>^>vv<><<>^<v<><v^vvv^><vv>^^<>^^^>^>>>>^<>^><<^v<>^>vv>^<v><^^vv<v><<><v<<^^>v<<^^^<<vv<<<<^^<^^^<^>^^^<^v<><>^<vv^v>>^>v<^>><vvv<^<v^v>^>^^>><^>>><<v<>v<<v^<^^><v>>v<>^>v>>v>^<>^>vv<>><^^^^^>^>v^>v^^v<v<^v^^<<v<^vv>v<>>><v^^v>^><^<>^<^^^^vv><<^<<>^<<>v^<<<^>v>>v>vv<<<><<<v>>v^v><<>>^><<<^<v<^>^v<<<<<<<<<^^^><><v<<^><^^<>^><v^^<<>>v>^<^^<v^<>><v^v>>vv^^^v>^>>>>>^^v<^v>><><vvv>^^v>>>^v<vvv<^<^^vv^<^<^>v><<<^<<><>v^^^v<v^<<>v><vvv^<<><<>^<<v><<<vvv^v<>><^>>><<>^^v<^^<^<>^vv><vv<v<v<^<<>>^>v>>^><<<<vv><>^><><vv<^<^^^>^<v<^v<>^^v<>><><<<<^v<<^>^v<>>v>^^^>v<v>^v
vv^^>v<^^<><<vv<>>v^^><v^<^v<<^^^><>>v<>>^<<vvv<v^<<^><<>vvv>^^>>>vv^v>^><^<v>><>><vv<v<v^>v>v><<<<>v>v^<>v>^><<^^<<<>>>v<<<<v<<^^vvv<v^<<<<>><>>^v<v>^>>>>^v^>v^<<v^>^^^^^vv<v><^<^>v>^^^<>v<v>v<<v<v<<^>^^^>^>^^^^^v<v><v^<^>^<>>^>^^vv^>^>vv<v^>>>>^v<^<>v^>v<<>>^<v<v<<<vv^>v<<^>>>^<<^^vv>^^<v<vv>vv<^v>>^<<<><v>vv^><v<<vv^v<^<<<^>>>^v<><vv>>^>v<^v<^^<>>><^v^^^<>vvv<vv>vv<<v<v<v<^vv>><^v^>^<<>>v^^v<>^vv<^^>^v^>^^^>^<<^<^<v>^v><^v^^>><^<>>^v><<<v<^vvv^<v^^>^^>v<>>v<>vv^<><v^<>^<v^>>^>v<v<vv<v^<^vv^><<^<><<<^>v^><v><<<v^v^^<<^<^<^><v<<v^v^>><^vv^<><>>>>>^>^v<v>vvv<^<<>v>v^v<^^>>vvv<^<<^>^v>v^vv><<<v^<<v>>^^^^><<<^>^^><^^<<<v>^^^><vv>><<vv^^<v<v<v<>v<^^v><^<v>^^>v^<>v>^^>vv<<vv>>v<><vvv^vv<>>^^<^<v>^v>><<v<v>^^>><vvv><^^^v><v<^>vv>>v>vv<>>^<vv<<<v>v^><><<>>v>>><>v^<v^^>v<<v><<^>^<v>>>^>vv>vv<^^^<v<<<<v<<<<>^^<>vv^><vvv<^>v><<v^^^v><^<^^<v>^<vv^<>>v<^><^^<><vv<<<>^>>vv>v^v^^<><^^<>v<<v<>v^v^>^^<>v<<^v>v^v<v>v>v>v<>^^^<>>^><v>>^^v>v><^^vv^>^>^<^><v^vvvv>v><^>v^v<>vv>^>v^^v^v^v<^>>v^^>>>v^v>>^^<
^>>>^v>v<v<<^>^^v^v>><<^><<<^>>><v>^<><<v>^<^><^v>><v^<v>>v>><v^^v<v^v^v>vv<v>^^>v^vvv<>v<^v<^^><vv>>>^>>^v<<^<<^^^>v^><vvv^><^>^>><<<^v><^v^>v><<<^<><^^>v<><>^<<v^<v<<><^><v<vv>v>><v<>^v<<<><^^<^<^v><<>vv^^<>>^^>>^^>v^v>v<>>>v<>v>>^v<<><v<<>vv^^^v<<>^^<^<vv^<<<<<><><^v<<>^<><^>^<<>>><^>^><v^>><vv<<^v^^^><vvvv^>vvv^<<vv^vv<^v>v^<^<^>>v^^><^^v^>>^<^v<>>^v^><>v>^vv^>><^v>>v<v^v>>v^v<<^^>v<v<>>>^^v><>^<>vvv>v<v<vv^><^^^^v<v>v^v^v<v<><<<>>^^<^<^>><^><>^>^<>>v<^v<^^^vv><v>^^v^<v>v^<><^v<<^v<>^^<<<<^^<<<^><>>><vv<>><<^vv>vv<^>v>>vv<>^<>^^^>^<<>>v<^<^>><v>v>^>v<^<>v<><<^v^<>^v^^<v>v>^v<><<^^<^>^^><><v^>vv<<^v><>vv>^<^^vvvv>>^>>^>>^><>>^<^vvvv^<<^v<>>v^<^<^>v^>v^<<^>><^<vv>^^<><>>v^<>vv><>^<><^>^<>>v^^<v<v>^<<>^<<^v^><<v>v<^^vvvv>>v<>>^^^<^^>><v^^^<v^v><^>^vv>vv<<>^<<<^^v<^v^><^<<>v<>>v<v<v>>^<><vv<<>>v<^v^>^v>>^<>v<<<>v><v^v>>^><^<vv^vvvv^v<>vvv>><^<<><><<^^v^^^^^^<^^v<^^^^<v^^^v^<<^<><<<>v<><^v><^<^v>>v>v<<^^<vv<<<^><^<vv<><<^<>>><>><vvv^v^<v^^<^<><^v>^v<vv>vvv^v^>><v<>^v^<><^^>v<v>>^<>>>v<<
>><v<v<v<^<><v>>>>v<v<v>>^v><v<<>^v^<<v<<>>>vv^vv><^>><^v>^<>v<^^v><<<vv>>v>><><><^^<vvv<>v^^<^<^v<<v>>><><>^v>v>^^>^^><>^^^^><vv<<<^>v>>v^><<^<>^><v<v>>^>v<^>>v^>><<<^v^^<v<^<>^<^v<v>^<>v<>>vv<^^^<>vvv><>^>^><vvv><v^v<>v<v<^^^>^^v>><^^^>^^^vvv<<^<^^>vvv^<v>>^<v<><<<v>><^vvv^v^v^v^^v^>>^><v<^<<v><^v>^>^v>v^>vv>^v^<>v<v>v>v^^<^^v^><^v<v<v<>^<v<<vv^^^>vvv><v^<v>>>v<v^^<><^>v^>^^><^vv>><>^v>>^><v<^<^<><v<>^v^^>>v>^vv<><>v<>>v<>vvv^<>>v<<^>v<>^^^<^<<vv^^v>v^<<<^>vv<><^^v^v<vv>^<<>v>v<>^<>>><<<vvv<^<>v^^v<><<^v><^><v<^>>>v<<^<v^<^<v>v>^><^<^>v^^v>^<>vv<^>^<^v^<<<<>><^v<>^<^>^>>>vv<<<v>>>>>v>v<v^<v^<^><^^<>v^^^v^v<<^v<<<^^>>>><v^^v<^^v^vv^^>v>^^<>vvvv<>><v>><v^^>^<>>>v^^v^<<<^>><^v>><>>^^>v>>>>v<v><><v<^^><<v>><v^v^v>^>>>^vv^^^>>v<^vvv<<>>v^vv<<^>>^^>>v<v^^>^<v>>v<v<v>^^^>><><><^^<>v^><>^^>^<v^^<vv^vv<<<^vv<^>><<v>^^<<v<^v^^><><v^<v><v<<>><vvvv^^<<^v^><<^v>>v>><^^<^>>^v<<^>vv<<vv^<<^<^vv^v><^<><vv<v^<>>v^vv<<<^>^v<^<^<>^v><v^^^><v<<v>v>^^<v>v><^<v<<>v^^^v^<>>^<<v^>^^<v>^>v>v<v<^v<v>vv<>><^><
^vv>v>vv^>^vv<>v>vv^<^^><>>^v^<^v<>^vvv^vvvv>>><^><<^<<v<^^<><>^^v>><<^vv^^^<>^v>v^^v^^^^><<>^<<><^v^<><^>v<>^v<^^v><v><v>^v<><<<>^v^<^<<v<<^^^<v^^>>v^>>^>^<v<>><<>v>v^<<>>^<v^<<<^v<^<<v^vv>v<>vv^^v^<<^<v^>v^vv<^>v^v><v<><<^v^^<<^v>v><>v>>>^>^^<<^><><><>>^>>^>vv^vv>^>>>v>v^<>><<v<^>><^^^>^v^<<vv>><>v><>vv>><^<^^>^^<^v>v^v>^^><<v<>vv<<<<<<v<>^^><^^<<<^><v>v><>v^<v^>vvv><><>^<>vv>^>^v^v<<^^<v>>v>>>vv<>>vv>^v>>^>>><<vv<vv<<<<vv^^><><>v<><^>^><<>^^^<v<^><vv<><<v^^>^^^^>><><^v>><<^<>^<<<v^<<<><^^^^^^><<<<<<^<<v>^<<<<<<>>><^^^vvvv<><^^>^^^v<>^^>vv<^>>>>><v>^><v^<>^<<v^v>^><v>>^<vvv^v<v><^>><>>^<vvv<^^>>v^<^^>^^<^v<^v^>^<>v<>>^>v<>^>v^>^<v^<^>^^vvv^^<^v<>v<v>v^v<>v^>^>^>v^<v<<<>vv^v^<<>^v>>v<^^^v>v><>>v^v>v<<^><<^v^<<v>>^^v^v^>><<v>v<^^>>>v^v>^^<>^<vv^><^vv>>v<^^><<^^>^><>>^<<v>>^^v<^^>^vv^<>^^v>v<^^>v>v^v>^<^v^<>^vv>^>>>>vv<v^v>v<^^<><^<^<v<^^^<<^v<^vv<v>v<<v^^<v<^v^<<v<^^v>>>>vvvv^>>^v<><>v<v<>^<<<^>>^><^<>>v>>v<<>v<^^>v<>><<v<vvvv<<<<v^v^v^>^>>>>>><><^^^>v><<<>^>^>v<><^vv^^>>v>v<><><^><<>v
>>>vv>><<<>v<^<<<^v><^^><^vv^<<^^^^><<>^><^>v^^><v^^<^<<<><^>>^v>>>v>vv<<<^<>vvv><<^<<^^^vv^^v^^v^^v^>^v>>>v^>v>vv<<<^<v>v^v<<^>>>><^<^>>^^^^>>>>vv>v<>><vvv^<>^<^<v^^>>^vv^^>^^><v^^<^v<^<v<>v^^vv<<^^<>v^^^^>^v<^<><^^v^>v>vv<vv<^v><>^v^<<<<^^>>>>^<^vv><>v>>>^v^><v><^^v^><<^<v<vv^>>^v<v>^v^<^<<<>><^^>><>^^v^>^^^>^<^v<^<<^>>^<>^><<^vv<v<v>>vv^^<<vv^v<vv>>vv>v><^v^^^>><>v<v><>v>>>>v^>><>>>^<v^<<<vv>^<<v<^^<^<<^<>^v>vv<>vv<^^<>>>v><v^^v><v>>><vv<^>^^v>v<^v^<v<^><>v<vv>>v><v>><>^v^v>vvv<^<<v>><<vv<^<^^v^^^^^>^><<<v^>>^^^v<v^vv<^^v^<<<>>^<v>v^>^>^>v<v^<v^v<>v>^^<<v>^><>vv<vvv<>><vvvv<<^<<>v<>>^^>v<^<vv^><><vv<>>vv>>^^^>^^v^^><<>>>v<><<^>vvv>^<v^v<<>>>v<>^v<^vv^vv^><<^^<vvv^^>vv^><^<<>v><><>>>^<^v^>v<^<^vvvv<v^v<<^^^v<<>>>>><^^v>>^<^^^<vv><<^^<^<>>^<<>^vv^v<>>>^vvv^v>^^><>v^<><^>vvvv^><<v^^vv^v^>v^<<^<><<vvv>v>v><>^<v<<<^>vv^^v<>>^<>>v>>^^v^^v^^^v><<>^<>><>v<<vv>>vvvv<<<v<^<^>^>^v^vvv>^<>^v><<^>^<^>^<<>v<vv<>^vvv^v^v^><<v^^v<^^^>^vv<^>><^^v^<><^<<>>vv^>^^<v<>>v<^^^^<v^^^>v>>v>v<^^^^v^><<>vv><v
v<v<>>>v^^^^^<v^<<v>v^<>v^^^>>v^vv^^^>>v<>^v>v>v<<^v><v^<><^v<<<v>v<v^>^^><^<>><><^^v<^vv>^v^vv>>>v>^<>^><vv><^v<>>^<<>^<v^^v^<<<>><>^^<>^^<^>^>^><<<^v><^>>^>v^v<v><v^v<<>^^v>v^<^vv^<<>v<^v^><><<<vvvvv<^^<>^vv>vv^^^<^^<^^>>^<>>>>><^v<v^^<<<>>^>>vv^<^<^<>><vvv<<>vv<>v>^>v^^v<>^v>>v<<^>vv^v^>^v^^v>v>v>><>^>^^v<v^<v^^^v^<v<<<><^>^<^>>^>><<><^><v>vv<^v><vv<^v>v<^vv^<><<^<^>><^v^><<^v>><^^v^vv^<>^^>^<<>^^>><^<^^<vv^>^vv><>^<v<<^<^<>><vv><><<v>v<v>v<^^^^^<<<v<>>v<<<v<v<><^>><v>^^^<<^^<>><^vv>vvvv^<>^<vv^v<v<v><>^<>vv^^<><<v<<<><^<^>^^vv>>v><<^<<>^<>^^><>^>>><<<^v><^v<^<vv<^^^v^vvvv^^^v>>^v>vv^^^<^^^>>vv^^>vv>><><^>>^>>v<^>^^>>>v><<<>^<<v>v<>v<>vvv<>^>>>^^>>v>>><<><>>v<^<v^v<>^^<>>>v>^<>^<<vv<<>^>>>^vv><vv>v^>>^^vv<<^v^>^v<^^^<>^^<v<><><vvvv<^<>>^v^<<^<>><>><v><>>v<v^^v<^v<<v^^>v^>vv<<v>>^<>vvv><<^><<>v^<>>>>vvv<vv^<>>v^>v^<>^<>^^^<^<^v<<vv^<v>>^v<v<v^<<^v<>v^v>><vv><<^<<^^>^<<^<^<<^<>^>^>v<^^><>vv<>v^^<vv^^^>^v<^^<^>>^<>v<v^>v^vv<^><<vv<>^<<<><<^<<<^<>v<<>>^>^<^^^v^<^^<>v><><<><^<>v^>^>^<<^v
<v^^^<^^<v<<<^^^^<^^>v^><^><v^^^<<^^>>^v^v^^<>^<>v><>>vv^v<<>^<>v<^<>v>^^<^^>v^>>vv^><<>vv^^v<>^^^><^v^<>vv^v<>v^>^^^>^<^<v^vv<^^>>^<>^>>>>^<v><<<<>>v^^v>><>>v<<^^vv>><vvv^v<<^<^>^><>v><<<v<<><v<^v<^<<v>^^><v<<^^>v><v><><<>>v<^<^<<>>><<>v><^>vv>^^>v<vvv<^><>^<<>^^v<<<<v^^><>>><^><^v<^^<vv<vv^v^<>^vvv<^>>^>^vv^v<<^^vv>v><^^<>v>^><>v<v<>v<vv>^^v^<^^<>>>^^^>>>v^>vvv>v><<<><<>^v^vv<^>^v>vvv>v<>vvv^>v<v<^^>><<^v<>v<<<<<<^><v^>><v^><^<<<>vvv<v>><^>>^v><>^<vvv^^>^<>v<>>^v<^v>>>><>v>v^^>>vvv>vvvv<<^v<<v^v<^<>>^<^v>v^<>v>v^vv>v<><v>v<<vv>><v^<<<<>>vvv<<^v<vv^<><v><>>><v<v^^^v<>^>>^<<v><^^vv^^<v<>vvv><>>>>^^>v<v<v<<<v^v^<v>v>><<>^v<<^v^<^^^v<^<<^<^><^>^^<<^<<>vvv><><>><vv>^>><v<v<^^^v^>>v^<>>vv^>v<<><^>^><<>^^^v<^<<^^>v>>>^vv>vv^^>>vv^<^v^v^^>vv<v<v^<<>><<<v<<>>^^^>v<>><v^<<^<><^<<^v^^v>v<<^^<>v>v>^<>>>>v<v^^v^<><^^^^v^vv>v^v<^^v<>v>>>v>v<><>^>^v^<><v^>>^<>><><v>^><v<<<<<<>v^>^<>v<vvv<<v^<<v<^v^>v<>^^vv^<^><v<^<v>>^<<v^<^<<>^^^<<^^vvv><^>vvvv>v>^^^^><v^v>^<<vv^^><v^<^^><^v^^<v>>v^<<<v<<<v^>>><>>
<^v^v<^v>v^^>>^>>^^<>>><^<^^<v>>><>^><^v>vv^<^<<<vvvv^>vv<<^^^>>v^v<v<v>^^<vvv>>v<vv^v>^>v>^vv^v>^v<>>^^v>>^>>^v><<>^v^>><<^^<vvv^<^v^^^^^>^v<^v<<<^<>><^vv^<<^<^^^^^v^>vvv><^^v<v>^^^^v^<<>>vv<<^<v<<>vv>>>>v>^v^<v<<^>v>v<^>v><>^^v<^^^^^<><v^v<^v<><>^^<^<^v>^^><<>v<v^>v><>^^<^<v><>v>^><^<>>>v>^vv>^><vv>v>v^<><^^<v<^>^^<<<^>vv^<v<^^<v>vv^^><vv^><<>^<>v>v>^vv<<^^^v^^>^<^<v<vvv<^v^v<^v>v^<<^^>>vv<v<<v<<><><^>v>^>v<<><^^^v^^<v>>>^^<<v^^^<>><<vv^vv^v><>><><><>>>><<>>>><<>^<>>v>^><^<>v<<v<>^>v>>v>vv>>>^^^>>>>v<>>^<^^^<^<^v>v^^<^>><^>^^v<<v>>>^<v<<v^>^<>^^v^>v<vvvv<<vv><>^^^<>>v<^<^^>^<^vv><>vv<^^vvv><v<^<vv>^v<<<>vv><><v<><vv>><<>v<v^<<<<>v^^<^>^>>><<<v<<v>v^<<<^v>v^<>vv<><><><>>^^v<v^><<<v><<<<v<>>v>^v^>v^^^<>vv<<<><<v^><>>^>v>v<v>>v<^^^>>vvv^<>^>v>>v>>v^<<>>^<<v<vv^v><>^>>>v^^^^vv^vv<<>vv<<vv<^^^^><><<v^^>^>^v<>v>^>^<v<<<^<v<<v^vv>v>>><<>^>vv^^<^v><v<><^>>vv>^^>^<^v<v^^vv>^><>>^>v^<<>^<^<v^><vv^^<^v<^v<<<<^^^^<^<v>>>^^^<v<><<>^><<<>v><<v^<vvv^vvvv>>v^<>>v<^>>^>^>><><^<><vv<<><><>v>^^v>^v<vv>
<^<^<><v^^vv<<^^<><>><>>>v^^^vvv<v>v^><^<^^<^<><v<<v<>^v>v<><><^<<<^vvv><v<>^vv^<<<^><><v<^<<^v^><>>^v<v<v>>^v<v^^^<><^><vv<^>vv><v><>>>>^v<>>><^vv>v><><>v>>><v^><<^>v^>v><>>^<<v<^<<v<v>v>v<>^vv>v>^v<vv>v>>vv^v<>^>^>>>^^v^><<^>v^vv^>vvvv>vv^<vv<>vv<v>^>v^^v>^<<<v<>>^>^<>v<^^v><vv<<v^^vv^>v<^><<^><v<>>v^vv>^v>>>v<>^v<<<<vv^<v><^vvv^<^<<<<<<^<vv^>^v<v<>v<^vv<><v>>>^^<><v^^v<^<v^^^v<v><^>^v>v^v<>>^^^v<>^<v^v>v<>><^><>>><v^<>v>^v><^<>^<><>v^<^>v^v>><v^vv>>>>v^v<>^^vv^^><<>v^><^>v<<vv^<^<>><<v><>><>^vv<<<<<v^^^<><>v>><><<v<v><v<v<vv^<^^<v^vv<<>>^<v^^v^<<>><vv>^v<<v<>^>^vvv^v>vv^v>>><><<>>v>vv>><>^v>>>>>>v<<>>v^^v<<>>^<<>vvvvv<<><^^^v<^>v<^v<v>v^vv^><>v<^^v<>^<^<<^v^v^vv^vv^<<>^v>>>><<^>vvv>v^><>>v><^^v>^v<<v<^>v^^>vvv>>>>><vv>vv<v<><<^v^v<vv>^>v<>v>>v^><>>^>vvv<<vv^^><v<>><v>>vvvv^^<^v^v^<^<><<>^<^<v<^>v>v>^^>><^<v><v>><>^>>>>><vv>vv>>v^^v^>>^vv<v^<<><>^^<>>^>v<^<vv^^v^v^><<<v<<<>>>>^^^vv^<^><^<<><<>^^^<^vv>vv<<<^<>>>v^vvv<<<>><>^^^^vvvv<><<^><vvv>v>>v>^>^^v>v<^><<^><<<v>><>v^v<^v><<^<vv^<>
^<^<^v^<<>^v^>v^v>v>v><><><>v^^>>vvvv<v>v<v^^v^v>v^^v>v^>^^>>v^^^vv^>v<v>v^vvvv^<v^^vvv><v>^>^v>>>^<<^v<^>^>>^<^v>>v^<<>v^v^>>vv<vvv><<><>^>vvvvv<>>v^<v^<vv<>><><v<><^<v<vv<v^^^>vv><vvvv^^v^^<v<><vvv>^<^<v^v^^>>><<<v<><^v^^^^v^vvv>^v<>v^<><>><<v><<vv>v^><^<^^^^<><^^<<<><v<<<>vv^v<v>vv<>vv^>^^v>v<^>^<<^<>>^v<v^^<><v<v<^<<vv>>><<vv^<vv<<^>v<v^<<v>^<^><v><vvv^<<<^>>v<v<<>>v^<^>^>^>v^<<^<^^<<^^<>v<>><>v<>v<^>><^v<<<v>vv^v^^v><^<^<^v^<>><<v>>^^>^^^^v<^<v^^^v>^<>v>>v>^>v<>v>^^^v^>v^>vv<<<v<v^>^^><v>v><><>^<>>>^><^v<>^>v><vv^>><<<v>>vv>>v><<v><vv><^<^>^v^v><><^v^v><>>>>>vv<v<<>>^><>^<^v<><<^^<>v<v^^<>v^<v<^^<>v<^<^<^^>vv^>>vv^^<<<>><<^<v<<^<>v>v^<>>^^<v>v>^>^^<v>v>v>><>v<v>>>^v<<v<>vvv^^<>v<><>^>v><v<v<<<<^^v<>>^>v<^<>>^^v^^v<v^^<>^^>vvv^^v><v^<v<>><>v^>v>>v^>^<>vvv^^<v>v^vv>>>v^<^^<<^>^<>>>v<^^><v^>v><vv^<v>>^v<>^<^vv<^>><v^v>vvv<^>v<vv><v<^>vv^>>^>>^v^v<<>^^<<v><<^^<>v^^<^<>>^^<^>^>>>><>^^>v>^><^<^^<v^v^^v><>v>^^^^>><^^<^>^v><<^>^v>v^><<>v<<v>v<^^vvv<^^v^>>>^<<^<^<<v<^>>>^<<<vv>>^^<<<<^^>v>
^><^<<vvv>v>^<<><vv>^<<<<v^vv<^>^^^>^<><vv^^v<<v<v>>>v^^<v<^>v>^>^<vv>>v>^^<><^v<^^v>vv^vv^v^<<v^<<<><v>v<^<>v<v<^vv<v^^^>vv<^><^<v^^^^^<v^>vv>>v>><<><>v<<v>v<<>>vvvvvv<v<vv<>^^^^^<v>>><>^v^>v<<>v>v^^<^<><><>>>>^^>>v^<^<^>>v^<<>>vvv>^<^>^v^^v<^<^^>>v<<v<vv^^<v>^<^><^^>^^>v><><><<<^v<vvv<>v^>v^>>v>>>^>vvvvv<^^<>>>^vv<>^<^^<vv>v<<vv^>>v^><^>^><><v<vvv<>>>>v<v<>^<<^<<v><<>^<vv<>^^>v>v<<^>>><^<^<v^<<v^><<>v^^<>^><^><<^^v>><>v<^>>v><<<>^^^^<v<^^^>v^>^^<^<>^^>v^>^>v>>v^^>><^<><<v>vv>v<^<v<>><<>v<<<><vv^^^><^v<<<v^^>vvv^>>vv^v<v>^<^>^><^<^^^vv>>>v<^vvvv^v<vv<^^^<^v^><^<<^vv<v^^^v<<><<^<<<<^>^v^<<vv<vv>v>>^^^^><>>^^<^^^^>^<<^><^v^^>^>>v^^>^v>>v^<^v<><>>>^^^^v<><<^v^^^>v<vvv>vvvv><v>^<v^>v>>^>>^^<>vv>>v<<<^<>v>v>>^v^<v><^^<<^vv>v<vv^<v>^v<>>><v<v<<><v><^<><>>v><v<<v<>><^v><<>^^<<<v^>v><^<<<^>v>>vv<v^^v^>>^v^<vv<<^<^>v<v<<<vv<><<<><vv<vv^^^^^<^^<><<vv<>v<^>v^>>>>><^vv>^>vvvv<v<<>>v<<v^v<v>><<><>^>^^^vv>>v^>^<v<vv<v^<v>>><<^^v>^<<^vv<v><>^<^><^v>^<<v<^>^<^^>>>^^<><<<<>vv<^v>>>>v<<<>vv<<^v<^^<<<^^
^>vvv><v><<^>^^>>v>vv>vv<<>v^>>v><<>^<><<<^><>v>^^vvvv^^v^>vvvvv>v>>>v^^^>^^<<^^<<<^^vvv>>^v<>v>^v>^<^^>v><^^<<<^<>^v<vv^v>^v<^><v<^<<<<<^v<v<v^>v<v><><<>v^<v<^>v><<>^<^^v<<>^>v^^v>vv<<<^>vvv^<v^^v>v<v<<^^^^<<^<vvv>^>v>>>^<v^^<^^vv<^^>><v<<^^>^^v>v^v^^v^><^vvv<>v<<<>v<v<>><^vvv<><><<<vvv<<^v<>><v>v<^v^><v<v<>v<^v>^^<>v>^^<<<v^v^>^>^>><>v^^<v<>>^>^v<v<^<><<^^<v>><<^v>>v<><^<<<<<<<<<>>><>^^<vv<<v<>>v^^<^>v^<<v>^><^>><^v<<v>v><<<<<^vvv>vv^v<<<vv^^^<>>>>v^vv^v<v>><^>>^v>^v>v^^v<^v<vv>>^^^^>^>>>v^v<v^^>v<v^^v^>v^^vvv^>>v<^v^^^v>^>^v<^^<v^><v><><^>vv<^^<^>^>v<>>v<^^^<<><^^^v<>>v^v<>vv><v^vv>^^vv^>><<>^^^v^^^^^>><^v^^<><v<^v>v^v^>^v^^v>>>><v^^v><vv<<<<>vv^><<v^v><^^v><<^v^<^<^^>v^<>v^^v^>^>^<<>^^v<^^>>^<>><^v^>>^<><^^><v>^><<v>><vv>^>^v>>><<v><^>v^><v<v<v<v>^vv<^<<<<>^^>^>>>^><v<<><^v^><v^<vv^<v>>>><^v><^<<v^^<v>><<<>><vv>>><^^>>>>^^>>^^<v<<v>^>v<^vv<^>v>v^>>v^^^^vv><<v^^^v<><^<<^^<^vv<<v<^^><<<<<<<vv^^^v>vv<>v<v>v^^>v^^^>>><vv<^><^^v<<^vvvv^^>>><<v<v<<><^<<v^^><<<>>><>^<>^<<>>><vvv>><>^<>^<^
vvv^^v>vv<vvv><v<v<^v<><v<>^<<v>v<vv^v^<v^^<^^<<^<^v<<vv^v<^^>v<vvv>^>^><<>^^vv><<>><>^>v^v>vvvvv^^^^><^>v<vv><^vv^^<<<v><v<<><<<vv<<v<>><<<><v^>>v^<>v^v>vvv^<<><>v>^^>^^><v>^vv<<<<^><>v><><><>>v^^^v>>>^vv^^^<^>^^>>^<^^^^<v><v><^^<v<v<vv<<^>>v^<v^<>><^<^v><<<vv>v<^v<^<^<vv>^v><v>v><<^<^>v>vvvv<<^>v>^^v>v^^v<<^<^v^>^><^^<><<^v<^v^<v^>>^>^v^^^v^v>^<<^v^>>>^v^<^v^><v><>^>^>^v<^<v^<^><<^^^<^<<>vv<>v^<<v^vv<vv>>^<>^>><<^><<v^^^^<>vv^^>vv<v><>v<^>v><>><<^v<<^>vv><^<v>>^v^v<v^^><>^v^<>^^>^><<v^v^v^>vvvv<><^<v^<<><v><><v^^v^v<v<^<<v>v^v^>>^v<^>^>^>v>^^>^^v^>><>>^v<^vv<<><^><^<>v>^^^>^>^<><<v<^>v<>v>v<vv<^^<<<<^<v<v<^^>v^<<<v><^>>v^>^>^^<^<>^>v><<<>v^vv<^><v^<v<<<^v^^<v<<^<<^>^>v^^vv<^^><>>v>><^^>^><<^^v<v<v<<>v^^<<^<^><^><vv^vv^^<v<<v><^<>v<v<v^v<<^^<^v>^^v^v><v><<v><>>^<v>^<^<v<v^v>^v><vv>v^<vv<^^<<^^^^<<^<vvv^>><v<<vv^<^^^><^^><^>^^v^^>^^vv<><<<<v^v>v>><>>>^<>>^<>>>vv<^^v>v><<^^^v<v>>^^^^>vv<>^>^<v^v^vv<>^>><<^^><^v<^^^^v<v>v>>>v<vv^^v^v><<^>v^<>^<^^<^<<v<^v<>>^>>v><v><>v^><>>>><^^vv^v><>><^
v^><vv<<v<><>>^<<v^>><<^^^>><>^^^><<^^v<>v<>v<v>^>v<<>v^<^>^<><>^><^vvvv^vvv>>v>v^<>vvv^^>v^v^<v<^v><^<<<v>>>vv><vv<>vvv>^v<^v>^vv<<>>v<^<v><<<<>^^v<<^^<v^v^^^<v<v^>vv>^<<>>>^v><^^><<><^>^vvv>>^^^vv^v^^^^<^<<^vv<<<>v^<^^^v>^<v><<^<vv>>>v<<<<v>>>v<>v<^^^v<^v^<vv^vv<^><^v<>^<>><v^^^>vv^<^<v>>>v<^^v^>v^<v^>><<<^^><^^vv^>>^^vv<>v<^vv<<^<<>^^>^<<<<^<>v>>v^v<>^>vvv^>^>><^<v<^>>>v<<^>><>>>vvv^<><<<>><vv^><^<v^vv^>>^^<<<>v<v<>^<^>v>^v^<^^^v>^<vvvv<<<v<^>>>vv>v^><<v>v<^v<v^<^^>^<v<><<v^^<<^^^^<^>>>>v<<<<<^><^^vv>^v^v>>v>>>v^vv<vvvv<>v>v>><<>v>v>vv<<v<^v<vv<<vv<<^<<v<<v<^<>^^^>>>v<>^v>^<vv^v<>>><>^>>>v<^>^>^><<v^v<<v<<>vv<v><^v>v<v><>><^>^v<><v>^<>><<v^^^^v>^>v<v><<^>>v><>>><><v><>v^v>vvv^<<^><^>>v<^^<>^><>^v<^v<><>>>^^<>>>v>^>^<^v>><>^^<<v^^>>^^<v>>>^><<>><<^^v><v<>v><<>^^^v<><<vvv<<^^^vv^vv^>v<><v^<v^>^^^>>vv<>v^>^<^<^v^v><<v^^><^<>v<<vvv>^>>^><<v<<v^^v^^<<>>>^^^v>^>>vv^^v<><^<<^^<^v<<^v^v^>^v<<^^<^^<^<<<<vv<<<<v>v>^v^<^>v>v^>^>v<v^<<<vv>>^<<vv^>v<^>^<>>^v>v>>>v>>><v><<<v>v>^>v>>^^^>>>^^v>v>>v"""

inp = inp_real

[field,commands] = inp.split("\n\n")

commands = commands.replace("\n","")
mp = [list(el) for el in field.splitlines()]

def print_mp(mp):
    for row in mp:
        print("".join(row))

def get_robot_pos(mp):
    for rowIdx,row in enumerate(mp):
        for colIdx, el in enumerate(row):
            if el == "@":
                return (rowIdx, colIdx)

get_left_coord = lambda x: (x[0],x[1]-1)
get_right_coord = lambda x: (x[0],x[1]+1)
get_down_coord = lambda x: (x[0]+1,x[1])
get_up_coord = lambda x: (x[0]-1,x[1])

def render_next_mp(mp,next_move):
    this_pos = get_robot_pos(mp)
    coord_handler = [("^", get_up_coord),(">",get_right_coord),("<",get_left_coord),("v",get_down_coord)]
    for (next_sign, get_next_coord) in coord_handler:
        if next_move == next_sign:
            # print("---")
            # print_mp(mp)
            next_coord = get_next_coord(this_pos)
            if mp[next_coord[0]][next_coord[1]] == "#":
                return mp
            if mp[next_coord[0]][next_coord[1]] == ".":
                mp[this_pos[0]][this_pos[1]] = "."
                mp[next_coord[0]][next_coord[1]] = "@"
            if mp[next_coord[0]][next_coord[1]] == "O":
                
                box_coords = [next_coord]
                step_ahead_coord = get_next_coord(next_coord)
                while mp[step_ahead_coord[0]][step_ahead_coord[1]] == "O":
                    box_coords.append(step_ahead_coord)
                    step_ahead_coord = get_next_coord(step_ahead_coord)
                # we break when step_ahead_coord != O, it can then be a wall or a dot
                # if a wall, dont do anything, just return the map
                if mp[step_ahead_coord[0]][step_ahead_coord[1]] == "#":
                    return mp
                # if a dot, move everything one up
                if mp[step_ahead_coord[0]][step_ahead_coord[1]] == ".":
                    mp[this_pos[0]][this_pos[1]] = "."
                    mp[box_coords[0][0]][box_coords[0][1]] = "@"
                    mp[step_ahead_coord[0]][step_ahead_coord[1]] = "O"
            return mp


for command in commands:
    mp = render_next_mp(mp, command)


def calc_gps(mp):
    val = 0
    for rowIdx, row in enumerate(mp):
        for colIdx, cel in enumerate(row):
            if cel == "O":
                this_val = rowIdx*100+colIdx
                val += this_val
    return val


print("\nFINAL:")
# print_mp(mp)
print(f"calc_gps {calc_gps(mp)}")