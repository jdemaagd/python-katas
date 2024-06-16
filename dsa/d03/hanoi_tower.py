"""
Tower of Hanoi:
We have three rods and N disks.
The objective of the puzzle is to move the entire stack to another rod.
Initially, these discs are in the rod 1.
You need to print all the steps of discs movement so that all the discs reach the 3rd rod.
Also, find & return the total moves.

Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N.
Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc.
You can only move 1 disk at a time.
"""


# Time Complexity: O(2^n) -> 2^n - 1 moves -> 2^n
#   1 disk: 1 move
#   2 disks: 3 moves
#   3 disks: 7 moves
#   4 disks: 15 moves
#   T(n) = 2 * T(n - 1) + 1
#        = 2 [2 * T(n - 2) + 1] + 1
#        = 2 [2 * [2 * T(n - 3) + 1] + 1] + 1
# Space Complexity: O(n) -> recursive call stack
def hanoi_tower(n, src, dest, aux):
    count = 0

    def helper(disks, src_rod, dest_rod, aux_rod):
        nonlocal count
        if disks == 1:
            print("move disk " + str(disks) + " from rod " + str(src_rod) + " to rod " + str(dest_rod))
            count += 1
            return
        helper(disks - 1, src_rod, aux_rod, dest_rod)    # swap dest and aux rods
        print("move disk " + str(disks) + " from rod " + str(src_rod) + " to rod " + str(dest_rod))
        count += 1
        helper(disks - 1, aux_rod, dest_rod, src_rod)    # swap src and aux rods

    helper(n, src, dest, aux)

    return count


print(hanoi_tower(3, 1, 3, 2))
