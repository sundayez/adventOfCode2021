def die_moves(first):
    second = (first + 1) % 100
    if second == 0:
        second = 100
    third = (second + 1) % 100
    if third == 0:
        third = 100
    return first, second, third


def part_one():
    pos1 = 2
    pos2 = 7
    points1 = 0
    points2 = 0
    round_dice = 1
    rolled = 0
    while True:
        first, second, third = die_moves(round_dice)
        pos1 = (pos1 + first + second + third) % 10
        if pos1 == 0:
            pos1 = 10
        points1 += pos1
        print("Player 1 rolls {}+{}+{} and moves to space {} for a total score of {}".format(first, second, third, pos1,
                                                                                             points1))
        round_dice = (round_dice + 3) % 100
        if round_dice == 0:
            round_dice = 100
        rolled += 3
        if points1 >= 1000:
            break

        first, second, third = die_moves(round_dice)
        pos2 = (pos2 + first + second + third) % 10
        if pos2 == 0:
            pos2 = 10
        points2 += pos2
        print("Player 2 rolls {}+{}+{} and moves to space {} for a total score of {}".format(first, second, third, pos2,
                                                                                             points2))
        round_dice = (round_dice + 3) % 100
        if round_dice == 0:
            round_dice = 100
        rolled += 3
        if points2 >= 1000:
            break
    print("Rolled {}".format(rolled))
    print("Points 1 {}".format(points1))
    print("Points 2 {}".format(points2))
    print("Result 1 {}".format(rolled * points1))
    print("Result 2 {}".format(rolled * points2))


def part_two():
    pos1 = 4
    pos2 = 8
    points1 = 0
    points2 = 0
    round_dice = 1
    rolled = 0
    while True:
        first, second, third = die_moves(round_dice)
        pos1 = (pos1 + first + second + third) % 10
        if pos1 == 0:
            pos1 = 10
        points1 += pos1
        print("Player 1 rolls {}+{}+{} and moves to space {} for a total score of {}".format(first, second, third, pos1,
                                                                                             points1))
        round_dice = (round_dice + 3) % 100
        if round_dice == 0:
            round_dice = 100
        rolled += 3
        if points1 >= 1000:
            break

        first, second, third = die_moves(round_dice)
        pos2 = (pos2 + first + second + third) % 10
        if pos2 == 0:
            pos2 = 10
        points2 += pos2
        print("Player 2 rolls {}+{}+{} and moves to space {} for a total score of {}".format(first, second, third, pos2,
                                                                                             points2))
        round_dice = (round_dice + 3) % 100
        if round_dice == 0:
            round_dice = 100
        rolled += 3
        if points2 >= 1000:
            break
    print("Rolled {}".format(rolled))
    print("Points 1 {}".format(points1))
    print("Points 2 {}".format(points2))
    print("Result 1 {}".format(rolled * points1))
    print("Result 2 {}".format(rolled * points2))


def main():
    part_one()
    part_two()


main()
